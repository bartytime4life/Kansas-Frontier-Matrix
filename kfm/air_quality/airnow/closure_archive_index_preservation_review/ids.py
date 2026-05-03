import hashlib, json

def cjson(o): return json.dumps(o,sort_keys=True,separators=(",",":"))

def sid(prefix,parts):
    h=hashlib.sha256((prefix+"|"+"|".join(str(x) for x in parts)).encode()).hexdigest()
    return f"{prefix}_{h[:16]}"
