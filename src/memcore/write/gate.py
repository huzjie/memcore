"""写入门控：组合显著性 / 新颖性 / 重要性，决定是否写入长期记忆。"""
from __future__ import annotations

from dataclasses import dataclass, field

from ..core.constants import (
    GATE_IMPORTANCE_WEIGHT, GATE_SALIENCE_WEIGHT, GATE_NOVELTY_WEIGHT,
    GATE_WRITE_THRESHOLD,
)
from ..adapters.base import LLMAdapter
from .salience import salience_score
from .novelty import novelty_score
from .importance import importance_score


@dataclass
class GateResult:
    decision: bool
    score: float
    components: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {"decision": self.decision, "score": self.score,
                "components": self.components}


class WriteGate:
    """快慢记忆的「慢」入口：只有足够重要的内容才进长期记忆。

    评分 = w_imp * importance + w_sal * salience + w_nov * novelty
    """

    def __init__(self, llm: LLMAdapter,
                 weights: tuple = (GATE_IMPORTANCE_WEIGHT, GATE_SALIENCE_WEIGHT,
                                   GATE_NOVELTY_WEIGHT),
                 threshold: float = GATE_WRITE_THRESHOLD):
        self.llm = llm
        self.w_imp, self.w_sal, self.w_nov = weights
        self.threshold = threshold

    def evaluate(self, content: str, existing: list) -> GateResult:
        imp = importance_score(content, self.llm)
        sal = salience_score(content)
        nov = novelty_score(content, existing)
        score = self.w_imp * imp + self.w_sal * sal + self.w_nov * nov
        decision = score >= self.threshold
        return GateResult(
            decision=decision, score=round(score, 4),
            components={"importance": round(imp, 4), "salience": round(sal, 4),
                        "novelty": round(nov, 4)},
        )
