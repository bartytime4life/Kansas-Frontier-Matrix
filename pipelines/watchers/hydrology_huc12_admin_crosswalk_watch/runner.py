#!/usr/bin/env python3
"""
KFM HUC12 ↔ administrative boundary crosswalk watcher runner.

Builds governed crosswalk candidate rows from processed PostGIS tables:

  kfm_crosswalk.huc12_processed
  kfm_crosswalk.admin_processed

Emits:

  data/receipts/crosswalk/<run_id>.json
  data/proofs/crosswalk/<run_id>/validation_summary.json

This runner does not publish artifacts.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path


ALGORITHM_VERSION = "huc12_admin_crosswalk_v0.1.0"
WATCHER = "hydrology_huc12_admin_crosswalk_watch"


def run(cmd: list[str], *, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        cmd,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )


def sql_quote(value: str) -> str:
    return value.replace("'", "''")


def run_psql(dsn: str, sql_path: Path, variables: dict[str, str] | None = None) -> None:
    cmd = ["psql", dsn, "-v", "ON_ERROR_STOP=1"]

    for key, value in (variables or {}).items():
        cmd.extend(["-v", f"{key}={value}"])

    cmd.extend(["-f", str(sql_path)])

    subprocess.run(cmd, check=True)


def scalar_psql(dsn: str, sql: str) -> str:
    result = run(["psql", dsn, "-v", "ON_ERROR_STOP=1", "-Atc", sql])
    return result.stdout.strip()


def exec_psql(dsn: str, sql: str) -> None:
    subprocess.run(
        ["psql", dsn, "-v", "ON_ERROR_STOP=1", "-c", sql],
        check=True,
    )


def ensure_required_files(root: Path) -> None:
    required = [
        root / "sql/001_schema.sql",
        root / "sql/010_build_crosswalk.sql",
    ]

    missing = [str(path) for path in required if not path.is_file()]

    if missing:
        raise SystemExit("Missing required runner SQL files: " + ", ".join(missing))


def ensure_output_dirs(repo_root: Path, run_id: str) -> tuple[Path, Path]:
    receipt_dir = repo_root / "data/receipts/crosswalk"
    proof_dir = repo_root / "data/proofs/crosswalk" / run_id

    receipt_dir.mkdir(parents=True, exist_ok=True)
    proof_dir.mkdir(parents=True, exist_ok=True)

    return receipt_dir, proof_dir


def table_count(dsn: str, table: str) -> int:
    value = scalar_psql(dsn, f"SELECT count(*) FROM {table};")
    return int(value or 0)


def collect_validation(dsn: str, receipt_id: str) -> dict[str, int]:
    safe_receipt_id = sql_quote(receipt_id)

    checks = {
        "negative_overlap": """
            SELECT count(*)
            FROM kfm_crosswalk.crosswalk_pairs
            WHERE run_receipt_id = '{receipt_id}'
              AND overlap_m2 < 0;
        """,
        "overlap_gt_huc_area": """
            SELECT count(*)
            FROM kfm_crosswalk.crosswalk_pairs
            WHERE run_receipt_id = '{receipt_id}'
              AND overlap_m2 > huc_area_m2;
        """,
        "overlap_gt_admin_area": """
            SELECT count(*)
            FROM kfm_crosswalk.crosswalk_pairs
            WHERE run_receipt_id = '{receipt_id}'
              AND overlap_m2 > admin_area_m2;
        """,
        "bad_overlap_pct_huc": """
            SELECT count(*)
            FROM kfm_crosswalk.crosswalk_pairs
            WHERE run_receipt_id = '{receipt_id}'
              AND (overlap_pct_huc < 0 OR overlap_pct_huc > 1);
        """,
        "bad_overlap_pct_admin": """
            SELECT count(*)
            FROM kfm_crosswalk.crosswalk_pairs
            WHERE run_receipt_id = '{receipt_id}'
              AND (overlap_pct_admin < 0 OR overlap_pct_admin > 1);
        """,
        "bad_weight": """
            SELECT count(*)
            FROM kfm_crosswalk.crosswalk_pairs
            WHERE run_receipt_id = '{receipt_id}'
              AND (weight < 0 OR weight > 1);
        """,
        "bad_crs": """
            SELECT count(*)
            FROM kfm_crosswalk.crosswalk_pairs
            WHERE run_receipt_id = '{receipt_id}'
              AND crs <> 'EPSG:5070';
        """,
        "missing_geometry_hash": """
            SELECT count(*)
            FROM kfm_crosswalk.crosswalk_pairs
            WHERE run_receipt_id = '{receipt_id}'
              AND geometry_hash !~ '^sha256:[a-f0-9]{{64}}$';
        """,
        "missing_spec_hash": """
            SELECT count(*)
            FROM kfm_crosswalk.crosswalk_pairs
            WHERE run_receipt_id = '{receipt_id}'
              AND spec_hash !~ '^sha256:[a-f0-9]{{64}}$';
        """,
        "missing_source_snapshots": """
            SELECT count(*)
            FROM kfm_crosswalk.crosswalk_pairs
            WHERE run_receipt_id = '{receipt_id}'
              AND array_length(source_snapshot_ids, 1) < 2;
        """,
    }

    results: dict[str, int] = {}

    for name, query in checks.items():
        sql = query.format(receipt_id=safe_receipt_id)
        results[name] = int(scalar_psql(dsn, sql) or 0)

    return results


def write_json(path: Path, payload: dict) -> None:
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build KFM HUC12 ↔ administrative boundary crosswalk candidate rows."
    )

    parser.add_argument(
        "--dsn",
        default=os.environ.get("DATABASE_URL"),
        help="PostgreSQL DSN. Defaults to DATABASE_URL.",
    )
    parser.add_argument(
        "--run-id",
        required=True,
        help="Stable run identifier used for receipts and proof output.",
    )
    parser.add_argument(
        "--no-publish",
        action="store_true",
        help="Explicitly keep disposition as candidate/no-publish.",
    )
    parser.add_argument(
        "--skip-schema",
        action="store_true",
        help="Skip applying sql/001_schema.sql.",
    )
    parser.add_argument(
        "--replace-run",
        action="store_true",
        help="Delete existing crosswalk rows for this run_receipt_id before rebuilding.",
    )

    args = parser.parse_args()

    if not args.dsn:
        raise SystemExit("DATABASE_URL or --dsn is required")

    watcher_dir = Path(__file__).resolve().parent
    repo_root = watcher_dir.parents[2]

    ensure_required_files(watcher_dir)

    receipt_dir, proof_dir = ensure_output_dirs(repo_root, args.run_id)

    receipt_id = f"run_receipt:{WATCHER}:{args.run_id}"
    safe_receipt_id = sql_quote(receipt_id)

    started_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    if not args.skip_schema:
        run_psql(args.dsn, watcher_dir / "sql/001_schema.sql")

    huc_count = table_count(args.dsn, "kfm_crosswalk.huc12_processed")
    admin_count = table_count(args.dsn, "kfm_crosswalk.admin_processed")

    if huc_count == 0:
        raise SystemExit("No rows found in kfm_crosswalk.huc12_processed")

    if admin_count == 0:
        raise SystemExit("No rows found in kfm_crosswalk.admin_processed")

    if args.replace_run:
        exec_psql(
            args.dsn,
            f"""
            DELETE FROM kfm_crosswalk.crosswalk_pairs
            WHERE run_receipt_id = '{safe_receipt_id}';
            """,
        )

    run_psql(
        args.dsn,
        watcher_dir / "sql/010_build_crosswalk.sql",
        {
            "run_receipt_id": receipt_id,
            "algorithm_version": ALGORITHM_VERSION,
        },
    )

    record_count = int(
        scalar_psql(
            args.dsn,
            f"""
            SELECT count(*)
            FROM kfm_crosswalk.crosswalk_pairs
            WHERE run_receipt_id = '{safe_receipt_id}';
            """,
        )
        or 0
    )

    validation = collect_validation(args.dsn, receipt_id)
    anomaly_count = sum(validation.values())

    finished_at = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    validation_summary = {
        "object_type": "validation_summary",
        "run_receipt_id": receipt_id,
        "watcher": WATCHER,
        "algorithm_version": ALGORITHM_VERSION,
        "record_count": record_count,
        "checks": validation,
        "anomaly_count": anomaly_count,
        "passed": anomaly_count == 0,
    }

    receipt = {
        "object_type": "run_receipt",
        "run_receipt_id": receipt_id,
        "watcher": WATCHER,
        "run_id": args.run_id,
        "algorithm_version": ALGORITHM_VERSION,
        "started_at": started_at,
        "finished_at": finished_at,
        "crs": "EPSG:5070",
        "input_tables": {
            "huc12_processed": "kfm_crosswalk.huc12_processed",
            "admin_processed": "kfm_crosswalk.admin_processed",
        },
        "input_counts": {
            "huc12_processed": huc_count,
            "admin_processed": admin_count,
        },
        "outputs": {
            "table": "kfm_crosswalk.crosswalk_pairs",
            "receipt_path": str(receipt_dir / f"{args.run_id}.json"),
            "proof_dir": str(proof_dir),
            "validation_summary": str(proof_dir / "validation_summary.json"),
        },
        "record_count": record_count,
        "anomaly_count": anomaly_count,
        "validation_passed": anomaly_count == 0,
        "disposition": (
            "candidate_no_publish"
            if args.no_publish
            else "candidate_ready_for_promotion_review"
        ),
        "publication": {
            "published": False,
            "reason": "watcher emits governed candidates only; promotion is separate",
        },
    }

    write_json(proof_dir / "validation_summary.json", validation_summary)
    write_json(receipt_dir / f"{args.run_id}.json", receipt)

    print(json.dumps(receipt, indent=2, sort_keys=True))

    if anomaly_count != 0:
        return 2

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        print(f"Command failed with exit code {exc.returncode}: {exc.cmd}", file=sys.stderr)
        if exc.stdout:
            print(exc.stdout, file=sys.stderr)
        if exc.stderr:
            print(exc.stderr, file=sys.stderr)
        raise
