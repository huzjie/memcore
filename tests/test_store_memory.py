from memcore.store.memory_store import MemoryStore
from memcore.core.types import MemoryItem


def test_add_get():
    s = MemoryStore()
    it = MemoryItem(content="x")
    s.add(it)
    assert s.get(it.id).content == "x"
    assert s.count() == 1


def test_delete():
    s = MemoryStore()
    it = MemoryItem(content="x")
    s.add(it)
    assert s.delete(it.id) is True
    assert s.delete(it.id) is False
