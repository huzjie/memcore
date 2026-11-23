from memcore.core.types import MemoryItem


def test_item_roundtrip():
    it = MemoryItem(content="hello", importance=0.8, tags=["a"])
    d = it.to_dict()
    it2 = MemoryItem.from_dict(d)
    assert it2.content == "hello"
    assert it2.importance == 0.8
    assert it2.tags == ["a"]


def test_touch():
    it = MemoryItem(content="x")
    it.touch()
    assert it.access_count == 1
