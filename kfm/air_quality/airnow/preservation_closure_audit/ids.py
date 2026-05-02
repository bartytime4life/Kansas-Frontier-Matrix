import hashlib,json
def cjson(o): return json.dumps(o,sort_keys=True,separators=(",",":"))
def sid(ns,parts):
    h=hashlib.sha256((ns+"|"+"|".join(str(x) for x in parts)).encode()).hexdigest(); return h
