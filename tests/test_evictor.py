from memcore.forget.evictor import Evictor
from memcore.core.types import MemoryItem


def test_no_evict_under_limit():
    items = [MemoryItem(content="x") for _ in range(5)]
    assert Evictor(max_items=10).select(items) == []


def test_evict_over_limit():
    items = [MemoryItem(content=f"x{i}") for i in range(50)]
    victims = Evictor(max_items=10).select(items)
    assert len(victims) > 0
