from pathlib import Path
import hashlib

def load_policy_profile(path: str):
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError("missing policy profile")
    b = p.read_bytes()
    return {"policy_profile_url": str(p), "policy_profile_hash": hashlib.sha256(b).hexdigest()}
