"""JSON 文件后端：每写入即落盘，单文件原子替换。"""
from __future__ import annotations

import os
import tempfile
from typing import Optional

from .base import Store
from ..core.types import MemoryItem
from ..util.jsonutil import dumps, loads


class JsonStore(Store):
    def __init__(self, path: str):
        self.path = path
        self._items: dict = {}
        if os.path.exists(path):
            self._load()

    def _load(self) -> None:
        try:
            with open(self.path, "r", encoding="utf-8") as f:
                raw = loads(f.read())
            for d in raw:
                item = MemoryItem.from_dict(d)
                self._items[item.id] = item
        except Exception:
            self._items = {}

    def flush(self) -> None:
        data = [it.to_dict() for it in self._items.values()]
        dirpath = os.path.dirname(self.path)
        if dirpath:
            os.makedirs(dirpath, exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=dirpath or ".", suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write(dumps(data, indent=2))
            os.replace(tmp, self.path)
        finally:
            if os.path.exists(tmp):
                os.remove(tmp)

    def add(self, item: MemoryItem) -> str:
        self._items[item.id] = item
        self.flush()
        return item.id

    def get(self, item_id: str) -> Optional[MemoryItem]:
        return self._items.get(item_id)

    def update(self, item: MemoryItem) -> bool:
        if item.id not in self._items:
            return False
        self._items[item.id] = item
        self.flush()
        return True

    def delete(self, item_id: str) -> bool:
        ok = self._items.pop(item_id, None) is not None
        if ok:
            self.flush()
        return ok

    def all(self) -> list:
        return list(self._items.values())

    def count(self) -> int:
        return len(self._items)

    def clear(self) -> None:
        self._items.clear()
        self.flush()
