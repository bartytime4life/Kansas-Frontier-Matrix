from governed_api.routes import bootstrap, evidence, layers

ROUTES = {
    bootstrap.PATH: bootstrap.bootstrap,
    layers.PATH: layers.layers,
    evidence.PATH: evidence.evidence,
}

REQUEST_AWARE_ROUTES = {
    layers.PATH: layers.layers,
    evidence.PATH: evidence.evidence,
}
