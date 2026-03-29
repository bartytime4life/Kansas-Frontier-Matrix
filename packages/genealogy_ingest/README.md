# `pipelines/genealogy_ingest/` starter

```text
pipelines/
└── genealogy_ingest/
    ├── README.md
    ├── pyproject.toml
    ├── schemas/
    │   ├── canonical.person.schema.json
    │   ├── canonical.event.schema.json
    │   ├── canonical.relationship.schema.json
    │   ├── canonical.dna_kit.schema.json
    │   └── canonical.provenance.schema.json
    ├── src/
    │   └── genealogy_ingest/
    │       ├── __init__.py
    │       ├── cli.py
    │       ├── models.py
    │       ├── normalize.py
    │       ├── gedcom.py
    │       ├── vendor_csv.py
    │       ├── dna_manifest.py
    │       └── receipts.py
    └── tests/
        ├── test_dates.py
        ├── test_gedcom_minimal.py
        ├── test_vendor_csv.py
        └── test_dna_manifest.py
```

---

## `README.md`

````md
# Genealogy Ingest

Evidence-first genealogy and DNA manifest ingestion into a canonical KFM-aligned model.

## Repo fit
- **Path:** `pipelines/genealogy_ingest/`
- **Upstream:** raw GEDCOM, GEDCOM 7 / GEDZip, vendor CSV/JSON, raw DNA text exports
- **Downstream:** catalog, graph projections, search, governed publication surfaces

## Accepted inputs
- GEDCOM 5.5.1
- GEDCOM 7.0 / GEDZip
- vendor genealogy CSV/JSON exports
- consumer raw DNA text exports (manifest-only by default)

## Exclusions
- no SNP-row normalization into authoritative truth by default
- no inferred kinship written as source truth
- no redistribution of source kit identifiers

## Truth posture
- **Authoritative:** source facts + normalized events + provenance + evidence refs
- **Derived:** graph edges, search indexes, clusters, embeddings
- **Fail-closed:** quarantine malformed dates, broken relationships, missing evidence, unresolved consent

```mermaid
flowchart LR
  A[Source edge] --> B[RAW]
  B --> C[WORK / PARSE]
  C --> D{Validation}
  D -- fail --> Q[QUARANTINE]
  D -- pass --> E[Normalize]
  E --> F[PROCESSED]
  F --> G[CATALOG / TRIPLET]
  G --> H[PUBLISHED]
````

````

---

## `pyproject.toml`

```toml
[project]
name = "genealogy-ingest"
version = "0.1.0"
description = "GEDCOM, genealogy CSV, and DNA manifest ingestion"
requires-python = ">=3.11"
dependencies = [
  "pydantic>=2.8",
  "jsonschema>=4.23",
  "python-dateutil>=2.9"
]

[project.scripts]
kfm-ingest-genealogy = "genealogy_ingest.cli:main"
````

---

## `src/genealogy_ingest/models.py`

```python
from __future__ import annotations

from typing import Literal, Optional
from pydantic import BaseModel, Field


EventType = Literal[
    "birth", "marriage", "death", "residence", "census", "immigration", "DNA_SAMPLE", "unknown"
]
RelationshipType = Literal["parent", "spouse", "child"]


class Place(BaseModel):
    place_name: str
    lat: Optional[float] = None
    lon: Optional[float] = None
    gnis_id: Optional[str] = None


class EvidenceRef(BaseModel):
    source_file: str
    pointer: str
    snippet: Optional[str] = None


class Provenance(BaseModel):
    record_id: str
    vendor: str
    export_date: Optional[str] = None
    spec_hash: str


class Person(BaseModel):
    id_hash: str
    name_norm: Optional[str] = None
    sex: Optional[str] = None
    birth_event_id: Optional[str] = None
    death_event_id: Optional[str] = None


class Relationship(BaseModel):
    id: str
    type: RelationshipType
    subject_id: str
    object_id: str
    evidence_ref: EvidenceRef


class Event(BaseModel):
    id: str
    person_id: str
    type: EventType
    date_iso8601: Optional[str] = None
    place: Optional[Place] = None
    evidence_ref: EvidenceRef


class DNAKit(BaseModel):
    kit_hash: str
    person_id: Optional[str] = None
    vendor: str
    genome_build: Optional[str] = None
    file_checksum: str


class Consent(BaseModel):
    person_id: str
    exports_allowed: bool = False
    redistribution: bool = False
```

---

## `src/genealogy_ingest/normalize.py`

```python
from __future__ import annotations

import hashlib
import hmac
import re
from datetime import datetime
from typing import Optional


GEDCOM_MONTHS = {
    "JAN": "01", "FEB": "02", "MAR": "03", "APR": "04",
    "MAY": "05", "JUN": "06", "JUL": "07", "AUG": "08",
    "SEP": "09", "OCT": "10", "NOV": "11", "DEC": "12",
}


def stable_hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def hmac_kit_hash(vendor_kit_id: str, salt: bytes) -> str:
    return hmac.new(salt, vendor_kit_id.encode("utf-8"), hashlib.sha256).hexdigest()


def normalize_name(raw: str) -> str:
    # GEDCOM often uses slashes around surnames: John /Smith/
    return re.sub(r"\s+", " ", raw.replace("/", "").strip())


def normalize_date(raw: Optional[str]) -> Optional[str]:
    if not raw:
        return None

    raw = raw.strip().upper()

    # Exact GEDCOM-style date: 12 MAR 1882
    m = re.fullmatch(r"(\d{1,2})\s+([A-Z]{3})\s+(\d{4})", raw)
    if m:
        day, mon, year = m.groups()
        return f"{year}-{GEDCOM_MONTHS[mon]}-{int(day):02d}"

    # Month year: MAR 1882
    m = re.fullmatch(r"([A-Z]{3})\s+(\d{4})", raw)
    if m:
        mon, year = m.groups()
        return f"{year}-{GEDCOM_MONTHS[mon]}"

    # Year only
    m = re.fullmatch(r"\d{4}", raw)
    if m:
        return raw

    # About / estimated year
    m = re.fullmatch(r"(ABT|ABOUT|EST|ESTIMATED)\s+(\d{4})", raw)
    if m:
        return m.group(2)

    return None


def map_gedcom_event(tag: str) -> str:
    return {
        "BIRT": "birth",
        "MARR": "marriage",
        "DEAT": "death",
        "RESI": "residence",
        "CENS": "census",
        "IMMI": "immigration",
    }.get(tag, "unknown")
```

---

## `src/genealogy_ingest/gedcom.py`

```python
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from .models import Event, EvidenceRef, Person, Relationship, Place
from .normalize import map_gedcom_event, normalize_date, normalize_name, stable_hash


@dataclass
class IndiRecord:
    xref: str
    name: Optional[str] = None
    sex: Optional[str] = None
    events: List[Tuple[str, Optional[str], Optional[str], str]] = field(default_factory=list)


@dataclass
class FamRecord:
    xref: str
    husb: Optional[str] = None
    wife: Optional[str] = None
    chil: List[str] = field(default_factory=list)
    marr_date: Optional[str] = None
    marr_place: Optional[str] = None


def parse_gedcom(path: str) -> tuple[list[Person], list[Event], list[Relationship]]:
    text = Path(path).read_text(encoding="utf-8", errors="replace").splitlines()

    indis: Dict[str, IndiRecord] = {}
    fams: Dict[str, FamRecord] = {}

    current_indi: Optional[IndiRecord] = None
    current_fam: Optional[FamRecord] = None
    current_event_tag: Optional[str] = None
    current_event_date: Optional[str] = None
    current_event_place: Optional[str] = None
    current_event_pointer: Optional[str] = None

    def flush_event():
        nonlocal current_event_tag, current_event_date, current_event_place, current_event_pointer, current_indi
        if current_indi and current_event_tag:
            current_indi.events.append(
                (current_event_tag, current_event_date, current_event_place, current_event_pointer or current_indi.xref)
            )
        current_event_tag = None
        current_event_date = None
        current_event_place = None
        current_event_pointer = None

    for line in text:
        parts = line.split(" ", 2)
        if len(parts) < 2:
            continue

        level = parts[0]
        if len(parts) == 2:
            tag, value = parts[1], ""
        else:
            tag, value = parts[1], parts[2]

        # New top-level record
        if level == "0":
            flush_event()
            current_indi = None
            current_fam = None

            if len(parts) == 3 and parts[2] in ("INDI", "FAM"):
                xref = parts[1]
                rec_type = parts[2]
                if rec_type == "INDI":
                    current_indi = indis[xref] = IndiRecord(xref=xref)
                elif rec_type == "FAM":
                    current_fam = fams[xref] = FamRecord(xref=xref)
            continue

        if current_indi:
            if tag == "NAME":
                current_indi.name = value
            elif tag == "SEX":
                current_indi.sex = value
            elif tag in {"BIRT", "DEAT", "RESI", "CENS", "IMMI"}:
                flush_event()
                current_event_tag = tag
                current_event_pointer = current_indi.xref
            elif tag == "DATE" and current_event_tag:
                current_event_date = value
            elif tag == "PLAC" and current_event_tag:
                current_event_place = value

        elif current_fam:
            if tag == "HUSB":
                current_fam.husb = value
            elif tag == "WIFE":
                current_fam.wife = value
            elif tag == "CHIL":
                current_fam.chil.append(value)
            elif tag == "MARR":
                current_event_tag = "MARR"
            elif tag == "DATE" and current_event_tag == "MARR":
                current_fam.marr_date = value
            elif tag == "PLAC" and current_event_tag == "MARR":
                current_fam.marr_place = value

    flush_event()

    persons: list[Person] = []
    events: list[Event] = []
    relationships: list[Relationship] = []

    for indi in indis.values():
        pid = stable_hash(indi.xref)
        person = Person(
            id_hash=pid,
            name_norm=normalize_name(indi.name) if indi.name else None,
            sex=indi.sex
        )
        persons.append(person)

        for idx, (tag, raw_date, raw_place, pointer) in enumerate(indi.events, start=1):
            eid = stable_hash(f"{indi.xref}:{tag}:{idx}")
            event = Event(
                id=eid,
                person_id=pid,
                type=map_gedcom_event(tag),
                date_iso8601=normalize_date(raw_date),
                place=Place(place_name=raw_place) if raw_place else None,
                evidence_ref=EvidenceRef(
                    source_file=Path(path).name,
                    pointer=pointer,
                    snippet=f"{tag} {raw_date or ''} {raw_place or ''}".strip(),
                )
            )
            events.append(event)
            if event.type == "birth":
                person.birth_event_id = eid
            elif event.type == "death":
                person.death_event_id = eid

    for fam in fams.values():
        if fam.husb and fam.wife:
            relationships.append(Relationship(
                id=stable_hash(f"{fam.xref}:spouse:{fam.husb}:{fam.wife}"),
                type="spouse",
                subject_id=stable_hash(fam.husb),
                object_id=stable_hash(fam.wife),
                evidence_ref=EvidenceRef(source_file=Path(path).name, pointer=fam.xref, snippet="FAM spouse")
            ))

        for child in fam.chil:
            if fam.husb:
                relationships.append(Relationship(
                    id=stable_hash(f"{fam.xref}:parent:{fam.husb}:{child}"),
                    type="parent",
                    subject_id=stable_hash(fam.husb),
                    object_id=stable_hash(child),
                    evidence_ref=EvidenceRef(source_file=Path(path).name, pointer=fam.xref, snippet="FAM father-child")
                ))
            if fam.wife:
                relationships.append(Relationship(
                    id=stable_hash(f"{fam.xref}:parent:{fam.wife}:{child}"),
                    type="parent",
                    subject_id=stable_hash(fam.wife),
                    object_id=stable_hash(child),
                    evidence_ref=EvidenceRef(source_file=Path(path).name, pointer=fam.xref, snippet="FAM mother-child")
                ))

    return persons, events, relationships
```

---

## `src/genealogy_ingest/vendor_csv.py`

```python
from __future__ import annotations

import csv
from pathlib import Path
from typing import List, Tuple

from .models import Event, EvidenceRef, Person, Relationship, Place
from .normalize import normalize_date, stable_hash


def parse_vendor_csv(path: str) -> tuple[list[Person], list[Event], list[Relationship]]:
    persons: list[Person] = []
    events: list[Event] = []
    relationships: list[Relationship] = []

    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row_num, row in enumerate(reader, start=2):
            name = (row.get("Name") or "").strip()
            if not name:
                continue

            pid = stable_hash(name)
            persons.append(Person(id_hash=pid, name_norm=name))

            birth = row.get("BirthDate")
            birth_place = row.get("BirthPlace")
            if birth or birth_place:
                events.append(Event(
                    id=stable_hash(f"{name}:birth"),
                    person_id=pid,
                    type="birth",
                    date_iso8601=normalize_date(birth),
                    place=Place(place_name=birth_place) if birth_place else None,
                    evidence_ref=EvidenceRef(
                        source_file=Path(path).name,
                        pointer=f"row:{row_num}",
                        snippet=f"BirthDate={birth}; BirthPlace={birth_place}"
                    )
                ))

            death = row.get("DeathDate")
            if death:
                events.append(Event(
                    id=stable_hash(f"{name}:death"),
                    person_id=pid,
                    type="death",
                    date_iso8601=normalize_date(death),
                    place=None,
                    evidence_ref=EvidenceRef(
                        source_file=Path(path).name,
                        pointer=f"row:{row_num}",
                        snippet=f"DeathDate={death}"
                    )
                ))

            spouse = (row.get("Spouse") or "").strip()
            if spouse:
                relationships.append(Relationship(
                    id=stable_hash(f"{name}:spouse:{spouse}"),
                    type="spouse",
                    subject_id=pid,
                    object_id=stable_hash(spouse),
                    evidence_ref=EvidenceRef(
                        source_file=Path(path).name,
                        pointer=f"row:{row_num}",
                        snippet=f"Spouse={spouse}"
                    )
                ))

    return persons, events, relationships
```

---

## `src/genealogy_ingest/dna_manifest.py`

```python
from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Optional

from .models import DNAKit
from .normalize import hmac_kit_hash


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_dna_manifest(path: str, vendor: str, vendor_kit_id: str, salt: bytes, genome_build: Optional[str] = None) -> DNAKit:
    return DNAKit(
        kit_hash=hmac_kit_hash(vendor_kit_id, salt),
        vendor=vendor,
        genome_build=genome_build,
        file_checksum=sha256_file(path),
    )
```

---

## `src/genealogy_ingest/receipts.py`

```python
from __future__ import annotations

import hashlib
import json
from datetime import datetime, UTC
from pathlib import Path


def spec_hash(*parts: str) -> str:
    joined = "|".join(parts)
    return hashlib.sha256(joined.encode("utf-8")).hexdigest()


def write_run_receipt(out_path: str, payload: dict) -> None:
    payload = {
        **payload,
        "created_at": datetime.now(UTC).isoformat(),
    }
    Path(out_path).write_text(json.dumps(payload, indent=2), encoding="utf-8")
```

---

## `src/genealogy_ingest/cli.py`

```python
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .dna_manifest import build_dna_manifest
from .gedcom import parse_gedcom
from .receipts import spec_hash, write_run_receipt
from .vendor_csv import parse_vendor_csv


def main() -> None:
    parser = argparse.ArgumentParser(description="Genealogy ingest")
    sub = parser.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("gedcom")
    g.add_argument("input")
    g.add_argument("--out", required=True)

    c = sub.add_parser("csv")
    c.add_argument("input")
    c.add_argument("--out", required=True)

    d = sub.add_parser("dna-manifest")
    d.add_argument("input")
    d.add_argument("--vendor", required=True)
    d.add_argument("--vendor-kit-id", required=True)
    d.add_argument("--salt-file", required=True)
    d.add_argument("--genome-build")
    d.add_argument("--out", required=True)

    args = parser.parse_args()
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.cmd == "gedcom":
        persons, events, relationships = parse_gedcom(args.input)
        (out_dir / "persons.json").write_text(json.dumps([p.model_dump() for p in persons], indent=2))
        (out_dir / "events.json").write_text(json.dumps([e.model_dump() for e in events], indent=2))
        (out_dir / "relationships.json").write_text(json.dumps([r.model_dump() for r in relationships], indent=2))
        write_run_receipt(str(out_dir / "run_receipt.json"), {
            "kind": "gedcom",
            "input": args.input,
            "spec_hash": spec_hash("genealogy-ingest", "gedcom", "v0.1.0"),
            "counts": {"persons": len(persons), "events": len(events), "relationships": len(relationships)},
        })

    elif args.cmd == "csv":
        persons, events, relationships = parse_vendor_csv(args.input)
        (out_dir / "persons.json").write_text(json.dumps([p.model_dump() for p in persons], indent=2))
        (out_dir / "events.json").write_text(json.dumps([e.model_dump() for e in events], indent=2))
        (out_dir / "relationships.json").write_text(json.dumps([r.model_dump() for r in relationships], indent=2))
        write_run_receipt(str(out_dir / "run_receipt.json"), {
            "kind": "vendor_csv",
            "input": args.input,
            "spec_hash": spec_hash("genealogy-ingest", "vendor_csv", "v0.1.0"),
            "counts": {"persons": len(persons), "events": len(events), "relationships": len(relationships)},
        })

    elif args.cmd == "dna-manifest":
        salt = Path(args.salt_file).read_bytes()
        manifest = build_dna_manifest(
            args.input,
            vendor=args.vendor,
            vendor_kit_id=args.vendor_kit_id,
            salt=salt,
            genome_build=args.genome_build,
        )
        (out_dir / "dna_manifest.json").write_text(json.dumps(manifest.model_dump(), indent=2))
        write_run_receipt(str(out_dir / "run_receipt.json"), {
            "kind": "dna_manifest",
            "input": args.input,
            "vendor": args.vendor,
            "spec_hash": spec_hash("genealogy-ingest", "dna_manifest", "v0.1.0"),
        })
```

---

## JSON schema example: `schemas/canonical.event.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "CanonicalEvent",
  "type": "object",
  "required": ["id", "person_id", "type", "evidence_ref"],
  "properties": {
    "id": { "type": "string" },
    "person_id": { "type": "string" },
    "type": {
      "type": "string",
      "enum": ["birth", "marriage", "death", "residence", "census", "immigration", "DNA_SAMPLE", "unknown"]
    },
    "date_iso8601": { "type": ["string", "null"] },
    "place": {
      "type": ["object", "null"],
      "properties": {
        "place_name": { "type": "string" },
        "lat": { "type": ["number", "null"] },
        "lon": { "type": ["number", "null"] },
        "gnis_id": { "type": ["string", "null"] }
      },
      "required": ["place_name"]
    },
    "evidence_ref": {
      "type": "object",
      "required": ["source_file", "pointer"],
      "properties": {
        "source_file": { "type": "string" },
        "pointer": { "type": "string" },
        "snippet": { "type": ["string", "null"] }
      }
    }
  }
}
```

---

## Tests

### `tests/test_dates.py`

```python
from genealogy_ingest.normalize import normalize_date


def test_normalize_exact_date():
    assert normalize_date("12 MAR 1882") == "1882-03-12"


def test_normalize_year_only():
    assert normalize_date("1882") == "1882"


def test_normalize_about_year():
    assert normalize_date("ABT 1880") == "1880"


def test_unparseable_date_returns_none():
    assert normalize_date("SPRING 1880") is None
```

### `tests/test_gedcom_minimal.py`

```python
from pathlib import Path
from genealogy_ingest.gedcom import parse_gedcom


def test_parse_minimal_gedcom(tmp_path: Path):
    ged = tmp_path / "sample.ged"
    ged.write_text(
        "0 @I1@ INDI\n"
        "1 NAME John /Smith/\n"
        "1 SEX M\n"
        "1 BIRT\n"
        "2 DATE 12 MAR 1882\n"
        "2 PLAC Ohio\n",
        encoding="utf-8"
    )

    persons, events, relationships = parse_gedcom(str(ged))
    assert len(persons) == 1
    assert persons[0].name_norm == "John Smith"
    assert len(events) == 1
    assert events[0].type == "birth"
    assert events[0].date_iso8601 == "1882-03-12"
    assert relationships == []
```

### `tests/test_vendor_csv.py`

```python
from pathlib import Path
from genealogy_ingest.vendor_csv import parse_vendor_csv


def test_parse_vendor_csv(tmp_path: Path):
    csvf = tmp_path / "tree.csv"
    csvf.write_text(
        "Name,BirthDate,BirthPlace,DeathDate,Spouse\n"
        "John Smith,1882,Ohio,1954,Mary Jones\n",
        encoding="utf-8"
    )

    persons, events, relationships = parse_vendor_csv(str(csvf))
    assert len(persons) == 1
    assert len(events) == 2
    assert len(relationships) == 1
```

### `tests/test_dna_manifest.py`

```python
from pathlib import Path
from genealogy_ingest.dna_manifest import build_dna_manifest


def test_dna_manifest(tmp_path: Path):
    raw = tmp_path / "dna.txt"
    raw.write_text("rsid\tchromosome\tposition\tgenotype\n", encoding="utf-8")

    manifest = build_dna_manifest(
        str(raw),
        vendor="23andMe",
        vendor_kit_id="KIT123",
        salt=b"secret-salt",
        genome_build="GRCh37",
    )

    assert manifest.vendor == "23andMe"
    assert manifest.genome_build == "GRCh37"
    assert manifest.kit_hash
    assert manifest.file_checksum
```

---

## Example runs

```bash
kfm-ingest-genealogy gedcom ./fixtures/family.ged --out ./out/gedcom_run
kfm-ingest-genealogy csv ./fixtures/vendor.csv --out ./out/csv_run
kfm-ingest-genealogy dna-manifest ./fixtures/23andme.txt \
  --vendor 23andMe \
  --vendor-kit-id KIT123 \
  --salt-file ./secrets/kit_salt.bin \
  --genome-build GRCh37 \
  --out ./out/dna_run
```

---

## KFM-specific hardening gates

Add these before promotion:

* require `evidence_ref.pointer` on every event and relationship
* quarantine any date that does not normalize cleanly
* reject DNA ingest when `vendor_kit_id` is missing
* forbid raw vendor kit ID from appearing in any published artifact
* sign `run_receipt.json`
* store raw DNA only in restricted storage; catalog manifest only

---

## Recommended next layer

After this ingest, project downstream into:

* `catalog/persons.parquet`
* `catalog/events.parquet`
* `catalog/relationships.parquet`
* optional Neo4j projection:

  * `(:Person {id_hash})`
  * `(:Person)-[:PARENT_OF]->(:Person)`
  * `(:Person)-[:SPOUSE_OF]->(:Person)`
  * `(:Person)-[:HAS_EVENT]->(:Event)`

If you want the next step, I’ll turn this into a full **KFM-style Markdown + Meta Block V2 + Mermaid + CI validation doc** for `pipelines/genealogy_ingest/README.md`.

