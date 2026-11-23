"""scope / tags 过滤检索示例。"""
from memcore import Memory

mem = Memory(use_gate=False)
mem.add("项目 A 的进度是 80%", scope="project-a", tags=["进度"], force=True)
mem.add("项目 B 的进度是 40%", scope="project-b", tags=["进度"], force=True)

for r in mem.search("进度"):
    print(f"[{r.item.scope}] {r.item.content}")
