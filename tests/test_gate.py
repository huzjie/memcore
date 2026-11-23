from memcore.write.gate import WriteGate
from memcore.adapters.mock import MockLLM


def test_gate_evaluate():
    g = WriteGate(MockLLM())
    res = g.evaluate("用户必须记住品牌色", [])
    assert 0.0 <= res.score <= 1.0
    assert isinstance(res.decision, bool)
