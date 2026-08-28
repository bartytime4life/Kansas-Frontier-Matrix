"""Expose the repository-local envelopes source tree to runtime-proof tests."""

from pathlib import Path
import sys


REPOSITORY_ROOT = Path(__file__).resolve().parents[5]
PACKAGE_SOURCE = REPOSITORY_ROOT / "packages" / "envelopes" / "src"
if str(PACKAGE_SOURCE) not in sys.path:
    sys.path.insert(0, str(PACKAGE_SOURCE))
