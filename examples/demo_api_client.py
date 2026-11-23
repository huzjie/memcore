"""HTTP 客户端示例：调 /v1/memories。"""
import json
import urllib.request

BASE = "http://127.0.0.1:8080"


def post(path, payload):
    req = urllib.request.Request(
        BASE + path, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())


print(post("/v1/memories", {"content": "用户偏好红色", "force": True}))
print(post("/v1/memories/search", {"query": "偏好", "limit": 3}))
