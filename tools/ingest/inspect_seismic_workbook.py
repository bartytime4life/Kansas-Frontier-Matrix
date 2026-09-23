"""Read-only OOXML preflight, not a KGS schema adapter or admission decision.

Only supplied bytes are inspected. No ZIP extraction, formula evaluation,
external-link resolution, macros, source request, or lifecycle write occurs.
The caller labels the product and candidate header row; neither is inferred.
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
from pathlib import PurePosixPath
import re
import stat
import sys
import xml.etree.ElementTree as ET
import zipfile

MAX_BYTES = 8 * 1024 * 1024
MAX_EXPANDED = 16 * 1024 * 1024
MAX_MEMBER = 2 * 1024 * 1024
S = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
P = "{http://schemas.openxmlformats.org/package/2006/relationships}"


class WorkbookInspectionError(ValueError):
    pass


def inspect_workbook(body: bytes, *, product_kind: str, header_row: int = 1) -> dict:
    """Return bounded sheet/header observations; every success still needs review."""
    if product_kind not in ("recorded-earthquakes", "felt-reports"):
        raise WorkbookInspectionError("PRODUCT_KIND_REQUIRED")
    if type(header_row) is not int or not 1 <= header_row <= 100:
        raise WorkbookInspectionError("HEADER_ROW_BOUND")
    if not isinstance(body, bytes) or not 0 < len(body) <= MAX_BYTES:
        raise WorkbookInspectionError("WORKBOOK_BYTE_BOUND")
    try:
        with zipfile.ZipFile(io.BytesIO(body)) as archive:
            infos = archive.infolist()
            if not 1 <= len(infos) <= 256 or sum(info.file_size for info in infos) > MAX_EXPANDED:
                raise WorkbookInspectionError("ARCHIVE_BOUND")
            names: set[str] = set()
            for info in infos:
                name = info.filename
                parts = PurePosixPath(name).parts
                if (not name or len(name) > 512 or name in names or name.startswith("/")
                        or "\\" in name or ":" in name or "\x00" in name
                        or any(part in ("", ".", "..") for part in name.rstrip("/").split("/"))
                        or not parts or info.flag_bits & 1
                        or stat.S_ISLNK(info.external_attr >> 16)):
                    raise WorkbookInspectionError("ARCHIVE_MEMBER")
                names.add(name)
                if (info.file_size > MAX_MEMBER
                        or info.file_size > max(1, info.compress_size) * 200):
                    raise WorkbookInspectionError("EXPANSION_BOUND")
                if "vbaproject" in name.lower() or "/activex/" in name.lower() or "/embeddings/" in name.lower():
                    raise WorkbookInspectionError("ACTIVE_CONTENT")

            def xml(name: str) -> ET.Element:
                if name not in names:
                    raise WorkbookInspectionError("MISSING_XML_PART")
                with archive.open(name) as stream:
                    raw = stream.read(MAX_MEMBER + 1)
                if len(raw) > MAX_MEMBER:
                    raise WorkbookInspectionError("EXPANSION_BOUND")
                # UTF-16/32 and DTD/entity declarations are outside this deliberately narrow profile.
                if b"\x00" in raw or re.search(br"<!\s*(?:DOCTYPE|ENTITY)\b", raw, re.I):
                    raise WorkbookInspectionError("XML_DECLARATION")
                root = ET.fromstring(raw)
                if sum(1 for _ in root.iter()) > 100000:
                    raise WorkbookInspectionError("XML_NODE_BOUND")
                return root

            content_types = xml("[Content_Types].xml")
            if content_types.tag != "{http://schemas.openxmlformats.org/package/2006/content-types}Types":
                raise WorkbookInspectionError("OOXML_PROFILE")
            if any("macroenabled" in element.attrib.get("ContentType", "").lower() for element in content_types):
                raise WorkbookInspectionError("ACTIVE_CONTENT")
            workbook = xml("xl/workbook.xml")
            relations = xml("xl/_rels/workbook.xml.rels")
            if workbook.tag != S + "workbook" or relations.tag != P + "Relationships":
                raise WorkbookInspectionError("OOXML_PROFILE")
            lookup: dict[str, str] = {}
            external_count = 0
            for name in sorted(names):
                if name.endswith(".rels"):
                    for relation in xml(name):
                        if relation.attrib.get("TargetMode") == "External":
                            external_count += 1
            for relation in relations:
                identifier = relation.attrib.get("Id", "")
                if not identifier or identifier in lookup:
                    raise WorkbookInspectionError("RELATION_ID")
                if relation.attrib.get("TargetMode") == "External":
                    lookup[identifier] = ""
                    continue
                target = relation.attrib.get("Target", "")
                target = target.lstrip("/") if target.startswith("/xl/") else "xl/" + target
                if not re.fullmatch(r"xl/worksheets/[A-Za-z0-9_.-]+\.xml", target):
                    # Other workbook relations (styles, sharedStrings, theme) are not worksheets.
                    if relation.attrib.get("Type", "").endswith("/worksheet"):
                        raise WorkbookInspectionError("WORKSHEET_TARGET")
                    lookup[identifier] = ""
                else:
                    lookup[identifier] = target
            strings: list[str] = []
            if "xl/sharedStrings.xml" in names:
                for item in xml("xl/sharedStrings.xml").findall(S + "si"):
                    text = "".join(node.text or "" for node in item.iter(S + "t"))
                    strings.append(text)
            sheets = workbook.findall(S + "sheets/" + S + "sheet")
            if not 1 <= len(sheets) <= 32:
                raise WorkbookInspectionError("SHEET_BOUND")
            reports = []
            seen_sheets: set[str] = set()
            for sheet in sheets:
                name = sheet.attrib.get("name", "")
                if not name or len(name) > 128 or name in seen_sheets:
                    raise WorkbookInspectionError("SHEET_ID")
                seen_sheets.add(name)
                target = lookup.get(sheet.attrib.get(R + "id", ""), "")
                if not target:
                    raise WorkbookInspectionError("WORKSHEET_TARGET")
                root = xml(target)
                if root.tag != S + "worksheet":
                    raise WorkbookInspectionError("OOXML_PROFILE")
                rows = root.findall(S + "sheetData/" + S + "row")
                headers = []
                formula_count = 0
                cells_seen: set[str] = set()
                row_ids: set[str] = set()
                for row in rows:
                    row_id = row.attrib.get("r", "")
                    if not re.fullmatch(r"[1-9][0-9]{0,6}", row_id) or row_id in row_ids:
                        raise WorkbookInspectionError("ROW_ID")
                    row_ids.add(row_id)
                    for cell in row.findall(S + "c"):
                        cell_ref = cell.attrib.get("r", "")
                        if (not re.fullmatch(r"[A-Z]{1,3}[1-9][0-9]{0,6}", cell_ref) or cell_ref in cells_seen
                                or re.sub(r"^[A-Z]+", "", cell_ref) != row_id):
                            raise WorkbookInspectionError("CELL_ID")
                        cells_seen.add(cell_ref)
                        formula = cell.find(S + "f") is not None
                        formula_count += formula
                        if row.attrib.get("r") != str(header_row):
                            continue
                        if len(headers) >= 256:
                            raise WorkbookInspectionError("HEADER_BOUND")
                        kind = cell.attrib.get("t", "n")
                        value = cell.findtext(S + "v", default="")
                        if formula:
                            value = "[FORMULA_NOT_EVALUATED]"
                        elif kind == "s":
                            if not re.fullmatch(r"[0-9]{1,6}", value) or int(value) >= len(strings):
                                raise WorkbookInspectionError("SHARED_STRING_INDEX")
                            value = strings[int(value)]
                        elif kind == "inlineStr":
                            value = "".join(node.text or "" for node in cell.iter(S + "t"))
                        if len(value) > 256:
                            raise WorkbookInspectionError("HEADER_BOUND")
                        headers.append({"cell": cell_ref, "type": kind, "literal": value})
                reports.append({"sheet_name": name, "rows_present": len(rows),
                                "cells_present": len(cells_seen), "formula_cells": formula_count,
                                "candidate_headers": headers})
            return {"outcome": "REVIEW_REQUIRED", "admission": "NOT_ADMITTED",
                    "product_kind_supplied_by_caller": product_kind,
                    "candidate_header_row": header_row,
                    "sha256": "sha256:" + hashlib.sha256(body).hexdigest(),
                    "byte_count": len(body), "external_relationships": external_count,
                    "sheets": reports,
                    "limits": "No event/felt-report schema, coordinate meaning, dates, rights or source origin inferred."}
    except (zipfile.BadZipFile, ET.ParseError, KeyError, OSError, RuntimeError, NotImplementedError):
        raise WorkbookInspectionError("WORKBOOK_UNREADABLE") from None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    parser.add_argument("--kind", required=True, choices=("recorded-earthquakes", "felt-reports"))
    parser.add_argument("--header-row", type=int, default=1)
    args = parser.parse_args()
    try:
        # Refuse leaf symlinks and non-regular files before reading. Parent-directory
        # authority remains operator-owned; this is not a hardened custody store.
        if not hasattr(os, "O_NOFOLLOW"):
            raise WorkbookInspectionError("NOFOLLOW_UNAVAILABLE")
        fd = os.open(args.path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
        with os.fdopen(fd, "rb") as source:
            metadata = os.fstat(source.fileno())
            if not stat.S_ISREG(metadata.st_mode) or metadata.st_size > MAX_BYTES:
                raise WorkbookInspectionError("INPUT_FILE_BOUND")
            body = source.read(MAX_BYTES + 1)
        report = inspect_workbook(body, product_kind=args.kind, header_row=args.header_row)
        print(json.dumps(report, ensure_ascii=True, sort_keys=True, indent=2))
        return 0  # inspection ran; REVIEW_REQUIRED is not admission or a PASS gate
    except (WorkbookInspectionError, OSError) as error:
        reason = str(error) if isinstance(error, WorkbookInspectionError) else "INPUT_UNREADABLE"
        print(json.dumps({"outcome": "ERROR", "reason": reason}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
