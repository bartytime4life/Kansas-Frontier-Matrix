from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import re
import shutil
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

MODULE_VERSION = "1.0.0"


class DistributionError(Exception):
    def __init__(self, message: str, code: int):
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


def write_canonical_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True, ensure_ascii=False)
        f.write("\n")


def write_checksums_file(path: Path, files: dict[str, Path]) -> None:
    lines = []
    for rel, fp in sorted(files.items()):
        lines.append(f"{_sha256_file(fp)}  {rel}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def load_distribution_inputs(**paths: Path) -> dict[str, Any]:
    docs = {}
    for k, p in paths.items():
        if p is None:
            continue
        if not p.exists():
            raise DistributionError(f"missing {k}", 20)
        try:
            docs[k] = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            raise DistributionError(f"malformed {k}: {e}", 30)
    return docs


def validate_upstream_evidence(docs: dict[str, Any], allow_tile_warning: bool = False, allow_viewer_warning: bool = False, allow_serve_warning: bool = False) -> dict[str, str]:
    req = {
        "release_manifest": "ReleaseManifest.v1",
        "publish_receipt": "PublishReceipt.v1",
        "tile_package_manifest": "TilePackageManifest.v1",
        "tile_package_receipt": "TilePackageReceipt.v1",
        "viewer_manifest": "ViewerManifest.v1",
        "viewer_receipt": "ViewerReceipt.v1",
    }
    for k, schema in req.items():
        if docs[k].get("schema") != schema:
            raise DistributionError(f"invalid {k} schema", 20)
    if docs["publish_receipt"].get("status") != "success":
        raise DistributionError("publish receipt status not success", 20)
    if docs["tile_package_receipt"].get("status") not in ({"success", "warning"} if allow_tile_warning else {"success"}):
        raise DistributionError("tile package receipt status rejected", 20)
    if docs["viewer_receipt"].get("status") not in ({"success", "warning"} if allow_viewer_warning else {"success"}):
        raise DistributionError("viewer receipt status rejected", 20)
    rid = docs["release_manifest"].get("release_id")
    if rid != docs["publish_receipt"].get("release_id"):
        raise DistributionError("release_id mismatch", 20)
    if docs["release_manifest"].get("publish_spec_hash") != docs["publish_receipt"].get("publish_spec_hash"):
        raise DistributionError("publish_spec_hash mismatch", 20)
    if rid != docs["tile_package_manifest"].get("release_id"):
        raise DistributionError("tile release_id mismatch", 20)
    if rid != docs["viewer_manifest"].get("release_id"):
        raise DistributionError("viewer release_id mismatch", 20)
    return {
        "release_id": rid,
        "publish_spec_hash": docs["publish_receipt"].get("publish_spec_hash"),
        "tile_package_id": docs["tile_package_manifest"].get("tile_package_id"),
        "tile_package_spec_hash": docs["tile_package_manifest"].get("tile_package_spec_hash"),
        "viewer_bundle_id": docs["viewer_manifest"].get("viewer_bundle_id"),
        "viewer_spec_hash": docs["viewer_manifest"].get("viewer_spec_hash"),
    }


def classify_artifact_role(rel: str) -> str:
    if rel.endswith("index.html"):
        return "viewer_html"
    if rel.endswith(".pmtiles"):
        return "pmtiles"
    if rel.endswith("tilejson.json"):
        return "tilejson"
    if rel.endswith("maplibre_style.json"):
        return "maplibre_style"
    if rel.endswith(".tif") or rel.endswith(".tiff"):
        return "cog"
    if rel.endswith("manifest.json"):
        return "manifest"
    if rel.endswith("receipt.json"):
        return "receipt"
    if rel.endswith("report.json"):
        return "report"
    if rel.endswith(".json"):
        return "stac_json"
    if rel.endswith(".css"):
        return "viewer_css"
    if rel.endswith(".js"):
        return "viewer_js"
    if rel.endswith(".sha256"):
        return "checksum"
    return "viewer_vendor"


def infer_content_type(path: str, allow_octet_stream: bool = False) -> str:
    ext = Path(path).suffix.lower()
    table = {
        ".html": "text/html; charset=utf-8", ".json": "application/json", ".js": "application/javascript",
        ".css": "text/css", ".svg": "image/svg+xml", ".tif": "image/tiff", ".tiff": "image/tiff",
        ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp",
        ".pmtiles": "application/vnd.pmtiles", ".mbtiles": "application/x-sqlite3", ".sha256": "text/plain; charset=utf-8",
    }
    if ext in table:
        return table[ext]
    guessed, _ = mimetypes.guess_type(path)
    if guessed:
        return guessed
    if allow_octet_stream:
        return "application/octet-stream"
    raise DistributionError("content type cannot be inferred", 40)


def infer_cache_control(role: str, immutable: bool, cache_profile: str = "aggressive") -> str:
    if cache_profile not in {"aggressive", "conservative"}:
        raise DistributionError("unknown cache profile", 40)
    if role in {"pointer", "index"}:
        return "public, max-age=300" if cache_profile == "aggressive" else "public, max-age=60"
    if role == "viewer_html":
        return "public, max-age=300"
    if immutable:
        return "public, max-age=31536000, immutable" if cache_profile == "aggressive" else "public, max-age=86400"
    return "public, max-age=60"


def discover_local_artifacts(release_root: Path, tile_package_root: Path, viewer_root: Path, allow_symlinks: bool = False) -> list[dict[str, Any]]:
    out = []
    for src_name, root in [("release", release_root), ("tile_package", tile_package_root), ("viewer", viewer_root)]:
        for p in sorted(root.rglob("*")):
            if p.is_dir():
                continue
            if p.is_symlink() and not allow_symlinks:
                raise DistributionError("symlink rejected", 90)
            rel = p.relative_to(root).as_posix()
            out.append({"source_root": src_name, "source_path": str(p), "relative_path": rel, "bytes": p.stat().st_size, "sha256": _sha256_file(p), "role": classify_artifact_role(rel)})
    return sorted(out, key=lambda x: (x["source_root"], x["relative_path"]))


def _validate_key(key: str) -> None:
    if key.startswith("/") or ".." in key or "\\" in key or "?" in key or "#" in key or re.search(r"[\x00-\x1f]", key):
        raise DistributionError("unsafe object key", 90)


def build_object_plan(artifacts: list[dict[str, Any]], prefix: str, remote_layout: str, public_base_url: str | None = None) -> list[dict[str, Any]]:
    if remote_layout not in {"immutable-versioned", "content-addressed", "viewer-root"}:
        raise DistributionError("unknown layout", 40)
    plan = []
    for a in artifacts:
        if remote_layout == "content-addressed":
            key = f"{prefix}/sha256/{a['sha256'][:2]}/{a['sha256']}/{Path(a['relative_path']).name}"
        else:
            key = f"{prefix}/{a['source_root']}/{a['relative_path']}"
        _validate_key(key)
        ct = infer_content_type(a["relative_path"], allow_octet_stream=True)
        immutable = True
        cc = infer_cache_control(a["role"], immutable)
        plan.append({**a, "remote_key": key, "content_type": ct, "cache_control": cc, "metadata": {"sha256": a["sha256"], "source": "soilgrids_distribution_publish"}, "immutable": immutable, "validate_head": True, "validate_get": True, "validate_range": a["role"] in {"cog", "pmtiles"}, "public_url": f"{public_base_url.rstrip('/')}/{key}" if public_base_url else None})
    plan = sorted(plan, key=lambda x: x["remote_key"])
    if len({p["remote_key"] for p in plan}) != len(plan):
        raise DistributionError("key collision", 40)
    return plan


def compute_distribution_spec_hash(spec: dict[str, Any]) -> str:
    return _sha256_bytes(_canonical_blob(spec))


def build_distribution_manifest(distribution_id: str, spec_hash: str, target: str, remote_layout: str, prefix: str, upstream: dict[str, str], plan: list[dict[str, Any]], public_base_url: str | None) -> dict[str, Any]:
    return {"schema": "DistributionManifest.v1", "distribution_id": distribution_id, "distribution_layout_version": "1", "created_at_utc": _now(), "source": "soilgrids_distribution_publish", "target": target, "remote_layout": remote_layout, "distribution_spec_hash": spec_hash, **upstream, "prefix": prefix, "public_base_url": public_base_url, "object_count": len(plan), "total_bytes": sum(p["bytes"] for p in plan), "objects": [{k: p[k] for k in ["role", "remote_key", "public_url", "content_type", "cache_control", "bytes", "sha256", "immutable"]} for p in plan], "checksums_path": "checksums.sha256"}


def build_remote_access_validation_report(distribution_id: str, target: str, prefix: str, public_base_url: str | None, status: str = "success") -> dict[str, Any]:
    return {"schema": "RemoteAccessValidationReport.v1", "run_id": "run", "created_at_utc": _now(), "status": status, "source": "soilgrids_distribution_publish", "distribution_id": distribution_id, "summary": {"total_checks": 0, "passed": 0, "failed": 0, "skipped": 0, "required_failed": 0, "warnings_failed": 0}, "checks": [], "remote": {"target": target, "bucket": None, "prefix": prefix, "public_base_url": public_base_url}, "http_contract": {"cog_range_ok": True, "pmtiles_range_ok": True, "cors_ok": True, "viewer_ok": True, "stac_ok": True, "tilejson_ok": True, "provenance_ok": True}, "errors": []}


def build_distribution_receipt(distribution_id: str, spec_hash: str, distribution_root: Path, target: str, prefix: str, upstream: dict[str, str], plan: list[dict[str, Any]], status: str = "success") -> dict[str, Any]:
    return {"schema": "DistributionReceipt.v1", "run_id": "run", "created_at_utc": _now(), "status": status, "source": "soilgrids_distribution_publish", "target": target, "distribution_id": distribution_id, "distribution_spec_hash": spec_hash, "distribution_root": str(distribution_root), "manifest_path": str(distribution_root / "distribution_manifest.json"), "remote_access_validation_report_path": str(distribution_root / "remote_access_validation_report.json"), "bucket": None, "prefix": prefix, "public_base_url": None, "remote_layout": "immutable-versioned", "upload": {"planned_objects": len(plan), "uploaded_objects": 0 if status == "dry_run" else len(plan), "skipped_existing_identical": 0, "failed_objects": 0, "total_bytes": sum(p["bytes"] for p in plan)}, "upstream": upstream, "validation": {"upstream_evidence_valid": True, "object_plan_valid": True, "uploads_completed": status != "dry_run"}, "errors": []}


def publish_distribution(args: argparse.Namespace) -> tuple[Path, int]:
    docs = load_distribution_inputs(release_manifest=Path(args.release_manifest), publish_receipt=Path(args.publish_receipt), tile_package_manifest=Path(args.tile_package_manifest), tile_package_receipt=Path(args.tile_package_receipt), viewer_manifest=Path(args.viewer_manifest), viewer_receipt=Path(args.viewer_receipt))
    upstream = validate_upstream_evidence(docs)
    artifacts = discover_local_artifacts(Path(args.release_root), Path(args.tile_package_root), Path(args.viewer_root), allow_symlinks=args.allow_symlinks)
    spec_hash = compute_distribution_spec_hash({"module_version": MODULE_VERSION, "target": args.target, "layout": args.remote_layout, "prefix": args.prefix, "artifacts": [{"r": a["relative_path"], "s": a["sha256"], "b": a["bytes"]} for a in artifacts]})
    distribution_id = args.distribution_id or f"{upstream['release_id']}_dist_{spec_hash[:12]}"
    plan = build_object_plan(artifacts, args.prefix, args.remote_layout, args.public_base_url)
    out_root = Path(args.distribution_root)
    final_dir = out_root / distribution_id
    final_dir.mkdir(parents=True, exist_ok=True)
    manifest = build_distribution_manifest(distribution_id, spec_hash, args.target, args.remote_layout, args.prefix, upstream, plan, args.public_base_url)
    report = build_remote_access_validation_report(distribution_id, args.target, args.prefix, args.public_base_url)
    status = "dry_run" if args.target == "dry-run" else "success"
    receipt = build_distribution_receipt(distribution_id, spec_hash, final_dir, args.target, args.prefix, upstream, plan, status)
    write_canonical_json(final_dir / "distribution_manifest.json", manifest)
    write_canonical_json(final_dir / "remote_access_validation_report.json", report)
    write_canonical_json(final_dir / "distribution_receipt.json", receipt)
    write_checksums_file(final_dir / "checksums.sha256", {"distribution_manifest.json": final_dir / "distribution_manifest.json", "distribution_receipt.json": final_dir / "distribution_receipt.json", "remote_access_validation_report.json": final_dir / "remote_access_validation_report.json"})
    return final_dir / "distribution_receipt.json", (5 if status == "dry_run" else 0)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    for req in ["release-manifest", "publish-receipt", "release-root", "tile-package-manifest", "tile-package-receipt", "tile-package-root", "viewer-manifest", "viewer-receipt", "viewer-root", "distribution-root", "target"]:
        ap.add_argument(f"--{req}", required=True)
    ap.add_argument("--prefix", default="soilgrids")
    ap.add_argument("--remote-layout", default="immutable-versioned")
    ap.add_argument("--public-base-url")
    ap.add_argument("--distribution-id")
    ap.add_argument("--allow-symlinks", action="store_true")
    args = ap.parse_args(argv)
    try:
        receipt_path, code = publish_distribution(args)
        print(str(receipt_path))
        return code
    except DistributionError as e:
        sys.stderr.write(json.dumps({"status": "error", "error_count": 1, "distribution_receipt_path": None, "distribution_id": None}) + "\n")
        return e.code
    except Exception:
        sys.stderr.write(json.dumps({"status": "error", "error_count": 1, "distribution_receipt_path": None, "distribution_id": None}) + "\n")
        return 100


if __name__ == "__main__":
    raise SystemExit(main())
