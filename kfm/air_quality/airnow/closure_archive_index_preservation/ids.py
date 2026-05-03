import hashlib,json
def sid(ns,payload):
 s=json.dumps(payload,sort_keys=True,separators=(',',':')) if not isinstance(payload,str) else payload
 return hashlib.sha256((ns+'|'+s).encode()).hexdigest()
