"""长期记忆：封装 store 与写入门控，持久保存高价值记忆。"""
from __future__ import annotations

from ..store.base import Store
from ..store.factory import create_store
from ..core.types import MemoryItem
from ..write.gate import WriteGate
from ..retrieve.searcher import Searcher
from ..forget.evictor import Evictor
from ..core.query import MemoryQuery
from ..core.constants import DEFAULT_MAX_ITEMS


class LongTermMemory:
    """慢记忆银行：add（过写入门控）/ search / get / delete / forget。"""

    def __init__(self, store: Store | None = None, gate: WriteGate | None = None,
                 max_items: int = DEFAULT_MAX_ITEMS):
        self.store = store or create_store()
        self.gate = gate
        self._searcher = Searcher()
        self._evictor = Evictor(max_items)

    def add(self, content: str, role: str = "user", scope: str = "global",
            tags: list | None = None, source: str = "agent",
            metadata: dict | None = None, force: bool = False) -> MemoryItem | None:
        """写入一条长期记忆。gate 为 None 时强制写入。"""
        if not content or not content.strip():
            return None
        existing = self.store.all()
        imp = 0.5
        sal = 0.5
        if self.gate is not None and not force:
            res = self.gate.evaluate(content, existing)
            if not res.decision:
                return None
            imp = res.components["importance"]
            sal = res.components["salience"]
        item = MemoryItem(
            content=content, role=role, scope=scope, importance=imp,
            salience=sal, tags=tags or [], source=source,
            metadata=metadata or {},
        )
        self.store.add(item)
        return item

    def search(self, query: str | MemoryQuery, limit: int = 5) -> list:
        q = query if isinstance(query, MemoryQuery) else MemoryQuery(query, limit=limit)
        items = self.store.all()
        self._searcher.index(items)
        return self._searcher.search(items, q)

    def get(self, item_id: str):
        return self.store.get(item_id)

    def delete(self, item_id: str) -> bool:
        return self.store.delete(item_id)

    def all(self) -> list:
        return self.store.all()

    def count(self) -> int:
        return self.store.count()

    def forget(self) -> int:
        """执行遗忘淘汰，返回被删除的记忆条数。"""
        victims = self._evictor.select(self.store.all())
        for vid in victims:
            self.store.delete(vid)
        return len(victims)

    def clear(self) -> None:
        self.store.clear()
