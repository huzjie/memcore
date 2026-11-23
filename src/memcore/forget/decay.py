"""时间衰减遗忘：按 (importance, 衰减后价值) 综合评分淘汰。"""
from __future__ import annotations

from ..util.timeutil import age_ms
from ..core.constants import RECENCY_HALF_LIFE_MS


class DecayPolicy:
    """价值 = importance * 衰减系数，越旧越不重要越容易被忘。"""

    def __init__(self, half_life: int = RECENCY_HALF_LIFE_MS):
        self.half_life = half_life

    def score(self, item) -> float:
        import math
        age = age_ms(item.created_at)
        decay = math.exp(-math.log(2) * age / self.half_life)
        return item.importance * decay
