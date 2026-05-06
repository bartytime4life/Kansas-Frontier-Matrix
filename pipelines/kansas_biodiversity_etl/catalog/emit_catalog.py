#!/usr/bin/env python3
"""
Emit STAC, DCAT, and PROV catalog records for the Kansas biodiversity ETL.

Supports:
- partitioned Parquet dataset metadata
- STAC Collection + one STAC Item per partition
- DCAT dataset/distribution record
- PROV lineage document

This does not promote data by itself. It only closes the catalog trail
for already-generated, gate-validated governed artifacts.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


JsonObject = Dict[str, Any]


def load_json(path: Path) -> JsonObject:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: JsonObject) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def slug(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_.=-]+", "-", value.strip())
    return cleaned.strip("-") or "unknown"


def evidence_bundle(evidence: JsonObject) -> JsonObject:
    try:
        bundle = evidence["evidenceBundle"]
    except KeyError as exc:
        raise ValueError("missing_evidenceBundle") from exc

    if not isinstance(bundle, dict):
        raise ValueError("invalid_evidenceBundle")

    return bundle


def metadata_partitions(metadata: JsonObject) -> List[JsonObject]:
    partitions = metadata.get("partitions")

    if isinstance(partitions, list) and partitions:
        return [p for p in partitions if isinstance(p, dict)]

    return [
        {
            "year": "unknown",
            "month": "unknown",
            "records": metadata.get("records", 0),
        }
    ]


def partition_id(dataset_id: str, partition: JsonObject) -> str:
    year = slug(str(partition.get("year", "unknown")))
    month = slug(str(partition.get("month", "unknown")))
    return f"{slug(dataset_id)}-year={year}-month={month}"


def partition_href(dataset_root: str, partition: JsonObject) -> str:
    year = str(partition.get("year", "unknown"))
    month = str(partition.get("month", "unknown"))
    return f"{dataset_root.rstrip('/')}/year={year}/month={month}"


def build_stac_collection(
    *,
    metadata: JsonObject,
    evidence_path: str,
    receipt_path: str,
    dcat_path: str,
    prov_path: str,
    item_hrefs: Iterable[str],
) -> JsonObject:
    dataset_id = metadata["dataset_id"]

    return {
        "type": "Collection",
        "stac_version": "1.0.0",
        "id": dataset_id,
        "title": "Kansas Biodiversity Occurrences",
        "description": (
            "Governed Kansas biodiversity occurrence dataset catalog closure. "
            "This collection describes partitioned dataset artifacts and references "
            "EvidenceBundle, receipt, DCAT, and PROV records."
        ),
        "license": "various",
        "extent": {
            "spatial": {"bbox": [[-102.1, 36.9, -94.5, 40.1]]},
            "temporal": {"interval": [[None, None]]},
        },
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
            {
                "rel": "describedby",
                "href": dcat_path,
                "type": "application/ld+json",
                "title": "DCAT dataset record",
            },
            {
                "rel": "describedby",
                "href": prov_path,
                "type": "application/json",
                "title": "PROV lineage record",
            },
            *[
                {
                    "rel": "item",
                    "href": href,
                    "type": "application/geo+json",
                    "title": Path(href).name,
                }
                for href in item_hrefs
            ],
        ],
        "summaries": {
            "kfm:spec_hash": [metadata["spec_hash"]],
            "kfm:records": [metadata.get("records")],
            "kfm:format": [metadata.get("format")],
            "kfm:partitioning": metadata.get("partitioning", []),
        },
    }


def build_stac_partition_item(
    *,
    dataset_root: str,
    metadata: JsonObject,
    partition: JsonObject,
    collection_href: str,
    evidence_path: str,
    receipt_path: str,
) -> JsonObject:
    dataset_id = metadata["dataset_id"]
    item_id = partition_id(dataset_id, partition)
    year = str(partition.get("year", "unknown"))
    month = str(partition.get("month", "unknown"))

    return {
        "type": "Feature",
        "stac_version": "1.0.0",
        "id": item_id,
        "collection": dataset_id,
        "geometry": None,
        "bbox": None,
        "properties": {
            "title": f"Kansas Biodiversity Occurrences — year={year} month={month}",
            "datetime": metadata["generated_at"],
            "kfm:dataset_id": dataset_id,
            "kfm:spec_hash": metadata["spec_hash"],
            "kfm:records": partition.get("records", 0),
            "kfm:format": metadata.get("format"),
            "kfm:partition_year": year,
            "kfm:partition_month": month,
        },
        "links": [
            {
                "rel": "collection",
                "href": collection_href,
                "type": "application/json",
                "title": "STAC Collection",
            },
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
            "partition": {
                "href": partition_href(dataset_root, partition),
                "type": "application/x-parquet",
                "roles": ["data"],
                "title": f"Partition year={year} month={month}",
            },
            "metadata": {
                "href": f"{dataset_root.rstrip('/')}/_dataset_metadata.json",
                "type": "application/json",
                "roles": ["metadata"],
                "title": "Dataset metadata",
            },
        },
    }


def build_dcat_dataset(
    *,
    dataset_root: str,
    metadata: JsonObject,
    evidence: JsonObject,
    stac_collection_path: str,
    prov_path: str,
) -> JsonObject:
    bundle = evidence_bundle(evidence)

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
        "kfm:format": metadata.get("format"),
        "dcat:distribution": [
            {
                "@type": "dcat:Distribution",
                "dcat:accessURL": dataset_root,
                "dct:format": metadata.get("format"),
                "kfm:spec_hash": metadata["spec_hash"],
            },
            {
                "@type": "dcat:Distribution",
                "dcat:accessURL": stac_collection_path,
                "dct:format": "STAC Collection JSON",
            },
            {
                "@type": "dcat:Distribution",
                "dcat:accessURL": prov_path,
                "dct:format": "PROV JSON",
            },
        ],
    }


def build_prov_document(
    *,
    dataset_root: str,
    metadata: JsonObject,
    evidence_path: str,
    receipt_path: str,
    stac_collection_path: str,
    dcat_path: str,
    evidence: JsonObject,
) -> JsonObject:
    bundle = evidence_bundle(evidence)

    return {
        "prefix": {
            "prov": "http://www.w3.org/ns/prov#",
            "kfm": "https://kansasfrontiermatrix.org/ns#",
        },
        "entity": {
            "dataset": {
                "prov:type": "kfm:PartitionedParquetDataset",
                "prov:location": dataset_root,
                "kfm:dataset_id": metadata["dataset_id"],
                "kfm:spec_hash": metadata["spec_hash"],
                "kfm:records": metadata["records"],
                "kfm:format": metadata.get("format"),
            },
            "evidence_bundle": {
                "prov:type": "kfm:EvidenceBundle",
                "prov:location": evidence_path,
            },
            "run_receipt": {
                "prov:type": "kfm:RunReceipt",
                "prov:location": receipt_path,
            },
            "stac_collection": {
                "prov:type": "kfm:StacCollection",
                "prov:location": stac_collection_path,
            },
            "dcat_dataset": {
                "prov:type": "kfm:DcatDataset",
                "prov:location": dcat_path,
            },
        },
        "activity": {
            "publish_activity": {
                "prov:type": "kfm:Publish",
                "prov:endedAtTime": metadata["generated_at"],
            },
            "catalog_activity": {
                "prov:type": "kfm:CatalogClosure",
                "prov:endedAtTime": metadata["generated_at"],
            },
        },
        "wasGeneratedBy": {
            "dataset_generation": {
                "prov:entity": "dataset",
                "prov:activity": "publish_activity",
            },
            "catalog_generation": {
                "prov:entity": "stac_collection",
                "prov:activity": "catalog_activity",
            },
        },
        "wasDerivedFrom": {
            "dataset_from_sources": {
                "prov:generatedEntity": "dataset",
                "prov:usedEntity": bundle.get("source_uris", []),
            },
            "catalog_from_dataset": {
                "prov:generatedEntity": "stac_collection",
                "prov:usedEntity": "dataset",
            },
        },
    }


def emit_stac(
    *,
    dataset_root: str,
    metadata: JsonObject,
    evidence_path: str,
    receipt_path: str,
    stac_output_root: Path,
    dcat_output: str,
    prov_output: str,
) -> Tuple[str, List[str]]:
    stac_output_root.mkdir(parents=True, exist_ok=True)

    collection_path = stac_output_root / "collection.json"
    partitions = metadata_partitions(metadata)

    item_paths: List[Path] = []

    for partition in partitions:
        year = slug(str(partition.get("year", "unknown")))
        month = slug(str(partition.get("month", "unknown")))
        item_path = stac_output_root / f"year={year}-month={month}.item.json"

        item = build_stac_partition_item(
            dataset_root=dataset_root,
            metadata=metadata,
            partition=partition,
            collection_href=str(collection_path),
            evidence_path=evidence_path,
            receipt_path=receipt_path,
        )

        write_json(item_path, item)
        item_paths.append(item_path)

    collection = build_stac_collection(
        metadata=metadata,
        evidence_path=evidence_path,
        receipt_path=receipt_path,
        dcat_path=dcat_output,
        prov_path=prov_output,
        item_hrefs=[str(path) for path in item_paths],
    )

    write_json(collection_path, collection)

    return str(collection_path), [str(path) for path in item_paths]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", required=True)
    parser.add_argument("--metadata", required=True)
    parser.add_argument("--evidence", required=True)
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--stac-output-root", required=True)
    parser.add_argument("--dcat-output", required=True)
    parser.add_argument("--prov-output", required=True)
    args = parser.parse_args()

    metadata = load_json(Path(args.metadata))
    evidence = load_json(Path(args.evidence))

    stac_collection_path, stac_item_paths = emit_stac(
        dataset_root=args.dataset_root,
        metadata=metadata,
        evidence_path=args.evidence,
        receipt_path=args.receipt,
        stac_output_root=Path(args.stac_output_root),
        dcat_output=args.dcat_output,
        prov_output=args.prov_output,
    )

    dcat = build_dcat_dataset(
        dataset_root=args.dataset_root,
        metadata=metadata,
        evidence=evidence,
        stac_collection_path=stac_collection_path,
        prov_path=args.prov_output,
    )

    prov = build_prov_document(
        dataset_root=args.dataset_root,
        metadata=metadata,
        evidence_path=args.evidence,
        receipt_path=args.receipt,
        stac_collection_path=stac_collection_path,
        dcat_path=args.dcat_output,
        evidence=evidence,
    )

    write_json(Path(args.dcat_output), dcat)
    write_json(Path(args.prov_output), prov)

    print(
        json.dumps(
            {
                "decision": "CATALOG_EMITTED",
                "stac_collection": stac_collection_path,
                "stac_items": stac_item_paths,
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
