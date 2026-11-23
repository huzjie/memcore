"""巩固调度：记忆数超阈值时触发一次巩固。"""
from __future__ import annotations

from ..core.constants import CONSOLIDATE_MIN_ITEMS


class ConsolidationScheduler:
    def __init__(self, min_items: int = CONSOLIDATE_MIN_ITEMS):
        self.min_items = min_items

    def should_run(self, item_count: int) -> bool:
        return item_count >= self.min_items
