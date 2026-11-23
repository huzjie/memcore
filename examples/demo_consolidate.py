"""巩固示例：多条相关记忆压缩成高层记忆。"""
from memcore import Memory

mem = Memory(use_gate=False)
for i in range(8):
    mem.add(f"用户第 {i} 次提到偏好简洁排版", force=True)
print("巩固前:", mem.count())
n = mem.consolidate()
print("巩固后:", mem.count(), "合并掉", n, "条")
