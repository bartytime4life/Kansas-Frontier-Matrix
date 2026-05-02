import hashlib
def sha256_path(p):
 h=hashlib.sha256(); h.update(open(p,'rb').read()); return h.hexdigest()
