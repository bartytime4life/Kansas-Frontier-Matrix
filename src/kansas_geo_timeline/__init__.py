"""
kansas_geo_timeline
===================

Core package utilities for the Kansas Geo Timeline / Kansas-Frontier-Matrix stack.

This module exposes:
- __version__: resolved from installed package metadata when available.
- path helpers for bundled schemas and Jinja templates.
- small loader helpers (e.g., JSON Schema loader).

Design notes
------------
Keep this file dependency-light so it can be imported by CLI tools, CI validators,
and static site builders without pulling in heavy GIS/ML stacks.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, Optional

# ---------------------------------------------------------------------------
# Version
# ---------------------------------------------------------------------------

def _resolve_version() -> str:
    """
    Return the installed package version if available; fallback to '0.0.0.dev'.
    """
    try:
        # Python 3.8+: importlib.metadata is stdlib
        from importlib.metadata import version, PackageNotFoundError  # type: ignore
    except Exception:  # pragma: no cover
        try:
            # Backport (for older environments)
            from importlib_metadata import version, PackageNotFoundError  # type: ignore
        except Exception:  # pragma: no cover
            return "0.0.0.dev"

    try:
        return version("kansas_geo_timeline")
    except Exception:  # PackageNotFoundError or other env issues
        return "0.0.0.dev"


__version__ = _resolve_version()

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

# Package directory (…/src/kansas_geo_timeline)
_PKG_DIR = Path(__file__).resolve().parent

# Default in-repo resource locations
_DEFAULT_SCHEMAS_DIR = _PKG_DIR / "schemas"
_DEFAULT_TEMPLATES_DIR = _PKG_DIR / "templates"

# Allow environment overrides for advanced setups (e.g., during CI or dev)
_SCHEMAS_DIR = Path(os.getenv("KGT_SCHEMAS_DIR", str(_DEFAULT_SCHEMAS_DIR))).resolve()
_TEMPLATES_DIR = Path(os.getenv("KGT_TEMPLATES_DIR", str(_DEFAULT_TEMPLATES_DIR))).resolve()


def package_dir() -> Path:
    """
    Return the kansas_geo_timeline package directory path.
    """
    return _PKG_DIR


def schemas_dir() -> Path:
    """
    Return the directory path that contains JSON Schemas.
    Respects KGT_SCHEMAS_DIR if set.
    """
    return _SCHEMAS_DIR


def templates_dir() -> Path:
    """
    Return the directory path that contains Jinja templates.
    Respects KGT_TEMPLATES_DIR if set.
    """
    return _TEMPLATES_DIR


def schema_path(name: str) -> Path:
    """
    Return absolute path to a schema file in the schemas directory.

    Parameters
    ----------
    name : str
        File name, e.g., 'stac_item.schema.json'.

    Raises
    ------
    FileNotFoundError
        If the schema file does not exist.
    """
    p = schemas_dir() / name
    if not p.is_file():
        raise FileNotFoundError(f"Schema not found: {p}")
    return p


def template_path(name: str) -> Path:
    """
    Return absolute path to a template file in the templates directory.

    Parameters
    ----------
    name : str
        File name, e.g., 'app.config.json.j2'.

    Raises
    ------
    FileNotFoundError
        If the template file does not exist.
    """
    p = templates_dir() / name
    if not p.is_file():
        raise FileNotFoundError(f"Template not found: {p}")
    return p


def load_json_schema(name: str) -> Dict[str, Any]:
    """
    Load and return a JSON schema from the schemas directory.

    Parameters
    ----------
    name : str
        File name, e.g., 'stac_item.schema.json'.

    Returns
    -------
    dict
        Parsed JSON schema object.
    """
    with schema_path(name).open("r", encoding="utf-8") as f:
        return json.load(f)


__all__ = [
    "__version__",
    "package_dir",
    "schemas_dir",
    "templates_dir",
    "schema_path",
    "template_path",
    "load_json_schema",
]

