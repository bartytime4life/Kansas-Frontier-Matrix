#!/usr/bin/env python3
"""Route explicit, fixture-only telemetry profiles to their owning validators.

This is a local validation entry point, not a general telemetry safety policy.
Unknown profiles and implicit profile selection fail closed. No emitter, sink,
network transport, or operational UI event is enabled by this command.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[2]
PROFILES = {
    "trace_receipt_link": "tools/validators/validate_trace_receipt_link.py",
    "openlineage_run_event_projection": (
        "tools/validators/telemetry/validate_openlineage_run_event_projection.py"
    ),
    "remote_sensing_lineage_activity": (
        "tools/validators/telemetry/validate_remote_sensing_lineage_activity.py"
    ),
    "map_build_sustainability": (
        "tools/validators/telemetry/validate_map_build_sustainability.py"
    ),
}
SCOPES = {
    "trace_receipt_link": "trace-receipt-evidence-linkage-only",
    "openlineage_run_event_projection": "telemetry.openlineage_run_event_projection",
    "remote_sensing_lineage_activity": "telemetry.remote_sensing_lineage_activity",
    "map_build_sustainability": "telemetry.map_build_sustainability.fixture",
}


def _fixture_report_ok(profile: str, output: str) -> bool:
    if profile == "trace_receipt_link":
        # This older validator emits one JSON line per case and a final summary.
        lines = output.splitlines()
        summary = re.fullmatch(
            r"CONFIRMED: [1-9]\d* valid and [1-9]\d* invalid trace receipt link fixtures passed exact polarity\.",
            lines[-1] if lines else "",
        )
        if len(lines) < 3 or summary is None:
            return False
        try:
            reports = [json.loads(line) for line in lines[:-1]]
        except (ValueError, TypeError):
            return False
        if not all(isinstance(report, dict) and report.get("scope") == SCOPES[profile]
                   and report.get("outcome") in {"PASS", "FAIL"} for report in reports):
            return False
        counts = {outcome: sum(r["outcome"] == outcome for r in reports)
                  for outcome in ("PASS", "FAIL")}
        return (counts["PASS"] > 0 and counts["FAIL"] > 0
                and lines[-1] == (f"CONFIRMED: {counts['PASS']} valid and {counts['FAIL']} "
                                  "invalid trace receipt link fixtures passed exact polarity."))
    try:
        report = json.loads(output)
    except (ValueError, TypeError):
        return False
    return (isinstance(report, dict) and report.get("scope") == SCOPES[profile]
            and report.get("ok") is True and isinstance(report.get("cases"), list)
            and bool(report["cases"])
            and all(isinstance(case, dict) and case.get("ok") is True
                    for case in report["cases"])
            and (profile != "map_build_sustainability"
                 or (report.get("authority") == "NONE" and report.get("outcome") == "PASS")))


def _run(profile: str, candidate: Path | None) -> str:
    command = [sys.executable, str(ROOT / PROFILES[profile])]
    if candidate is None:
        command.append("--fixtures")
    elif profile == "trace_receipt_link":
        # The subprocess runs from ROOT. Bind relative paths to the caller's
        # working directory before that change, without following symlinks.
        command.extend(("--", str(candidate.absolute())))
    else:
        command.extend(("--candidate", str(candidate.absolute())))
    # Fixed, reviewed validator paths only; no shell or caller-supplied program.
    try:
        result = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
            timeout=60,
        )
    except (OSError, subprocess.TimeoutExpired):
        return "ERROR"
    if candidate is None:
        return "PASS" if result.returncode == 0 and _fixture_report_ok(profile, result.stdout) else "ERROR"
    try:
        report = json.loads(result.stdout)
        if not isinstance(report, dict) or report.get("scope") != SCOPES[profile]:
            return "ERROR"
        if profile != "trace_receipt_link" and report.get("authority") != "NONE":
            return "ERROR"
        outcome = report["outcome"]
    except (ValueError, KeyError, TypeError):
        return "ERROR"
    if outcome == "FAIL":
        outcome = "DENY"
    if not isinstance(outcome, str) or outcome not in {
        "PASS", "ABSTAIN", "DENY", "ERROR"
    }:
        return "ERROR"
    if (outcome in {"PASS", "ABSTAIN"}) != (result.returncode == 0):
        return "ERROR"
    return outcome


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--fixtures", action="store_true")
    mode.add_argument("--candidate", type=Path)
    parser.add_argument("--profile", choices=tuple(PROFILES))
    args = parser.parse_args(argv)
    if args.candidate is not None and args.profile is None:
        parser.error("--candidate requires an explicit --profile")

    profiles = (args.profile,) if args.profile else tuple(PROFILES)
    results = {profile: _run(profile, args.candidate) for profile in profiles}
    outcome = next(
        (value for value in ("ERROR", "DENY", "ABSTAIN") if value in results.values()),
        "PASS",
    )
    print(json.dumps(
        {
            "authority": "NONE",
            "execution_mode": "FIXTURE_ONLY_NO_NETWORK",
            "outcome": outcome,
            "profiles": results,
            "scope": "bounded_telemetry_profile_validation_only",
        },
        sort_keys=True,
        separators=(",", ":"),
    ))
    return 0 if outcome in {"PASS", "ABSTAIN"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
