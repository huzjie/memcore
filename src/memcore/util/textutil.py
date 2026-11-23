"""文本工具：规范化、截断、空白判断。"""
from __future__ import annotations

import re

_WS = re.compile(r"\s+")


def normalize(text: str) -> str:
    """折叠空白、去首尾空格，返回小写。"""
    return _WS.sub(" ", text.strip()).lower()


def truncate(text: str, max_len: int = 200, ellipsis: str = "…") -> str:
    if len(text) <= max_len:
        return text
    return text[: max_len - len(ellipsis)] + ellipsis


def is_blank(text: str | None) -> bool:
    return text is None or not text.strip()
