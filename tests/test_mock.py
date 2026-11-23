from memcore.adapters.mock import MockLLM


def test_mock_score_numeric():
    llm = MockLLM()
    assert 0.0 <= llm.score("内容") <= 1.0


def test_mock_summarize():
    llm = MockLLM()
    out = llm.complete("请总结\n内容:a\n内容:b")
    assert "要点" in out
