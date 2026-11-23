"""LRU 淘汰：按最近访问时间排序，最久未用者优先淘汰。"""
from __future__ import annotations


class LruPolicy:
    def rank(self, item) -> int:
        """返回越小越先淘汰（最久未访问）。"""
        return item.last_accessed_at
