# Next Layer — Catalog Closure Emitters

Add this file:

```text
pipelines/kansas_biodiversity_etl/catalog/emit_catalog.py
```

This emits:

```text
data/catalog/stac/kansas_biodiversity_occurrences.item.json
data/catalog/dcat/kansas_biodiversity_occurrences.dataset.json
data/catalog/prov/kansas_biodiversity_occurrences.prov.json
```

---

## `pipelines/kansas_biodiversity_etl/catalog/emit_catalog.py`

```python
#!/usr/bin/env python3
"""
Emit STAC, DCAT, and PROV catalog records for the Kansas biodiversity ETL.

Inputs:
- dataset metadata JSON
- EvidenceBundle JSON
- run receipt JSON

Outputs:
- STAC Item
- DCAT Dataset
- PROV lineage document

This does not promote data by itself. It only closes the catalog trail
for already-generated governed artifacts.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def build_stac_item(
    *,
    dataset_root: str,
    metadata: Dict[str, Any],
    evidence_path: str,
    receipt_path: str,
) -> Dict[str, Any]:
    return {
        "type": "Feature",
        "stac_version": "1.0.0",
        "id": metadata["dataset_id"],
        "properties": {
            "title": "Kansas Biodiversity Occurrences",
            "datetime": metadata["generated_at"],
            "kfm:spec_hash": metadata["spec_hash"],
            "kfm:records": metadata["records"],
            "kfm:format": metadata["format"],
            "kfm:partitioning": metadata.get("partitioning", []),
        },
        "geometry": None,
        "bbox": None,
        "links": [
            {
                "rel": "derived_from",
                "href": evidence_path,
                "type": "application/json",
                "title": "EvidenceBundle",
            },
            {
                "rel": "via",
                "href": receipt_path,
                "type": "application/json",
                "title": "Run receipt",
            },
        ],
        "assets": {
            "dataset": {
                "href": dataset_root,
                "type": "application/x-parquet",
                "roles": ["data"],
                "title": "Partitioned Parquet dataset",
            },
            "metadata": {
                "href": "_dataset_metadata.json",
                "type": "application/json",
                "roles": ["metadata"],
                "title": "Dataset metadata",
            },
        },
    }


def build_dcat_dataset(
    *,
    dataset_root: str,
    metadata: Dict[str, Any],
    evidence: Dict[str, Any],
) -> Dict[str, Any]:
    bundle = evidence["evidenceBundle"]

    return {
        "@context": {
            "dcat": "http://www.w3.org/ns/dcat#",
            "dct": "http://purl.org/dc/terms/",
            "kfm": "https://kansasfrontiermatrix.org/ns#",
        },
        "@type": "dcat:Dataset",
        "@id": metadata["dataset_id"],
        "dct:title": "Kansas Biodiversity Occurrences",
        "dct:identifier": metadata["dataset_id"],
        "dct:issued": metadata["generated_at"],
        "dct:modified": metadata["generated_at"],
        "dct:license": bundle.get("license"),
        "dct:rightsHolder": bundle.get("attribution"),
        "kfm:spec_hash": metadata["spec_hash"],
        "kfm:records": metadata["records"],
        "dcat:distribution": [
            {
                "@type": "dcat:Distribution",
                "dcat:accessURL": dataset_root,
                "dct:format": metadata["format"],
            }
        ],
    }


def build_prov_document(
    *,
    dataset_root: str,
    metadata: Dict[str, Any],
    evidence_path: str,
    receipt_path: str,
    evidence: Dict[str, Any],
) -> Dict[str, Any]:
    bundle = evidence["evidenceBundle"]

    return {
        "prefix": {
            "prov": "http://www.w3.org/ns/prov#",
            "kfm": "https://kansasfrontiermatrix.org/ns#",
        },
        "entity": {
            "dataset": {
                "prov:type": "kfm:PartitionedParquetDataset",
                "prov:location": dataset_root,
                "kfm:spec_hash": metadata["spec_hash"],
                "kfm:records": metadata["records"],
            },
            "evidence_bundle": {
                "prov:type": "kfm:EvidenceBundle",
                "prov:location": evidence_path,
            },
            "run_receipt": {
                "prov:type": "kfm:RunReceipt",
                "prov:location": receipt_path,
            },
        },
        "activity": {
            "publish_activity": {
                "prov:type": "kfm:Publish",
                "prov:endedAtTime": metadata["generated_at"],
            }
        },
        "wasGeneratedBy": {
            "dataset_generation": {
                "prov:entity": "dataset",
                "prov:activity": "publish_activity",
            }
        },
        "wasDerivedFrom": {
            "dataset_from_sources": {
                "prov:generatedEntity": "dataset",
                "prov:usedEntity": bundle.get("source_uris", []),
            }
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", required=True)
    parser.add_argument("--metadata", required=True)
    parser.add_argument("--evidence", required=True)
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--stac-output", required=True)
    parser.add_argument("--dcat-output", required=True)
    parser.add_argument("--prov-output", required=True)
    args = parser.parse_args()

    metadata = load_json(Path(args.metadata))
    evidence = load_json(Path(args.evidence))

    stac = build_stac_item(
        dataset_root=args.dataset_root,
        metadata=metadata,
        evidence_path=args.evidence,
        receipt_path=args.receipt,
    )

    dcat = build_dcat_dataset(
        dataset_root=args.dataset_root,
        metadata=metadata,
        evidence=evidence,
    )

    prov = build_prov_document(
        dataset_root=args.dataset_root,
        metadata=metadata,
        evidence_path=args.evidence,
        receipt_path=args.receipt,
        evidence=evidence,
    )

    write_json(Path(args.stac_output), stac)
    write_json(Path(args.dcat_output), dcat)
    write_json(Path(args.prov_output), prov)

    print(
        json.dumps(
            {
                "decision": "CATALOG_EMITTED",
                "stac": args.stac_output,
                "dcat": args.dcat_output,
                "prov": args.prov_output,
                "spec_hash": metadata["spec_hash"],
            },
            sort_keys=True,
        )
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

---

## Makefile Additions

Add:

```makefile
CATALOG_STAC := $(DATA_ROOT)/catalog/stac/kansas_biodiversity_occurrences.item.json
CATALOG_DCAT := $(DATA_ROOT)/catalog/dcat/kansas_biodiversity_occurrences.dataset.json
CATALOG_PROV := $(DATA_ROOT)/catalog/prov/kansas_biodiversity_occurrences.prov.json
```

Update:

```makefile
.PHONY: all harvest normalize dedupe publish gate clean sample catalog
```

Change:

```makefile
all: harvest normalize dedupe publish gate
```

to:

```makefile
all: harvest normalize dedupe publish gate catalog
```

Add:

```makefile
catalog:
	@echo "=== Catalog Closure: STAC + DCAT + PROV ==="
	python catalog/emit_catalog.py \
		--dataset-root $(DATASET_ROOT) \
		--metadata $(METADATA) \
		--evidence $(EVIDENCE) \
		--receipt $(RECEIPT) \
		--stac-output $(CATALOG_STAC) \
		--dcat-output $(CATALOG_DCAT) \
		--prov-output $(CATALOG_PROV)
```

---

## Path Summary

```text
pipelines/kansas_biodiversity_etl/catalog/emit_catalog.py
```

Outputs:

```text
data/catalog/stac/kansas_biodiversity_occurrences.item.json
data/catalog/dcat/kansas_biodiversity_occurrences.dataset.json
data/catalog/prov/kansas_biodiversity_occurrences.prov.json
```
