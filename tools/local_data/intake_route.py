"""Deterministic placement decisions for profiled local files, with a GitHub storage guard.

Four destinations are considered for every file:

* ``local_store`` — the private external KFM_DATA_ROOT. Bulk bytes always stay here.
* ``database``   — the local intake index (metadata, extent, time and decisions).
* ``work_lane``  — an explicit, operator-applied staging copy under
  ``data/work/intake/<domain>/...`` for review; never PROCESSED or PUBLISHED.
* ``git_repo``   — a small metadata card only. File bytes never enter Git history.
* ``github_release`` — a curated release-asset *candidate*, allowed only for
  redistributable public data inside the storage budget.

Decisions are recommendations. Nothing here uploads, commits, admits a
source, or changes rights; unknown rights or sensitivity always hold.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
BUDGET_PATH = REPO / "tools/local_data/catalogs/github-storage-budget.json"
BASELINE_PATH = REPO / "tools/local_data/catalogs/github-baseline/baseline-manifest.json"
DECISION_SCHEMA = "kfm-intake-decision/v1"
SAFE_SEGMENT = re.compile(r"[^A-Za-z0-9._-]+")

# Copying a highly compressed archive is harmless; only extraction is not, so that ratio is informational.
BLOCKING_ISSUES = {"zip_unsafe_member_paths", "format_reader_failed"}
REVIEW_DOMAINS = {"archaeology", "people", "people-dna-land"}


class BudgetError(ValueError):
    pass


def load_budget(path: Path = BUDGET_PATH, baseline: Path | None = BASELINE_PATH) -> dict:
    """Load and validate the storage policy; cross-check it against the baseline manifest."""
    value = json.loads(path.read_text("utf-8"))
    required = {"github_limit_bytes", "reserved_for_code_and_interface_bytes", "max_release_asset_bytes",
                "max_git_card_bytes", "max_git_cards_total_bytes", "min_release_candidate_bytes", "committed"}
    if value.get("schema") != "kfm-github-storage-budget/v1" or not required <= set(value):
        raise BudgetError("BUDGET_SHAPE_INVALID")
    for key in required - {"committed"}:
        if not isinstance(value[key], int) or value[key] < 0:
            raise BudgetError("BUDGET_VALUE_INVALID")
    if value["reserved_for_code_and_interface_bytes"] >= value["github_limit_bytes"]:
        raise BudgetError("BUDGET_RESERVE_EXCEEDS_LIMIT")
    ids = set()
    for row in value["committed"]:
        if not isinstance(row, dict) or not isinstance(row.get("bytes"), int) or row["bytes"] < 0 or row.get("id") in ids:
            raise BudgetError("BUDGET_COMMITTED_INVALID")
        ids.add(row["id"])
    value["baseline_check"] = "not-checked"
    if baseline is not None and baseline.is_file():
        manifest = json.loads(baseline.read_text("utf-8"))
        release = next((r for r in value["committed"] if r["id"] == "release:" + str(manifest.get("release_tag"))), None)
        value["baseline_check"] = "match" if release and release["bytes"] == manifest.get("data_archive_bytes") else "mismatch"
    return value


def budget_state(budget: dict, planned_bytes: int = 0) -> dict:
    """Summarize GitHub usage. ``data_ceiling`` keeps the code/interface reserve untouched."""
    committed = sum(row["bytes"] for row in budget["committed"])
    ceiling = budget["github_limit_bytes"] - budget["reserved_for_code_and_interface_bytes"]
    available = ceiling - committed - planned_bytes
    warn_fraction = budget.get("warn_at_fraction_of_data_ceiling", 0.85)
    used_fraction = (committed + planned_bytes) / ceiling if ceiling else 1.0
    return {
        "schema": "kfm-github-storage-state/v1",
        "github_limit_bytes": budget["github_limit_bytes"],
        "reserved_for_code_and_interface_bytes": budget["reserved_for_code_and_interface_bytes"],
        "data_ceiling_bytes": ceiling,
        "committed_bytes": committed,
        "planned_bytes": planned_bytes,
        "available_for_new_data_bytes": max(0, available),
        "used_fraction_of_data_ceiling": round(used_fraction, 4),
        "level": "over" if available < 0 else "warn" if used_fraction >= warn_fraction else "ok",
        "committed": [{"id": r["id"], "bytes": r["bytes"]} for r in budget["committed"]],
        "baseline_check": budget.get("baseline_check", "not-checked"),
        "max_release_asset_bytes": budget["max_release_asset_bytes"],
    }


def _segment(value: str | None, fallback: str) -> str:
    cleaned = SAFE_SEGMENT.sub("-", value or "").strip("-.")[:64]
    return cleaned or fallback


def work_target(item: dict, domain: str) -> str:
    """Relative store path for a staged review copy; deterministic and collision-free per item."""
    declared = item.get("declared") or {}
    source = _segment(declared.get("source_id"), "unregistered")
    dataset = _segment(declared.get("dataset_id"), "")
    name = item["relative_path"].rsplit("/", 1)[-1]
    if not dataset:
        dataset = _segment(name.rsplit(".", 1)[0], "dataset")
    filename = _segment(name, "file")
    if item.get("lane") == "quarantine" and declared.get("relative_path"):
        filename = _segment(declared["relative_path"].rsplit("/", 1)[-1], filename)
    return f"data/work/intake/{_segment(domain, 'unassigned')}/{source}/{dataset}/{item['id'][:12]}-{filename}"


def decide(item: dict, profile: dict, budget: dict, *, planned_bytes: int = 0) -> dict:
    """Return a placement decision for one indexed item and its profile."""
    state = budget_state(budget, planned_bytes)
    declared = item.get("declared") or {}
    rights = (declared.get("rights") or {}).get("redistribution", "unknown")
    sensitivity = declared.get("sensitivity", "unknown")
    issues = set(profile.get("issues", []))
    flags = list(profile.get("hints", {}).get("review_flags", []))
    domain = profile.get("hints", {}).get("domain")
    family = profile.get("format", {}).get("family", "unknown")
    kansas = profile.get("spatial", {}).get("kansas", "unknown")
    size = item.get("size_bytes", 0)
    holds: list[str] = []

    blocked = sorted(issues & BLOCKING_ISSUES)
    if domain in REVIEW_DOMAINS:
        flags.append("sensitive_domain")
    flags = sorted(set(flags))

    placements = [
        {"tier": "local_store", "action": "keep", "reason": "BULK_BYTES_STAY_LOCAL",
         "path": item["store_path"] if item.get("lane") != "inbox" else None},
        {"tier": "database", "action": "index", "reason": "PROFILE_AND_EXTENT_INDEXED"},
    ]

    # Work lane: an explicit review copy, only for captured bytes with a resolved domain.
    if item.get("lane") == "inbox":
        placements.append({"tier": "work_lane", "action": "capture_first", "reason": "INBOX_FILES_ENTER_QUARANTINE_FIRST"})
        holds.append("CAPTURE_REQUIRED")
    elif blocked:
        placements.append({"tier": "work_lane", "action": "hold", "reason": "BLOCKING_ISSUE"})
    elif family == "unknown":
        placements.append({"tier": "work_lane", "action": "hold", "reason": "FORMAT_UNRECOGNIZED"})
        holds.append("FORMAT_UNRECOGNIZED")
    elif not domain:
        placements.append({"tier": "work_lane", "action": "hold", "reason": "DOMAIN_UNRESOLVED"})
        holds.append("DOMAIN_UNRESOLVED")
    else:
        placements.append({"tier": "work_lane", "action": "stage", "reason": "REVIEW_COPY_AVAILABLE",
                           "target": work_target(item, domain)})

    public = rights == "allowed" and sensitivity == "public"
    if rights != "allowed":
        holds.append("RIGHTS_" + rights.upper())
    if sensitivity != "public":
        holds.append("SENSITIVITY_" + sensitivity.upper())
    if flags:
        holds.append("REVIEW_FLAGS")

    # Git: metadata card only, and only for public redistributable data without review flags.
    if public and not flags and not blocked:
        placements.append({"tier": "git_repo", "action": "metadata_card", "reason": "PUBLIC_METADATA_CARD",
                           "max_bytes": budget["max_git_card_bytes"]})
    else:
        placements.append({"tier": "git_repo", "action": "hold", "reason": "CARD_REQUIRES_PUBLIC_RIGHTS_AND_REVIEW"})

    # GitHub release: curated, redistributable, Kansas-relevant, and inside the data ceiling.
    release = {"tier": "github_release", "bytes": size}
    if not public or flags or blocked:
        release.update(action="hold", reason="RELEASE_REQUIRES_PUBLIC_RIGHTS_AND_REVIEW")
    elif family == "unknown":
        release.update(action="hold", reason="FORMAT_UNRECOGNIZED")
    elif kansas == "outside":
        release.update(action="deny", reason="OUTSIDE_KANSAS")
    elif size < budget["min_release_candidate_bytes"]:
        release.update(action="bundle", reason="SMALL_FILE_BUNDLE_WITH_COLLECTION")
    elif size > state["available_for_new_data_bytes"]:
        release.update(action="deny", reason="GITHUB_BUDGET_EXCEEDED")
        holds.append("GITHUB_BUDGET_EXCEEDED")
    else:
        parts = -(-size // budget["max_release_asset_bytes"])
        release.update(action="candidate", reason="WITHIN_BUDGET", asset_parts=parts,
                       budget_after_bytes=state["available_for_new_data_bytes"] - size)
    placements.append(release)

    if blocked:
        status = "blocked"
    elif holds:
        status = "review"
    else:
        status = "ready"
    if kansas == "outside":
        holds.append("OUTSIDE_KANSAS")
    return {
        "schema": DECISION_SCHEMA,
        "status": status,
        "domain": domain,
        "holds": sorted(set(holds)),
        "blocking_issues": blocked,
        "review_flags": flags,
        "placements": placements,
        "authority": {"network": False, "source_admission": False, "promotion": False, "release": False, "publication": False},
    }


def metadata_card(item: dict, profile: dict, decision: dict) -> dict:
    """Small, byte-free description suitable for review in a repository pull request."""
    declared = item.get("declared") or {}
    card = {
        "schema": "kfm-intake-card/v1",
        "item_id": item["id"],
        "sha256": item.get("sha256"),
        "size_bytes": item.get("size_bytes"),
        "source_id": declared.get("source_id"),
        "dataset_id": declared.get("dataset_id"),
        "version": declared.get("version"),
        "source_uri": declared.get("source_uri"),
        "license_id": (declared.get("rights") or {}).get("license_id"),
        "domain": decision.get("domain"),
        "format": profile.get("format"),
        "spatial": {k: profile.get("spatial", {}).get(k) for k in ("crs", "bbox_wgs84", "kansas")},
        "temporal": profile.get("temporal"),
        "structure": {k: v for k, v in profile.get("structure", {}).items() if k != "fields"},
        "fields": (profile.get("structure", {}).get("fields") or [])[:60],
        "status": "candidate-metadata; not-admitted; not-released",
    }
    return card
