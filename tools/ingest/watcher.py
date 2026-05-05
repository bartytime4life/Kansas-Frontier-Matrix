from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from .event_queue import JsonlQueue
from .http_client import head_probe
from .models import ChangeEvent, ProbeResult, RunnerSettings, SourceSpec, load_config
from .utils import atomic_write_json, canonical_dumps, read_json, safe_id, sha256_prefixed_text, utc_now


def meta_path(settings: RunnerSettings, source_id: str) -> Path:
    return Path(settings.meta_dir) / f"{safe_id(source_id)}.json"


def compute_spec_hash(probe: ProbeResult, spec: SourceSpec) -> str:
    material_tuple = {
        "etag": probe.etag or "",
        "last_modified": probe.last_modified or "",
        "download_key": spec.download_key,
        "source_version": spec.source_version,
    }
    return sha256_prefixed_text(canonical_dumps(material_tuple))


def _status_for_probe(probe: ProbeResult, high_risk: bool) -> str:
    if probe.error or probe.status == 0:
        return "error"
    if probe.status >= 500:
        return "fail_closed_http_5xx"
    if probe.status < 200 or probe.status >= 400:
        return "fail_closed_http_non_success"
    if high_risk:
        return "missing_http_validators"
    return "ok"


def check_source(spec: SourceSpec, settings: RunnerSettings, *, seed_only: bool = False, dry_run: bool = False) -> ChangeEvent | None:
    probe = head_probe(spec.url, spec.headers)
    high_risk = (not probe.etag or not probe.last_modified) and not spec.allow_missing_http_validators
    status = _status_for_probe(probe, high_risk)
    existing = read_json(meta_path(settings, spec.source_id), default=None)

    # Fail closed on network, 5xx, and non-success status by recording state but not enqueueing a download.
    if status.startswith("fail_closed") or status == "error":
        meta = {
            "source_id": spec.source_id,
            "etag": probe.etag,
            "last_modified": probe.last_modified,
            "download_key": spec.download_key,
            "spec_hash": existing.get("spec_hash") if existing else None,
            "checked_at": utc_now(),
            "status": status,
            "http_status": probe.status,
            "content_length": probe.content_length,
            "content_type": probe.content_type,
            "error": probe.error,
        }
        if not dry_run:
            atomic_write_json(meta_path(settings, spec.source_id), meta)
        return None

    spec_hash = compute_spec_hash(probe, spec)
    prev_hash = existing.get("spec_hash") if existing else None
    material = prev_hash != spec_hash
    reason = "initial" if existing is None else "changed" if material else "unchanged"
    if high_risk:
        reason = f"{reason}:missing_http_validators"
    meta = {
        "source_id": spec.source_id,
        "etag": probe.etag,
        "last_modified": probe.last_modified,
        "download_key": spec.download_key,
        "spec_hash": spec_hash,
        "checked_at": utc_now(),
        "status": status,
        "http_status": probe.status,
        "content_length": probe.content_length,
        "content_type": probe.content_type,
        "high_risk": high_risk,
        "error": probe.error,
    }
    if not dry_run:
        atomic_write_json(meta_path(settings, spec.source_id), meta)

    if seed_only or not material:
        return None
    return ChangeEvent(
        source_id=spec.source_id,
        prev_spec_hash=prev_hash,
        next_spec_hash=spec_hash,
        material=True,
        reason=reason,
        high_risk=high_risk,
        seen_at=utc_now(),
    )


def check_sources(config_path: str | Path, *, seed_only: bool = False, dry_run: bool = False) -> dict[str, Any]:
    settings, sources_by_id = load_config(config_path)
    queue = JsonlQueue(settings.queue_path)
    events: list[ChangeEvent] = []
    for spec in sources_by_id.values():
        event = check_source(spec, settings, seed_only=seed_only, dry_run=dry_run)
        if event:
            events.append(event)
    if events and not dry_run:
        queue.append_many([event.to_dict() for event in events])
    return {
        "checked": len(sources_by_id),
        "enqueued": len(events),
        "seed_only": seed_only,
        "dry_run": dry_run,
        "events": [event.to_dict() for event in events],
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="KFM HEAD watcher")
    parser.add_argument("--config", required=True, help="Path to config JSON")
    parser.add_argument("--seed-only", action="store_true", help="Persist .last_meta state without enqueueing material events")
    parser.add_argument("--dry-run", action="store_true", help="Probe and print changes without writing state or queue files")
    args = parser.parse_args(argv)
    result = check_sources(args.config, seed_only=args.seed_only, dry_run=args.dry_run)
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
