from memcore.consolidate.cluster import Clusterer
from memcore.core.types import MemoryItem


def test_cluster():
    items = [
        MemoryItem(content="偏好红色"), MemoryItem(content="偏好红色主题"),
        MemoryItem(content="会议在周一"),
    ]
    clusters = Clusterer(0.6).cluster(items)
    assert len(clusters) >= 2
