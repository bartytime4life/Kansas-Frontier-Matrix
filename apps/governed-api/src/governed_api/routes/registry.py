from governed_api.routes import bootstrap, evidence, layers
from governed_api.stub import make_abstain_envelope


def _layers_scaffold() -> dict:
    """Preserve the zero-argument lifecycle-overlay registry contract."""
    return make_abstain_envelope("layers")


def _evidence_scaffold() -> dict:
    """Preserve the zero-argument lifecycle-overlay registry contract."""
    return make_abstain_envelope("evidence")

ROUTES = {
    bootstrap.PATH: bootstrap.bootstrap,
    layers.PATH: _layers_scaffold,
    evidence.PATH: _evidence_scaffold,
}

REQUEST_AWARE_ROUTES = {
    layers.PATH: layers.layers,
    evidence.PATH: evidence.evidence,
}
