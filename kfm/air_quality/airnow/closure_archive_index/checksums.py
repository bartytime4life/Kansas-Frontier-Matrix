import hashlib
def sha256_path(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for c in iter(lambda:f.read(131072),b''): h.update(c)
    return h.hexdigest()
