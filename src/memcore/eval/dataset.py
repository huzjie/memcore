"""内置评测数据集：事实 + 偏好两类记忆与查询对。"""
from __future__ import annotations

FACTS = [
    "用户的公司是用友网络，负责项目管理卓越中心",
    "用户偏好口语化、直接的表达风格，反感教科书式八股",
    "用户每周五需要提交周报，收件人是 shuangjinwei",
    "周报主题格式为：姓名 的周工作报告-起止日期",
    "用户常用红色 #E60012 作为品牌强调色",
    "项目监控看板正在从 MySQL 迁移到 PostgreSQL",
    "用户偏好结构化、观点鲜明的汇报材料",
    "团队例会定在每周一上午十点",
]
QUERIES = [
    ("用户在哪家公司工作？", ["0"]),
    ("周报要发给谁？", ["2"]),
    ("用户的写作风格偏好是什么？", ["1"]),
    ("品牌强调色是什么？", ["4"]),
]


def build_dataset() -> tuple:
    """返回 (facts, queries)，queries 为 (query, gold_indices)。"""
    return list(FACTS), list(QUERIES)
