"""去重：相似记忆保留一条，其余并入 tags 标记。"""
from __future__ import annotations

from ..embed.vectors import cosine
from ..embed.hashing import HashingVectorizer
from ..embed.tokenizer import DEFAULT_TOKENIZER


def deduplicate(items: list, threshold: float = 0.90) -> list:
    """返回去重后的记忆列表（保留重要性更高者）。"""
    vec = HashingVectorizer(4096)
    tok = DEFAULT_TOKENIZER
    keep: list = []
    for it in sorted(items, key=lambda x: x.importance, reverse=True):
        q = vec(tok.tokenize(it.content))
        dup = False
        for k in keep:
            d = vec(tok.tokenize(k.content))
            if cosine(q, d) >= threshold:
                dup = True
                break
        if not dup:
            keep.append(it)
    return keep
