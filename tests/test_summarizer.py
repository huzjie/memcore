from memcore.consolidate.summarizer import Summarizer
from memcore.adapters.mock import MockLLM


def test_summarize():
    s = Summarizer(MockLLM())
    out = s.summarize(["偏好红色", "偏好简洁"])
    assert out.startswith("要点：")
