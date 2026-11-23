"""写入门控示例：不重要的话被拒之门外。"""
from memcore import Memory

mem = Memory(use_gate=True)
items = [
    "今天天气不错，心情很好",        # 无长期价值，被门控拒绝
    "用户偏好口语化表达，反感八股",   # 重要，通过
    "用户每周五需要提交周报",         # 重要，通过
]
for c in items:
    it = mem.add(c)
    print(f"{'写' if it else '拒'} | {c}")
