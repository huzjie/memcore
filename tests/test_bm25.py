from memcore.embed.bm25 import BM25Index


def test_bm25_search():
    idx = BM25Index()
    idx.add(["生成", "发票"])
    idx.add(["天气", "不错"])
    res = idx.search(["发票"], top_k=1)
    assert res and res[0][0] == 0
