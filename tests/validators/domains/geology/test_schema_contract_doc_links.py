"""Keep Geology schema metadata linked to existing semantic contracts."""

from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
SCHEMA_ROOT = REPO_ROOT / "schemas" / "contracts" / "v1" / "domains" / "geology"
EXPECTED_CONTRACT_LINKS = {
    "aem_survey_campaign.schema.json": "contracts/domains/geology/AemSurveyCampaign.md",
    "borehole_reference.schema.json": "contracts/domains/geology/BoreholeReference.md",
    "core_sample.schema.json": "contracts/domains/geology/CoreSample.md",
    "cross_section.schema.json": "contracts/domains/geology/CrossSection.md",
    "extraction_site.schema.json": "contracts/domains/geology/ExtractionSite.md",
    "geochemistry_sample.schema.json": "contracts/domains/geology/GeochemistrySample.md",
    "geologic_age.schema.json": "contracts/domains/geology/GeologicAge.md",
    "geologic_unit.schema.json": "contracts/domains/geology/GeologicUnit.md",
    "geophysical_observation.schema.json": "contracts/domains/geology/GeophysicalObservation.md",
    "hydrostratigraphic_unit.schema.json": "contracts/domains/geology/HydrostratigraphicUnit.md",
    "lithology.schema.json": "contracts/domains/geology/Lithology.md",
    "mineral_occurrence.schema.json": "contracts/domains/geology/MineralOccurrence.md",
    "reclamation_record.schema.json": "contracts/domains/geology/ReclamationRecord.md",
    "resource_deposit.schema.json": "contracts/domains/geology/ResourceDeposit.md",
    "resource_estimate.schema.json": "contracts/domains/geology/ResourceEstimate.md",
    "stratigraphic_interval.schema.json": "contracts/domains/geology/StratigraphicInterval.md",
    "structure_feature.schema.json": "contracts/domains/geology/StructureFeature.md",
    "well_log_reference.schema.json": "contracts/domains/geology/WellLogReference.md",
}


def test_existing_object_family_contract_links_resolve_exactly() -> None:
    """Every adopted Geology schema/contract pair must remain present and exact."""

    mismatches: list[str] = []

    for schema_name, expected in sorted(EXPECTED_CONTRACT_LINKS.items()):
        schema_path = SCHEMA_ROOT / schema_name
        contract_path = REPO_ROOT / expected

        if not schema_path.is_file():
            mismatches.append(f"missing Geology schema: {schema_path.relative_to(REPO_ROOT)}")
            continue
        if not contract_path.is_file():
            mismatches.append(f"missing Geology contract: {expected}")
            continue

        document = json.loads(schema_path.read_text(encoding="utf-8"))
        declared = document.get("x-kfm", {}).get("contract_doc")
        if declared != expected:
            mismatches.append(
                f"{schema_path.relative_to(REPO_ROOT).as_posix()}: "
                f"expected {expected!r}, got {declared!r}"
            )

    assert not mismatches, "\n".join(mismatches)
