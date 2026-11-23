from memcore.eval.benchmark import Benchmark


def test_benchmark():
    r = Benchmark().run()
    assert "recall@5" in r
    assert "mrr" in r
    assert 0.0 <= r["recall@5"] <= 1.0
