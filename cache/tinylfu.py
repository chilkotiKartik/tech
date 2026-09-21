"""
High-Performance TinyLFU Cache with Count-Min Sketch & Singleflight Protection
Implements W-TinyLFU cache admission policy to prevent cache pollution and dogpiling.
"""

from typing import Dict, Optional, Any, Callable
import hashlib
import threading
import time
from collections import OrderedDict

class CountMinSketch:
    def __init__(self, width: int = 1024, depth: int = 4):
        self.width = width
        self.depth = depth
        self.table = [[0] * width for _ in range(depth)]
        self.total_count = 0
        self.reset_threshold = width * 10

    def _hash(self, key: str, i: int) -> int:
        h = int(hashlib.md5(f"{key}:{i}".encode("utf-8")).hexdigest(), 16)
        return h % self.width

    def increment(self, key: str):
        for i in range(self.depth):
            idx = self._hash(key, i)
            if self.table[i][idx] < 15:  # 4-bit saturation counter
                self.table[i][idx] += 1
        self.total_count += 1
        if self.total_count >= self.reset_threshold:
            self._halve_counts()

    def estimate(self, key: str) -> int:
        return min(self.table[i][self._hash(key, i)] for i in range(self.depth))

    def _halve_counts(self):
        # Ageing mechanism: halve counters on reset to decay historical frequency
        for i in range(self.depth):
            for j in range(self.width):
                self.table[i][j] //= 2
        self.total_count //= 2

class SingleflightGroup:
    """Prevents duplicate concurrent in-flight computations (cache dogpiling)"""
    def __init__(self):
        self._lock = threading.Lock()
        self._calls: Dict[str, threading.Event] = {}
        self._results: Dict[str, Any] = {}
        self._errors: Dict[str, Exception] = {}

    def do(self, key: str, fn: Callable[[], Any]) -> Any:
        event = None
        with self._lock:
            if key in self._calls:
                event = self._calls[key]
            else:
                event = threading.Event()
                self._calls[key] = event
        
        if event and key in self._results:
            event.wait()
            if key in self._errors:
                raise self._errors[key]
            return self._results[key]

        # Primary executor
        try:
            val = fn()
            with self._lock:
                self._results[key] = val
            return val
        except Exception as e:
            with self._lock:
                self._errors[key] = e
            raise
        finally:
            with self._lock:
                event.set()
                self._calls.pop(key, None)

class TinyLFUCache:
    def __init__(self, capacity: int = 100):
        self.capacity = capacity
        self.window_capacity = max(1, int(capacity * 0.01))
        self.protected_capacity = int(capacity * 0.8)
        self.probation_capacity = capacity - self.window_capacity - self.protected_capacity

        self.sketch = CountMinSketch()
        self.singleflight = SingleflightGroup()

        # Segmented LRU queues
        self.window_lru: OrderedDict[str, Any] = OrderedDict()
        self.probation_lru: OrderedDict[str, Any] = OrderedDict()
        self.protected_lru: OrderedDict[str, Any] = OrderedDict()
        self.lock = threading.Lock()

    def get(self, key: str) -> Optional[Any]:
        with self.lock:
            self.sketch.increment(key)
            if key in self.window_lru:
                self.window_lru.move_to_end(key)
                return self.window_lru[key]
            if key in self.protected_lru:
                self.protected_lru.move_to_end(key)
                return self.protected_lru[key]
            if key in self.probation_lru:
                # Promote to protected LRU on hit
                val = self.probation_lru.pop(key)
                if len(self.protected_lru) >= self.protected_capacity:
                    # Demote victim from protected to probation
                    k_demote, v_demote = self.protected_lru.popitem(last=False)
                    self.probation_lru[k_demote] = v_demote
                self.protected_lru[key] = val
                return val
            return None

    def put(self, key: str, value: Any):
        with self.lock:
            self.sketch.increment(key)
            # Already exists in queues?
            for lru in (self.window_lru, self.protected_lru, self.probation_lru):
                if key in lru:
                    lru[key] = value
                    lru.move_to_end(key)
                    return

            self.window_lru[key] = value
            if len(self.window_lru) > self.window_capacity:
                # Evict from window to probation
                candidate_k, candidate_v = self.window_lru.popitem(last=False)
                self._admit_to_probation(candidate_k, candidate_v)

    def _admit_to_probation(self, key: str, value: Any):
        if len(self.probation_lru) < self.probation_capacity:
            self.probation_lru[key] = value
            return

        # TinyLFU admission comparison
        victim_k, victim_v = self.probation_lru.popitem(last=False)
        if self.sketch.estimate(key) >= self.sketch.estimate(victim_k):
            # Candidate wins admission
            self.probation_lru[key] = value
        else:
            # Victim stays
            self.probation_lru[victim_k] = victim_v
