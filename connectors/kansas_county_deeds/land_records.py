"""Lawfully obtained county deed exports only. No SVQ, login or paid scraping."""
from people_dna_land.land_capture import capture_export


def capture(source, raw, *, url, retrieved_at, documents=()):
    if source not in {"sedgwick-deeds", "johnson-deeds", "shawnee-tax-sales", "leavenworth-tax-sales"}:
        raise ValueError("REGISTERED_COUNTY_SOURCE_REQUIRED")
    if source.endswith("tax-sales") and not documents:
        raise ValueError("AUCTION_ORIGINAL_DOCUMENT_REQUIRED")
    return capture_export(source, raw, url=url, retrieved_at=retrieved_at, format="mapped-csv", documents=documents)
