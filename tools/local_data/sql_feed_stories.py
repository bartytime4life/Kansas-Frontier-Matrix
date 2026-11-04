"""Build the start page's story bundles from the pipeline's SQLite databases.

Each ``tools/local_data/stories/*.py`` builder (its contract is that package's docstring) turns tables into one
compact JSON bundle. Feed ``story-bundles`` keeps them in ``observations.sqlite``:

    kfm_story_bundles(story_id TEXT PRIMARY KEY, version INTEGER, built_at TEXT, sha256 TEXT, bytes INTEGER, bundle_json TEXT)

A row is written, under the pipeline lock, only when its bundle's content changed; ``sha256`` covers everything but
``built_at``. Builders read through a separate read-only connection, so a builder's failure cannot touch the database.
A story whose tables are missing or empty keeps any bundle it already has and is reported as waiting.

Nothing here is registered in ``sql_feeds.FEEDS`` yet, and the website does not publish the table: the relay's
``stories`` dataset is held in ``PENDING_DATASETS`` until the owner approves publication.

Preview, which writes no database:

    python3 -m tools.local_data.sql_feed_stories export --db OBS [--bulk-db BULK] [--tiger TIGER] --out DIR [--story ID]
    python3 -m tools.local_data.sql_feed_stories list --db OBS [--bulk-db BULK] [--tiger TIGER]
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import importlib
import json
import os
from pathlib import Path
import pkgutil
import sqlite3
import sys
from types import ModuleType
from urllib.parse import quote

from tools.local_data import stories as stories_package
from tools.local_data import sql_feeds as core
from tools.local_data.sql_feeds import FeedError
from tools.local_data.stories import MAX_BUNDLE_BYTES, has_rows

FORMAT = "kfm-story-bundle-v1"
STORY_DDL = """CREATE TABLE IF NOT EXISTS kfm_story_bundles (
  story_id TEXT PRIMARY KEY, version INTEGER NOT NULL, built_at TEXT NOT NULL, sha256 TEXT NOT NULL,
  bytes INTEGER NOT NULL, bundle_json TEXT NOT NULL) WITHOUT ROWID"""


def validate_story(module: ModuleType) -> dict:
    """A builder module's STORY, or FeedError naming what is wrong with it."""
    story, name = getattr(module, "STORY", None), module.__name__
    if not isinstance(story, dict) or not callable(getattr(module, "build", None)):
        raise FeedError(f"STORY_CONTRACT {name}: needs STORY and build(db)")
    for key, kind in (("id", str), ("version", int), ("db", str), ("tables", list), ("sources", list)):
        if not isinstance(story.get(key), kind) or not story[key]:
            raise FeedError(f"STORY_CONTRACT {name}: {key}")
    if story["db"] not in ("observations", "bulk"):
        raise FeedError(f"STORY_CONTRACT {name}: db must be observations or bulk")
    if story["id"].replace("-", "_") != name.rsplit(".", 1)[-1]:
        raise FeedError(f"STORY_CONTRACT {name}: id {story['id']} does not match the file name")
    for source in story["sources"]:
        if not all(isinstance(source.get(k), str) and source[k] for k in ("name", "license", "url", "citation")):
            raise FeedError(f"STORY_CONTRACT {name}: each source needs name, license, url and citation")
    return story


def builders() -> list[ModuleType]:
    """Every builder module, in id order."""
    modules = [importlib.import_module(f"{stories_package.__name__}.{info.name}")
               for info in pkgutil.iter_modules(stories_package.__path__) if not info.name.startswith("_")]
    for module in modules:
        validate_story(module)
    return sorted(modules, key=lambda m: m.STORY["id"])


def read_only(path: Path, tiger: Path | None = None, other: Path | None = None) -> sqlite3.Connection:
    """Open a database strictly read-only, attaching TIGER and the other database the same way when given."""
    db = sqlite3.connect(f"file:{quote(str(path))}?mode=ro", uri=True, timeout=30)
    db.execute("PRAGMA query_only=ON")
    for name, attached in (("tiger", tiger), ("other", other)):
        if attached:
            db.execute(f"ATTACH DATABASE ? AS {name}", (f"file:{quote(str(attached))}?mode=ro",))
    return db


@dataclass
class Paths:
    observations: Path
    bulk: Path | None = None
    tiger: Path | None = None

    def for_story(self, story: dict) -> Path | None:
        path = self.observations if story["db"] == "observations" else self.bulk
        return path if path and Path(path).is_file() else None

    def other_for(self, story: dict) -> Path | None:
        """The database a story reads as ``other``, when it declares tables there and the file exists."""
        path = self.bulk if story["db"] == "observations" else self.observations
        return path if story.get("other_tables") and path and Path(path).is_file() else None


def missing_tables(db, story: dict, *, other_attached: bool = False) -> list[str]:
    missing = [table for table in story["tables"] if not has_rows(db, table)]
    for table in story.get("other_tables", []):
        if not other_attached or not has_rows(db, table, "other"):
            missing.append(f"other.{table}")
    return missing


def serialize(bundle: dict) -> str:
    return json.dumps(bundle, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)


def content_hash(bundle: dict) -> str:
    """SHA-256 of the bundle without its build time, so that a rebuild of the same rows changes nothing."""
    return hashlib.sha256(serialize({k: v for k, v in bundle.items() if k != "built_at"}).encode()).hexdigest()


def build_bundle(module: ModuleType, db, built_at: str) -> dict | None:
    """The bundle for one story, or None when its builder has nothing yet. Oversized bundles are errors."""
    story = validate_story(module)
    data = module.build(db)
    if data is None:
        return None
    data = dict(data)
    observed = data.pop("_observed", None) or {"from": None, "to": None}
    bundle = {"format": FORMAT, "story": story["id"], "version": story["version"], "built_at": built_at,
              "sources": story["sources"], "observed": {"from": observed.get("from"), "to": observed.get("to")},
              "data": data}
    size = len(serialize(bundle).encode())
    if size > MAX_BUNDLE_BYTES:
        raise FeedError(f"STORY_BUNDLE_TOO_LARGE {story['id']} {size}")
    return bundle


def _built_at(now: datetime) -> str:
    return now.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _assess(module: ModuleType, paths: Paths, built_at: str, *, build: bool = True) -> dict:
    """Build one story, or say why it is waiting."""
    story = validate_story(module)
    path = paths.for_story(story)
    if path is None:
        return {"state": "waiting", "reason": f"{story['db']} database not available", "missing": list(story["tables"])}
    other = paths.other_for(story)
    db = read_only(path, paths.tiger, other)
    try:
        missing = missing_tables(db, story, other_attached=other is not None)
        if missing:
            return {"state": "waiting", "reason": "tables missing or empty", "missing": missing}
        if not build:
            return {"state": "ready"}
        bundle = build_bundle(module, db, built_at)
    finally:
        db.close()
    if bundle is None:
        return {"state": "waiting", "reason": "builder found too little data", "missing": []}
    return {"state": "ready", "bundle": bundle}


def story_bundles(ctx) -> dict:
    """Feed ``story-bundles``: rebuild every story whose tables are present and store what changed."""
    paths = Paths(ctx.db_path, ctx.bulk_db, ctx.tiger)
    built_at = _built_at(ctx.now())
    results = {"built": [], "unchanged": [], "waiting": {}, "failed": {}}
    fresh = []
    for module in builders():
        story = module.STORY
        try:
            outcome = _assess(module, paths, built_at)
        except (FeedError, sqlite3.Error, ValueError, KeyError, TypeError) as error:
            results["failed"][story["id"]] = f"{type(error).__name__}: {error}"
            ctx.note("story-failed", story=story["id"], error=str(error))
            continue
        if outcome["state"] == "waiting":
            results["waiting"][story["id"]] = {"reason": outcome["reason"], "missing": outcome["missing"]}
            ctx.note("story-waiting", story=story["id"], missing=outcome["missing"])
        else:
            fresh.append((story, outcome["bundle"]))
    db = core.open_db(ctx)
    try:
        core.guard(ctx)
        with core.pipeline_lock(ctx):
            db.execute(STORY_DDL)
            db.execute("BEGIN IMMEDIATE")
            try:
                for story, bundle in fresh:
                    digest = content_hash(bundle)
                    row = db.execute("SELECT sha256 FROM kfm_story_bundles WHERE story_id=?", (story["id"],)).fetchone()
                    if row and row[0] == digest:
                        results["unchanged"].append(story["id"])
                        continue
                    text = serialize(bundle)
                    db.execute("INSERT OR REPLACE INTO kfm_story_bundles VALUES (?,?,?,?,?,?)",
                               (story["id"], story["version"], bundle["built_at"], digest, len(text.encode()), text))
                    results["built"].append(story["id"])
                db.execute("COMMIT")
            except BaseException:
                db.execute("ROLLBACK")
                raise
    finally:
        db.close()
    ctx.note("story-bundles", **{k: results[k] for k in ("built", "unchanged")}, waiting=sorted(results["waiting"]))
    if results["failed"]:
        raise FeedError("STORY_BUILD_FAILED " + ",".join(sorted(results["failed"])))
    return results


def _selected(story_id: str | None) -> list[ModuleType]:
    modules = builders()
    if story_id is None:
        return modules
    chosen = [m for m in modules if m.STORY["id"] == story_id]
    if not chosen:
        raise FeedError(f"STORY_UNKNOWN {story_id}")
    return chosen


def export(paths: Paths, out: Path, story_id: str | None = None, *, now: datetime | None = None) -> dict:
    """Write ``out/<id>.json`` for each story with data. Opens databases read-only and writes none."""
    out.mkdir(parents=True, exist_ok=True)
    built_at = _built_at(now or core.utc_now())
    result: dict[str, dict] = {}
    for module in _selected(story_id):
        story = module.STORY
        outcome = _assess(module, paths, built_at)
        if outcome["state"] == "waiting":
            result[story["id"]] = {"state": "waiting", "reason": outcome["reason"], "missing": outcome["missing"]}
            continue
        text = serialize(outcome["bundle"])
        temporary = out / f".{story['id']}.json.partial"
        temporary.write_text(text, encoding="utf-8")
        os.replace(temporary, out / f"{story['id']}.json")
        result[story["id"]] = {"state": "ready", "bytes": len(text.encode()), "sha256": content_hash(outcome["bundle"])}
    return result


def listing(paths: Paths) -> dict:
    """Each story's state without building it."""
    result = {}
    for module in builders():
        outcome = _assess(module, paths, "", build=False)
        result[module.STORY["id"]] = outcome
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("command", choices=["export", "list"])
    parser.add_argument("--db", type=Path, required=True)
    parser.add_argument("--bulk-db", type=Path)
    parser.add_argument("--tiger", type=Path)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--story")
    args = parser.parse_args(argv)
    if not args.db.is_file():
        parser.error(f"no database at {args.db}")
    paths = Paths(args.db, args.bulk_db, args.tiger)
    try:
        if args.command == "list":
            result = listing(paths)
        else:
            if not args.out:
                parser.error("export needs --out")
            result = export(paths, args.out, args.story)
    except FeedError as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=1, sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
