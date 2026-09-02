from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from tools.validators._common.jsonschema_runner import run


ROOT = Path(__file__).resolve().parents[4]
SCHEMA = (
    ROOT
    / "schemas/contracts/v1/domains/people-dna-land/domain_layer_descriptor.schema.json"
)
FIXTURES = ROOT / "fixtures/domains/people-dna-land/domain_layer_descriptor"


def main(argv: list[str] | None = None) -> int:
    """Validate structural People/DNA/Land DomainLayerDescriptor candidates.

    This entrypoint proves only conformance to the repository's current PROPOSED
    schema scaffold and deterministic synthetic fixture polarity. It does not
    authorize rendering, release, publication, source admission, identity,
    kinship, DNA, residence, title, parcel, consent, or policy decisions.
    """
    args = list(sys.argv[1:] if argv is None else argv)
    if "--fixtures" in args and len(args) != 1:
        print(
            "Cannot combine --fixtures with explicit DomainLayerDescriptor files",
            file=sys.stderr,
        )
        return 2
    return run(SCHEMA, FIXTURES, args)


if __name__ == "__main__":
    raise SystemExit(main())
