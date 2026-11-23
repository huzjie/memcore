import os
import tempfile
from memcore.store.sqlite_store import SqliteStore
from memcore.core.types import MemoryItem


def test_sqlite_roundtrip():
    d = tempfile.mkdtemp()
    s = SqliteStore(os.path.join(d, "m.db"))
    it = MemoryItem(content="sqlite 记忆", tags=["x"], metadata={"k": 1})
    s.add(it)
    got = s.get(it.id)
    assert got.content == "sqlite 记忆"
    assert got.tags == ["x"]
    assert got.metadata == {"k": 1}
    s.close()
