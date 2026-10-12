#!/usr/bin/env python3
"""Check a repository-control projection against an explicitly observed head."""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SHA_RE = re.compile(r"^[0-9a-f]{40}$")


class CurrentnessError(ValueError):
    """A bounded currentness failure."""


def load_projection(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CurrentnessError(
            f"{path}: unreadable JSON-compatible projection: {exc}"
        ) from exc
    if not isinstance(data, dict):
        raise CurrentnessError("projection root must be an object")
    return data


def parse_timestamp(value: str) -> datetime:
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(
            timezone.utc
        )
    except (TypeError, ValueError) as exc:
        raise CurrentnessError(f"invalid base.observed_at: {value!r}") from exc


def check_currentness(
    projection: dict[str, Any],
    *,
    observed_main_sha: str,
    max_age_days: int | None = None,
    now: datetime | None = None,
) -> None:
    if not SHA_RE.fullmatch(observed_main_sha):
        raise CurrentnessError(
            "--observed-main-sha must be a full lowercase 40-char SHA"
        )

    status = projection.get("projection_status")
    base = projection.get("base")
    if not isinstance(base, dict):
        raise CurrentnessError("base must be an object")
    recorded_sha = base.get("current_main_sha")
    if not isinstance(recorded_sha, str) or not SHA_RE.fullmatch(recorded_sha):
        raise CurrentnessError("base.current_main_sha is not a full lowercase SHA")

    if status == "SUPERSEDED":
        raise CurrentnessError(
            f"PROJECTION_SUPERSEDED: recorded {recorded_sha}; "
            f"observed {observed_main_sha}"
        )
    if status != "CONFIRMED":
        raise CurrentnessError(f"projection_status is not current: {status!r}")
    if recorded_sha != observed_main_sha:
        raise CurrentnessError(
            f"STALE_MAIN: recorded {recorded_sha}; observed {observed_main_sha}"
        )

    if max_age_days is not None:
        if max_age_days < 0:
            raise CurrentnessError("--max-age-days must be non-negative")
        observed_at = parse_timestamp(base.get("observed_at"))
        reference = now or datetime.now(timezone.utc)
        age_seconds = (reference - observed_at).total_seconds()
        if age_seconds < 0:
            raise CurrentnessError("base.observed_at is in the future")
        if age_seconds > max_age_days * 86400:
            raise CurrentnessError(
                f"STALE_AGE: projection age exceeds {max_age_days} days"
            )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "projection",
        nargs="?",
        type=Path,
        default=Path("control_plane/repository_control_state.yaml"),
    )
    parser.add_argument("--observed-main-sha", required=True)
    parser.add_argument("--max-age-days", type=int)
    args = parser.parse_args()
    try:
        projection = load_projection(args.projection)
        check_currentness(
            projection,
            observed_main_sha=args.observed_main_sha,
            max_age_days=args.max_age_days,
        )
    except CurrentnessError as exc:
        print(f"REPOSITORY_CONTROL_NOT_CURRENT: {exc}")
        return 3
    print("REPOSITORY_CONTROL_CURRENT")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
