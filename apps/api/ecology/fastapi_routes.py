from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Query

from .routes import get_ecology_evidence_bundle


router = APIRouter(
    prefix="/v1/ecology",
    tags=["ecology"],
)


@router.get("/evidence-bundles/{candidate_id}")
def read_ecology_evidence_bundle(
    candidate_id: str,
    spec_hash: Annotated[str | None, Query()] = None,
    include_receipts: Annotated[bool, Query()] = True,
    include_catalog_refs: Annotated[bool, Query()] = True,
    include_uncertainty: Annotated[bool, Query()] = True,
) -> dict:
    return get_ecology_evidence_bundle(
        candidate_id=candidate_id,
        spec_hash=spec_hash,
        include_receipts=include_receipts,
        include_catalog_refs=include_catalog_refs,
        include_uncertainty=include_uncertainty,
    )
