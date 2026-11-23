"""哈希工具：稳定哈希（进程间一致）与文本指纹。"""
from __future__ import annotations

import hashlib


def stable_hash(text: str) -> str:
    """对文本做 SHA-256 摘要，返回 16 位十六进制指纹，跨进程稳定。"""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def hash_text(text: str, buckets: int = 65536) -> int:
    """把文本哈希到 [0, buckets) 区间，用于特征哈希索引。"""
    if buckets <= 0:
        raise ValueError("buckets must be positive")
    digest = hashlib.md5(text.encode("utf-8")).hexdigest()
    return int(digest, 16) % buckets
