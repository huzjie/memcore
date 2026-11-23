from memcore.consolidate.dedup import deduplicate
from memcore.core.types import MemoryItem


def test_dedup():
    items = [
        MemoryItem(content="用户偏好红色", importance=0.5),
        MemoryItem(content="用户偏好红色", importance=0.9),
    ]
    out = deduplicate(items)
    assert len(out) == 1
