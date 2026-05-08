from fastapi import FastAPI

from governed_api.routes import bootstrap, evidence, layers

app = FastAPI(title="KFM Governed API", version="0.1.0")
app.include_router(bootstrap.router)
app.include_router(layers.router)
app.include_router(evidence.router)
