"""Run the repository's public-boundary deny suites and emit one finite summary.

Each suite is a fixed, reviewed command; nothing is discovered from arguments or
the environment. A suite that exits non-zero, times out, or collects no tests
fails the run, so an empty or placeholder deny test can never read as a pass.
The summary is a review aid, not release, policy, or publication evidence.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_VERSION = "kfm.deny-test-run/v1"
DETERMINISTIC_ENV = {"KFM_NO_NETWORK": "1", "PYTHONHASHSEED": "0",
                     "PYTHONDONTWRITEBYTECODE": "1", "PYTHONUNBUFFERED": "1", "TZ": "UTC"}
# Output markers that mean a runner executed nothing.
EMPTY_MARKERS = ("no tests ran", "Ran 0 tests", "collected 0 items")


@dataclass(frozen=True)
class Suite:
    suite_id: str
    argv: tuple[str, ...]
    required_paths: tuple[str, ...]
    pythonpath: tuple[str, ...] = ()


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
           "fixtures/packages/evidence_resolver/v1alpha1")),
    Suite("release-publication-deny-dry-run",
          ("-m", "unittest", "-v", "tests.release.test_publication_deny_dry_run"),
          ("tests/release/test_publication_deny_dry_run.py",)),
)


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
    if completed.returncode != 0:
        status = "FAIL"
    elif any(marker in output for marker in EMPTY_MARKERS):
        status = "EMPTY"
    else:
        status = "PASS"
    tail = output.strip().splitlines()[-1:] if output.strip() else []
    return {"suite": suite.suite_id, "status": status, "exit_code": completed.returncode,
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
