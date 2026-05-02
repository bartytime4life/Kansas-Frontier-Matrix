import hashlib,json
def sid(ns,payload):
 s=json.dumps([ns,payload],sort_keys=True,separators=(",",":")); return hashlib.sha256(s.encode()).hexdigest()
