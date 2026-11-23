"""SQLite 后端：标准库 sqlite3，支持大规模记忆与并发读。"""
from __future__ import annotations

import sqlite3
from typing import Optional

from .base import Store
from ..core.types import MemoryItem
from ..util.jsonutil import dumps, loads

_SCHEMA = """
CREATE TABLE IF NOT EXISTS memories (
    id TEXT PRIMARY KEY,
    content TEXT NOT NULL,
    role TEXT, scope TEXT,
    importance REAL, salience REAL,
    created_at INTEGER, last_accessed_at INTEGER, access_count INTEGER,
    tags TEXT, source TEXT, metadata TEXT
);
CREATE INDEX IF NOT EXISTS idx_scope ON memories(scope);
CREATE INDEX IF NOT EXISTS idx_created ON memories(created_at);
"""


class SqliteStore(Store):
    def __init__(self, path: str):
        self.path = path
        self._conn = sqlite3.connect(path, check_same_thread=False)
        self._conn.row_factory = sqlite3.Row
        self._conn.execute(_SCHEMA)
        self._conn.commit()

    def _row_to_item(self, row) -> MemoryItem:
        return MemoryItem(
            content=row["content"], id=row["id"], role=row["role"],
            scope=row["scope"], importance=row["importance"],
            salience=row["salience"], created_at=row["created_at"],
            last_accessed_at=row["last_accessed_at"],
            access_count=row["access_count"],
            tags=loads(row["tags"] or "[]"),
            source=row["source"], metadata=loads(row["metadata"] or "{}"),
        )

    def add(self, item: MemoryItem) -> str:
        self._conn.execute(
            "INSERT OR REPLACE INTO memories VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
            (item.id, item.content, item.role, item.scope, item.importance,
             item.salience, item.created_at, item.last_accessed_at,
             item.access_count, dumps(item.tags), item.source,
             dumps(item.metadata)),
        )
        self._conn.commit()
        return item.id

    def get(self, item_id: str) -> Optional[MemoryItem]:
        row = self._conn.execute(
            "SELECT * FROM memories WHERE id=?", (item_id,)).fetchone()
        return self._row_to_item(row) if row else None

    def update(self, item: MemoryItem) -> bool:
        if self.get(item.id) is None:
            return False
        self.add(item)
        return True

    def delete(self, item_id: str) -> bool:
        cur = self._conn.execute("DELETE FROM memories WHERE id=?", (item_id,))
        self._conn.commit()
        return cur.rowcount > 0

    def all(self) -> list:
        rows = self._conn.execute("SELECT * FROM memories").fetchall()
        return [self._row_to_item(r) for r in rows]

    def count(self) -> int:
        return self._conn.execute("SELECT COUNT(*) FROM memories").fetchone()[0]

    def clear(self) -> None:
        self._conn.execute("DELETE FROM memories")
        self._conn.commit()

    def flush(self) -> None:
        self._conn.commit()

    def close(self) -> None:
        self._conn.close()
