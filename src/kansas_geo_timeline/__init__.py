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
from typing import Any, Dict, Iterable, List, Optional

# ---------------------------------------------------------------------------
# Version (stdlib importlib.metadata with backport fallback)
# ---------------------------------------------------------------------------

def _resolve_version() -> str:
    """
    Return the installed package version if available; fallback to '0.0.0.dev'.
    """
    try:
        from importlib.metadata import version, PackageNotFoundError  # type: ignore
    except Exception:  # pragma: no cover
        try:
            from importlib_metadata import version, PackageNotFoundError  # type: ignore
        except Exception:  # pragma: no cover
            return "0.0.0.dev"

    try:
        return version("kansas_geo_timeline")
    except Exception:  # PackageNotFoundError or other env issues
        return "0.0.0.dev"


__version__ = _resolve_version()

# ---------------------------------------------------------------------------
# importlib.resources shims
# ---------------------------------------------------------------------------

try:
    # Python 3.9+: files() is available
    from importlib.resources import files as _res_files  # type: ignore[attr-defined]
except Exception:  # pragma: no cover
    # Python 3.8 compat via backport
    from importlib_resources import files as _res_files  # type: ignore # noqa: F401

# ---------------------------------------------------------------------------
# Paths and resource resolution
# ---------------------------------------------------------------------------

# Package directory (…/src/kansas_geo_timeline)
_PKG_DIR = Path(__file__).resolve().parent

# Default in-repo resource locations (source tree / editable installs)
_DEFAULT_SCHEMAS_DIR = _PKG_DIR / "schemas"
_DEFAULT_TEMPLATES_DIR = _PKG_DIR / "templates"

# Environment overrides (absolute or relative paths are accepted)
_ENV_SCHEMAS = os.getenv("KGT_SCHEMAS_DIR")
_ENV_TEMPLATES = os.getenv("KGT_TEMPLATES_DIR")

def _coerce_dir(p: Optional[str | Path]) -> Optional[Path]:
    if p is None or f"{p}".strip() == "":
        return None
    return Path(p).expanduser().resolve()

# Resolved overrides (may be None)
_ENV_SCHEMAS_DIR = _coerce_dir(_ENV_SCHEMAS)
_ENV_TEMPLATES_DIR = _coerce_dir(_ENV_TEMPLATES)

def _resource_pkg_dir(subdir: str) -> Optional[Path]:
    """
    Return a resolved path to a subdir (e.g., 'schemas', 'templates') when the
    package is installed as a wheel. Uses importlib.resources to find data.
    Returns None if not present (e.g., during early scaffolding).
    """
    try:
        root = _res_files(__package__) / subdir  # type: ignore[arg-type]
        p = Path(str(root))
        return p if p.exists() else None
    except Exception:  # pragma: no cover
        return None

def _first_existing(paths: Iterable[Optional[Path]]) -> Optional[Path]:
    for p in paths:
        if p and p.exists() and p.is_dir():
            return p
    return None

# Final resolved directories (order: ENV → source tree → installed resources)
_SCHEMAS_DIR = _first_existing([_ENV_SCHEMAS_DIR, _DEFAULT_SCHEMAS_DIR, _resource_pkg_dir("schemas")])
_TEMPLATES_DIR = _first_existing([_ENV_TEMPLATES_DIR, _DEFAULT_TEMPLATES_DIR, _resource_pkg_dir("templates")])

def _ensure_available(kind: str, p: Optional[Path]) -> Path:
    if p is None:
        raise FileNotFoundError(
            f"{kind} directory could not be located. "
            f"Tried env override and packaged defaults. "
            f"Set KGT_{kind.upper()}_DIR or ensure '{kind.lower()}' is included in the package data."
        )
    return p

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
    return _ensure_available("SCHEMAS", _SCHEMAS_DIR)

def templates_dir() -> Path:
    """
    Return the directory path that contains Jinja templates.
    Respects KGT_TEMPLATES_DIR if set.
    """
    return _ensure_available("TEMPLATES", _TEMPLATES_DIR)

# ---------------------------------------------------------------------------
# Safe file resolution helpers
# ---------------------------------------------------------------------------

def _safe_join(root: Path, name: str) -> Path:
    """
    Join 'name' under 'root' while preventing directory traversal.
    """
    if name.startswith(("/", "..")):
        raise ValueError(f"Illegal resource name (path traversal): {name}")
    p = (root / name).resolve()
    if root not in p.parents and p != root:
        raise ValueError(f"Resource escapes root: {p} (root={root})")
    return p

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
    root = schemas_dir()
    p = _safe_join(root, name)
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
    root = templates_dir()
    p = _safe_join(root, name)
    if not p.is_file():
        raise FileNotFoundError(f"Template not found: {p}")
    return p

# ---------------------------------------------------------------------------
# Convenience: list & load helpers
# ---------------------------------------------------------------------------

def list_schemas(suffix: str | None = ".json") -> List[str]:
    """
    List schema filenames (optionally filtered by suffix).
    """
    root = schemas_dir()
    items = []
    for p in sorted(root.glob("**/*")):
        if p.is_file() and (suffix is None or p.name.endswith(suffix)):
            items.append(str(p.relative_to(root)))
    return items

def list_templates(suffix: str | None = None) -> List[str]:
    """
    List template filenames (optionally filtered by suffix, e.g., '.j2').
    """
    root = templates_dir()
    items = []
    for p in sorted(root.glob("**/*")):
        if p.is_file() and (suffix is None or p.name.endswith(suffix)):
            items.append(str(p.relative_to(root)))
    return items

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

# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

__all__ = [
    "__version__",
    "package_dir",
    "schemas_dir",
    "templates_dir",
    "schema_path",
    "template_path",
    "list_schemas",
    "list_templates",
    "load_json_schema",
]
