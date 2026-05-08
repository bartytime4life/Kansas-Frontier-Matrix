from fastapi import APIRouter

from governed_api.stub import make_abstain_envelope

router = APIRouter()


@router.get("/layers")
def layers() -> dict:
    return make_abstain_envelope("layers")
