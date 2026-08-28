from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[4]))
from tools.validators._common.jsonschema_runner import run

if __name__ == '__main__':
    raise SystemExit(run(Path('schemas/contracts/v1/domains/hydrology/aquifer_observation.schema.json'), Path('fixtures/domains/hydrology/aquifer_observation'), sys.argv[1:]))
