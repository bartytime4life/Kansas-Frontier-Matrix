from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
from tools.validators._common.jsonschema_runner import run

if __name__ == '__main__':
    raise SystemExit(run(Path('schemas/contracts/v1/domains/hydrology/run_receipt.schema.json'), Path('fixtures/domains/hydrology/run_receipt'), sys.argv[1:]))
