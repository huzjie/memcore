"""持久化示例：JSON 文件后端，跨进程保留。"""
from memcore import Memory

mem = Memory(store_url="json://memory.json", use_gate=False)
mem.add("团队例会每周一上午十点", force=True)
print("已写入", mem.count(), "条")
# 再次运行本脚本，记忆仍在
