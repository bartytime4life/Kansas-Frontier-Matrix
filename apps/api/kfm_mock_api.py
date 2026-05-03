import json
from http.server import BaseHTTPRequestHandler,HTTPServer
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
class H(BaseHTTPRequestHandler):
  def _j(self,o,c=200): self.send_response(c);self.send_header("Content-Type","application/json");self.end_headers();self.wfile.write(json.dumps(o).encode())
  def do_GET(self):
    if self.path=="/healthz": return self._j({"status":"ok"})
    if self.path.startswith("/v1/evidence/"): return self._j(json.loads((ROOT/"fixtures/evidence/evidence_bundle.valid.json").read_text()))
    if self.path.startswith("/v1/drawer/"): return self._j(json.loads((ROOT/"fixtures/ui/evidence_drawer_payload.valid.json").read_text()))
    self._j({"outcome":"ERROR"},404)
  def do_POST(self):
    if self.path!="/v1/focus": return self._j({"outcome":"ERROR"},404)
    l=int(self.headers.get("Content-Length","0")); req=json.loads(self.rfile.read(l) or b"{}")
    q=req.get("question","")
    if "sensitive" in q.lower(): return self._j({"outcome":"DENY","citations":[]})
    return self._j({"outcome":"ANSWER","citations":["evb-hydro-001"]})
if __name__=="__main__": HTTPServer(("127.0.0.1",8000),H).serve_forever()
