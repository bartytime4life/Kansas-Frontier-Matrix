from fastapi import APIRouter

from governed_api.stub import make_abstain_envelope

router = APIRouter()


@router.get("/bootstrap")
def bootstrap() -> dict:
    return make_abstain_envelope("bootstrap")
