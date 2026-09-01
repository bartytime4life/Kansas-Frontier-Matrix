from __future__ import annotations

import builtins
import importlib.util
import inspect
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent


def _add_path(path: Path) -> None:
    resolved = str(path.resolve())
    if resolved not in sys.path:
        sys.path.insert(0, resolved)


for app_src in sorted((REPO_ROOT / "apps").glob("*/src"), key=lambda p: str(p)):
    _add_path(app_src)
for package_src in sorted((REPO_ROOT / "packages").glob("*/src"), key=lambda p: str(p), reverse=True):
    _add_path(package_src)
for test_dir in sorted((REPO_ROOT / "tests").glob("*"), key=lambda p: str(p), reverse=True):
    if test_dir.is_dir():
        _add_path(test_dir)


_MODULE_NAMES = {
    "_support",
    "stale_scan_support",
    "path_alias_cases_repository",
    "path_alias_cases_safety",
    "path_alias_cases_schema",
    "path_alias_test_support",
}
_ORIGINAL_IMPORT = builtins.__import__


def _patched_import(name, globals=None, locals=None, fromlist=(), level=0):
    if name in _MODULE_NAMES:
        frame = inspect.currentframe()
        try:
            next_frame = frame.f_back if frame is not None else None
            while next_frame is not None:
                filename = next_frame.f_code.co_filename
                if filename and not filename.startswith("<") and "site-packages" not in filename:
                    candidate = Path(filename).resolve().parent / f"{name}.py"
                    if candidate.exists():
                        spec = importlib.util.spec_from_file_location(name, candidate)
                        if spec is not None and spec.loader is not None:
                            module = importlib.util.module_from_spec(spec)
                            sys.modules[name] = module
                            spec.loader.exec_module(module)
                            return module
                next_frame = next_frame.f_back
        finally:
            del frame

    return _ORIGINAL_IMPORT(name, globals, locals, fromlist, level)


builtins.__import__ = _patched_import
