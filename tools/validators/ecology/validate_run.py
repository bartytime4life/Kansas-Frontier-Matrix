#!/usr/bin/env python3
"""KFM ecology governed-ingestion fixture validator.

The canonical JSON implementation below is intentionally strict for this starter
fixture: it supports the I-JSON subset used here and rejects floats so Python's
native JSON number rendering cannot diverge from the RFC 8785/JCS intent.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import re
import struct
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

HUC12_RE = re.compile(r"^\d{12}$")
VALID_OUTCOMES = {"ANSWER", "ABSTAIN", "DENY", "ERROR"}
FORBIDDEN_PUBLIC_LANES = {"RAW", "WORK"}
PMTILES_HEADER_LEN = 127
PMTILES_MAX_FIXTURE_BYTES = 1_000_000


class ValidationError(Exception):
    """Raised when a validation gate fails closed."""


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        raise ValidationError(f"{path}: invalid JSON: {exc}") from exc


def write_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def reject_unsupported_json_numbers(obj: Any, at: str = "$.") -> None:
    if isinstance(obj, float):
        raise ValidationError(f"{at}: floats are not accepted by this fixture JCS implementation")
    if isinstance(obj, dict):
        for key, value in obj.items():
            if not isinstance(key, str):
                raise ValidationError(f"{at}: JSON object keys must be strings")
            reject_unsupported_json_numbers(value, f"{at}{key}.")
    elif isinstance(obj, list):
        for i, value in enumerate(obj):
            reject_unsupported_json_numbers(value, f"{at}[{i}].")
    elif isinstance(obj, int):
        # I-JSON interoperable integer range. This fixture does not need larger integers.
        if not (-(2**53) + 1 <= obj <= (2**53) - 1):
            raise ValidationError(f"{at}: integer outside I-JSON interoperable range")


def canonical_json_bytes(obj: Any) -> bytes:
    reject_unsupported_json_numbers(obj)
    return json.dumps(
        obj,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    if not path.exists():
        raise ValidationError(f"missing file: {path}")
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def spec_hash_for(obj: dict[str, Any], field: str = "spec_hash") -> str:
    clone = copy.deepcopy(obj)
    clone.pop(field, None)
    return sha256_bytes(canonical_json_bytes(clone))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def read_varint(buf: bytes, offset: int) -> tuple[int, int]:
    shift = 0
    result = 0
    while True:
        if offset >= len(buf):
            raise ValidationError("directory varint truncated")
        byte = buf[offset]
        offset += 1
        result |= (byte & 0x7F) << shift
        if byte < 0x80:
            return result, offset
        shift += 7
        if shift > 63:
            raise ValidationError("directory varint exceeds 64-bit range")


def rot(n: int, x: int, y: int, rx: int, ry: int) -> tuple[int, int]:
    if ry == 0:
        if rx == 1:
            x = n - 1 - x
            y = n - 1 - y
        x, y = y, x
    return x, y


def hilbert_index(z: int, x: int, y: int) -> int:
    n = 1 << z
    d = 0
    s = n // 2
    while s > 0:
        rx = 1 if (x & s) else 0
        ry = 1 if (y & s) else 0
        d += s * s * ((3 * rx) ^ ry)
        x, y = rot(s, x, y, rx, ry)
        s //= 2
    return d


def zxy_to_tileid(z: int, x: int, y: int) -> int:
    require(z >= 0, "z must be non-negative")
    limit = 1 << z
    require(0 <= x < limit and 0 <= y < limit, f"invalid z/x/y: {z}/{x}/{y}")
    return ((1 << (2 * z)) - 1) // 3 + hilbert_index(z, x, y)


def decode_position(data: bytes) -> dict[str, float]:
    lon, lat = struct.unpack("<ii", data)
    return {"lon": lon / 10_000_000, "lat": lat / 10_000_000}


@dataclass
class PMTilesHeader:
    root_offset: int
    root_length: int
    metadata_offset: int
    metadata_length: int
    leaf_offset: int
    leaf_length: int
    tile_data_offset: int
    tile_data_length: int
    num_addressed_tiles: int
    num_tile_entries: int
    num_tile_contents: int
    clustered: int
    internal_compression: int
    tile_compression: int
    tile_type: int
    min_zoom: int
    max_zoom: int
    min_position: dict[str, float]
    max_position: dict[str, float]
    center_zoom: int
    center_position: dict[str, float]


def parse_pmtiles_header(data: bytes) -> PMTilesHeader:
    require(len(data) >= PMTILES_HEADER_LEN, "PMTiles file is smaller than the 127-byte v3 header")
    require(data[:7] == b"PMTiles", "PMTiles magic number mismatch")
    require(data[7] == 3, f"PMTiles version mismatch: expected 3, got {data[7]}")
    fields = struct.unpack_from("<11Q", data, 8)
    flags = struct.unpack_from("<6B", data, 96)
    return PMTilesHeader(
        root_offset=fields[0],
        root_length=fields[1],
        metadata_offset=fields[2],
        metadata_length=fields[3],
        leaf_offset=fields[4],
        leaf_length=fields[5],
        tile_data_offset=fields[6],
        tile_data_length=fields[7],
        num_addressed_tiles=fields[8],
        num_tile_entries=fields[9],
        num_tile_contents=fields[10],
        clustered=flags[0],
        internal_compression=flags[1],
        tile_compression=flags[2],
        tile_type=flags[3],
        min_zoom=flags[4],
        max_zoom=flags[5],
        min_position=decode_position(data[102:110]),
        max_position=decode_position(data[110:118]),
        center_zoom=data[118],
        center_position=decode_position(data[119:127]),
    )


def decode_directory(buf: bytes) -> list[dict[str, int]]:
    n, offset = read_varint(buf, 0)
    require(n > 0, "PMTiles root directory must contain at least one entry")
    entries = [{"tile_id": 0, "run_length": 0, "length": 0, "offset": 0} for _ in range(n)]
    last_id = 0
    for i in range(n):
        delta, offset = read_varint(buf, offset)
        last_id += delta
        entries[i]["tile_id"] = last_id
    for i in range(n):
        entries[i]["run_length"], offset = read_varint(buf, offset)
    for i in range(n):
        entries[i]["length"], offset = read_varint(buf, offset)
        require(entries[i]["length"] > 0, f"directory entry {i}: length must be > 0")
    for i in range(n):
        value, offset = read_varint(buf, offset)
        if value == 0 and i > 0:
            prev = entries[i - 1]
            entries[i]["offset"] = prev["offset"] + prev["length"]
        else:
            require(value > 0, f"directory entry {i}: first offset cannot be encoded as 0")
            entries[i]["offset"] = value - 1
    require(offset == len(buf), "trailing bytes found after PMTiles root directory")
    return entries


def validate_crosswalk(path: Path) -> dict[str, Any]:
    obj = load_json(path)
    require(obj.get("object_type") == "HydrologyCrosswalk", f"{path}: object_type must be HydrologyCrosswalk")
    require(obj.get("table_name") == "huc12_comid_crosswalk", f"{path}: unexpected table_name")
    rows = obj.get("rows")
    require(isinstance(rows, list) and rows, f"{path}: rows must be a non-empty list")
    seen: set[str] = set()
    total_mappings = 0
    for i, row in enumerate(rows):
        huc12 = row.get("huc12")
        require(isinstance(huc12, str) and HUC12_RE.fullmatch(huc12), f"{path}: row {i} has malformed HUC12")
        require(huc12 not in seen, f"{path}: duplicate HUC12 {huc12}")
        seen.add(huc12)
        comids = row.get("comids")
        require(isinstance(comids, list) and comids, f"{path}: row {i} has empty COMID list")
        for comid in comids:
            require(isinstance(comid, int) and comid > 0, f"{path}: row {i} has invalid COMID {comid!r}")
        for required in ("source_version", "acquisition_date", "transform_id"):
            require(row.get(required), f"{path}: row {i} missing {required}")
        total_mappings += len(comids)
    provenance = obj.get("provenance", {})
    for required in ("source_system", "source_dataset", "source_version", "acquisition_date", "transform_id"):
        require(provenance.get(required), f"{path}: provenance missing {required}")
    return {"rows": len(rows), "mappings": total_mappings, "huc12_count": len(seen)}


def validate_tilejson(tilejson: dict[str, Any]) -> None:
    require(tilejson.get("tilejson") == "3.0.0", "TileJSON version must be 3.0.0")
    require(tilejson.get("format") == "pmtiles-v3", "TileJSON format must be pmtiles-v3")
    require(tilejson.get("kfm:delta") is True, "TileJSON must mark kfm:delta=true")
    layers = tilejson.get("vector_layers")
    require(isinstance(layers, list) and layers, "TileJSON vector_layers must be non-empty")
    matrix = tilejson.get("kfm:tile_matrix")
    require(isinstance(matrix, list) and matrix, "TileJSON kfm:tile_matrix must be non-empty")
    for t in matrix:
        require(all(k in t for k in ("z", "x", "y")), "each TileJSON tile matrix entry needs z/x/y")
        zxy_to_tileid(int(t["z"]), int(t["x"]), int(t["y"]))


def validate_pmtiles(pmtiles_path: Path, tilejson_path: Path) -> dict[str, Any]:
    data = pmtiles_path.read_bytes()
    require(len(data) <= PMTILES_MAX_FIXTURE_BYTES, f"{pmtiles_path}: fixture exceeds byte-size cap")
    header = parse_pmtiles_header(data)
    require(header.root_offset + header.root_length <= len(data), "root directory extends beyond file")
    require(PMTILES_HEADER_LEN + header.root_length <= 16_384, "header + root directory exceeds 16 KiB")
    require(header.metadata_offset + header.metadata_length <= len(data), "metadata extends beyond file")
    require(header.tile_data_offset + header.tile_data_length <= len(data), "tile data extends beyond file")
    require(header.internal_compression == 1, "fixture expects internal compression=None")
    require(header.tile_compression == 1, "fixture expects tile compression=None")
    require(header.tile_type == 1, "fixture expects PMTiles tile type=MVT Vector Tile")
    require(header.min_zoom <= header.max_zoom, "PMTiles min zoom exceeds max zoom")
    root_bytes = data[header.root_offset:header.root_offset + header.root_length]
    entries = decode_directory(root_bytes)
    require(len(entries) == header.num_tile_entries, "PMTiles header num_tile_entries mismatch")
    require(header.num_addressed_tiles >= len(entries), "PMTiles addressed-tile count is smaller than entries")
    for i, entry in enumerate(entries):
        require(entry["run_length"] > 0, f"entry {i}: leaf-directory entries are not expected in minimal fixture")
        end = entry["offset"] + entry["length"]
        require(end <= header.tile_data_length, f"entry {i}: tile data range extends beyond tile section")
    metadata_bytes = data[header.metadata_offset:header.metadata_offset + header.metadata_length]
    try:
        metadata = json.loads(metadata_bytes.decode("utf-8"))
    except Exception as exc:  # noqa: BLE001
        raise ValidationError(f"PMTiles metadata is not valid UTF-8 JSON: {exc}") from exc
    require(isinstance(metadata, dict), "PMTiles metadata must be a JSON object")
    require("vector_layers" in metadata, "MVT PMTiles metadata must include vector_layers")
    tilejson = load_json(tilejson_path)
    validate_tilejson(tilejson)
    require(metadata.get("vector_layers") == tilejson.get("vector_layers"), "TileJSON vector_layers mismatch")
    require(metadata.get("name") == tilejson.get("name"), "TileJSON name mismatch")
    require(header.min_zoom == tilejson.get("minzoom"), "TileJSON minzoom mismatch")
    require(header.max_zoom == tilejson.get("maxzoom"), "TileJSON maxzoom mismatch")
    actual_tileids = {e["tile_id"] for e in entries}
    requested_tileids = {zxy_to_tileid(int(t["z"]), int(t["x"]), int(t["y"])) for t in tilejson["kfm:tile_matrix"]}
    missing = sorted(requested_tileids - actual_tileids)
    require(not missing, f"PMTiles missing requested TileJSON z/x/y entries; tile_ids={missing}")
    return {
        "bytes": len(data),
        "entries": len(entries),
        "min_zoom": header.min_zoom,
        "max_zoom": header.max_zoom,
        "tile_ids": sorted(actual_tileids),
    }


def validate_spec_hash(obj: dict[str, Any], label: str) -> None:
    expected = spec_hash_for(obj)
    require(obj.get("spec_hash") == expected, f"{label}: stale spec_hash; expected {expected}, got {obj.get('spec_hash')}")


def validate_decision_log(path: Path) -> None:
    log = load_json(path)
    require(log.get("object_type") == "DecisionLog", "decision_log object_type mismatch")
    validate_spec_hash(log, "decision_log")
    outcomes = log.get("outcomes")
    require(isinstance(outcomes, list) and outcomes, "decision_log outcomes must be non-empty")
    for i, outcome in enumerate(outcomes):
        value = outcome.get("outcome")
        require(value in VALID_OUTCOMES, f"decision_log outcome {i} is not finite: {value!r}")
        require(value not in {"DENY", "ERROR"}, f"decision_log outcome {i} is fail-closed: {value}")
        if value == "ABSTAIN":
            require(outcome.get("abstain_permitted") is True, f"decision_log outcome {i}: ABSTAIN is not doctrine-permitted")
    require(not log.get("denials"), "decision_log contains denials")


def validate_evidence(root: Path, allow_unsigned: bool = False) -> dict[str, Any]:
    proof_dir = root / "data" / "proofs"
    evidence_path = proof_dir / "evidencebundle.json"
    decision_path = proof_dir / "decision_log.json"
    receipt_path = proof_dir / "run_receipt.json"
    evidence = load_json(evidence_path)
    require(evidence.get("object_type") == "EvidenceBundle", "evidence object_type mismatch")
    require(evidence.get("domain") == "ecology", "evidence domain must be ecology")
    require(evidence.get("policy_label") == "public", "evidence policy_label must be public")
    require(evidence.get("rights_status") == "open", "evidence rights_status must be open")
    require(evidence.get("sensitivity") == "public", "evidence sensitivity must be public")
    validate_spec_hash(evidence, "evidencebundle")
    require(isinstance(evidence.get("source_refs"), list) and evidence["source_refs"], "source_refs must be non-empty")
    require(isinstance(evidence.get("object_refs"), list) and evidence["object_refs"], "object_refs must be non-empty")
    result: dict[str, Any] = {"objects": {}}
    for ref in evidence["object_refs"]:
        path_value = ref.get("path")
        require(path_value, f"object_ref {ref.get('name')}: missing path")
        parts_upper = {p.upper() for p in Path(path_value).parts}
        require(not (parts_upper & FORBIDDEN_PUBLIC_LANES), f"object_ref {ref.get('name')}: RAW/WORK lane path is not public-safe")
        path = root / path_value
        actual_hash = sha256_file(path)
        require(actual_hash == ref.get("hash"), f"object_ref {ref.get('name')}: hash mismatch")
        if ref.get("type") == "table" and ref.get("name") == "huc12_comid_crosswalk":
            info = validate_crosswalk(path)
            require(info["rows"] == ref.get("rows"), "evidence table row count mismatch")
            result["objects"]["huc12_comid_crosswalk"] = info
        elif ref.get("type") == "pmtiles" and ref.get("name") == "pmtiles_delta_min":
            tilejson_path = root / ref.get("tilejson_ref", "")
            require(sha256_file(tilejson_path) == ref.get("tilejson_hash"), "object_ref pmtiles: tilejson hash mismatch")
            result["objects"]["pmtiles_delta_min"] = validate_pmtiles(path, tilejson_path)
        else:
            raise ValidationError(f"unsupported object_ref: {ref}")
    validate_decision_log(decision_path)
    receipt = load_json(receipt_path)
    require(receipt.get("object_type") == "RunReceipt", "receipt object_type mismatch")
    fingerprint_path = proof_dir / "run_receipt.fingerprint"
    expected_fp = sha256_bytes(canonical_json_bytes(receipt))
    require(fingerprint_path.exists(), "missing run_receipt.fingerprint")
    actual_fp = fingerprint_path.read_text(encoding="utf-8").strip()
    require(expected_fp == actual_fp, f"receipt fingerprint mismatch; expected {expected_fp}, got {actual_fp}")
    output_hashes = {o["name"]: o["sha256"] for o in receipt.get("outputs", []) if "name" in o and "sha256" in o}
    require(output_hashes.get("evidencebundle") == sha256_file(evidence_path), "receipt evidencebundle hash mismatch")
    require(output_hashes.get("decision_log") == sha256_file(decision_path), "receipt decision_log hash mismatch")
    if not allow_unsigned:
        bundle_dir = proof_dir / "cosign"
        for bundle_name in ("evidencebundle.bundle", "decision_log.bundle"):
            bundle_path = bundle_dir / bundle_name
            require(bundle_path.exists() and bundle_path.stat().st_size > 0, f"missing cosign bundle: {bundle_path}")
    result["receipt_fingerprint"] = expected_fp
    return result


def refresh_hashes(root: Path) -> None:
    proof_dir = root / "data" / "proofs"
    evidence_path = proof_dir / "evidencebundle.json"
    decision_path = proof_dir / "decision_log.json"
    receipt_path = proof_dir / "run_receipt.json"
    evidence = load_json(evidence_path)
    for ref in evidence["object_refs"]:
        path = root / ref["path"]
        ref["hash"] = sha256_file(path)
        if ref.get("type") == "table":
            ref["rows"] = validate_crosswalk(path)["rows"]
        if ref.get("type") == "pmtiles":
            ref["tilejson_hash"] = sha256_file(root / ref["tilejson_ref"])
    evidence["source_refs"][0]["hash"] = evidence["object_refs"][0]["hash"]
    evidence["spec_hash"] = spec_hash_for(evidence)
    write_json(evidence_path, evidence)
    decision = load_json(decision_path)
    decision["spec_hash"] = spec_hash_for(decision)
    write_json(decision_path, decision)
    receipt = load_json(receipt_path)
    receipt["generated_at"] = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    for item in receipt.get("inputs", []):
        if "path" in item:
            item["sha256"] = sha256_file(root / item["path"])
    for item in receipt.get("outputs", []):
        if item.get("name") == "evidencebundle":
            item["sha256"] = sha256_file(evidence_path)
        if item.get("name") == "decision_log":
            item["sha256"] = sha256_file(decision_path)
    write_json(receipt_path, receipt)
    fingerprint(root)


def fingerprint(root: Path) -> str:
    receipt_path = root / "data" / "proofs" / "run_receipt.json"
    receipt = load_json(receipt_path)
    fp = sha256_bytes(canonical_json_bytes(receipt))
    fp_path = root / "data" / "proofs" / "run_receipt.fingerprint"
    fp_path.write_text(fp + "\n", encoding="utf-8")
    return fp


def find_first_key(obj: Any, key: str) -> Any | None:
    if isinstance(obj, dict):
        if key in obj:
            return obj[key]
        for value in obj.values():
            found = find_first_key(value, key)
            if found is not None:
                return found
    elif isinstance(obj, list):
        for value in obj:
            found = find_first_key(value, key)
            if found is not None:
                return found
    return None


def record_signature(root: Path, signed_by: str) -> None:
    proof_dir = root / "data" / "proofs"
    receipt_path = proof_dir / "run_receipt.json"
    receipt = load_json(receipt_path)
    bundle_paths = {
        "evidencebundle": proof_dir / "cosign" / "evidencebundle.bundle",
        "decision_log": proof_dir / "cosign" / "decision_log.bundle",
    }
    entries = []
    for name, path in bundle_paths.items():
        require(path.exists() and path.stat().st_size > 0, f"missing bundle: {path}")
        bundle = load_json(path)
        entries.append({
            "artifact": name,
            "bundle": str(path.relative_to(root)),
            "bundle_sha256": sha256_file(path),
            "log_index": find_first_key(bundle, "logIndex"),
        })
    receipt["signed_by"] = signed_by
    receipt["signature_bundle"] = {
        "status": "present",
        "evidencebundle": "data/proofs/cosign/evidencebundle.bundle",
        "decision_log": "data/proofs/cosign/decision_log.bundle",
    }
    receipt["rekor"] = {"status": "present", "entries": entries}
    write_json(receipt_path, receipt)
    fingerprint(root)


def run_negative(root: Path) -> list[dict[str, str]]:
    cases: list[tuple[str, callable]] = [
        ("bad_huc12", lambda: validate_crosswalk(root / "data/fixtures/dlq_inputs/bad_huc12.json")),
        ("empty_comid_list", lambda: validate_crosswalk(root / "data/fixtures/dlq_inputs/empty_comid_list.json")),
        ("mismatched_tilejson", lambda: validate_pmtiles(root / "data/fixtures/tiles/pmtiles_delta_min.pmtiles", root / "data/fixtures/dlq_inputs/mismatched_tilejson.json")),
        ("malformed_pmtiles", lambda: validate_pmtiles(root / "data/fixtures/dlq_inputs/malformed_pmtiles.pmtiles", root / "data/fixtures/tiles/pmtiles_delta_min.tilejson.json")),
        ("stale_spec_hash", lambda: validate_spec_hash(load_json(root / "data/fixtures/dlq_inputs/stale_spec_hash_evidencebundle.json"), "stale_spec_hash_fixture")),
    ]
    entries: list[dict[str, str]] = []
    unexpected_passes: list[str] = []
    for name, fn in cases:
        try:
            fn()
        except ValidationError as exc:
            entries.append({"fixture": name, "status": "DLQ", "reason": str(exc)})
        else:
            unexpected_passes.append(name)
    report = {
        "schema_version": "v1",
        "dlq_policy": "malformed-fixtures-only",
        "generated_at": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "entries": entries,
    }
    write_json(root / "data" / "dlq" / "dlq_report.json", report)
    if unexpected_passes:
        raise ValidationError(f"negative fixtures unexpectedly passed: {unexpected_passes}")
    return entries


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate KFM ecology governed-ingestion fixtures")
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("validate", "negative", "refresh", "fingerprint"):
        p = sub.add_parser(name)
        p.add_argument("--root", default=".", type=Path)
        if name == "validate":
            p.add_argument("--allow-unsigned", action="store_true", help="Allow missing cosign bundles for local fixture validation")
    p = sub.add_parser("record-signature")
    p.add_argument("--root", default=".", type=Path)
    p.add_argument("--signed-by", required=True)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        if args.command == "validate":
            info = validate_evidence(root, allow_unsigned=args.allow_unsigned)
            print(json.dumps({"status": "PASS", **info}, indent=2))
        elif args.command == "negative":
            entries = run_negative(root)
            print(json.dumps({"status": "PASS", "dlq_entries": entries}, indent=2))
        elif args.command == "refresh":
            refresh_hashes(root)
            print(json.dumps({"status": "PASS", "message": "hashes and receipt fingerprint refreshed"}, indent=2))
        elif args.command == "fingerprint":
            fp = fingerprint(root)
            print(json.dumps({"status": "PASS", "run_receipt_fingerprint": fp}, indent=2))
        elif args.command == "record-signature":
            record_signature(root, args.signed_by)
            print(json.dumps({"status": "PASS", "message": "receipt signature metadata recorded"}, indent=2))
        return 0
    except ValidationError as exc:
        print(json.dumps({"status": "FAIL", "reason": str(exc)}, indent=2), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
