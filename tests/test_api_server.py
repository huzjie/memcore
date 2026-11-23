import json
import threading
import time
import urllib.request

from memcore.core.memory import Memory
from memcore.api.server import serve


def _get(url):
    return json.loads(urllib.request.urlopen(url).read().decode())


def test_server_health():
    srv = threading.Thread(target=serve,
                           args=(Memory(use_gate=False), "127.0.0.1", 8901),
                           daemon=True)
    srv.start()
    time.sleep(0.5)
    data = _get("http://127.0.0.1:8901/health")
    assert data["data"]["status"] == "ok"
