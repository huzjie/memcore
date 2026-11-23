from memcore.forget.budget import BudgetEvictor
from memcore.forget.decay import DecayPolicy
from memcore.core.types import MemoryItem


def test_budget_evict():
    items = [MemoryItem(content=f"x{i}", importance=0.1 * i) for i in range(10)]
    keep, evicted = BudgetEvictor(max_items=5).evict(items, DecayPolicy())
    assert len(keep) + len(evicted) == 10
    assert len(keep) <= 5
