"""灌入演示数据。"""
from memcore import Memory

mem = Memory(store_url="json://memory.json", use_gate=False)
facts = [
    "用户公司是用友网络，负责项目管理卓越中心",
    "用户偏好口语化、直接的表达，反感八股",
    "用户每周五提交周报，收件人 shuangjinwei",
    "用户品牌强调色为红色 #E60012",
]
for f in facts:
    mem.add(f, force=True)
print("seeded", mem.count())
