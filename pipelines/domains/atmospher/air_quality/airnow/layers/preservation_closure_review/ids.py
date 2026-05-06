import hashlib, json

def sid(ns, payload):
 return hashlib.sha256((ns+"|"+json.dumps(payload,sort_keys=True,separators=(",",":"))).encode()).hexdigest()
