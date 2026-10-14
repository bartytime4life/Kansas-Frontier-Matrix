"""Capture -> deterministic normalization -> private quarantine ledger.

This stage-first implementation introduces no alternate land-ownership writer
under the existing pipelines/domains/people-dna-land scaffold. Release, public
projection, legal title and external source admission remain separate duties.
"""
from connectors.blm.src.blm.land_records import capture as capture_blm
from connectors.kshs.land_records import capture as capture_archive
from connectors.kansas_county_deeds.land_records import capture as capture_county
from people_dna_land.land_records import normalize
from people_dna_land.land_store import stage


def ingest(root, source, raw, *, url, retrieved_at, format="mapped-csv", mapping=None, documents=(), max_records=100):
    options = {"url": url, "retrieved_at": retrieved_at, "documents": documents}
    if source in {"blm-glo", "blm-mlrs"}:
        manifest, objects = capture_blm(source, raw, format=format, **options)
    elif source == "kshs-land-sales" and format == "mapped-csv":
        manifest, objects = capture_archive(raw, **options)
    elif source in {"sedgwick-deeds", "johnson-deeds"} and format == "mapped-csv":
        manifest, objects = capture_county(source, raw, **options)
    else:
        raise ValueError("SOURCE_FORMAT_NOT_SUPPORTED")
    candidate = normalize(raw, manifest, mapping=mapping, max_records=max_records)
    return stage(root, manifest, objects, candidate)
