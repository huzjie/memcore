"""存储抽象：统一增删改查接口。"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from ..core.types import MemoryItem


class Store(ABC):
    """长期记忆的持久化后端，所有实现必须保证 id 唯一。"""

    @abstractmethod
    def add(self, item: MemoryItem) -> str:
        """写入一条记忆，返回其 id。"""

    @abstractmethod
    def get(self, item_id: str) -> Optional[MemoryItem]:
        """按 id 读取，不存在返回 None。"""

    @abstractmethod
    def update(self, item: MemoryItem) -> bool:
        """整体覆盖一条记忆，返回是否成功。"""

    @abstractmethod
    def delete(self, item_id: str) -> bool:
        """删除一条记忆。"""

    @abstractmethod
    def all(self) -> list:
        """返回全部记忆列表。"""

    @abstractmethod
    def count(self) -> int:
        """记忆总数。"""

    @abstractmethod
    def clear(self) -> None:
        """清空全部记忆。"""

    def flush(self) -> None:
        """持久化后端落盘（内存后端可空实现）。"""
