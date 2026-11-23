"""HTTP 服务：标准库 http.server 实现，零第三方依赖。"""
from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from ..core.memory import Memory
from ..api.schema import ok, err, to_json, from_json


class _Handler(BaseHTTPRequestHandler):
    memory: Memory = None

    def _send(self, code: int, payload: dict) -> None:
        body = to_json(payload).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _body(self) -> dict:
        length = int(self.headers.get("Content-Length", "0"))
        if length <= 0:
            return {}
        return from_json(self.rfile.read(length).decode("utf-8"))

    def do_GET(self):
        if self.path == "/health":
            return self._send(200, ok({"status": "ok", **self.memory.stats()}))
        return self._send(404, err("not found", 404))

    def do_POST(self):
        data = self._body()
        if self.path == "/v1/memories":
            content = data.get("content", "")
            item = self.memory.add(content, force=data.get("force", False))
            return self._send(200, ok({
                "stored": item is not None,
                "item": item.to_dict() if item else None,
            }))
        if self.path == "/v1/memories/search":
            query = data.get("query", "")
            results = self.memory.search(query, limit=data.get("limit", 5))
            return self._send(200, ok({"results": [r.to_dict() for r in results]}))
        return self._send(404, err("not found", 404))

    def log_message(self, format, *args):
        pass


def serve(memory: Memory, host: str = "127.0.0.1", port: int = 8080):
    _Handler.memory = memory
    server = HTTPServer((host, port), _Handler)
    print(f"memcore server listening on http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
