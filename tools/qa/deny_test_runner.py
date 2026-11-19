"""Run the repository's public-boundary deny suites and emit one finite summary.

Each suite is a fixed, reviewed command; nothing is discovered from arguments or
the environment. A suite must exit zero and report positive passing cases in its
registered runner summary. Empty, entirely skipped/expected-failure, and missing
or unrecognized summaries cannot report PASS.
The summary is a review aid, not release, policy, or publication evidence.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Literal

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_VERSION = "kfm.deny-test-run/v1"
DETERMINISTIC_ENV = {"KFM_NO_NETWORK": "1", "PYTHONHASHSEED": "0",
                     "PYTHONDONTWRITEBYTECODE": "1", "PYTHONUNBUFFERED": "1", "TZ": "UTC"}


@dataclass(frozen=True)
class Suite:
    suite_id: str
    argv: tuple[str, ...]
    required_paths: tuple[str, ...]
    pythonpath: tuple[str, ...] = ()
    result_format: Literal["pytest", "unittest", "evidence-fixtures"] = "pytest"


SUITES = (
    Suite("governed-api-boundary-guards",
          ("-m", "pytest", "-q", "-p", "no:cacheprovider", "--strict-config",
           "--strict-markers", "apps/governed-api/tests/test_boundary_guards.py"),
          ("apps/governed-api/tests/test_boundary_guards.py",),
          ("apps/governed-api/src",)),
    Suite("governed-api-abstain-routes",
          ("-m", "pytest", "-q", "-p", "no:cacheprovider", "--strict-config",
           "--strict-markers", "apps/governed-api/tests/test_abstain_routes.py"),
          ("apps/governed-api/tests/test_abstain_routes.py",),
          ("apps/governed-api/src",)),
    Suite("evidence-resolver-negative-fixtures",
          ("tools/validators/evidence_resolver/validate_candidate.py", "--fixtures",
           "fixtures/packages/evidence_resolver/v1alpha1", "--negative-only"),
          ("tools/validators/evidence_resolver/validate_candidate.py",
           "fixtures/packages/evidence_resolver/v1alpha1"),
          result_format="evidence-fixtures"),
    Suite("release-publication-deny-dry-run",
          ("-m", "unittest", "-v", "tests.release.test_publication_deny_dry_run"),
          ("tests/release/test_publication_deny_dry_run.py",),
          result_format="unittest"),
)


def passing_cases(result_format: str, output: str) -> int | None:
    """Read only known terminal summaries; None means insufficient evidence."""
    lines = output.strip().splitlines()
    if not lines:
        return None
    final = lines[-1].strip()
    if result_format == "pytest":
        final = final.strip("= ")
        if re.fullmatch(r"no tests ran in \d+(?:\.\d+)?s", final):
            return 0
        summary = re.fullmatch(r"(.+) in \d+(?:\.\d+)?s(?: \([\d:]+\))?", final)
        if summary is None:
            return None
        counts: dict[str, int] = {}
        for item in summary[1].split(", "):
            match = re.fullmatch(
                r"(\d+) (passed|failed|skipped|deselected|xfailed|xpassed|errors?|"
                r"warnings?|subtests (?:passed|failed|skipped))", item)
            if match is None or match[2] in counts:
                return None
            counts[match[2]] = int(match[1])
        if any(counts.get(key, 0) for key in ("failed", "error", "errors", "subtests failed")):
            return None
        return counts.get("passed", 0)
    if result_format == "unittest":
        summary = re.fullmatch(r"OK(?: \((.+)\))?", final)
        runs = list(re.finditer(r"^Ran (\d+) tests? in [^\n]+$", output, re.MULTILINE))
        if summary is None or not runs:
            return None
        excluded = 0
        seen: set[str] = set()
        if summary[1]:
            for item in summary[1].split(", "):
                match = re.fullmatch(r"(skipped|expected failures)=(\d+)", item)
                if match is None or match[1] in seen:
                    return None
                seen.add(match[1])
                excluded += int(match[2])
        total = int(runs[-1][1])
        return total - excluded if total >= excluded else None
    if result_format == "evidence-fixtures":
        summary = re.fullmatch(
            r"SUMMARY DENIED=(\d+) ERROR=(\d+) RESOLVED=0 UNRESOLVED=(\d+) FAILED=0", final)
        return sum(int(value) for value in summary.groups()) if summary else None
    return None


def run_suite(suite: Suite, *, timeout: int) -> dict[str, object]:
    missing = [path for path in suite.required_paths if not (ROOT / path).exists()]
    if missing:
        return {"suite": suite.suite_id, "status": "MISSING", "missing_paths": missing}
    env = {key: value for key, value in os.environ.items() if key != "PYTHONPATH"}
    env.update(DETERMINISTIC_ENV)
    if suite.pythonpath:
        env["PYTHONPATH"] = os.pathsep.join(str(ROOT / path) for path in suite.pythonpath)
    try:
        completed = subprocess.run([sys.executable, *suite.argv], cwd=ROOT, env=env,
                                   capture_output=True, text=True, timeout=timeout,
                                   check=False)
    except subprocess.TimeoutExpired:
        return {"suite": suite.suite_id, "status": "TIMEOUT", "timeout_seconds": timeout}
    output = completed.stdout + completed.stderr
    verified = passing_cases(suite.result_format, output) if completed.returncode == 0 else None
    if completed.returncode != 0:
        status = "FAIL"
    elif verified is None:
        status = "UNVERIFIED"
    elif verified == 0:
        status = "EMPTY"
    else:
        status = "PASS"
    tail = output.strip().splitlines()[-1:] if output.strip() else []
    return {"suite": suite.suite_id, "status": status, "exit_code": completed.returncode,
            "passing_cases": verified,
            "last_line": tail[0][:300] if tail else ""}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--list", action="store_true", help="print suite ids and exit")
    parser.add_argument("--suite", action="append", choices=[s.suite_id for s in SUITES],
                        help="run only the named suite (repeatable)")
    parser.add_argument("--timeout", type=int, default=300)
    args = parser.parse_args(argv)
    if args.list:
        print("\n".join(suite.suite_id for suite in SUITES))
        return 0
    if not 1 <= args.timeout <= 1800:
        parser.error("--timeout must be between 1 and 1800 seconds")
    selected = [s for s in SUITES if not args.suite or s.suite_id in args.suite]
    results = [run_suite(suite, timeout=args.timeout) for suite in selected]
    ok = all(result["status"] == "PASS" for result in results)
    print(json.dumps({"schema_version": SCHEMA_VERSION, "status": "PASS" if ok else "FAIL",
                      "suites": results,
                      "authority_boundary": "Review aid only; not release, policy, or "
                                            "publication evidence."},
                     indent=2, sort_keys=True))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
