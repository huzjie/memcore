"""遗忘编排：组合预算 + 衰减，返回应删除的 id 列表。"""
from __future__ import annotations

from .decay import DecayPolicy
from .budget import BudgetEvictor


class Evictor:
    def __init__(self, max_items: int | None = None):
        self.max_items = max_items
        self._decay = DecayPolicy()
        self._budget = BudgetEvictor(max_items or 10_000)

    def select(self, items: list) -> list:
        if self.max_items is None or len(items) <= self.max_items:
            return []
        keep, evicted = self._budget.evict(items, self._decay)
        return [it.id for it in evicted]
