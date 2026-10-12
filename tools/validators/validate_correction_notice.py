"""Compatibility entry point for the canonical CorrectionNotice validator."""

from pathlib import Path
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.correction.validate_correction_notice import (  # noqa: E402
    FIXTURES_ROOT,
    MAX_JSON_BYTES,
    SCHEMA_PATH,
    load_document,
    main,
    run_fixtures,
    validate_document,
    validate_path,
)

__all__ = [
    "FIXTURES_ROOT",
    "MAX_JSON_BYTES",
    "SCHEMA_PATH",
    "load_document",
    "main",
    "run_fixtures",
    "validate_document",
    "validate_path",
]


if __name__ == "__main__":
    raise SystemExit(main())
