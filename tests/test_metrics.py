from memcore.eval.metrics import recall_at_k, mrr, retention_rate


def test_recall():
    assert recall_at_k(["a", "b"], ["a"], 5) == 1.0
    assert recall_at_k(["a", "b"], ["c"], 5) == 0.0


def test_mrr():
    assert mrr(["a", "b"], ["b"]) == 0.5


def test_retention():
    assert retention_rate(10, 5) == 0.5
