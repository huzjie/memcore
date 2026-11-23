"""遗忘策略工厂。"""
from __future__ import annotations

from .decay import DecayPolicy
from .lru import LruPolicy
from .evictor import Evictor


def build_policy(name: str = "decay", **kw):
    if name == "lru":
        return LruPolicy()
    if name == "evictor":
        return Evictor(**kw)
    return DecayPolicy(**kw)
