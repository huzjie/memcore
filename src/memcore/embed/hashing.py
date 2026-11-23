"""特征哈希向量化：把 token 序列映射为固定维度稀疏向量。"""
from __future__ import annotations

from ..util.hashutil import hash_text


class HashingVectorizer:
    """使用 signed hashing trick 生成固定维度向量，无需维护词表。"""

    def __init__(self, dim: int = 4096):
        self.dim = dim

    def transform(self, tokens: list) -> list:
        vec = [0.0] * self.dim
        for tok in tokens:
            idx = hash_text(tok, self.dim)
            sign = 1.0 if hash_text(tok + "#sign", 2) == 0 else -1.0
            vec[idx] += sign
        return vec

    def __call__(self, tokens: list) -> list:
        return self.transform(tokens)
