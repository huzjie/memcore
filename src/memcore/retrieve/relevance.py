"""相关性：BM25 + TF-IDF 混合稀疏召回。"""
from __future__ import annotations

from ..embed.tokenizer import DEFAULT_TOKENIZER
from ..embed.tfidf import TfidfIndex
from ..embed.bm25 import BM25Index


class RelevanceIndex:
    """维护一个可增量更新的相关性索引。"""

    def __init__(self):
        self._tok = DEFAULT_TOKENIZER
        self._tfidf = TfidfIndex()
        self._bm25 = BM25Index()
        self._doc_ids: list = []

    def add(self, item_id: str, content: str) -> None:
        tokens = self._tok.tokenize(content)
        self._doc_ids.append(item_id)
        self._tfidf.add(tokens)
        self._bm25.add(tokens)

    def remove_all(self) -> None:
        self._tfidf = TfidfIndex()
        self._bm25 = BM25Index()
        self._doc_ids = []

    def search(self, query: str, top_k: int = 20) -> dict:
        qt = self._tok.tokenize(query)
        t_scores = dict(self._tfidf.search(qt, top_k * 4))
        b_scores = dict(self._bm25.search(qt, top_k * 4))
        merged = {}
        for idx, s in t_scores.items():
            merged[idx] = merged.get(idx, 0.0) + 0.5 * s
        for idx, s in b_scores.items():
            merged[idx] = merged.get(idx, 0.0) + 0.5 * s
        out = {}
        for idx, s in merged.items():
            if idx < len(self._doc_ids):
                out[self._doc_ids[idx]] = s
        return out


_default = RelevanceIndex()


def relevance_score(query: str, content: str) -> float:
    """单条内容的即时相关性（小规模兜底，不依赖索引）。"""
    from ..embed.vectors import cosine
    from ..embed.hashing import HashingVectorizer
    vec = HashingVectorizer(4096)
    tok = DEFAULT_TOKENIZER
    return cosine(vec(tok.tokenize(query)), vec(tok.tokenize(content)))
