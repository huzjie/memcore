"""内存后端：进程内 dict，适合测试与无持久化场景。"""
from __future__ import annotations

from typing import Optional

from .base import Store
from ..core.types import MemoryItem


class MemoryStore(Store):
    def __init__(self):
        self._items: dict = {}

    def add(self, item: MemoryItem) -> str:
        self._items[item.id] = item
        return item.id

    def get(self, item_id: str) -> Optional[MemoryItem]:
        return self._items.get(item_id)

    def update(self, item: MemoryItem) -> bool:
        if item.id not in self._items:
            return False
        self._items[item.id] = item
        return True

    def delete(self, item_id: str) -> bool:
        return self._items.pop(item_id, None) is not None

    def all(self) -> list:
        return list(self._items.values())

    def count(self) -> int:
        return len(self._items)

    def clear(self) -> None:
        self._items.clear()
