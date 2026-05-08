from governed_api.stub import make_abstain_envelope

PATH = "/evidence"

def evidence() -> dict:
    return make_abstain_envelope("evidence")
