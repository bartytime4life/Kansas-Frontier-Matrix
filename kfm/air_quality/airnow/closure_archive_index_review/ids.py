import hashlib, json

def cjson(o):
    return json.dumps(o, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sid(prefix, parts):
    joined = "|".join(str(x) for x in parts)
    return f"{prefix}_{hashlib.sha256((prefix+'|'+joined).encode()).hexdigest()[:16]}"
