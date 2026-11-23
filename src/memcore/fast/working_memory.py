"""工作记忆：当前会话的短时上下文，环形缓冲自动淘汰最旧。"""
from __future__ import annotations

from collections import deque

from ..core.constants import WORKING_MEMORY_CAPACITY


class WorkingMemory:
    """快记忆：容量受限的最近消息队列，直接拼进 prompt。

    与长期记忆（慢）相对——快记忆每次会话重建，慢记忆跨会话持久。
    """

    def __init__(self, capacity: int = WORKING_MEMORY_CAPACITY):
        self.capacity = capacity
        self._buf = deque(maxlen=capacity)

    def add(self, content: str, role: str = "user") -> None:
        self._buf.append({"role": role, "content": content})

    def peek(self, n: int | None = None) -> list:
        items = list(self._buf)
        if n is None:
            return items
        return items[-n:]

    def as_messages(self) -> list:
        return list(self._buf)

    def clear(self) -> None:
        self._buf.clear()

    def __len__(self) -> int:
        return len(self._buf)

    def full(self) -> bool:
        return len(self._buf) >= self.capacity
