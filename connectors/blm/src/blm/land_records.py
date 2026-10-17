"""Preserve explicitly selected GLO/MLRS export bytes; no scraping or admission."""
from people_dna_land.land_capture import capture_export


def capture(source, raw, *, url, retrieved_at, format, documents=()):
    if source not in {"blm-glo", "blm-mlrs"}:
        raise ValueError("BLM_SOURCE_REQUIRED")
    return capture_export(source, raw, url=url, retrieved_at=retrieved_at, format=format, documents=documents)
