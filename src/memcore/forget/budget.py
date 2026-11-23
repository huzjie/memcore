"""预算淘汰：超过 max_items 时按分数丢弃最低分。"""
from __future__ import annotations

from ..core.constants import DEFAULT_MAX_ITEMS, FORGET_SAFETY_MARGIN


class BudgetEvictor:
    def __init__(self, max_items: int = DEFAULT_MAX_ITEMS,
                 safety: float = FORGET_SAFETY_MARGIN):
        self.max_items = max_items
        self.safety = safety

    def evict(self, items: list, scorer) -> tuple:
        """返回 (保留列表, 被淘汰列表)。"""
        if len(items) <= self.max_items:
            return items, []
        limit = int(self.max_items * (1 - self.safety))
        ranked = sorted(items, key=lambda it: scorer.score(it))
        keep = ranked[len(ranked) - limit:]
        evicted = ranked[: len(ranked) - limit]
        return keep, evicted
