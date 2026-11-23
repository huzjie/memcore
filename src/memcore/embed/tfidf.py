"""TF-IDF 索引：增量构建词表与文档向量，支持相似度检索。"""
from __future__ import annotations

import math


class TfidfIndex:
    """把一组文档转成 TF-IDF 向量空间，可对查询做余弦检索。"""

    def __init__(self):
        self._docs = []          # 每个文档的 token 列表
        self._df = {}            # term -> document frequency
        self._n_docs = 0

    def add(self, tokens: list) -> int:
        self._docs.append(tokens)
        seen = set()
        for tok in tokens:
            if tok not in seen:
                self._df[tok] = self._df.get(tok, 0) + 1
                seen.add(tok)
        self._n_docs += 1
        return self._n_docs - 1

    def _vector(self, tokens: list) -> dict:
        tf = {}
        for tok in tokens:
            tf[tok] = tf.get(tok, 0) + 1
        vec = {}
        n = max(1, self._n_docs)
        for tok, c in tf.items():
            df = self._df.get(tok, 0)
            idf = math.log((n + 1) / (df + 1)) + 1.0
            vec[tok] = c * idf
        return vec

    def _cosine(self, a: dict, b: dict) -> float:
        common = set(a) & set(b)
        if not common:
            return 0.0
        num = sum(a[t] * b[t] for t in common)
        na = math.sqrt(sum(v * v for v in a.values())) or 1.0
        nb = math.sqrt(sum(v * v for v in b.values())) or 1.0
        return num / (na * nb)

    def search(self, query_tokens: list, top_k: int = 5) -> list:
        q = self._vector(query_tokens)
        scored = []
        for i, tokens in enumerate(self._docs):
            d = self._vector(tokens)
            s = self._cosine(q, d)
            if s > 0:
                scored.append((i, s))
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]
