"""检索编排：过滤 -> 打分 -> 排序 -> top-k。"""
from __future__ import annotations

from ..core.types import MemoryItem
from ..core.query import MemoryQuery
from ..core.result import MemoryResult
from .scorer import HybridScorer
from .relevance import RelevanceIndex


class Searcher:
    def __init__(self):
        self._scorer = HybridScorer()
        self._index = RelevanceIndex()

    def index(self, items: list) -> None:
        self._index.remove_all()
        for it in items:
            self._index.add(it.id, it.content)

    def search(self, items: list, query: MemoryQuery) -> list:
        rel = self._index.search(query.query, top_k=max(20, query.limit * 4))
        results = []
        for item in items:
            if query.scope and item.scope != query.scope:
                continue
            if query.tags and not set(query.tags).issubset(set(item.tags or [])):
                continue
            rel_score = rel.get(item.id, 0.0)
            score = self._scorer.score(item, query, rel_score)
            if score < query.min_score:
                continue
            item.touch()
            results.append(MemoryResult(
                item=item, score=round(score, 4),
                reasons={"relevance": round(rel_score, 4)},
            ))
        results.sort(key=lambda r: r.score, reverse=True)
        return results[: query.limit]
