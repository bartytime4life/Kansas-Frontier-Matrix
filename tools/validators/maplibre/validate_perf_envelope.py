#!/usr/bin/env python3
"""Validate MapLibre performance-envelope candidates without network access.

Passing this machine-shape check does not establish benchmark methodology,
observed performance, policy approval, release readiness, or publication
authority.
"""

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.jsonschema_runner import run  # noqa: E402

SCHEMA_PATH = REPO_ROOT / "schemas/maplibre/perf-envelope.schema.json"
FIXTURE_ROOT = REPO_ROOT / "tests/fixtures/maplibre/perf-envelope"


def main(argv: list[str] | None = None) -> int:
    """Run explicit-file or reviewed fixture-polarity validation."""

    return run(
        SCHEMA_PATH,
        FIXTURE_ROOT,
        sys.argv[1:] if argv is None else argv,
    )


if __name__ == "__main__":
    raise SystemExit(main())
