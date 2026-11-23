"""中英文分词：规则 + 停用词 + 二元组增强，零依赖。"""
from __future__ import annotations

import re

_STOPWORDS = {
    "的", "了", "和", "与", "或", "是", "在", "我", "你", "他", "她", "它",
    "我们", "你们", "他们", "这", "那", "有", "就", "都", "而", "及",
    "把", "被", "让", "给", "对", "从", "到", "中", "上", "下", "a", "an",
    "the", "of", "to", "in", "on", "for", "and", "or", "is", "are", "was",
    "were", "be", "it", "this", "that", "with", "as", "at", "by",
}
_TOKEN_RE = re.compile(r"[a-zA-Z0-9_]+|[\u4e00-\u9fff]")


class Tokenizer:
    """把文本切成 token 序列，支持停用词过滤与二元组。"""

    def __init__(self, stopwords: set | None = None, bigrams: bool = True):
        self.stopwords = stopwords if stopwords is not None else set(_STOPWORDS)
        self.bigrams = bigrams

    def tokenize(self, text: str) -> list:
        text = (text or "").lower()
        tokens = _TOKEN_RE.findall(text)
        tokens = [t for t in tokens if t not in self.stopwords and len(t) > 0]
        if not self.bigrams:
            return tokens
        # 对连续汉字做二元组，增强短语匹配（如 "发票 生成" -> "发票生成"）
        bigrams = []
        for i in range(len(tokens) - 1):
            a, b = tokens[i], tokens[i + 1]
            if a.isascii() or b.isascii():
                continue
            bigrams.append(a + b)
        return tokens + bigrams

    def terms(self, text: str) -> list:
        return self.tokenize(text)


DEFAULT_TOKENIZER = Tokenizer()
