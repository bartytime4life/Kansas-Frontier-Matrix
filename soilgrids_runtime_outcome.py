#!/usr/bin/env python3
"""Compatibility shim for the canonical script location.

The runtime outcome tool now lives under scripts/ to keep repository
entrypoints organized. This wrapper preserves existing integrations.
"""

from __future__ import annotations

import runpy
from pathlib import Path


if __name__ == "__main__":
    target = Path(__file__).resolve().parent / "scripts" / "soilgrids_runtime_outcome.py"
    runpy.run_path(str(target), run_name="__main__")
