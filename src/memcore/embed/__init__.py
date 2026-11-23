"""零依赖嵌入与相似度：分词 / TF-IDF / BM25 / 特征哈希。"""
from .tokenizer import Tokenizer, DEFAULT_TOKENIZER
from .tfidf import TfidfIndex
from .bm25 import BM25Index
from .hashing import HashingVectorizer
from .vectors import cosine, dot, l2_norm, normalize_vec

__all__ = [
    "Tokenizer", "DEFAULT_TOKENIZER", "TfidfIndex", "BM25Index",
    "HashingVectorizer", "cosine", "dot", "l2_norm", "normalize_vec",
]
