import json

def loadj(p): return json.loads(open(p,'r',encoding='utf-8').read())
def loadjl(p):
 return [json.loads(x) for x in open(p,'r',encoding='utf-8').read().splitlines() if x.strip()]
