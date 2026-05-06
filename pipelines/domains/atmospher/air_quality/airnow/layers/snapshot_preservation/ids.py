import hashlib, json

def sid(ns,parts):
 if not isinstance(parts,list): parts=[parts]
 raw=ns+"|"+"|".join(str(p) for p in parts)
 return hashlib.sha256(raw.encode()).hexdigest()[:24]

def cjson(o):
 return json.dumps(o,sort_keys=True,separators=(",",":"))
