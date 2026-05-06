import hashlib, json
def cjson(o): return json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def sid(prefix,parts):
    return f"{prefix}_{hashlib.sha256((prefix+'|'+ '|'.join(str(x) for x in parts)).encode()).hexdigest()[:16]}"
