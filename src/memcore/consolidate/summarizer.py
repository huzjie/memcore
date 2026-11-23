"""总结器：把一组记忆内容压缩成一条高层记忆。"""
from __future__ import annotations

from ..adapters.base import LLMAdapter

_PROMPT = (
    "请把以下多条相关记忆总结成一条简洁的高层记忆，保留关键事实与用户偏好，"
    "只输出总结文本本身。\n"
)


class Summarizer:
    def __init__(self, llm: LLMAdapter):
        self.llm = llm

    def summarize(self, contents: list) -> str:
        if not contents:
            return ""
        lines = "\n".join(f"内容:{c}" for c in contents)
        return self.llm.complete(_PROMPT + lines, max_tokens=256).strip()
