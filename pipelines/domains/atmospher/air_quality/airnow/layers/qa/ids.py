import hashlib,json,unicodedata

def canonical_json(x):
    return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False)

def sha256_text(s):
    return hashlib.sha256(unicodedata.normalize("NFC",s).encode()).hexdigest()

def make_id(prefix,parts):
    return f"{prefix}:{sha256_text(canonical_json(parts))}"

def round_ratio(n,d):
    if not d:return None
    return round(n/d,6)
