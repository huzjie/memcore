"""新颖性打分：与已有记忆越不重复，越值得写入。"""
from __future__ import annotations

from ..embed.vectors import cosine
from ..embed.hashing import HashingVectorizer
from ..embed.tokenizer import DEFAULT_TOKENIZER


class NoveltyScorer:
    def __init__(self, dim: int = 4096, threshold: float = 0.85):
        self._vec = HashingVectorizer(dim)
        self._tok = DEFAULT_TOKENIZER
        self.threshold = threshold
        self._history: list = []

    def score(self, content: str, existing: list) -> float:
        """返回 [0,1]：1 表示全新，0 表示与已有高度重复。"""
        if not existing:
            return 1.0
        q = self._vec(self._tok.tokenize(content))
        best = 0.0
        for item in existing:
            d = self._vec(self._tok.tokenize(item.content))
            s = cosine(q, d)
            best = max(best, s)
        # 相似度超过阈值 → 视为重复，新颖性趋近 0
        if best >= self.threshold:
            return 0.0
        return 1.0 - best


_default = NoveltyScorer()


def novelty_score(content: str, existing: list) -> float:
    return _default.score(content, existing)
