"""显著性启发式打分：无需模型，规则抽取信号。"""
from __future__ import annotations

import re

_IMPERATIVE = ("必须", "不要", "禁止", "记住", "务必", "关键", "重要", "目标", "偏好", "下次")
_EMOTION = ("喜欢", "讨厌", "满意", "不满", "开心", "烦恼", "担心", "期待")
_NUM_RE = re.compile(r"\d{3,}|\d+\.?\d*%")


def salience_score(content: str) -> float:
    """基于启发式规则给内容打显著性分 [0,1]。"""
    text = content or ""
    score = 0.15
    if any(w in text for w in _IMPERATIVE):
        score += 0.25
    if any(w in text for w in _EMOTION):
        score += 0.15
    if _NUM_RE.search(text):
        score += 0.15
    if len(text) >= 40:
        score += 0.1
    if len(text) >= 100:
        score += 0.05
    return max(0.0, min(1.0, score))
