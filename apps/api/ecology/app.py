from __future__ import annotations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from apps.governed_api.ecology.fastapi_routes import router as ecology_router
from apps.governed_api.ecology.focus_mode import answer_focus_request


app = FastAPI(title="KFM Governed Ecology API")
app.include_router(ecology_router)


class FocusModeRequest(BaseModel):
    payload: dict


@app.post("/ecology/focus")
def ecology_focus(req: FocusModeRequest) -> dict:
    try:
        return answer_focus_request(req.payload)
    except Exception as exc:  # pragma: no cover - defensive runtime boundary
        raise HTTPException(status_code=500, detail=str(exc)) from exc
