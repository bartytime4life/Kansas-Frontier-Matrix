"""Owner-private data workspace configuration for the local Studio launcher.

The launcher historically started Studio without Working Data or the Library,
so held intake reviews could not be sent onward. This file lets the owner record
those roots once, on this PC, outside Git. Values are operator configuration,
never browser input. The backend still performs its own full validation.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
import re
import stat
import tempfile

CONFIG = Path.home() / ".config/kfm-intake-studio/workspace.json"
MAX_BYTES = 16384

# key: (server flag, kind, plain-language label)
OPTIONS = {
    "kfm_root": ("--kfm-root", "dir", "Working Data store (receives items sent from intake holds)"),
    "library_root": ("--library-root", "dir", "Data Library catalog (read-only)"),
    "archive_root": ("--archive-root", "dir", "Original archive for Library file locations"),
    "inbox": ("--inbox", "dir", "Downloads inbox scanned by Working Data (read-only)"),
    "raster_python": ("--raster-python", "file", "Spatial preview Python for Working Data"),
    "pipeline_lock": ("--pipeline-lock", "lock", "Shared pipeline lock file"),
    "store_check": ("--store-check", "file", "Trusted volume-identity check script"),
    "working_connection": ("--working-connection", "file", "Legacy Working Data connection JSON"),
    "qwen_model": ("--qwen-model", "text", "Local Qwen model name"),
    "qwen_digest": ("--qwen-digest", "text", "Exact Ollama model digest"),
}


class ConfigError(ValueError):
    pass


def _text(key, value):
    if not isinstance(value, str) or not 1 <= len(value) <= 4096 or any(ord(c) < 32 or ord(c) == 127 for c in value):
        raise ConfigError(f"{key}: value must be one line of text")
    kind = OPTIONS[key][1]
    if kind == "text":
        if not re.fullmatch(r"[A-Za-z0-9._:/@-]{1,200}", value):
            raise ConfigError(f"{key}: unexpected characters")
        return value
    path = Path(value).expanduser()
    if not path.is_absolute() or ".." in path.parts:
        raise ConfigError(f"{key}: use a full path such as /media/you/KFM-pipeline")
    return str(path)


def normalize(values):
    if not isinstance(values, dict):
        raise ConfigError("workspace configuration must be a JSON object")
    unknown = set(values) - set(OPTIONS)
    if unknown:
        raise ConfigError("unknown setting(s): " + ", ".join(sorted(unknown)))
    result = {key: _text(key, values[key]) for key in OPTIONS if values.get(key) not in (None, "")}
    if bool(result.get("qwen_model")) != bool(result.get("qwen_digest")):
        raise ConfigError("qwen_model and qwen_digest must be set together")
    if "archive_root" in result and "library_root" not in result:
        raise ConfigError("archive_root needs library_root")
    return result


def load(path=None):
    """Return validated settings; missing file means nothing is configured."""
    path = Path(path or CONFIG)
    try:
        info = path.lstat()
    except FileNotFoundError:
        return {}
    if not stat.S_ISREG(info.st_mode) or info.st_uid != os.getuid() or stat.S_IMODE(info.st_mode) & 0o077:
        raise ConfigError(f"{path} must be a regular file owned by you with mode 600")
    if info.st_size > MAX_BYTES:
        raise ConfigError(f"{path} is too large")
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
    with os.fdopen(fd, "rb") as stream:
        raw = stream.read(MAX_BYTES + 1)
    try:
        return normalize(json.loads(raw.decode("utf-8")))
    except (UnicodeError, json.JSONDecodeError) as error:
        raise ConfigError(f"{path} is not valid JSON") from error


def save(values, path=None):
    values = normalize(values)
    path = Path(path or CONFIG)
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    parent = path.parent.lstat()
    if not stat.S_ISDIR(parent.st_mode) or parent.st_uid != os.getuid():
        raise ConfigError(f"{path.parent} must be a directory owned by you")
    os.chmod(path.parent, 0o700)
    if path.is_symlink():
        raise ConfigError(f"{path} must not be a symbolic link")
    fd, temporary = tempfile.mkstemp(prefix=".workspace-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(values, stream, indent=2, sort_keys=True); stream.write("\n")
            stream.flush(); os.fsync(stream.fileno())
        os.chmod(temporary, 0o600)
        os.replace(temporary, path)
    except BaseException:
        Path(temporary).unlink(missing_ok=True); raise
    return values


def server_args(values):
    """Fixed-order argument list for private_server.py; no shell is involved."""
    values = normalize(values)
    args = []
    for key, (flag, _, _) in OPTIONS.items():
        if key in values:
            args += [flag, values[key]]
    return args


def problems(values):
    """Human-readable reasons Studio would refuse this configuration at startup."""
    from tools.local_data import intake  # deferred: repository path is set by callers
    found = []
    for key, value in normalize(values).items():
        kind = OPTIONS[key][1]
        path = Path(value)
        if kind == "dir" and not path.is_dir():
            found.append(f"{key}: folder not found: {value}")
        elif kind == "file" and not path.is_file():
            found.append(f"{key}: file not found: {value}")
        elif kind == "lock" and not path.parent.is_dir():
            found.append(f"{key}: parent folder not found: {path.parent}")
    for key in ("kfm_root", "library_root"):
        if key in values and Path(values[key]).is_dir():
            try:
                intake.resolve_root(values[key])
            except ValueError as error:
                hint = {"STORE_NOT_INITIALIZED": "not an initialized KFM data store (use 'workspace init')",
                        "STORE_NOT_OWNER_PRIVATE": "must be owned by you with mode 700",
                        "ROOT_MUST_BE_SEPARATE_FROM_REPOSITORY": "must be outside the Git checkout"}.get(str(error), str(error))
                found.append(f"{key}: {hint}")
    return found
