"""聚簇：把记忆按内容相似度分组。"""
from __future__ import annotations

from ..embed.vectors import cosine
from ..embed.hashing import HashingVectorizer
from ..embed.tokenizer import DEFAULT_TOKENIZER


class Clusterer:
    def __init__(self, threshold: float = 0.70):
        self.threshold = threshold
        self._vec = HashingVectorizer(4096)
        self._tok = DEFAULT_TOKENIZER

    def cluster(self, items: list) -> list:
        """贪心聚簇，返回 [[items], [items], ...]。"""
        clusters: list = []
        for it in items:
            q = self._vec(self._tok.tokenize(it.content))
            placed = False
            for cl in clusters:
                d = self._vec(self._tok.tokenize(cl[0].content))
                if cosine(q, d) >= self.threshold:
                    cl.append(it)
                    placed = True
                    break
            if not placed:
                clusters.append([it])
        return clusters
