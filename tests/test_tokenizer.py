from memcore.embed.tokenizer import Tokenizer


def test_tokenize_chinese():
    t = Tokenizer()
    toks = t.tokenize("生成一张发票")
    assert "生成" in toks or "发" in toks or "票" in toks


def test_stopwords_removed():
    t = Tokenizer(stopwords={"的"})
    assert "的" not in t.tokenize("红色的")


def test_bigrams():
    t = Tokenizer(bigrams=True)
    toks = t.tokenize("生成发票")
    assert "生成发票" in toks
