"""确定性 Mock LLM：不接网络也能复现「打分/总结」完整链路。"""
from __future__ import annotations

import re

from .base import LLMAdapter


class MockLLM(LLMAdapter):
    """基于规则的确定性后端，用于离线评测与 CI。

    - 打分：从 prompt 中抽取启发式信号（长度、关键词、数字）。
    - 总结：把多条内容合并成一行「要点摘要」。
    """

    _SALIENCE_WORDS = ("必须", "重要", "记住", "偏好", "不要", "禁止", "关键", "目标")

    def complete(self, prompt: str, max_tokens: int = 256) -> str:
        if "总结" in prompt or "summary" in prompt.lower():
            return self._summarize(prompt)
        return self._score_text(prompt)

    def _score_text(self, prompt: str) -> str:
        # 只对「信息：」后的正文打分，避免 prompt 模板里的关键词干扰
        marker = "信息："
        text = prompt.split(marker, 1)[1] if marker in prompt else prompt
        score = 0.2
        if any(w in text for w in self._SALIENCE_WORDS):
            score += 0.4
        if any(w in text for w in ("喜欢", "讨厌", "偏好", "习惯", "需要", "负责")):
            score += 0.2
        if re.search(r"\d{4}", text):
            score += 0.1
        if len(text) > 80:
            score += 0.1
        return f"{min(score, 1.0):.3f}"

    def _summarize(self, prompt: str) -> str:
        # 提取「内容:」后的正文，取若干条合并
        lines = [ln for ln in prompt.splitlines() if ln.strip() and "内容:" in ln]
        parts = []
        for ln in lines[:8]:
            parts.append(ln.split("内容:", 1)[1].strip()[:60])
        if not parts:
            parts = [ln.strip()[:60] for ln in prompt.splitlines() if ln.strip()][:5]
        body = "；".join(parts)
        return f"要点：{body}" if body else "要点：无"
