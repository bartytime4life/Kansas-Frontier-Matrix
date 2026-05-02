import hashlib, json

def cjson(v): return json.dumps(v, sort_keys=True, separators=(',',':'), ensure_ascii=False)
def sid(prefix,v): return f"{prefix}:{hashlib.sha256((v if isinstance(v,str) else cjson(v)).encode()).hexdigest()}"
