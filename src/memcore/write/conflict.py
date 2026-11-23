"""冲突检测：新记忆与旧记忆语义相反时给出告警。"""
from __future__ import annotations

from ..embed.vectors import cosine
from ..embed.hashing import HashingVectorizer
from ..embed.tokenizer import DEFAULT_TOKENIZER

_NEGATORS = ("不要", "不再", "禁止", "取消", "撤回", "别", "停止")


def detect_conflict(content: str, existing: list, threshold: float = 0.70) -> list:
    """返回与新内容可能冲突的已有记忆 id 列表（启发式）。"""
    vec = HashingVectorizer(4096)
    tok = DEFAULT_TOKENIZER
    q = vec(tok.tokenize(content))
    hits = []
    neg_new = any(w in content for w in _NEGATORS)
    for item in existing:
        d = vec(tok.tokenize(item.content))
        s = cosine(q, d)
        if s >= threshold and (neg_new or any(w in item.content for w in _NEGATORS)):
            hits.append(item.id)
    return hits
