import hashlib, json, unicodedata

def cjson(obj):
    return json.dumps(obj, sort_keys=True, separators=(",",":"), ensure_ascii=False)

def sha256_text(text):
    if not isinstance(text,str):
        text=str(text)
    return hashlib.sha256(unicodedata.normalize("NFC",text).encode("utf-8")).hexdigest()

def stable_id(prefix,parts):
    return f"{prefix}:{sha256_text(cjson(parts))}"
