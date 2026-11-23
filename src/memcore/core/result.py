"""检索结果对象。"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .types import MemoryItem


@dataclass
class MemoryResult:
    item: MemoryItem
    score: float = 0.0
    reasons: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "item": self.item.to_dict(),
            "score": self.score,
            "reasons": dict(self.reasons),
        }

    @classmethod
    def from_dict(cls, d: dict) -> "MemoryResult":
        return cls(
            item=MemoryItem.from_dict(d["item"]),
            score=d.get("score", 0.0),
            reasons=d.get("reasons", {}),
        )
