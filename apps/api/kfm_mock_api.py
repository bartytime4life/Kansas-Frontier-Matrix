import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _load_fixture(path: str) -> dict:
    return json.loads((ROOT / path).read_text())


def _resolver_state() -> tuple[dict, dict, dict]:
    return (
        _load_fixture("fixtures/evidence/evidence_ref.valid.json"),
        _load_fixture("fixtures/evidence/evidence_bundle.valid.json"),
        _load_fixture("fixtures/source/source_descriptor.valid.json"),
    )


def _evidence_closure() -> tuple[str, str]:
    evidence_ref, bundle, source = _resolver_state()
    if evidence_ref.get("bundle_id") != bundle.get("id"):
        return "ABSTAIN", "MISSING_EVIDENCE"
    if evidence_ref.get("id") not in bundle.get("evidence_refs", []):
        return "ABSTAIN", "MISSING_EVIDENCE"
    if source.get("source_role") is None or source.get("activation_status") != "synthetic_only":
        return "ERROR", "INVALID_RESOLVER_STATE"
    if source.get("rights_status") == "UNKNOWN" and source.get("public_release_allowed") is True:
        return "DENY", "POLICY_BLOCKED"
    return "ANSWER", "RESOLVED"


def get_evidence_bundle(evidence_bundle_id: str) -> tuple[dict, int]:
    bundle = _load_fixture("fixtures/evidence/evidence_bundle.valid.json")
    if evidence_bundle_id not in {bundle.get("id"), "evb-hydro-001"}:
        return {"outcome": "ABSTAIN", "reason": "MISSING_EVIDENCE"}, 404
    bundle_out = dict(bundle)
    if evidence_bundle_id == "evb-hydro-001":
        bundle_out["id"] = "evb-hydro-001"
    return bundle_out, 200


def get_drawer(drawer_id: str) -> tuple[dict, int]:
    drawer = _load_fixture("fixtures/ui/evidence_drawer_payload.valid.json")
    if drawer_id != drawer.get("id"):
        unresolved = {"outcome": "ABSTAIN", "reason": "MISSING_EVIDENCE", **dict(drawer)}
        unresolved["ui_trust_state"] = "EVIDENCE_MISSING"
        unresolved["release_status"] = "ABSTAIN"
        return unresolved, 404
    return drawer, 200


def focus_decision(request: dict) -> tuple[dict, int]:
    question = str(request.get("question", "")).strip().lower()
    if not question:
        return {"outcome": "ABSTAIN", "reason": "EMPTY_QUERY"}, 400
    if "missing" in question:
        return {"outcome": "ABSTAIN", "reason": "MISSING_EVIDENCE", "citations": []}, 200
    if "policy blocked" in question or "sensitive" in question:
        return {"outcome": "DENY", "reason": "DENIED_BY_POLICY", "citations": []}, 200
    outcome, reason = _evidence_closure()
    if outcome == "ANSWER":
        return {
            "outcome": "ANSWER",
            "reason": reason,
            "citations": ["evr-hydro-synth-001", "evb-hydro-synth-001"],
        }, 200
    if outcome == "DENY":
        return {"outcome": "DENY", "reason": reason, "citations": []}, 200
    if outcome == "ABSTAIN":
        return {"outcome": "ABSTAIN", "reason": reason, "citations": []}, 200
    return {"outcome": "ERROR", "reason": reason, "citations": []}, 500


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format: str, *args) -> None:
        # Keep validation/test output clean in synthetic baseline runs.
        return

    def _json(self, payload: dict, code: int = 200) -> None:
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(payload).encode())

    def do_GET(self) -> None:
        if self.path == "/healthz":
            return self._json({"status": "ok"})
        if self.path.startswith("/v1/evidence/"):
            bundle_id = self.path.rsplit("/", 1)[-1]
            payload, code = get_evidence_bundle(bundle_id)
            return self._json(payload, code)
        if self.path.startswith("/v1/drawer/"):
            drawer_id = self.path.rsplit("/", 1)[-1]
            payload, code = get_drawer(drawer_id)
            return self._json(payload, code)
        return self._json({"outcome": "ERROR", "reason": "NOT_FOUND"}, 404)

    def do_POST(self) -> None:
        if self.path != "/v1/focus":
            return self._json({"outcome": "ERROR", "reason": "NOT_FOUND"}, 404)
        body_len = int(self.headers.get("Content-Length", "0"))
        request = json.loads(self.rfile.read(body_len) or b"{}")
        payload, code = focus_decision(request)
        return self._json(payload, code)


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
