"""遗忘示例：预算淘汰。"""
from memcore import Memory

mem = Memory(use_gate=False, max_items=50)
for i in range(100):
    mem.add(f"临时信息 {i}", force=True)
print("写入后:", mem.count())
n = mem.forget()
print("遗忘后:", mem.count(), "淘汰", n, "条")
