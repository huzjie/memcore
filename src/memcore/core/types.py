"""核心类型：记忆条目 MemoryItem。"""
from __future__ import annotations

import time
import uuid
from dataclasses import dataclass, field
from typing import Any


def new_id() -> str:
    return uuid.uuid4().hex


def now_ms() -> int:
    return int(time.time() * 1000)


@dataclass
class MemoryItem:
    """一条长期记忆。

    - importance: 重要性 [0,1]，由写入门控打分。
    - salience:   显著性 [0,1]，由启发式规则打分。
    - access_count / last_accessed_at: 用于 LRU 与遗忘策略。
    """
    content: str
    id: str = field(default_factory=new_id)
    role: str = "user"
    scope: str = "global"
    importance: float = 0.5
    salience: float = 0.5
    created_at: int = field(default_factory=now_ms)
    last_accessed_at: int = field(default_factory=now_ms)
    access_count: int = 0
    tags: list = field(default_factory=list)
    source: str = "agent"
    metadata: dict = field(default_factory=dict)

    def touch(self) -> None:
        self.access_count += 1
        self.last_accessed_at = now_ms()

    def to_dict(self) -> dict:
        return {
            "content": self.content,
            "id": self.id,
            "role": self.role,
            "scope": self.scope,
            "importance": self.importance,
            "salience": self.salience,
            "created_at": self.created_at,
            "last_accessed_at": self.last_accessed_at,
            "access_count": self.access_count,
            "tags": list(self.tags),
            "source": self.source,
            "metadata": dict(self.metadata),
        }

    @classmethod
    def from_dict(cls, d: dict) -> "MemoryItem":
        fields = {
            "content", "id", "role", "scope", "importance", "salience",
            "created_at", "last_accessed_at", "access_count", "tags",
            "source", "metadata",
        }
        return cls(**{k: v for k, v in d.items() if k in fields})

    def __repr__(self) -> str:
        body = self.content if len(self.content) <= 40 else self.content[:40] + "..."
        return f"<MemoryItem {self.id[:8]} imp={self.importance:.2f} {body!r}>"
