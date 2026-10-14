#!/usr/bin/env python3
"""Explicit bounded Kansas land-record imports, status, listing and integrity audit."""
from pathlib import Path
import argparse
import importlib.util
import json
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT), str(ROOT / "packages/domains/people-dna-land/src")]
from people_dna_land.land_records import MAX_BYTES, SOURCES, canonical, instant, stamp
from people_dna_land.land_store import initialize, list_records, read_file, status


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True, help="Fresh private directory outside every Git checkout")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init")
    sub.add_parser("status")
    sub.add_parser("audit")
    p = sub.add_parser("withdraw-capture")
    p.add_argument("--capture-id", required=True)
    p.add_argument("--reason", required=True)
    p = sub.add_parser("import")
    p.add_argument("--source", required=True, choices=sorted(SOURCES))
    p.add_argument("--file", type=Path, required=True)
    p.add_argument("--url", required=True)
    p.add_argument("--retrieved-at", required=True, help="UTC time of export/capture, YYYY-MM-DDTHH:MM:SSZ")
    p.add_argument("--format", choices=["glo-text", "mapped-csv"], default="mapped-csv")
    p.add_argument("--mapping", type=Path, help="Explicit KFM field -> source column JSON map")
    p.add_argument("--document", type=Path, action="append", default=[])
    p.add_argument("--document-url", action="append", default=[])
    p.add_argument("--max-records", type=int, default=100)
    p.add_argument("--max-bytes", type=int, default=2 * 1024 * 1024)
    p = sub.add_parser("list")
    for flag in ("source", "county", "kind", "start", "end", "after"):
        p.add_argument("--" + flag)
    p.add_argument("--limit", type=int, default=25)
    args = parser.parse_args(argv)
    try:
        if args.command == "init":
            initialize(args.root)
            result = status(args.root)
        elif args.command == "status":
            result = status(args.root)
        elif args.command == "audit":
            from people_dna_land.land_store import audit
            result = audit(args.root)
        elif args.command == "withdraw-capture":
            from people_dna_land.land_store import withdraw_capture
            result = withdraw_capture(args.root, args.capture_id, args.reason)
        elif args.command == "list":
            result = list_records(args.root, **{k: getattr(args, k) for k in ("source", "county", "kind", "start", "end", "after", "limit")})
        else:
            if not 1 <= args.max_bytes <= MAX_BYTES or len(args.document) != len(args.document_url) or len(args.document) > 10:
                raise ValueError("IMPORT_BUDGET_OR_DOCUMENTS_INVALID")
            instant(args.retrieved_at)
            if args.retrieved_at > stamp():
                raise ValueError("CAPTURE_TIME_IN_FUTURE")
            raw = read_file(args.file.absolute(), args.max_bytes)
            documents = [(url, read_file(path.absolute(), args.max_bytes)) for path, url in zip(args.document, args.document_url)]
            if len(raw) + sum(len(b) for _, b in documents) > args.max_bytes:
                raise ValueError("IMPORT_TOTAL_BYTE_LIMIT")
            mapping = json.loads(read_file(args.mapping.absolute(), 8192)) if args.mapping else None
            spec = importlib.util.spec_from_file_location("kfm_land_ingest", ROOT / "pipelines/ingest/people-dna-land/land_records.py")
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            result = module.ingest(args.root, args.source, raw, url=args.url, retrieved_at=args.retrieved_at, format=args.format, mapping=mapping, documents=documents, max_records=args.max_records)
    except (OSError, ValueError, KeyError, TypeError, UnicodeError) as error:
        reason = str(error) if isinstance(error, ValueError) and str(error).replace("_", "").isalnum() and str(error).isupper() else "LAND_IMPORT_FAILED"
        print(canonical({"outcome": "ERROR", "reason_code": reason, "authority": "CANDIDATE_ONLY"}).decode())
        return 1
    print(canonical(result).decode())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
