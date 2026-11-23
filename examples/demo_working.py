"""快记忆窗口示例：最近 N 条自动淘汰最旧。"""
from memcore import Memory

mem = Memory(working_capacity=3)
for i in range(5):
    mem.remember_now(f"第 {i} 条消息")
print("快记忆窗口:", [m["content"] for m in mem.working.peek()])
