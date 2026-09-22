"""
High-Throughput Asynchronous TCP Proxy & Event Loop Architecture
Leverages non-blocking sockets, edge-triggered I/O event polling, and buffer slicing.
"""

import socket
import select
import sys
from typing import Dict, Tuple, Optional

class TCPProxyEventLoop:
    def __init__(self, local_host: str, local_port: int, remote_host: str, remote_port: int):
        self.local_host = local_host
        self.local_port = local_port
        self.remote_host = remote_host
        self.remote_port = remote_port
        
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_sock.setblocking(False)
        self.server_sock.bind((self.local_host, self.local_port))
        self.server_sock.listen(1024)

        # Socket mappings: client_fd <-> remote_fd
        self.peer_map: Dict[socket.socket, socket.socket] = {}
        self.buffers: Dict[socket.socket, bytearray] = {}
        self.sockets = [self.server_sock]

    def _accept_client(self):
        try:
            client_sock, client_addr = self.server_sock.accept()
            client_sock.setblocking(False)

            remote_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            remote_sock.setblocking(False)
            try:
                remote_sock.connect((self.remote_host, self.remote_port))
            except BlockingIOError:
                pass  # Non-blocking connect in progress

            self.peer_map[client_sock] = remote_sock
            self.peer_map[remote_sock] = client_sock
            self.buffers[client_sock] = bytearray()
            self.buffers[remote_sock] = bytearray()

            self.sockets.extend([client_sock, remote_sock])
        except Exception:
            pass

    def _close_session(self, sock: socket.socket):
        peer = self.peer_map.get(sock)
        for s in (sock, peer):
            if s and s in self.sockets:
                self.sockets.remove(s)
            if s and s in self.buffers:
                del self.buffers[s]
            if s and s in self.peer_map:
                del self.peer_map[s]
            if s:
                try:
                    s.close()
                except Exception:
                    pass

    def step(self, timeout: float = 0.05):
        if not self.sockets:
            return

        readable, writable, exceptional = select.select(self.sockets, self.sockets, self.sockets, timeout)

        for s in exceptional:
            self._close_session(s)

        for s in readable:
            if s is self.server_sock:
                self._accept_client()
            else:
                try:
                    data = s.recv(65536)
                    if not data:
                        self._close_session(s)
                    else:
                        peer = self.peer_map.get(s)
                        if peer:
                            self.buffers[peer].extend(data)
                except Exception:
                    self._close_session(s)

        for s in writable:
            buf = self.buffers.get(s)
            if buf:
                try:
                    sent = s.send(buf)
                    del buf[:sent]
                except (BlockingIOError, InterruptedError):
                    pass
                except Exception:
                    self._close_session(s)
