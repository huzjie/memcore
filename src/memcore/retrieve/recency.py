"""时间衰减：越新的记忆得分越高。"""
from __future__ import annotations

import math

from ..core.constants import RECENCY_HALF_LIFE_MS
from ..util.timeutil import age_ms


def exponential_decay(age: int, half_life: int = RECENCY_HALF_LIFE_MS) -> float:
    """指数衰减：age 越大越接近 0，半衰期为 half_life。"""
    if half_life <= 0:
        return 1.0
    return math.exp(-math.log(2) * age / half_life)


def recency_score(item, half_life: int = RECENCY_HALF_LIFE_MS) -> float:
    age = age_ms(item.created_at)
    return exponential_decay(age, half_life)
