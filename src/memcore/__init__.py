"""memcore —— 记忆原生 Agent 的记忆内核。

快慢记忆双通道：快记忆承载会话上下文，慢记忆跨会话持久化高价值记忆，
配套写入门控 / 混合检索 / 记忆巩固 / 遗忘淘汰，零第三方依赖。
"""
from .version import __version__
from .core import Memory, MemoryItem, MemoryQuery, MemoryResult
from .core.errors import (
    MemcoreError, ItemNotFoundError, StoreError, ConfigError, GateRejectedError,
)

__all__ = [
    "Memory", "MemoryItem", "MemoryQuery", "MemoryResult",
    "MemcoreError", "ItemNotFoundError", "StoreError",
    "ConfigError", "GateRejectedError", "__version__",
]
