from governed_api.stub import make_abstain_envelope

PATH = "/bootstrap"

def bootstrap() -> dict:
    return make_abstain_envelope("bootstrap")
