"""基础示例：快慢记忆 + 检索。"""
from memcore import Memory

mem = Memory(use_gate=False)
mem.remember_now("用户问：我的品牌色是什么？")
mem.add("用户的品牌强调色是红色 #E60012", force=True)
for r in mem.search("强调色"):
    print(f"[{r.score}] {r.item.content}")
print(mem.stats())
