"""压测检索吞吐（简单计时）。"""
import time
from memcore import Memory

mem = Memory(use_gate=False)
for i in range(1000):
    mem.add(f"记忆条目 {i}，记录一些事实内容", force=True)

t0 = time.time()
for _ in range(100):
    mem.search("记忆条目")
dt = time.time() - t0
print(f"100 次检索耗时 {dt:.3f}s，平均 {dt/100*1000:.1f}ms")
