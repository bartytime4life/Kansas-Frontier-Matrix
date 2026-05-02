from __future__ import annotations

import argparse
import hashlib
import json
import logging
import mimetypes
import os
import tempfile
import threading
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse, unquote
from urllib.request import Request, urlopen

MODULE_VERSION = "1.0.0"
LOCAL_HOSTS = {"localhost", "127.0.0.1", "::1"}
REMOTE_PREFIXES = ("s3://", "gs://", "az://", "/vsicurl/", "/vsis3/", "/vsigs/", "/vsiaz/")


class ExitCode(Enum):
    SUCCESS = 0
    WARNING = 10
    EVIDENCE_REJECTED = 20
    MALFORMED_INPUT = 30
    HTTP_CONTRACT_FAILURE = 40
    SERVER_FAILURE = 50
    UNSAFE_URL_OR_PATH = 60
    INTERNAL_ERROR = 70


class ServeValidationError(Exception):
    def __init__(self, message: str, code: ExitCode):
        super().__init__(message)
        self.code = code


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canonical_blob(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for c in iter(lambda: f.read(1024 * 1024), b""):
            h.update(c)
    return h.hexdigest()


def write_canonical_json(path: Path, obj: Any, keep_temp: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix="tmp_", suffix=".json", dir=str(path.parent))
    tmp_path = Path(tmp_name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(obj, f, sort_keys=True, indent=2, ensure_ascii=False)
            f.write("\n")
        json.loads(tmp_path.read_text(encoding="utf-8"))
        os.replace(tmp_path, path)
    except Exception:
        if not keep_temp and tmp_path.exists():
            tmp_path.unlink()
        raise


def _load_json(path: Path, label: str) -> dict[str, Any]:
    if not path.exists():
        raise ServeValidationError(f"missing {label}", ExitCode.EVIDENCE_REJECTED)
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise ServeValidationError(f"malformed {label}: {e}", ExitCode.MALFORMED_INPUT)


def validate_publish_receipt(doc: dict[str, Any], release_root: Path, manifest_sha: str) -> None:
    if doc.get("schema") != "PublishReceipt.v1":
        raise ServeValidationError("invalid publish receipt schema", ExitCode.EVIDENCE_REJECTED)
    if doc.get("status") != "success":
        raise ServeValidationError("publish receipt status not success", ExitCode.EVIDENCE_REJECTED)
    if not doc.get("release_id") or not doc.get("publish_spec_hash"):
        raise ServeValidationError("publish receipt missing required fields", ExitCode.EVIDENCE_REJECTED)
    if doc.get("release_manifest_sha256") and doc.get("release_manifest_sha256") != manifest_sha:
        raise ServeValidationError("release_manifest_sha256 mismatch", ExitCode.EVIDENCE_REJECTED)
    rp = doc.get("release_path", "")
    if rp and Path(rp).name != release_root.name:
        raise ServeValidationError("release receipt does not match provided release_root", ExitCode.EVIDENCE_REJECTED)


def validate_release_manifest(doc: dict[str, Any], publish_receipt: dict[str, Any], release_root: Path) -> dict[str, str]:
    if doc.get("schema") != "ReleaseManifest.v1":
        raise ServeValidationError("invalid release manifest schema", ExitCode.EVIDENCE_REJECTED)
    if doc.get("release_id") != publish_receipt.get("release_id"):
        raise ServeValidationError("release_id mismatch", ExitCode.EVIDENCE_REJECTED)
    if doc.get("publish_spec_hash") != publish_receipt.get("publish_spec_hash"):
        raise ServeValidationError("publish_spec_hash mismatch", ExitCode.EVIDENCE_REJECTED)
    artifacts = doc.get("artifacts") or []
    if not artifacts:
        raise ServeValidationError("manifest artifacts empty", ExitCode.EVIDENCE_REJECTED)
    roles = {a.get("role"): a for a in artifacts}
    required = ["asset", "stac_catalog", "stac_collection", "stac_item"]
    for r in required:
        if r not in roles:
            raise ServeValidationError(f"missing required artifact role: {r}", ExitCode.EVIDENCE_REJECTED)
    return {
        "asset": roles["asset"]["path"],
        "catalog": roles["stac_catalog"]["path"],
        "collection": roles["stac_collection"]["path"],
        "item": roles["stac_item"]["path"],
    }


def validate_checksums_file(checksums_path: Path, required_paths: list[str], release_root: Path) -> dict[str, str]:
    if not checksums_path.exists():
        raise ServeValidationError("checksums file missing", ExitCode.EVIDENCE_REJECTED)
    mapping: dict[str, str] = {}
    for line in checksums_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split("  ")
        if len(parts) != 2:
            raise ServeValidationError("malformed checksums line", ExitCode.EVIDENCE_REJECTED)
        sha, rel = parts
        if len(sha) != 64 or sha.lower() != sha:
            raise ServeValidationError("invalid checksum hash", ExitCode.EVIDENCE_REJECTED)
        mapping[rel] = sha
        fp = (release_root / rel).resolve()
        if not fp.exists() or _sha256_file(fp) != sha:
            raise ServeValidationError("checksum mismatch", ExitCode.EVIDENCE_REJECTED)
    for p in required_paths:
        if p not in mapping:
            raise ServeValidationError(f"required artifact absent from checksums: {p}", ExitCode.EVIDENCE_REJECTED)
    return mapping


def validate_content_type(content_type: str, expected_ext: str) -> bool:
    ct = (content_type or "").split(";")[0].strip().lower()
    if expected_ext == ".json":
        return ct == "application/json"
    if expected_ext in (".tif", ".tiff"):
        return ct in {"image/tiff", "application/octet-stream"}
    if expected_ext == ".sha256":
        return ct == "text/plain"
    return True


class StaticHandler(BaseHTTPRequestHandler):
    root: Path

    def _safe(self, rel: str) -> Path | None:
        path = unquote(rel).lstrip("/")
        candidate = (self.root / path).resolve()
        if self.root.resolve() not in [candidate] and self.root.resolve() not in candidate.parents:
            return None
        if not candidate.exists() or not candidate.is_file():
            return None
        return candidate

    def _send_err(self, code: int, msg: str) -> None:
        body = _canonical_blob({"status": "error", "message": msg})
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def _serve(self, head_only: bool) -> None:
        p = self._safe(urlparse(self.path).path)
        if p is None:
            self._send_err(404, "not found")
            return
        data = p.read_bytes()
        total = len(data)
        ctype = "application/octet-stream"
        if p.suffix == ".json": ctype = "application/json"
        elif p.suffix in (".tif", ".tiff"): ctype = "image/tiff"
        elif p.suffix == ".sha256": ctype = "text/plain"
        range_h = self.headers.get("Range")
        if range_h:
            if "," in range_h:
                self.send_response(416); self.end_headers(); return
            unit, spec = range_h.split("=", 1)
            if unit != "bytes":
                self.send_response(416); self.end_headers(); return
            start, end = spec.split("-", 1)
            if start == "":
                n = int(end); chunk = data[-n:] if n <= total else data
                rs, re = total - len(chunk), total - 1
            else:
                rs = int(start); re = int(end) if end else total - 1
                if rs >= total or re < rs:
                    self.send_response(416); self.end_headers(); return
                re = min(re, total - 1)
                chunk = data[rs:re + 1]
            self.send_response(206)
            self.send_header("Accept-Ranges", "bytes")
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Range", f"bytes {rs}-{re}/{total}")
            self.send_header("Content-Length", str(len(chunk)))
            self.end_headers()
            if not head_only: self.wfile.write(chunk)
            return
        self.send_response(200)
        self.send_header("Accept-Ranges", "bytes")
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(total))
        self.end_headers()
        if not head_only:
            self.wfile.write(data)

    def do_GET(self): self._serve(False)
    def do_HEAD(self): self._serve(True)
    def log_message(self, format: str, *args: Any) -> None: return


def start_local_server(release_root: Path, host: str, port: int):
    if host == "0.0.0.0":
        raise ServeValidationError("public bind rejected", ExitCode.UNSAFE_URL_OR_PATH)
    handler = type("_H", (StaticHandler,), {})
    handler.root = release_root
    server = ThreadingHTTPServer((host, port), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


def stop_local_server(server: ThreadingHTTPServer, thread: threading.Thread) -> None:
    server.shutdown(); server.server_close(); thread.join(timeout=2)


def _request(url: str, method: str = "GET", headers: dict[str, str] | None = None) -> tuple[int, dict[str, str], bytes]:
    req = Request(url, method=method, headers=headers or {})
    try:
        with urlopen(req, timeout=5) as r:
            return r.status, dict(r.headers.items()), r.read()
    except HTTPError as e:
        return e.code, dict(e.headers.items()) if e.headers else {}, e.read() if hasattr(e, "read") else b""
    except URLError as e:
        raise ServeValidationError(f"http error: {e}", ExitCode.HTTP_CONTRACT_FAILURE)


def compute_serve_spec_hash(payload: dict[str, Any]) -> str:
    return _sha256_bytes(_canonical_blob(payload))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--publish-receipt", required=True)
    ap.add_argument("--release-manifest", required=True)
    ap.add_argument("--release-root", required=True)
    ap.add_argument("--mode", choices=["local-static-server", "existing-base-url"], required=True)
    ap.add_argument("--output-dir", required=True)
    ap.add_argument("--base-url")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=0)
    ap.add_argument("--range-start", type=int, default=0)
    ap.add_argument("--range-length", type=int, default=512)
    args = ap.parse_args()

    server = None; thread = None
    try:
        release_root = Path(args.release_root)
        pr_path = Path(args.publish_receipt); rm_path = Path(args.release_manifest)
        pr = _load_json(pr_path, "publish receipt")
        rm = _load_json(rm_path, "release manifest")
        validate_publish_receipt(pr, release_root, _sha256_file(rm_path))
        artifact_paths = validate_release_manifest(rm, pr, release_root)
        checksums = validate_checksums_file(release_root / "checksums.sha256", list(artifact_paths.values()), release_root)

        if args.mode == "existing-base-url":
            if not args.base_url:
                raise ServeValidationError("base-url required", ExitCode.MALFORMED_INPUT)
            parsed = urlparse(args.base_url)
            if parsed.hostname not in LOCAL_HOSTS:
                raise ServeValidationError("external base url rejected", ExitCode.UNSAFE_URL_OR_PATH)
            base_url = args.base_url if args.base_url.endswith("/") else args.base_url + "/"
        else:
            server, thread = start_local_server(release_root, args.host, args.port)
            base_url = f"http://{args.host}:{server.server_address[1]}/"

        catalog_url = urljoin(base_url, artifact_paths["catalog"])
        collection_url = urljoin(base_url, artifact_paths["collection"])
        item_url = urljoin(base_url, artifact_paths["item"])
        asset_url = urljoin(base_url, artifact_paths["asset"])

        for u in [catalog_url, collection_url, item_url]:
            st, h, b = _request(u)
            if st != 200:
                raise ServeValidationError("stac fetch failed", ExitCode.HTTP_CONTRACT_FAILURE)
            if not validate_content_type(h.get("Content-Type", ""), ".json"):
                raise ServeValidationError("bad json content-type", ExitCode.HTTP_CONTRACT_FAILURE)
            json.loads(b.decode("utf-8"))

        st, h, _ = _request(asset_url, method="HEAD")
        if st != 200:
            raise ServeValidationError("cog head failed", ExitCode.HTTP_CONTRACT_FAILURE)
        total = int(h.get("Content-Length", "0"))
        local_asset = release_root / artifact_paths["asset"]
        if total != local_asset.stat().st_size:
            raise ServeValidationError("head content-length mismatch", ExitCode.HTTP_CONTRACT_FAILURE)

        start = args.range_start
        end = start + args.range_length - 1
        st, h, b = _request(asset_url, headers={"Range": f"bytes={start}-{end}"})
        if st != 206:
            raise ServeValidationError("range request failed", ExitCode.HTTP_CONTRACT_FAILURE)
        expected = local_asset.read_bytes()[start:start + len(b)]
        if b != expected:
            raise ServeValidationError("range bytes mismatch", ExitCode.HTTP_CONTRACT_FAILURE)

        spec_hash = compute_serve_spec_hash({"release_id": pr["release_id"], "publish_spec_hash": pr["publish_spec_hash"], "checksums": checksums, "mode": args.mode})
        outdir = Path(args.output_dir); outdir.mkdir(parents=True, exist_ok=True)
        report_path = outdir / f"serve_validation_report_{spec_hash[:12]}.json"
        receipt_path = outdir / f"serve_access_receipt_{spec_hash[:12]}.json"
        report = {"schema": "ServeValidationReport.v1", "run_id": _sha256_bytes(_now().encode())[:16], "created_at_utc": _now(), "status": "success", "source": "soilgrids_serve_validate", "mode": args.mode, "base_url": base_url, "release_id": pr["release_id"], "publish_spec_hash": pr["publish_spec_hash"], "summary": {"total_checks": 1, "passed": 1, "failed": 0, "skipped": 0, "required_failed": 0, "warnings_failed": 0}, "checks": []}
        receipt = {"schema": "ServeAccessReceipt.v1", "run_id": report["run_id"], "created_at_utc": report["created_at_utc"], "status": "success", "source": "soilgrids_serve_validate", "mode": args.mode, "serve_spec_hash": spec_hash, "release_id": pr["release_id"], "release_root": str(release_root), "publish_receipt_path": str(pr_path), "release_manifest_path": str(rm_path), "serve_validation_report_path": str(report_path), "base_url": base_url}
        write_canonical_json(report_path, report)
        write_canonical_json(receipt_path, receipt)
        print(str(receipt_path))
        return ExitCode.SUCCESS.value
    except ServeValidationError as e:
        err = {"status": "error", "error_count": 1, "serve_access_receipt_path": None, "serve_validation_report_path": None, "release_id": None}
        print(json.dumps(err, sort_keys=True), file=os.sys.stderr)
        return e.code.value
    except Exception:
        err = {"status": "error", "error_count": 1, "serve_access_receipt_path": None, "serve_validation_report_path": None, "release_id": None}
        print(json.dumps(err, sort_keys=True), file=os.sys.stderr)
        return ExitCode.INTERNAL_ERROR.value
    finally:
        if server and thread:
            stop_local_server(server, thread)


if __name__ == "__main__":
    raise SystemExit(main())
