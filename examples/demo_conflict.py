"""冲突检测示例：新记忆与旧记忆矛盾时告警。"""
from memcore import Memory
from memcore.write.conflict import detect_conflict

mem = Memory(use_gate=False)
mem.add("用户偏好红色作为强调色", force=True)

hits = detect_conflict("用户不再偏好红色，改用蓝色", mem.all())
print("检测到冲突的记忆数:", len(hits))
