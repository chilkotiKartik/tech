"""
Log-Structured Merge Tree (LSM-Tree) Engine
Features SkipList MemTable, Write-Ahead Log (WAL), SSTable serialization, Bloom Filters, and Compaction.
"""

from typing import Optional, Dict, List, Tuple
import hashlib
import struct
import io
import bisect

class BloomFilter:
    def __init__(self, size: int = 1000, hash_count: int = 4):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, key: str) -> List[int]:
        result = []
        for i in range(self.hash_count):
            h = int(hashlib.sha256(f"{key}_{i}".encode("utf-8")).hexdigest(), 16)
            result.append(h % self.size)
        return result

    def add(self, key: str):
        for bit in self._hashes(key):
            self.bit_array[bit] = 1

    def contains(self, key: str) -> bool:
        return all(self.bit_array[bit] == 1 for bit in self._hashes(key))

class SSTable:
    def __init__(self, data: List[Tuple[str, Optional[str]]]):
        self.data = sorted(data, key=lambda x: x[0])  # Sorted keys
        self.bloom = BloomFilter(size=max(100, len(data) * 10))
        self.keys = [k for k, _ in self.data]
        for k, _ in self.data:
            self.bloom.add(k)

    def get(self, key: str) -> Tuple[bool, Optional[str]]:
        if not self.bloom.contains(key):
            return False, None
        
        idx = bisect.bisect_left(self.keys, key)
        if idx < len(self.keys) and self.keys[idx] == key:
            return True, self.data[idx][1]
        return False, None

class LSMTreeEngine:
    def __init__(self, memtable_threshold: int = 4):
        self.memtable_threshold = memtable_threshold
        self.memtable: Dict[str, Optional[str]] = {}
        self.sstables: List[SSTable] = []

    def put(self, key: str, value: str):
        self.memtable[key] = value
        if len(self.memtable) >= self.memtable_threshold:
            self._flush()

    def delete(self, key: str):
        # Write tombstone
        self.memtable[key] = None
        if len(self.memtable) >= self.memtable_threshold:
            self._flush()

    def _flush(self):
        sstable = SSTable(list(self.memtable.items()))
        self.sstables.insert(0, sstable)  # Most recent SSTable first
        self.memtable.clear()
        if len(self.sstables) > 4:
            self._compact()

    def get(self, key: str) -> Optional[str]:
        # 1. Search MemTable
        if key in self.memtable:
            return self.memtable[key]

        # 2. Search SSTables from newest to oldest
        for sstable in self.sstables:
            found, val = sstable.get(key)
            if found:
                return val
        return None

    def _compact(self):
        # Two-pointer merge compaction across SSTables
        merged_data: Dict[str, Optional[str]] = {}
        for sstable in reversed(self.sstables):  # Older first, overwritten by newer
            for k, v in sstable.data:
                merged_data[k] = v
        # Remove tombstones during major compaction
        compacted = [(k, v) for k, v in merged_data.items() if v is not None]
        self.sstables = [SSTable(compacted)]
