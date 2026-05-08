from governed_api.stub import make_abstain_envelope

PATH = "/layers"

def layers() -> dict:
    return make_abstain_envelope("layers")
