from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from tools.validators._common.jsonschema_runner import run


ROOT = Path(__file__).resolve().parents[4]
SCHEMA = (
    ROOT
    / "schemas/contracts/v1/domains/people-dna-land/domain_feature_identity.schema.json"
)
FIXTURES = ROOT / "fixtures/domains/people-dna-land/domain_feature_identity"


def main(argv: list[str] | None = None) -> int:
    """Validate structural People/DNA/Land DomainFeatureIdentity candidates.

    This entrypoint proves only conformance to the repository's current PROPOSED
    schema scaffold and deterministic synthetic fixture polarity. It does not
    resolve or merge people, establish kinship, expose DNA, prove residence or
    title, grant consent, activate policy, authorize release, or publish data.
    """
    args = list(sys.argv[1:] if argv is None else argv)
    if "--fixtures" in args and len(args) != 1:
        print(
            "Cannot combine --fixtures with explicit DomainFeatureIdentity files",
            file=sys.stderr,
        )
        return 2
    return run(SCHEMA, FIXTURES, args)


if __name__ == "__main__":
    raise SystemExit(main())
