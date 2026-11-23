from memcore.eval.oracle import MemoryOracle
from memcore.eval.dataset import build_dataset


def test_oracle_runs():
    facts, queries = build_dataset()
    out = MemoryOracle().run(facts, queries)
    assert len(out["items"]) == len(facts)
    assert len(out["rows"]) == len(queries)
