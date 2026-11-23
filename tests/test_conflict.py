from memcore.write.conflict import detect_conflict
from memcore.core.types import MemoryItem


def test_no_conflict_empty():
    assert detect_conflict("新内容", []) == []
