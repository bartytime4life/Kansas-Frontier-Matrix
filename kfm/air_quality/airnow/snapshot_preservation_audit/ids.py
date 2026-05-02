import hashlib, json

def cjson(o):
 return json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False)

def sid(ns,parts):
 return hashlib.sha256((ns+"|"+"|".join(str(p) for p in parts)).encode()).hexdigest()
