from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from tools.validators._common.jsonschema_runner import run


if __name__ == '__main__':
    raise SystemExit(run(

        Path('schemas/contracts/v1/evidence/evidence_bundle.schema.json'),
        Path('fixtures/contracts/v1/evidence/evidence_bundle'),
        __import__('sys').argv[1:]
    ))
