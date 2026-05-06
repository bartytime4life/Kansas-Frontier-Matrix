import hashlib

def sid(ns,val):
 s=val if isinstance(val,str) else '|'.join(str(x) for x in val)
 return hashlib.sha256(f"{ns}|{s}".encode()).hexdigest()
