"""异常体系：全部继承 MemcoreError，便于统一捕获。"""
from __future__ import annotations


class MemcoreError(Exception):
    """memcore 根异常。"""


class ItemNotFoundError(MemcoreError):
    """记忆条目不存在。"""


class StoreError(MemcoreError):
    """存储后端读写失败。"""


class ConfigError(MemcoreError):
    """配置非法。"""


class GateRejectedError(MemcoreError):
    """写入门控拒绝（重要性不足，未写入长期记忆）。"""
