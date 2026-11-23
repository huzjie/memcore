"""检索查询对象。"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class MemoryQuery:
    """描述一次记忆检索的意图与权重。

    - recency_bias:      时间衰减权重（越大越偏向最近）。
    - importance_weight: 重要性权重。
    - relevance_weight:  语义相关性权重。
    """
    query: str
    limit: int = 5
    recency_bias: float = 0.5
    importance_weight: float = 0.5
    relevance_weight: float = 1.0
    tags: Optional[list] = None
    scope: Optional[str] = None
    min_score: float = 0.0
    metadata: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "query": self.query, "limit": self.limit,
            "recency_bias": self.recency_bias,
            "importance_weight": self.importance_weight,
            "relevance_weight": self.relevance_weight,
            "tags": self.tags, "scope": self.scope,
            "min_score": self.min_score, "metadata": dict(self.metadata),
        }

    @classmethod
    def from_dict(cls, d: dict) -> "MemoryQuery":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})
