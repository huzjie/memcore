from memcore.util.textutil import normalize, is_blank, truncate
from memcore.util.hashutil import stable_hash, hash_text


def test_normalize():
    assert normalize("  Hello   World  ") == "hello world"


def test_blank():
    assert is_blank("   ") is True
    assert is_blank("x") is False


def test_truncate():
    assert len(truncate("a" * 100, 20)) == 20


def test_hash_stable():
    assert stable_hash("abc") == stable_hash("abc")
    assert 0 <= hash_text("abc") < 65536
