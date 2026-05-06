import io
import json
import tarfile
from pathlib import Path

from .checksums import sha256_path
from .constants import FORBIDDEN_RECEIPT_TRUE, REQUIRED_L27
from .ids import cjson, sid
from .loaders import loadj
from .manifest import validate_manifest, validate_path_safe
from .receipts import make_receipt


def _wj(p, o):
    Path(p).write_text(json.dumps(o, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _wjl(p, rows):
    Path(p).write_text("".join(cjson(r) + "\n" for r in rows), encoding="utf-8")


def _build_packet(out_dir: Path):
    packet = out_dir / "closure_archive_index_packet.tar.gz"
    members = sorted(
        [p for p in out_dir.iterdir() if p.is_file() and p.name != packet.name],
        key=lambda p: p.name,
    )
    with tarfile.open(packet, "w:gz", format=tarfile.PAX_FORMAT, compresslevel=9) as tf:
        for p in members:
            if ".." in p.name or p.name.startswith("/"):
                raise ValueError("INVALID_PACKET_MEMBER_PATH")
            data = p.read_bytes()
            ti = tarfile.TarInfo(name=p.name)
            ti.size = len(data)
            ti.mtime = 0
            ti.mode = 0o644
            ti.uid = ti.gid = 0
            ti.uname = ti.gname = ""
            tf.addfile(ti, io.BytesIO(data))
    return sha256_path(packet)


def run_closure_archive_index_plan(manifest_path, out_dir, created_at):
    m = loadj(manifest_path)
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    e = []
    e.extend(validate_manifest(m))
    d = m.get("layer27_inputs", {})
    for k in sorted(REQUIRED_L27):
        p = d.get(k)
        if not p:
            e.append(f"MISSING_REQUIRED_INPUT:layer27_inputs:{k}")
            continue
        if not validate_path_safe(p):
            e.append(f"UNSAFE_PATH:layer27_inputs:{k}")
            continue
        if not Path(p).exists():
            e.append(f"MISSING_INPUT_FILE:layer27_inputs:{k}")
    r = make_receipt(m.get("manifest_id"), created_at, e)
    if e:
        _wj(out / "closure_archive_index_receipt.json", r)
        return r
    ar = loadj(d["preservation_closure_audit_receipt_json"])
    if ar.get("object_type") != "AirNowPreservationClosureAuditReceipt":
        e.append("INVALID_LAYER27_AUDIT_RECEIPT_OBJECT_TYPE")
    for f in FORBIDDEN_RECEIPT_TRUE:
        if ar.get(f) is True:
            e.append(f"L27_RECEIPT_FORBIDDEN:{f}")
    if e:
        r = make_receipt(m.get("manifest_id"), created_at, e)
        _wj(out / "closure_archive_index_receipt.json", r)
        return r

    inv = []
    for k, v in sorted(d.items()):
        p = Path(v)
        inv.append({"record_id": sid("layer28inv", [m.get("manifest_id"), k]), "input_key": k, "path": v, "sha256": sha256_path(p), "byte_size": p.stat().st_size, "created_at": created_at})
    inv = sorted(inv, key=lambda x: x["record_id"])
    _wj(out / "closure_archive_index_manifest.resolved.json", {"object_type": "AirNowClosureArchiveIndexManifestResolved", "manifest_id": m.get("manifest_id"), "created_at": created_at})
    _wj(out / "closure_archive_index_input_inventory.json", {"object_type": "AirNowClosureArchiveIndexInputInventory", "records": inv, "created_at": created_at}); _wjl(out / "closure_archive_index_input_inventory.jsonl", inv)
    scope = [{"scope_id": sid("scope", [x["input_key"]]), "scope_key": x["input_key"], "internal_only": True} for x in inv]; scope = sorted(scope, key=lambda x: x["scope_id"])
    _wj(out / "closure_archive_scope_index.json", {"object_type": "AirNowClosureArchiveScopeIndex", "records": scope, "created_at": created_at}); _wjl(out / "closure_archive_scope_index.jsonl", scope)
    member = [{"member_id": sid("member", [x["record_id"]]), "record_id": x["record_id"], "planned_index_action": "INTERNAL_INDEX_PLAN_ONLY"} for x in inv]
    member = sorted(member, key=lambda x: x["member_id"])
    _wj(out / "closure_archive_member_index_plan.json", {"object_type": "AirNowClosureArchiveMemberIndexPlan", "records": member, "created_at": created_at}); _wjl(out / "closure_archive_member_index_plan.jsonl", member)
    h = [{"hash_id": sid("hash", [x["sha256"]]), "sha256": x["sha256"], "source_record_id": x["record_id"]} for x in inv]
    hc = loadj(d["preservation_closure_hash_chain_json"]).get("hashes", [])
    for z in hc:
        h.append({"hash_id": sid("hashchain", [z]), "sha256": z, "source_record_id": "layer27_hash_chain"})
    h = sorted(h, key=lambda x: x["hash_id"]); _wj(out / "closure_archive_hash_index.json", {"object_type": "AirNowClosureArchiveHashIndex", "records": h, "created_at": created_at}); _wjl(out / "closure_archive_hash_index.jsonl", h)
    rec = loadj(d["preservation_closure_receipt_ledger_json"]).get("records", []); ri = sorted([{"receipt_index_id": sid("ridx", [i]), "source": x} for i, x in enumerate(rec)], key=lambda x: x["receipt_index_id"])
    _wj(out / "closure_archive_receipt_index.json", {"object_type": "AirNowClosureArchiveReceiptIndex", "records": ri, "created_at": created_at}); _wjl(out / "closure_archive_receipt_index.jsonl", ri)
    dec = loadj(d["preservation_closure_decision_ledger_json"]).get("records", []); di = sorted([{"decision_index_id": sid("didx", [i]), "source": x} for i, x in enumerate(dec)], key=lambda x: x["decision_index_id"])
    _wj(out / "closure_archive_decision_index.json", {"object_type": "AirNowClosureArchiveDecisionIndex", "records": di, "created_at": created_at}); _wjl(out / "closure_archive_decision_index.jsonl", di)
    pol = loadj(d["preservation_closure_policy_ledger_json"]).get("records", []); pi = sorted([{"policy_index_id": sid("pidx", [i]), "source": x} for i, x in enumerate(pol)], key=lambda x: x["policy_index_id"])
    _wj(out / "closure_archive_policy_index.json", {"object_type": "AirNowClosureArchivePolicyIndex", "records": pi, "created_at": created_at}); _wjl(out / "closure_archive_policy_index.jsonl", pi)
    _wj(out / "closure_archive_caveat_index.json", {"object_type": "AirNowClosureArchiveCaveatIndex", "record": loadj(d["preservation_closure_caveat_registry_json"]), "created_at": created_at})
    li = loadj(d["preservation_closure_lineage_graph_json"]).get("edges", []); lr = sorted([{"lineage_index_id": sid("lidx", [i]), "edge": x} for i, x in enumerate(li)], key=lambda x: x["lineage_index_id"])
    _wj(out / "closure_archive_lineage_index.json", {"object_type": "AirNowClosureArchiveLineageIndex", "records": lr, "created_at": created_at}); _wjl(out / "closure_archive_lineage_index.jsonl", lr)
    ai = sorted([{"access_id": sid("acc", [x["record_id"]]), "record_id": x["record_id"], "classification": "INTERNAL_SENSITIVE", "public_access_allowed": False} for x in inv], key=lambda x: x["access_id"])
    _wj(out / "closure_archive_access_index.json", {"object_type": "AirNowClosureArchiveAccessIndex", "records": ai, "created_at": created_at}); _wjl(out / "closure_archive_access_index.jsonl", ai)
    sk = sorted([{"search_key_id": sid("sk", [x["record_id"]]), "record_id": x["record_id"], "search_key": f"internal::{x['input_key']}"} for x in inv], key=lambda x: x["search_key_id"])
    _wj(out / "closure_archive_search_key_plan.json", {"object_type": "AirNowClosureArchiveSearchKeyPlan", "records": sk, "created_at": created_at}); _wjl(out / "closure_archive_search_key_plan.jsonl", sk)
    _wjl(out / "closure_archive_blockers.jsonl", [])
    _wj(out / "closure_archive_non_execution_attestation.json", {"object_type": "AirNowClosureArchiveNonExecutionAttestation", "index_executed": False, "database_write_executed": False, "search_service_created": False, "public_catalog_created": False, "closure_executed": False, "created_at": created_at})
    _wj(out / "closure_archive_readiness_summary.json", {"object_type": "AirNowClosureArchiveReadinessSummary", "status": "READY_FOR_INTERNAL_INDEX_PLANNING_ONLY", "created_at": created_at})
    _wj(out / "closure_archive_rerun_plan.json", {"object_type": "AirNowClosureArchiveRerunPlan", "steps": [], "created_at": created_at})
    _wj(out / "closure_archive_status_board.json", {"object_type": "AirNowClosureArchiveStatusBoard", "board_status": "CLOSURE_ARCHIVE_INDEX_PLAN_COMPLETE_INTERNAL_ONLY", "created_at": created_at})
    (out / "closure_archive_status_board.md").write_text("# AirNow Layer 28 Closure Archive Index Status Board\n\nInternal-only planning complete.\n", encoding="utf-8")
    (out / "closure_archive_index_report.md").write_text("# AirNow Layer 28 Closure Archive Index Report\n\nInternal-only planning report; no command execution, no publication, no database indexing, and no search service creation.\n", encoding="utf-8")
    r = make_receipt(m.get("manifest_id"), created_at, [])
    if m.get("index_policy", {}).get("include_packet") is True:
        r["output_hashes"]["closure_archive_index_packet_hash"] = _build_packet(out)
    _wj(out / "closure_archive_index_receipt.json", r)
    return r
