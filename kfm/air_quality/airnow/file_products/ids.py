import hashlib, json, unicodedata

def canon(v):
    return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False)

def sha256_text(t):
    return hashlib.sha256(unicodedata.normalize("NFC",t).encode()).hexdigest()

def source_record_hash(row):
    return sha256_text(canon(row))

def make_id(prefix,seed):
    return f"{prefix}:{sha256_text(canon(seed))}"
