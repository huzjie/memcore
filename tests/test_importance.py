from memcore.write.importance import importance_score
from memcore.adapters.mock import MockLLM


def test_score_range():
    s = importance_score("用户必须记住偏好红色", MockLLM())
    assert 0.0 <= s <= 1.0
