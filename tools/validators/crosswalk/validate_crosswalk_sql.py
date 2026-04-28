#!/usr/bin/env python3
"""Run crosswalk SQL validator and optionally fail on non-zero failures."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


DEFAULT_SQL = Path(__file__).with_name("validate_crosswalk_sql.sql")


def run_validator(dsn: str, sql_path: Path) -> list[tuple[str, int]]:
    if not sql_path.is_file():
        raise FileNotFoundError(f"validator SQL not found: {sql_path}")

    cmd = [
        "psql",
        dsn,
        "-v",
        "ON_ERROR_STOP=1",
        "-At",
        "-F",
        "|",
        "-f",
        str(sql_path),
    ]
    proc = subprocess.run(cmd, check=True, text=True, capture_output=True)

    rows: list[tuple[str, int]] = []
    for line in proc.stdout.splitlines():
        if not line.strip():
            continue
        name, count = line.split("|", 1)
        rows.append((name, int(count)))
    return rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dsn", required=True, help="Postgres DSN for validator execution")
    parser.add_argument(
        "--sql",
        type=Path,
        default=DEFAULT_SQL,
        help="Path to validation SQL file",
    )
    parser.add_argument(
        "--fail-on-errors",
        action="store_true",
        help="Exit non-zero when any validation rule reports failures",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        rows = run_validator(args.dsn, args.sql)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    except subprocess.CalledProcessError as exc:
        print(exc.stderr.strip() or str(exc), file=sys.stderr)
        return exc.returncode or 1

    total = 0
    for check_name, failures in rows:
        total += failures
        print(f"{check_name}\t{failures}")

    print(f"total_failures\t{total}")
    if args.fail_on_errors and total > 0:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
