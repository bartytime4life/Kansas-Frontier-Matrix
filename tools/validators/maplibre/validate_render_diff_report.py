from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from tools.validators._common.jsonschema_runner import run

if __name__ == '__main__':
    raise SystemExit(run(Path('schemas/maplibre/render-diff-report.schema.json'), None, sys.argv[1:]))
