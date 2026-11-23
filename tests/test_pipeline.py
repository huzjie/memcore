from memcore.consolidate.pipeline import consolidate
from memcore.adapters.mock import MockLLM
from memcore.core.types import MemoryItem


def test_consolidate_reduces():
    items = [MemoryItem(content=f"偏好简洁 {i}") for i in range(4)]
    out = consolidate(items, MockLLM())
    assert len(out) < len(items)
