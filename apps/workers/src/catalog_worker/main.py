"""Bounded operator worker; delegates to the existing CLI, grants no approval."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))
from tools.catalog_builders.build_catalog import main
if __name__ == "__main__":
    raise SystemExit(main())
