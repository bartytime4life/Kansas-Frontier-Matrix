import hashlib,json

def cjson(o): return json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def sid(prefix,parts): return prefix+":"+hashlib.sha256(("|".join(str(p) for p in parts)).encode()).hexdigest()[:16]
