from memcore.write.novelty import novelty_score
from memcore.core.types import MemoryItem


def test_duplicate_low():
    existing = [MemoryItem(content="用户偏好红色")]
    assert novelty_score("用户偏好红色", existing) < 0.5


def test_fresh_high():
    existing = [MemoryItem(content="用户偏好红色")]
    assert novelty_score("团队例会每周一", existing) > 0.5
