"""向量运算：余弦、点积、L2、归一化。"""
from __future__ import annotations

import math
from typing import Iterable


def dot(a: Iterable, b: Iterable) -> float:
    return sum(x * y for x, y in zip(a, b))


def l2_norm(vec: Iterable) -> float:
    s = sum(x * x for x in vec)
    return math.sqrt(s) if s > 0 else 0.0


def normalize_vec(vec: list) -> list:
    n = l2_norm(vec)
    if n == 0.0:
        return [0.0] * len(vec)
    return [x / n for x in vec]


def cosine(a: list, b: list) -> float:
    if len(a) != len(b):
        raise ValueError("vector length mismatch")
    na, nb = l2_norm(a), l2_norm(b)
    if na == 0.0 or nb == 0.0:
        return 0.0
    return dot(a, b) / (na * nb)
