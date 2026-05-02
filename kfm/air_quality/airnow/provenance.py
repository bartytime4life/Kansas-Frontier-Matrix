from .constants import SOURCE_DOC_REFS

def make_provenance(manifest_id: str, created_at: str, forecast: bool=False) -> dict:
    notes = [
        "AirNow data are preliminary and subject to change.",
    ]
    if forecast:
        notes.append("Forecast record is not an observation.")
    notes.append("Record is normalized for internal KFM analysis only and is not publication output.")
    return {
        "source_doc_url": SOURCE_DOC_REFS[0],
        "source_doc_refs": SOURCE_DOC_REFS,
        "input_manifest_id": manifest_id,
        "normalizer": "airnow_layer2",
        "normalizer_version": "v1",
        "created_at": created_at,
        "rights_status": "public_government_source_preliminary",
        "notes": notes,
    }
