import hashlib, json, unicodedata

def stable_json_dumps(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sha256_text(text: str) -> str:
    return hashlib.sha256(unicodedata.normalize("NFC", text).encode("utf-8")).hexdigest()

def source_record_hash(record: dict) -> str:
    return sha256_text(stable_json_dumps(record))

def canonical_id(prefix: str, seed_parts: list[str]) -> str:
    return f"{prefix}:{sha256_text('|'.join(seed_parts))}"
