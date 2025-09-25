#!/usr/bin/env python3
"""
write_meta.py — emit a checksum file and a .meta.json next to (or for) an artifact.

Usage:
  # basic (same as before)
  python scripts/write_meta.py PATH/TO/ARTIFACT --inputs in1 in2 ...

  # choose digest algorithm and put outputs elsewhere
  python scripts/write_meta.py artifact.tif --algo sha256 --outdir data/cogs --inputs in1.txt in2.bin

  # attach extra fields (K=V) and/or load a JSON/YAML blob
  python scripts/write_meta.py artifact.bin --extra run_id=42 stage=terrain --extra-json extras.json

Notes:
  * The checksum sidecar is named "<artifact>.<algo>" (e.g., .sha256) and uses the common "HEX  *filename" format.
  * .meta.json includes artifact + inputs digests, sizes, mtimes, command, CWD, git info (if in a repo), etc.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import subprocess
import sys
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

# ------------------------------
# utilities
# ------------------------------

_CHUNK = 1 << 20  # 1 MiB

def _iso_utc(ts: float) -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(ts))

def _digest_file(p: Path, algo: str) -> str:
    h = hashlib.new(algo)
    with p.open("rb") as f:
        while True:
            b = f.read(_CHUNK)
            if not b:
                break
            h.update(b)
    return h.hexdigest()

def _safe_stat(p: Path) -> Dict[str, object]:
    try:
        st = p.stat()
        return {
            "size": st.st_size,
            "mtime": _iso_utc(st.st_mtime),
            "mode": oct(st.st_mode & 0o777),
        }
    except FileNotFoundError:
        return {"size": None, "mtime": None, "mode": None, "missing": True}

def _git_info(cwd: Path) -> Dict[str, Optional[str]]:
    def _run(args: List[str]) -> Optional[str]:
        try:
            out = subprocess.check_output(args, cwd=str(cwd), stderr=subprocess.DEVNULL).decode().strip()
            return out or None
        except Exception:
            return None
    root = _run(["git", "rev-parse", "--show-toplevel"])
    if not root:
        return {}
    return {
        "git_root": root,
        "git_commit": _run(["git", "rev-parse", "HEAD"]),
        "git_branch": _run(["git", "rev-parse", "--abbrev-ref", "HEAD"]),
        "git_dirty": "1" if _run(["git", "status", "--porcelain"]) else "0",
    }

def _atomic_write_text(path: Path, text: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)

def _parse_kv_pairs(pairs: Iterable[str]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for kv in pairs:
        if "=" in kv:
            k, v = kv.split("=", 1)
            out[k.strip()] = v.strip()
    return out

def _load_extra_json(path: Optional[str]) -> Dict[str, object]:
    if not path:
        return {}
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"--extra-json not found: {p}")
    text = p.read_text(encoding="utf-8")
    # allow either JSON or very simple YAML (key: value lines)
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        try:
            data: Dict[str, object] = {}
            for line in text.splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if ":" in line:
                    k, v = line.split(":", 1)
                    data[k.strip()] = v.strip()
            return data
        except Exception as e:
            raise ValueError(f"Failed to parse {p} as JSON or simple YAML: {e}")

# ------------------------------
# models
# ------------------------------

@dataclass
class FileDigest:
    path: str
    algo: str
    digest: Optional[str]
    size: Optional[int]
    mtime: Optional[str]
    missing: bool = False

@dataclass
class MetaDocument:
    generated: str
    command: str
    cwd: str
    host: str
    platform: str
    python: str
    git: Dict[str, Optional[str]] = field(default_factory=dict)

    artifact: Dict[str, object] = field(default_factory=dict)
    artifact_digest: FileDigest | None = None

    inputs: List[FileDigest] = field(default_factory=list)
    inputs_digest_rollup: Dict[str, str] = field(default_factory=dict)

    extras: Dict[str, object] = field(default_factory=dict)

# ------------------------------
# main
# ------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("artifact", type=Path, help="File to describe and checksum")
    ap.add_argument("--inputs", nargs="*", default=[], help="List of input file paths")
    ap.add_argument("--extra", nargs="*", default=[], help="K=V pairs to include")
    ap.add_argument("--extra-json", help="JSON or simple YAML file with extra fields")
    ap.add_argument("--algo", default="sha256", choices=hashlib.algorithms_available,
                    help="Digest algorithm (default: sha256)")
    ap.add_argument("--outdir", type=Path, help="Write sidecars to this directory instead of alongside artifact")
    ap.add_argument("--no-checksum", action="store_true", help="Do not write the checksum sidecar (still computes)")
    args = ap.parse_args()

    art = args.artifact
    if not art.exists():
        print(f"[ERR] artifact not found: {art}", file=sys.stderr)
        return 2

    # Resolve output directory and sidecar names
    outdir = args.outdir if args.outdir else art.parent
    outdir.mkdir(parents=True, exist_ok=True)

    # Compute artifact digest
    algo = args.algo.lower()
    try:
        art_digest = _digest_file(art, algo)
    except Exception as e:
        print(f"[ERR] failed to digest artifact: {e}", file=sys.stderr)
        return 3

    # Optionally write checksum sidecar in common format
    if not args.no-checksum:
        sidecar = outdir / f"{art.name}.{algo}"
        line = f"{art_digest}  *{art.name}\n"
        _atomic_write_text(sidecar, line)

    # Inputs digests (missing inputs are recorded but not fatal)
    inputs: List[FileDigest] = []
    for s in args.inputs:
        p = Path(s)
        st = _safe_stat(p)
        if st.get("missing"):
            inputs.append(FileDigest(path=str(p), algo=algo, digest=None,
                                     size=None, mtime=None, missing=True))
            continue
        digest = _digest_file(p, algo)
        inputs.append(FileDigest(path=str(p), algo=algo, digest=digest,
                                 size=st["size"], mtime=st["mtime"], missing=False))

    # Derive a deterministic roll-up over inputs (sorted by path)
    rollup = hashlib.new(algo)
    for fd in sorted(inputs, key=lambda x: x.path):
        rollup.update((fd.path + "\n").encode("utf-8"))
        if fd.digest:
            rollup.update((fd.digest + "\n").encode("utf-8"))
    inputs_digest_rollup = {
        "algo": algo,
        "paths_and_digests_hash": rollup.hexdigest(),
        "count": str(len(inputs)),
    }

    # Build meta doc
    st_art = art.stat()
    md = MetaDocument(
        generated=_iso_utc(time.time()),
        command=" ".join(sys.argv),
        cwd=os.getcwd(),
        host=platform.node(),
        platform=f"{platform.system()} {platform.release()} ({platform.machine()})",
        python=platform.python_version(),
        git=_git_info(Path.cwd()),

        artifact={
            "path": str(art),
            "name": art.name,
            "size": st_art.st_size,
            "mtime": _iso_utc(st_art.st_mtime),
        },
        artifact_digest=FileDigest(
            path=str(art),
            algo=algo,
            digest=art_digest,
            size=st_art.st_size,
            mtime=_iso_utc(st_art.st_mtime),
            missing=False,
        ),
        inputs=inputs,
        inputs_digest_rollup=inputs_digest_rollup,
        extras={**_parse_kv_pairs(args.extra), **_load_extra_json(args.extra_json)},
    )

    # Write .meta.json (atomic)
    meta_path = outdir / f"{art.name}.meta.json"
    # Use dataclasses.asdict but convert nested dataclasses
    def _to_jsonable(obj):
        if isinstance(obj, list):
            return [_to_jsonable(x) for x in obj]
        if hasattr(obj, "__dataclass_fields__"):
            return {k: _to_jsonable(v) for k, v in asdict(obj).items()}
        if isinstance(obj, dict):
            return {k: _to_jsonable(v) for k, v in obj.items()}
        return obj

    _atomic_write_text(meta_path, json.dumps(_to_jsonable(md), indent=2, sort_keys=False) + "\n")
    print(f"[OK] checksum → {outdir / (art.name + '.' + algo)}" if not args.no-checksum else "[OK] checksum (skipped write)")
    print(f"[OK] meta → {meta_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
