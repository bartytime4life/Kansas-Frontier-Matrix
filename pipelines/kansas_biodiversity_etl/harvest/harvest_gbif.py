# Next File — GBIF Harvest Stub

Create:

```text
pipelines/kansas_biodiversity_etl/harvest/harvest_gbif.py
```

```python
#!/usr/bin/env python3
"""
Harvest Kansas biodiversity occurrences from the GBIF occurrence API.

Thin-slice behavior:
- Queries GBIF occurrence search endpoint.
- Filters stateProvince=Kansas.
- Supports modified/since window.
- Writes Darwin Core-like JSONL for downstream normalize_dwc.py.
- Emits a harvest receipt beside the raw output.

NOTE:
This is an online harvester. Network access is required at runtime.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


GBIF_OCCURRENCE_SEARCH_URL = "https://api.gbif.org/v1/occurrence/search"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def build_url(
    *,
    state: str,
    since: Optional[str],
    limit: int,
    offset: int,
) -> str:
    params: Dict[str, Any] = {
        "stateProvince": state,
        "limit": limit,
        "offset": offset,
    }

    if since:
        # GBIF supports modified as a search parameter.
        params["modified"] = since

    return GBIF_OCCURRENCE_SEARCH_URL + "?" + urllib.parse.urlencode(params)


def fetch_json(url: str, timeout: int = 60) -> Dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "Kansas-Frontier-Matrix biodiversity ETL thin-slice",
        },
    )

    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def gbif_to_dwc_like(record: Dict[str, Any]) -> Dict[str, Any]:
    """
    Convert GBIF occurrence API record into the DwC-like keys expected by normalize_dwc.py.
    """
    return {
        "catalogNumber": record.get("catalogNumber") or record.get("key"),
        "scientificName": record.get("scientificName"),
        "eventDate": record.get("eventDate"),
        "decimalLatitude": record.get("decimalLatitude"),
        "decimalLongitude": record.get("decimalLongitude"),
        "coordinateUncertaintyInMeters": record.get("coordinateUncertaintyInMeters"),
        "institutionCode": record.get("institutionCode"),
        "collectionCode": record.get("collectionCode"),
        "basisOfRecord": record.get("basisOfRecord"),
        "license": record.get("license"),
        "rightsHolder": record.get("rightsHolder"),
        "gbifKey": record.get("key"),
        "datasetKey": record.get("datasetKey"),
        "publishingOrgKey": record.get("publishingOrgKey"),
        "lastInterpreted": record.get("lastInterpreted"),
        "modified": record.get("modified"),
    }


def write_jsonl(records: Iterable[Dict[str, Any]], path: Path) -> int:
    path.parent.mkdir(parents=True, exist_ok=True)

    count = 0
    with path.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, sort_keys=True, separators=(",", ":"), ensure_ascii=False))
            handle.write("\n")
            count += 1

    return count


def harvest(
    *,
    state: str,
    since: Optional[str],
    output: Path,
    receipt_output: Path,
    page_size: int,
    max_records: int,
    sleep_seconds: float,
) -> int:
    harvested: List[Dict[str, Any]] = []
    source_uris: List[str] = []

    offset = 0

    while True:
        if max_records and len(harvested) >= max_records:
            break

        url = build_url(state=state, since=since, limit=page_size, offset=offset)
        source_uris.append(url)

        payload = fetch_json(url)
        results = payload.get("results", [])

        if not results:
            break

        for item in results:
            if max_records and len(harvested) >= max_records:
                break
            harvested.append(gbif_to_dwc_like(item))

        end_of_records = bool(payload.get("endOfRecords"))
        if end_of_records:
            break

        offset += page_size

        if sleep_seconds > 0:
            time.sleep(sleep_seconds)

    count = write_jsonl(harvested, output)

    receipt = {
        "harvested_at": utc_now(),
        "source": "GBIF occurrence API",
        "stateProvince": state,
        "since": since,
        "records": count,
        "output": str(output),
        "source_uris": source_uris,
        "status": "generated_not_promoted",
    }

    receipt_output.parent.mkdir(parents=True, exist_ok=True)
    receipt_output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(json.dumps(receipt, sort_keys=True))
    return count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", default="Kansas")
    parser.add_argument("--since", default=None)
    parser.add_argument("--output", required=True)
    parser.add_argument("--receipt-output", required=True)
    parser.add_argument("--page-size", type=int, default=300)
    parser.add_argument("--max-records", type=int, default=1000)
    parser.add_argument("--sleep-seconds", type=float, default=0.25)

    args = parser.parse_args()

    try:
        harvest(
            state=args.state,
            since=args.since,
            output=Path(args.output),
            receipt_output=Path(args.receipt_output),
            page_size=args.page_size,
            max_records=args.max_records,
            sleep_seconds=args.sleep_seconds,
        )
    except Exception as exc:
        print(json.dumps({"decision": "FAIL", "reason": str(exc)}, sort_keys=True), file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## Makefile Patch

Add:

```makefile
RAW_DIR := ../../data/raw/kansas_biodiversity_etl/20260425
RAW_GBIF := $(RAW_DIR)/gbif_occurrences.jsonl
HARVEST_RECEIPT := $(RAW_DIR)/harvest_receipt.json
```

Change:

```makefile
RAW_SAMPLE := samples/dwc_occurrences_sample.jsonl
```

to keep sample mode available, but update normalize to use the real harvest output:

```makefile
normalize:
	python normalize/normalize_dwc.py \
		--input $(RAW_GBIF) \
		--output $(NORMALIZED)
```

Add:

```makefile
harvest:
	python harvest/harvest_gbif.py \
		--state Kansas \
		--since 2026-04-01T00:00:00Z \
		--output $(RAW_GBIF) \
		--receipt-output $(HARVEST_RECEIPT) \
		--max-records 1000
```

Change:

```makefile
all: normalize dedupe publish gate
```

to:

```makefile
all: harvest normalize dedupe publish gate
```

---

## Run

```bash
make clean
make all
```

For offline testing, keep a separate target:

```makefile
sample:
	python normalize/normalize_dwc.py \
		--input $(RAW_SAMPLE) \
		--output $(NORMALIZED)
	$(MAKE) dedupe
	$(MAKE) publish
	$(MAKE) gate
```
