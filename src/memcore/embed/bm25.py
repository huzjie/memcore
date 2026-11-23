"""BM25 检索：经典稀疏检索打分，参数可调。"""
from __future__ import annotations

import math


class BM25Index:
    """标准 BM25，k1/b 可调，用于记忆库的稀疏关键词召回。"""

    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self._docs = []
        self._df = {}
        self._n_docs = 0
        self._avg_len = 0.0

    def add(self, tokens: list) -> int:
        self._docs.append(tokens)
        seen = set()
        for tok in tokens:
            if tok not in seen:
                self._df[tok] = self._df.get(tok, 0) + 1
                seen.add(tok)
        self._n_docs += 1
        total = sum(len(d) for d in self._docs)
        self._avg_len = total / self._n_docs
        return self._n_docs - 1

    def _idf(self, term: str) -> float:
        df = self._df.get(term, 0)
        return math.log(1 + (self._n_docs - df + 0.5) / (df + 0.5))

    def score(self, query_tokens: list, doc_idx: int) -> float:
        doc = self._docs[doc_idx]
        dl = len(doc)
        tf = {}
        for tok in doc:
            tf[tok] = tf.get(tok, 0) + 1
        s = 0.0
        for q in query_tokens:
            if q not in tf:
                continue
            idf = self._idf(q)
            numerator = tf[q] * (self.k1 + 1)
            denominator = tf[q] + self.k1 * (1 - self.b + self.b * dl / max(1.0, self._avg_len))
            s += idf * numerator / denominator
        return s

    def search(self, query_tokens: list, top_k: int = 5) -> list:
        scored = [(i, self.score(query_tokens, i)) for i in range(self._n_docs)]
        scored = [(i, s) for i, s in scored if s > 0]
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]
