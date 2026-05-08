from fastapi import APIRouter

from governed_api.stub import make_abstain_envelope

router = APIRouter()


@router.get("/evidence")
def evidence() -> dict:
    return make_abstain_envelope("evidence")
