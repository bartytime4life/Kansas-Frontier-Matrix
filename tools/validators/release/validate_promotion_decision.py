from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.validators._common.jsonschema_runner import run

SCHEMA = ROOT / "schemas/contracts/v1/release/promotion_decision.schema.json"
FIXTURES = ROOT / "fixtures/release/promotion_decision"

if __name__ == "__main__":
    raise SystemExit(run(SCHEMA, FIXTURES, sys.argv[1:]))
