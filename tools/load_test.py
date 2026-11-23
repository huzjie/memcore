"""HTTP 接口压测（并发）。"""
import json
import threading
import time
import urllib.request

URL = "http://127.0.0.1:8080/v1/memories/search"


def hit():
    req = urllib.request.Request(URL, data=json.dumps({"query": "偏好"}).encode(),
                                 headers={"Content-Type": "application/json"},
                                 method="POST")
    urllib.request.urlopen(req).read()


threads = [threading.Thread(target=hit) for _ in range(50)]
t0 = time.time()
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"50 并发完成，耗时 {time.time()-t0:.3f}s")
