#!/usr/bin/env python3
"""Validate HabitatPatch candidates against the current (scaffold) schema.

``schemas/contracts/v1/domains/habitat/habitat_patch.schema.json`` is a
PROPOSED scaffold with empty ``properties`` and ``additionalProperties:
true`` (see ``contracts/domains/habitat/habitat_patch.md``, "Schema posture"
and "Recommended semantics" -- the field list there is explicitly not yet
enforced, and open questions such as the canonical source-role spelling and
which sibling contract document is canonical remain NEEDS VERIFICATION
pending a domain-steward decision).

This entrypoint therefore checks only what the shared JSON Schema runner
already checks against whatever the schema currently declares: valid JSON, a
JSON object at the root, no duplicate object keys, no non-finite numbers, and
conformance with the schema's (currently permissive) constraints. It asserts
no HabitatPatch identity, source-role, geometry, evidence, sensitivity,
policy, or release semantics. Field-level checks must be added only after the
schema itself is expanded by a domain steward.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.jsonschema_runner import run  # noqa: E402


SCHEMA_PATH = (
    REPO_ROOT / "schemas/contracts/v1/domains/habitat/habitat_patch.schema.json"
)
FIXTURES_DIR = REPO_ROOT / "fixtures/domains/habitat/patch"


def main(argv: Sequence[str] | None = None) -> int:
    """Run shared shape validation for explicit files or the fixture profile."""

    arguments = list(sys.argv[1:] if argv is None else argv)
    if "--fixtures" in arguments and any(
        argument != "--fixtures" for argument in arguments
    ):
        print("Cannot combine --fixtures with explicit files", file=sys.stderr)
        return 2
    return run(SCHEMA_PATH, FIXTURES_DIR, arguments)


if __name__ == "__main__":
    raise SystemExit(main())
