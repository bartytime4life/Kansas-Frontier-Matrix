"""Project reviewed local inventory receipts into Site discovery metadata only.

No PDF reads, acquisition, upload, relocation, source admission or release writes.
Output is deterministic for the four explicitly selected input files.
"""
import argparse
import csv
import hashlib
import json
import re
from pathlib import Path, PurePosixPath

COLLECTIONS = ["Kansas bridges", "Kansas Road Maps", "KFM County Roadways",
               "KFM Historic County Township Maps", "KFM Past Published County Maps", "KFM Urban Roadways"]


def project(reconciliation, additional, sheets, screening):
    files = reconciliation["files"]
    if not 0 < len(files) <= 1000:
        raise ValueError("Inventory exceeds the bounded archive")
    by_path = {r["source_path"]: r for r in sheets}
    controls = {r["source_path"]: r for r in screening}
    extra = {r["path"]: r for r in additional["rows"]}
    if len(by_path) != len(sheets) or len(controls) != len(screening) or len(extra) != len(additional["rows"]):
        raise ValueError("Duplicate metadata identity")
    identities, hashes, records = set(), {}, []
    for row in files:
        name, digest, size = row["path"], row["sha256"], row["bytes"]
        parts = PurePosixPath(name).parts
        if (len(parts) != 2 or parts[0] not in COLLECTIONS or "\\" in name or len(name) > 260
                or not parts[1].lower().endswith(".pdf") or any(ord(c) < 32 for c in name)
                or name in identities or not re.fullmatch(r"[0-9a-f]{64}", digest)
                or not isinstance(size, int) or isinstance(size, bool) or not 0 < size <= 100 * 1024 * 1024):
            raise ValueError("Invalid inventory identity")
        identities.add(name)
        hashes.setdefault(digest, []).append(name)
        prior, control, later = by_path.get(name), controls.get(name), extra.get(name)
        for record, key in [(prior, "sha256"), (control, "source_sha256"), (later, "sha256")]:
            if record and record[key] != digest:
                raise ValueError("Prior metadata does not match current PDF bytes")
        flags = []
        if later and later.get("readerWarnings"):
            flags.append("pdf-reader-warning")
        if prior and prior.get("ocr_status") == "blank_source":
            flags.append("blank-source")
        # Existing statewide inventory records this 977-byte file as blank.
        if name == "Kansas Road Maps/1967 Kansas.pdf" and size == 977:
            flags.append("blank-source")
        label, basis, start, end = None, "unknown", None, None
        if prior and prior.get("edition_label"):
            label, basis = prior["edition_label"], prior["edition_basis"]
            start = int(prior["edition_start_year"]) if prior.get("edition_start_year") else None
            end = int(prior["edition_end_year"]) if prior.get("edition_end_year") else start
        elif years := re.findall(r"(?<!\d)(?:18|19|20)\d{2}(?!\d)", parts[1]):
            start, end = int(years[0]), int(years[-1])
            label, basis = "–".join(dict.fromkeys(years)), "source_filename_label"
        if start is not None and (end is None or not 1800 <= start <= end <= 2100 or end - start > 5):
            raise ValueError("Unbounded or invalid edition-year clue")
        if start is not None and end is not None and start != end:
            label = f"{start}–{end}"
        embedded = (control and control["embedded_control_status"] == "embedded_georeference_candidate") or (later and later["state"] == "embedded-control-candidate")
        records.append(dict(id=name, collection=parts[0], fileName=parts[1], sizeBytes=size, sha256=digest,
                            placeHint=(prior.get("county") or prior.get("city") or None) if prior else None,
                            editionLabel=label, editionBasis=basis, startYear=start, endYear=end,
                            alignment="embedded-control-unreviewed" if embedded else "manual-control-needed",
                            flags=sorted(set(flags))))
    for record in records:
        aliases = hashes[record["sha256"]]
        if len(aliases) > 1:
            record["flags"].append("conflicting-filenames")
            record.update(editionLabel=None, editionBasis="identity-conflict", startYear=None, endYear=None, placeHint=None)
        record["sameBytesAs"] = [name for name in aliases if name != record["id"]]
    return {"version": 1, "inventorySnapshotAt": reconciliation["createdAt"], "role": "LOCAL_DISCOVERY_ONLY",
            "collections": COLLECTIONS, "records": sorted(records, key=lambda r: r["id"])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("reconciliation", "additional", "sheets", "screening", "output"):
        parser.add_argument("--" + name, required=True, type=Path)
    args = parser.parse_args()
    result = project(json.loads(args.reconciliation.read_text()), json.loads(args.additional.read_text()),
                     list(csv.DictReader(args.sheets.open())), list(csv.DictReader(args.screening.open())))
    result["inputDigests"] = {name: hashlib.sha256(getattr(args, name).read_bytes()).hexdigest()
                             for name in ("reconciliation", "additional", "sheets", "screening")}
    args.output.write_text(json.dumps(result, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n")


if __name__ == "__main__":
    main()
