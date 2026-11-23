"""Memory 门面：把快记忆 + 慢记忆编排成统一入口。"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

from ..adapters.base import LLMAdapter
from ..adapters.mock import MockLLM
from ..fast.working_memory import WorkingMemory
from ..slow.longterm import LongTermMemory
from ..write.gate import WriteGate
from ..store.factory import create_store
from ..consolidate.pipeline import consolidate as _consolidate
from ..core.query import MemoryQuery


@dataclass
class Memory:
    """一个「记忆原生」Agent 的记忆内核。

    快记忆（working）承载当前会话上下文；
    慢记忆（longterm）跨会话持久化高价值记忆。
    """

    llm: LLMAdapter = field(default_factory=MockLLM)
    store_url: str | None = None
    use_gate: bool = True
    max_items: int = 10_000
    working_capacity: int = 16

    def __post_init__(self):
        gate = WriteGate(self.llm) if self.use_gate else None
        store = create_store(self.store_url)
        self.working = WorkingMemory(self.working_capacity)
        self.longterm = LongTermMemory(store=store, gate=gate,
                                       max_items=self.max_items)

    # ---- 快记忆 ----
    def remember_now(self, content: str, role: str = "user") -> None:
        self.working.add(content, role)

    # ---- 慢记忆 ----
    def add(self, content: str, role: str = "user", scope: str = "global",
            tags: list | None = None, force: bool = False,
            metadata: dict | None = None):
        return self.longterm.add(content, role=role, scope=scope,
                                 tags=tags, force=force, metadata=metadata)

    def search(self, query: str, limit: int = 5):
        return self.longterm.search(MemoryQuery(query, limit=limit))

    def get(self, item_id: str):
        return self.longterm.get(item_id)

    def delete(self, item_id: str) -> bool:
        return self.longterm.delete(item_id)

    def all(self):
        return self.longterm.all()

    def count(self) -> int:
        return self.longterm.count()

    def forget(self) -> int:
        return self.longterm.forget()

    def consolidate(self) -> int:
        """巩固长期记忆，返回被合并掉的记忆条数。"""
        items = self.longterm.all()
        if len(items) < 2:
            return 0
        new_contents = _consolidate(items, self.llm)
        before = len(items)
        self.longterm.clear()
        for c in new_contents:
            self.longterm.add(c, force=True)
        return max(0, before - len(new_contents))

    def clear(self) -> None:
        self.working.clear()
        self.longterm.clear()

    def stats(self) -> dict:
        return {
            "working_items": len(self.working),
            "longterm_items": self.longterm.count(),
            "gate": self.use_gate,
            "store": type(self.longterm.store).__name__,
        }

    # 兼容别名
    remember = add
    recall = search
