from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from tools.validators._common.jsonschema_runner import run


SCHEMA = Path("schemas/contracts/v1/domains/agriculture/evidence_bundle.schema.json")
FIXTURES = Path("fixtures/contracts/v1/evidence/evidence_bundle")


if __name__ == "__main__":
    raise SystemExit(run(SCHEMA, FIXTURES, sys.argv[1:]))
