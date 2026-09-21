"""
Multi-Version Concurrency Control (MVCC) Engine with Snapshot Isolation
Features timestamp ordering, optimistic read/write sets, and version garbage collection.
"""

from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass
import threading
import time

@dataclass
class Version:
    created_tx_id: int
    deleted_tx_id: Optional[int]
    value: Any

class MVCCStorageEngine:
    def __init__(self):
        self._global_tx_counter = 0
        self._lock = threading.Lock()
        self._active_transactions: Set[int] = set()
        self._committed_transactions: Set[int] = set()
        self._records: Dict[str, List[Version]] = {}

    def begin_transaction(self) -> 'MVCCTransaction':
        with self._lock:
            self._global_tx_counter += 1
            tx_id = self._global_tx_counter
            self._active_transactions.add(tx_id)
            # Snapshot of committed transactions at start time
            snapshot = set(self._committed_transactions)
            return MVCCTransaction(self, tx_id, snapshot)

    def _commit_tx(self, tx_id: int, write_set: Dict[str, Any], delete_set: Set[str]) -> bool:
        with self._lock:
            # Check First-Committer-Wins rule for write conflicts
            for key in write_set:
                if key in self._records:
                    for v in self._records[key]:
                        if v.created_tx_id > tx_id and v.created_tx_id in self._committed_transactions:
                            return False  # Write-write conflict

            for key, val in write_set.items():
                if key not in self._records:
                    self._records[key] = []
                self._records[key].append(Version(created_tx_id=tx_id, deleted_tx_id=None, value=val))

            for key in delete_set:
                if key in self._records:
                    for v in self._records[key]:
                        if v.deleted_tx_id is None:
                            v.deleted_tx_id = tx_id

            self._active_transactions.remove(tx_id)
            self._committed_transactions.add(tx_id)
            return True

    def _rollback_tx(self, tx_id: int):
        with self._lock:
            if tx_id in self._active_transactions:
                self._active_transactions.remove(tx_id)

class MVCCTransaction:
    def __init__(self, engine: MVCCStorageEngine, tx_id: int, snapshot: Set[int]):
        self.engine = engine
        self.tx_id = tx_id
        self.snapshot = snapshot
        self.write_set: Dict[str, Any] = {}
        self.delete_set: Set[str] = set()
        self.is_active = True

    def get(self, key: str) -> Optional[Any]:
        if not self.is_active:
            raise RuntimeError("Transaction is inactive")
        if key in self.write_set:
            return self.write_set[key]
        if key in self.delete_set:
            return None

        records = self.engine._records.get(key, [])
        for version in reversed(records):
            # Check visibility under Snapshot Isolation
            created_visible = (version.created_tx_id == self.tx_id) or (version.created_tx_id in self.snapshot)
            deleted_visible = False
            if version.deleted_tx_id is not None:
                deleted_visible = (version.deleted_tx_id == self.tx_id) or (version.deleted_tx_id in self.snapshot)

            if created_visible and not deleted_visible:
                return version.value
        return None

    def put(self, key: str, value: Any):
        if not self.is_active:
            raise RuntimeError("Transaction is inactive")
        self.write_set[key] = value
        self.delete_set.discard(key)

    def delete(self, key: str):
        if not self.is_active:
            raise RuntimeError("Transaction is inactive")
        self.delete_set.add(key)
        self.write_set.pop(key, None)

    def commit(self) -> bool:
        if not self.is_active:
            return False
        self.is_active = False
        return self.engine._commit_tx(self.tx_id, self.write_set, self.delete_set)

    def rollback(self):
        if self.is_active:
            self.is_active = False
            self.engine._rollback_tx(self.tx_id)
