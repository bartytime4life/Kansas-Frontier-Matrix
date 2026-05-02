from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import stat
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

MODULE_VERSION = "1.0.0"
RELEASE_LAYOUT_VERSION = "1"
REMOTE_PREFIXES = ("http://", "https://", "s3://", "gs://", "az://", "/vsicurl/", "/vsis3/", "/vsigs/", "/vsiaz/")


class PublishError(Exception):
    def __init__(self, message: str, code: int = 40):
        super().__init__(message)
        self.code = code


@dataclass
class PublishInputs:
    paths: dict[str, Path]
    docs: dict[str, Any]
    hashes: dict[str, str]


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for c in iter(lambda: f.read(1024 * 1024), b""):
            h.update(c)
    return h.hexdigest()


def _canonical_blob(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def write_canonical_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def _is_remote(s: str) -> bool:
    return isinstance(s, str) and s.startswith(REMOTE_PREFIXES)


def load_publish_inputs(**kwargs: str) -> PublishInputs:
    paths = {k: Path(v) for k, v in kwargs.items()}
    docs, hashes = {}, {}
    for k, p in paths.items():
        if not p.exists():
            raise PublishError(f"missing input: {k}", 30)
        if k == "cog_asset":
            if _is_remote(str(p)):
                raise PublishError("remote paths are rejected", 40)
            hashes[f"{k}_sha256"] = _sha256_file(p)
            continue
        try:
            text = p.read_text(encoding="utf-8")
            docs[k] = json.loads(text)
            hashes[f"{k}_sha256"] = _sha256_bytes(text.encode("utf-8"))
        except json.JSONDecodeError as e:
            raise PublishError(f"malformed json for {k}: {e}", 30)
    return PublishInputs(paths=paths, docs=docs, hashes=hashes)


def validate_decision_envelope(d: dict[str, Any]) -> None:
    if d.get("schema") != "DecisionEnvelope.v1":
        raise PublishError("invalid decision envelope schema", 30)
    if d.get("decision") != "promote":
        raise PublishError("decision gate rejected", 20)
    if d.get("promotion", {}).get("eligible") is not True:
        raise PublishError("promotion is not eligible", 20)


def validate_validation_report(v: dict[str, Any]) -> None:
    if v.get("status") != "success":
        raise PublishError("validation report not successful", 40)
    if v.get("summary", {}).get("required_failed") != 0:
        raise PublishError("validation report has required failures", 40)
    if v.get("cross_layer", {}).get("provenance_chain_valid") is not True:
        raise PublishError("provenance chain invalid", 40)


def validate_publish_inputs(inp: PublishInputs, allow_symlinks: bool = False) -> None:
    d = inp.docs
    validate_decision_envelope(d["decision_envelope"])
    validate_validation_report(d["validation_report"])
    run, cog, stac = d["run_receipt"], d["cog_receipt"], d["stac_receipt"]
    if run.get("status") != "success" or cog.get("status") != "success" or stac.get("status") != "success":
        raise PublishError("broken receipt status chain")
    if cog.get("source_receipt", {}).get("spec_hash") != run.get("spec_hash"):
        raise PublishError("broken receipt chain")
    srs = stac.get("source_receipts", {})
    if srs.get("cog_spec_hash") != cog.get("spec_hash") or srs.get("run_spec_hash") != run.get("spec_hash"):
        raise PublishError("broken stac receipt chain")
    cogp = inp.paths["cog_asset"]
    if cogp.is_symlink() and not allow_symlinks:
        raise PublishError("symlink inputs rejected")
    sz = cogp.stat().st_size
    sha = _sha256_file(cogp)
    if sz <= 0 or sz != cog.get("output_bytes") or sz != stac.get("asset_bytes"):
        raise PublishError("cog size mismatch")
    if sha != cog.get("output_sha256") or sha != stac.get("asset_sha256"):
        raise PublishError("cog checksum mismatch")
    item, collection, catalog = d["stac_item"], d["stac_collection"], d["stac_catalog"]
    if item.get("collection") != collection.get("id"):
        raise PublishError("stac item collection mismatch")
    if item.get("id") != d["decision_envelope"].get("promotion", {}).get("item_id"):
        raise PublishError("item id mismatch")
    if collection.get("id") != d["decision_envelope"].get("promotion", {}).get("collection_id"):
        raise PublishError("collection id mismatch")
    if catalog.get("id") != d["decision_envelope"].get("promotion", {}).get("catalog_id"):
        raise PublishError("catalog id mismatch")
    asset = item.get("assets", {}).get("data", {})
    if asset.get("file:size") != sz:
        raise PublishError("stac asset size mismatch")
    if asset.get("file:checksum") != f"1220{sha}":
        raise PublishError("stac asset checksum mismatch")


def compute_publish_spec_hash(inp: PublishInputs, mode: str, catalog_root_mode: str, asset_href_mode: str, release_id_override: str | None = None) -> str:
    d = inp.docs
    payload = {
        "module_version": MODULE_VERSION,
        "publish_mode": mode,
        "catalog_root_mode": catalog_root_mode,
        "asset_href_mode": asset_href_mode,
        "release_id_override": release_id_override,
        "source_hashes": inp.hashes,
        "receipt_spec_hashes": {
            "run": d["run_receipt"].get("spec_hash"),
            "cog": d["cog_receipt"].get("spec_hash"),
            "stac": d["stac_receipt"].get("spec_hash"),
            "decision": d["decision_envelope"].get("spec_hash"),
        },
        "stac": {
            "item_id": d["stac_item"].get("id"),
            "collection_id": d["stac_collection"].get("id"),
            "catalog_id": d["stac_catalog"].get("id"),
            "bbox": d["stac_item"].get("bbox"),
            "license": d["stac_item"].get("properties", {}).get("license"),
            "dataset_datetime": d["stac_item"].get("properties", {}).get("datetime"),
        },
        "release_layout_version": RELEASE_LAYOUT_VERSION,
    }
    return _sha256_bytes(_canonical_blob(payload))


def compute_release_id(collection_id: str, dataset_datetime: str, publish_spec_hash: str, release_id_override: str | None = None) -> str:
    if release_id_override:
        if not re.match(r"^[A-Za-z0-9._-]+$", release_id_override):
            raise PublishError("invalid release id override", 30)
        return release_id_override
    slug = dataset_datetime.replace("-", "").replace(":", "")
    return f"{collection_id}_{slug}_{publish_spec_hash[:12]}"


def rewrite_stac_hrefs_for_release(item: dict[str, Any], collection: dict[str, Any], catalog: dict[str, Any], collection_id: str, item_id: str, cog_name: str, asset_href_mode: str, release_root: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any]]:
    irel = Path("stac") / "collections" / collection_id / "items" / f"{item_id}.json"
    crel = Path("stac") / "collections" / collection_id / "collection.json"
    rrel = Path("stac") / "catalog.json"
    arel = Path("assets") / "cog" / cog_name
    href = os.path.relpath(arel, irel.parent) if asset_href_mode == "relative" else str((release_root / arel).resolve())
    item = json.loads(json.dumps(item))
    collection = json.loads(json.dumps(collection))
    catalog = json.loads(json.dumps(catalog))
    item["assets"]["data"]["href"] = href
    for l in item.get("links", []):
        if l.get("rel") == "self": l["href"] = str(irel)
        if l.get("rel") == "root": l["href"] = str(rrel)
        if l.get("rel") == "collection": l["href"] = str(crel)
    for l in collection.get("links", []):
        if l.get("rel") == "self": l["href"] = str(crel)
        if l.get("rel") == "root": l["href"] = str(rrel)
    for l in catalog.get("links", []):
        if l.get("rel") in ("child", "collection"):
            l["href"] = str(Path("stac") / "collections" / collection_id / "collection.json")
        if l.get("rel") == "self":
            l["href"] = str(rrel)
    return item, collection, catalog


def build_release_manifest(release_id: str, publish_spec_hash: str, inp: PublishInputs, cog_name: str, asset_href: str) -> dict[str, Any]:
    d = inp.docs
    return {"schema": "ReleaseManifest.v1", "release_id": release_id, "release_layout_version": RELEASE_LAYOUT_VERSION,
            "created_at_utc": _now(), "source": "soilgrids_release_publish", "publish_spec_hash": publish_spec_hash,
            "collection_id": d["stac_collection"]["id"], "catalog_id": d["stac_catalog"]["id"], "item_id": d["stac_item"]["id"],
            "dataset_datetime": d["stac_item"]["properties"]["datetime"], "bbox": d["stac_item"]["bbox"],
            "license": d["stac_item"]["properties"].get("license"), "artifacts": [],
            "provenance": {"run_receipt_spec_hash": d["run_receipt"].get("spec_hash"), "cog_receipt_spec_hash": d["cog_receipt"].get("spec_hash"),
                           "stac_registration_spec_hash": d["stac_receipt"].get("spec_hash"), "decision_spec_hash": d["decision_envelope"].get("spec_hash"),
                           "validation_report_sha256": inp.hashes["validation_report_sha256"], "decision_envelope_sha256": inp.hashes["decision_envelope_sha256"]},
            "stac": {"catalog_path": "stac/catalog.json", "collection_path": f"stac/collections/{d['stac_collection']['id']}/collection.json",
                     "item_path": f"stac/collections/{d['stac_collection']['id']}/items/{d['stac_item']['id']}.json", "asset_href_mode": "relative", "asset_href": asset_href},
            "checksums_path": "checksums.sha256"}


def stage_release_tree(inp: PublishInputs, publish_root: Path, release_id: str, asset_href_mode: str) -> Path:
    staging = Path(tempfile.mkdtemp(prefix="stage_", dir=publish_root / ".staging")) / release_id
    (staging / "assets/cog").mkdir(parents=True)
    (staging / "stac/collections" / inp.docs["stac_collection"]["id"] / "items").mkdir(parents=True)
    (staging / "provenance").mkdir(parents=True)
    cog_name = inp.paths["cog_asset"].name
    shutil.copyfile(inp.paths["cog_asset"], staging / "assets/cog" / cog_name)
    item, col, cat = rewrite_stac_hrefs_for_release(inp.docs["stac_item"], inp.docs["stac_collection"], inp.docs["stac_catalog"], inp.docs["stac_collection"]["id"], inp.docs["stac_item"]["id"], cog_name, asset_href_mode, staging)
    write_canonical_json(staging / f"stac/collections/{inp.docs['stac_collection']['id']}/items/{inp.docs['stac_item']['id']}.json", item)
    write_canonical_json(staging / f"stac/collections/{inp.docs['stac_collection']['id']}/collection.json", col)
    write_canonical_json(staging / "stac/catalog.json", cat)
    for k, out in (("run_receipt", "run_receipt.json"), ("cog_receipt", "cog_receipt.json"), ("stac_receipt", "stac_registration_receipt.json"), ("validation_report", "validation_report.json"), ("decision_envelope", "decision_envelope.json")):
        shutil.copyfile(inp.paths[k], staging / "provenance" / out)
    return staging


def validate_staged_release(staging: Path) -> None:
    required = ["stac/catalog.json", "checksums.sha256", "release_manifest.json", "assets/cog"]
    for r in required:
        if not (staging / r).exists():
            raise PublishError(f"missing staged file: {r}")


def commit_release_atomically(staged_release_dir: Path, final_release_dir: Path) -> None:
    if final_release_dir.exists():
        raise PublishError("existing release directory", 40)
    os.replace(staged_release_dir, final_release_dir)


def update_latest_pointer(publish_root: Path, release_id: str, manifest: dict[str, Any], publish_spec_hash: str) -> None:
    obj = {"schema": "LatestReleasePointer.v1", "release_id": release_id, "release_path": f"releases/{release_id}", "release_manifest_path": f"releases/{release_id}/release_manifest.json", "stac_catalog_path": f"releases/{release_id}/stac/catalog.json", "item_id": manifest["item_id"], "collection_id": manifest["collection_id"], "publish_spec_hash": publish_spec_hash, "updated_at_utc": _now()}
    write_canonical_json(publish_root / "latest.json", obj)


def update_release_indexes(publish_root: Path, manifest: dict[str, Any], allow_item_republish: bool = False) -> None:
    idxd = publish_root / "indexes"
    ridx = idxd / "releases.json"
    iidx = idxd / "items.json"
    releases = {"schema": "ReleaseIndex.v1", "releases": []} if not ridx.exists() else json.loads(ridx.read_text())
    items = {"schema": "PublishedItemIndex.v1", "items": []} if not iidx.exists() else json.loads(iidx.read_text())
    rel = {"release_id": manifest["release_id"], "release_manifest_path": f"releases/{manifest['release_id']}/release_manifest.json", "stac_catalog_path": f"releases/{manifest['release_id']}/stac/catalog.json", "item_id": manifest["item_id"], "collection_id": manifest["collection_id"], "dataset_datetime": manifest["dataset_datetime"], "bbox": manifest["bbox"], "publish_spec_hash": manifest["publish_spec_hash"]}
    if any(r["release_id"] == rel["release_id"] for r in releases["releases"]):
        raise PublishError("duplicate release id", 40)
    releases["releases"].append(rel)
    releases["releases"].sort(key=lambda x: x["release_id"])
    item = {"item_id": manifest["item_id"], "collection_id": manifest["collection_id"], "release_id": manifest["release_id"], "stac_item_path": f"releases/{manifest['release_id']}/{manifest['stac']['item_path']}", "asset_path": f"releases/{manifest['release_id']}/assets/cog/{Path(manifest['stac']['asset_href']).name}", "bbox": manifest["bbox"], "dataset_datetime": manifest["dataset_datetime"], "asset_sha256": next(a["sha256"] for a in manifest["artifacts"] if a["role"] == "asset")}
    for i in items["items"]:
        if i["item_id"] == item["item_id"] and i["asset_sha256"] != item["asset_sha256"] and not allow_item_republish:
            raise PublishError("duplicate item conflict", 40)
    items["items"].append(item)
    items["items"].sort(key=lambda x: (x["collection_id"], x["item_id"], x["release_id"]))
    write_canonical_json(ridx, releases)
    write_canonical_json(iidx, items)


def build_publish_receipt(status: str, run_id: str, mode: str, release_id: str | None, publish_spec_hash: str | None, publish_root: Path, errors: list[str], **extra: Any) -> dict[str, Any]:
    return {"schema": "PublishReceipt.v1", "run_id": run_id, "created_at_utc": _now(), "status": status, "source": "soilgrids_release_publish", "mode": mode, "release_id": release_id, "publish_spec_hash": publish_spec_hash, "publish_root": str(publish_root), "errors": errors, **extra}


def publish_approved_bundle(inp: PublishInputs, publish_root: Path, mode: str = "immutable-release", catalog_root_mode: str = "latest-release", asset_href_mode: str = "relative", release_id_override: str | None = None, make_readonly: bool = False) -> tuple[dict[str, Any], int, Path]:
    run_id = hashlib.sha256(f"{_now()}|{mode}".encode()).hexdigest()[:16]
    publish_root.mkdir(parents=True, exist_ok=True)
    (publish_root / ".staging").mkdir(exist_ok=True)
    lock = publish_root / ".publish.lock"
    if lock.exists():
        raise PublishError("publish lock exists", 50)
    write_canonical_json(lock, {"run_id": run_id, "created_at_utc": _now()})
    try:
        validate_publish_inputs(inp)
        ps = compute_publish_spec_hash(inp, mode, catalog_root_mode, asset_href_mode, release_id_override)
        rid = compute_release_id(inp.docs["stac_collection"]["id"], inp.docs["stac_item"]["properties"]["datetime"], ps, release_id_override)
        manifest = build_release_manifest(rid, ps, inp, inp.paths["cog_asset"].name, f"../../../../assets/cog/{inp.paths['cog_asset'].name}")
        if mode == "dry-run":
            rpath = publish_root / ".dry_run" / f"publish_receipt_{ps[:12]}.json"
            receipt = build_publish_receipt("dry_run", run_id, mode, rid, ps, publish_root, [], release_manifest_path=None)
            write_canonical_json(rpath, receipt)
            return receipt, 5, rpath
        staged = stage_release_tree(inp, publish_root, rid, asset_href_mode)
        # checksums + manifest
        artifacts = []
        for rel, role, mtype in [
            (f"assets/cog/{inp.paths['cog_asset'].name}", "asset", "image/tiff; application=geotiff; profile=cloud-optimized"),
            (f"stac/collections/{manifest['collection_id']}/items/{manifest['item_id']}.json", "stac_item", "application/json"),
            (f"stac/collections/{manifest['collection_id']}/collection.json", "stac_collection", "application/json"),
            ("stac/catalog.json", "stac_catalog", "application/json"),
        ]:
            p = staged / rel
            artifacts.append({"role": role, "logical_name": role if role != "asset" else "data_cog", "path": rel, "media_type": mtype, "bytes": p.stat().st_size, "sha256": _sha256_file(p), "immutable": True})
        manifest["artifacts"] = artifacts
        write_canonical_json(staged / "release_manifest.json", manifest)
        lines = []
        for p in sorted([x for x in staged.rglob("*") if x.is_file()]):
            lines.append(f"{_sha256_file(p)}  {p.relative_to(staged).as_posix()}")
        (staged / "checksums.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8")
        validate_staged_release(staged)
        final = publish_root / "releases" / rid
        final.parent.mkdir(parents=True, exist_ok=True)
        commit_release_atomically(staged, final)
        if make_readonly:
            for p in final.rglob("*"):
                if p.is_file(): p.chmod(stat.S_IREAD | stat.S_IRGRP | stat.S_IROTH)
        update_latest_pointer(publish_root, rid, manifest, ps)
        update_release_indexes(publish_root, manifest)
        receipt = build_publish_receipt("success", run_id, mode, rid, ps, publish_root, [], release_path=str(final), release_manifest_path=str(final / "release_manifest.json"), checksums_path=str(final / "checksums.sha256"))
        rpath = final / "publish_receipt.json"
        write_canonical_json(rpath, receipt)
        return receipt, 0, rpath
    finally:
        if lock.exists():
            lock.unlink()


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser()
    for a in ["decision-envelope", "validation-report", "run-receipt", "cog-receipt", "stac-receipt", "stac-item", "stac-collection", "stac-catalog", "publish-root", "mode"]:
        p.add_argument(f"--{a}", required=True)
    p.add_argument("--catalog-root-mode", default="latest-release")
    p.add_argument("--asset-href-mode", default="relative")
    p.add_argument("--release-id")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)
    mode = "dry-run" if args.dry_run else args.mode
    try:
        inp = load_publish_inputs(decision_envelope=args.decision_envelope, validation_report=args.validation_report, run_receipt=args.run_receipt, cog_receipt=args.cog_receipt, stac_receipt=args.stac_receipt, stac_item=args.stac_item, stac_collection=args.stac_collection, stac_catalog=args.stac_catalog, cog_asset=json.loads(Path(args.stac_receipt).read_text()).get("asset_path"))
        receipt, code, rpath = publish_approved_bundle(inp, Path(args.publish_root), mode=mode, catalog_root_mode=args.catalog_root_mode, asset_href_mode=args.asset_href_mode, release_id_override=args.release_id)
        print(str(rpath))
        return code
    except PublishError as e:
        err = {"status": "error", "error_count": 1, "publish_receipt_path": None, "release_id": None}
        print(json.dumps(err), file=os.sys.stderr)
        return e.code
    except Exception:
        err = {"status": "error", "error_count": 1, "publish_receipt_path": None, "release_id": None}
        print(json.dumps(err), file=os.sys.stderr)
        return 70


if __name__ == "__main__":
    raise SystemExit(main())
