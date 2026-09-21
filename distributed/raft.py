"""
Raft Distributed Consensus State Machine
Implements Leader Election, Log Replication, Heartbeats, and State Machine Application.
"""

from typing import List, Dict, Optional, Tuple, Any
from dataclasses import dataclass, field
import random
import time
import enum

class NodeState(enum.Enum):
    FOLLOWER = "FOLLOWER"
    CANDIDATE = "CANDIDATE"
    LEADER = "LEADER"

@dataclass
class LogEntry:
    term: int
    index: int
    command: Any

@dataclass
class RequestVoteArgs:
    term: int
    candidate_id: int
    last_log_index: int
    last_log_term: int

@dataclass
class RequestVoteReply:
    term: int
    vote_granted: bool

@dataclass
class AppendEntriesArgs:
    term: int
    leader_id: int
    prev_log_index: int
    prev_log_term: int
    entries: List[LogEntry]
    leader_commit: int

@dataclass
class AppendEntriesReply:
    term: int
    success: bool
    match_index: int = 0

class RaftNode:
    def __init__(self, node_id: int, peers: List[int]):
        self.node_id = node_id
        self.peers = peers
        self.state = NodeState.FOLLOWER
        
        # Persistent state on all servers
        self.current_term = 0
        self.voted_for: Optional[int] = None
        self.log: List[LogEntry] = [LogEntry(term=0, index=0, command=None)]  # 1-indexed dummy
        
        # Volatile state on all servers
        self.commit_index = 0
        self.last_applied = 0
        
        # Volatile state on leaders
        self.next_index: Dict[int, int] = {}
        self.match_index: Dict[int, int] = {}
        
        # In-memory applied state machine
        self.kv_store: Dict[str, Any] = {}

    def get_last_log_index_and_term(self) -> Tuple[int, int]:
        last_entry = self.log[-1]
        return last_entry.index, last_entry.term

    def request_vote(self, args: RequestVoteArgs) -> RequestVoteReply:
        if args.term > self.current_term:
            self.current_term = args.term
            self.state = NodeState.FOLLOWER
            self.voted_for = None

        vote_granted = False
        if args.term == self.current_term and (self.voted_for is None or self.voted_for == args.candidate_id):
            last_index, last_term = self.get_last_log_index_and_term()
            # Candidate's log is up-to-date check
            if (args.last_log_term > last_term) or (args.last_log_term == last_term and args.last_log_index >= last_index):
                vote_granted = True
                self.voted_for = args.candidate_id

        return RequestVoteReply(term=self.current_term, vote_granted=vote_granted)

    def append_entries(self, args: AppendEntriesArgs) -> AppendEntriesReply:
        if args.term > self.current_term:
            self.current_term = args.term
            self.state = NodeState.FOLLOWER
            self.voted_for = None

        if args.term < self.current_term:
            return AppendEntriesReply(term=self.current_term, success=False)

        self.state = NodeState.FOLLOWER

        # Check log consistency
        if args.prev_log_index >= len(self.log) or self.log[args.prev_log_index].term != args.prev_log_term:
            return AppendEntriesReply(term=self.current_term, success=False)

        # Append new entries not already in the log
        insert_idx = args.prev_log_index + 1
        for entry in args.entries:
            if insert_idx < len(self.log):
                if self.log[insert_idx].term != entry.term:
                    self.log = self.log[:insert_idx]
                    self.log.append(entry)
            else:
                self.log.append(entry)
            insert_idx += 1

        # Update commit index
        if args.leader_commit > self.commit_index:
            self.commit_index = min(args.leader_commit, len(self.log) - 1)
            self._apply_logs()

        return AppendEntriesReply(term=self.current_term, success=True, match_index=len(self.log) - 1)

    def _apply_logs(self):
        while self.last_applied < self.commit_index:
            self.last_applied += 1
            cmd = self.log[self.last_applied].command
            if isinstance(cmd, tuple) and len(cmd) == 2:
                k, v = cmd
                self.kv_store[k] = v

    def start_election(self) -> RequestVoteArgs:
        self.current_term += 1
        self.state = NodeState.CANDIDATE
        self.voted_for = self.node_id
        last_index, last_term = self.get_last_log_index_and_term()
        return RequestVoteArgs(
            term=self.current_term,
            candidate_id=self.node_id,
            last_log_index=last_index,
            last_log_term=last_term
        )

    def become_leader(self):
        self.state = NodeState.LEADER
        last_index, _ = self.get_last_log_index_and_term()
        for p in self.peers:
            self.next_index[p] = last_index + 1
            self.match_index[p] = 0
