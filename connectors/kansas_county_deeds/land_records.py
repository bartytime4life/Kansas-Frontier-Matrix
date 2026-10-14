"""Lawfully obtained county deed exports only. No SVQ, login or paid scraping."""
from people_dna_land.land_capture import capture_export
from people_dna_land.land_records import decimal, iso_date, text
import csv
import io
import re
from decimal import Decimal


def transcribe_shawnee(table):
    """Render an explicit operator transcription; never infer fields from a PDF.

    Reconcile every printed financial total before emitting the existing mapped
    CSV contract. Purchasers remain distinct from the source's Deed label.
    """
    if not isinstance(table, dict) or set(table) != {"case_number", "event_date", "units", "totals", "expected_tracts"}:
        raise ValueError("SHAWNEE_TRANSCRIPT_FIELDS_INVALID")
    case = table["case_number"]
    if not isinstance(case, str) or not re.fullmatch(r"SN-\d{4}-CV-\d{6}", case):
        raise ValueError("SHAWNEE_CASE_INVALID")
    date = iso_date(table["event_date"], required=True)
    units = table["units"]
    if not isinstance(units, list) or not 1 <= len(units) <= 1000 or type(table["expected_tracts"]) is not int:
        raise ValueError("SHAWNEE_TRANSCRIPT_BUDGET_INVALID")
    names = ("total_lien", "court_costs", "taxes", "purchase_price")
    totals = dict.fromkeys(names, Decimal(0))
    rows, seen_units, seen_tracts = [], set(), set()
    def money(value):
        if value is None:
            return None
        if not isinstance(value, str) or not re.fullmatch(r"\d+\.\d{2}", value):
            raise ValueError("SHAWNEE_AMOUNT_INVALID")
        return decimal(value)
    for unit in units:
        if not isinstance(unit, dict) or set(unit) != {"unit_id", "purchaser", "deed_name", "parcels", "purchase_price", "result", "pages"}:
            raise ValueError("SHAWNEE_UNIT_FIELDS_INVALID")
        key = text(unit["unit_id"], 128, required=True)
        if key in seen_units:
            raise ValueError("SHAWNEE_DUPLICATE_UNIT")
        seen_units.add(key)
        purchaser = text(unit["purchaser"], 256, required=True)
        deed = text(unit["deed_name"], 256)
        price = money(unit["purchase_price"])
        result = unit["result"]
        if result not in {"PURCHASE_REPORTED", "INVALIDATED_SALE"} or (result == "PURCHASE_REPORTED" and (price is None or not deed)) or (result == "INVALIDATED_SALE" and (price is not None or deed)):
            raise ValueError("SHAWNEE_RESULT_INVALID")
        pages = unit["pages"]
        if not isinstance(pages, list) or not pages or len(pages) > 100 or any(type(p) is not int or not 1 <= p <= 100 for p in pages) or len(set(pages)) != len(pages):
            raise ValueError("SHAWNEE_PAGES_INVALID")
        parcels = unit["parcels"]
        if not isinstance(parcels, list) or not 1 <= len(parcels) <= 100:
            raise ValueError("SHAWNEE_PARCELS_INVALID")
        references, finances = [], []
        for parcel in parcels:
            if not isinstance(parcel, dict) or set(parcel) != {"tract", "parcel_id", "total_lien", "court_costs", "taxes"}:
                raise ValueError("SHAWNEE_PARCEL_FIELDS_INVALID")
            tract = text(parcel["tract"], 128, required=True)
            # A printed combined tract row retains its combined financial values.
            tract_ids = tract.split(",")
            if any(not re.fullmatch(r"\d+", p) or p in seen_tracts for p in tract_ids) or len(set(tract_ids)) != len(tract_ids):
                raise ValueError("SHAWNEE_DUPLICATE_OR_INVALID_TRACT")
            seen_tracts.update(tract_ids)
            ids = parcel["parcel_id"]
            if not isinstance(ids, list) or len(ids) != len(tract_ids) or any(not isinstance(p, str) or not re.fullmatch(r"\d{16}", p) for p in ids):
                raise ValueError("SHAWNEE_PARCEL_ID_INVALID")
            values = {n: money(parcel[n]) for n in names[:3]}
            if result == "PURCHASE_REPORTED" and (any(v is None for v in values.values()) or Decimal(values["total_lien"]) != Decimal(values["court_costs"]) + Decimal(values["taxes"])):
                raise ValueError("SHAWNEE_LIEN_RECONCILIATION_FAILED")
            for n, v in values.items():
                if v is not None:
                    totals[n] += Decimal(v)
            references.extend(f"Tract {t}: {p}" for t, p in zip(tract_ids, ids))
            finances.append(f"Tract {tract}: lien {values['total_lien'] or '-'}; costs {values['court_costs'] or '-'}; taxes {values['taxes'] or '-'} USD")
        if price is not None:
            totals["purchase_price"] += Decimal(price)
        notes = (f"Official Exhibit B transcription; source pages {','.join(map(str, pages))}. "
                 f"Printed purchaser(s): {purchaser}. Printed Deed name: {deed or 'not supplied'}. "
                 f"Reported result: {result}.\n" + "\n".join(finances) +
                 "\nPurchase price covers this entire sale unit; no allocation to individual parcels. Court confirmation and current ownership are not established.")
        rows.append({"source_record_id": f"{case}:{key}", "instrument_type": "tax_foreclosure_sale", "event_date": date,
                     "state": "KS", "county": "Shawnee", "transaction_status": "AUCTION_REPORTED", "grantee": deed or "",
                     "legal_description": text("Printed tract and parcel references; not a surveyed legal description:\n" + "\n".join(references), 8192),
                     "amount": price or "", "amount_kind": "auction_purchase_price" if price is not None else "", "currency": "USD" if price is not None else "",
                     "notes": text(notes, 4096, required=True)})
    if len(seen_tracts) != table["expected_tracts"] or not isinstance(table["totals"], dict) or set(table["totals"]) != set(names) or any(Decimal(money(table["totals"][n]) or '-1') != totals[n] for n in names):
        raise ValueError("SHAWNEE_TOTALS_RECONCILIATION_FAILED")
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue().encode(), {k: k for k in rows[0]}, {"units": len(rows), "tracts": len(seen_tracts), "totals": {k: str(v) for k, v in totals.items()}}


def capture(source, raw, *, url, retrieved_at, documents=()):
    if source not in {"sedgwick-deeds", "johnson-deeds", "shawnee-tax-sales", "leavenworth-tax-sales"}:
        raise ValueError("REGISTERED_COUNTY_SOURCE_REQUIRED")
    if source.endswith("tax-sales") and not documents:
        raise ValueError("AUCTION_ORIGINAL_DOCUMENT_REQUIRED")
    return capture_export(source, raw, url=url, retrieved_at=retrieved_at, format="mapped-csv", documents=documents)
