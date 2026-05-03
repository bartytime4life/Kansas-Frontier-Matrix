import hashlib, json

def cjson(o):
    return json.dumps(o, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sid(prefix, parts):
    raw = prefix + "|" + "|".join(str(x) for x in parts)
    return f"{prefix}:{hashlib.sha256(raw.encode()).hexdigest()}"
