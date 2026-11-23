"""混合打分：把时间 / 重要性 / 相关性归一后加权融合。"""
from __future__ import annotations

from ..core.types import MemoryItem
from ..core.query import MemoryQuery
from .recency import recency_score
from .relevance import relevance_score


class HybridScorer:
    """score = w_rel * relevance + w_rec * recency + w_imp * importance。"""

    def score(self, item: MemoryItem, query: MemoryQuery,
              rel_score: float | None = None) -> float:
        if rel_score is None:
            rel_score = relevance_score(query.query, item.content)
        rec = recency_score(item)
        imp = item.importance
        w_rel = query.relevance_weight
        w_rec = query.recency_bias
        w_imp = query.importance_weight
        total = w_rel + w_rec + w_imp
        if total == 0:
            return 0.0
        return (w_rel * rel_score + w_rec * rec + w_imp * imp) / total
