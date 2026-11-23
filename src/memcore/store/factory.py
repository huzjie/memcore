"""存储工厂：按配置或 URL 创建后端。"""
from __future__ import annotations

from .base import Store
from .memory_store import MemoryStore
from .json_store import JsonStore
from .sqlite_store import SqliteStore


def create_store(url: str | None = None, **kw) -> Store:
    """支持 URL 形如 memory:// / json://path / sqlite://path；缺省内存后端。"""
    url = url or "memory://"
    scheme, _, rest = url.partition("://")
    if scheme == "json":
        return JsonStore(rest or kw.get("path", "memory.json"))
    if scheme == "sqlite":
        return SqliteStore(rest or kw.get("path", "memory.db"))
    return MemoryStore()
