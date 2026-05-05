#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from copy import deepcopy

FORBIDDEN_FIELDS={"decimalLatitude","decimalLongitude","occurrenceLatitude","occurrenceLongitude","exact_coordinate","exactCoordinates","raw_occurrence_point","rawGbifCoordinate","site_level_location","precise_location","private_geometry","raw_point_geometry"}
FORBIDDEN_PHRASES=["confirmed present","verified present","known population","exact location","site-level record","precise coordinates","occurrence point","raw gbif location","raw point location"]
REQ_PRESENCE="reported_occurrence_not_confirmed_presence"

def canonicalize(v):
    if isinstance(v,dict): return {k:canonicalize(v[k]) for k in sorted(v)}
    if isinstance(v,list):
        c=[canonicalize(x) for x in v]
        if all(isinstance(x,(str,int,float,bool,type(None))) for x in c):
            return sorted(c,key=lambda x: json.dumps(x,sort_keys=True))
        return c
    return v

def stable_hash(doc, exclude=()):
    c=deepcopy(doc)
    for k in exclude: c.pop(k,None)
    return 'sha256:'+hashlib.sha256(json.dumps(canonicalize(c),sort_keys=True,separators=(',',':')).encode()).hexdigest()

def scan_forbidden(obj,path='$',errs=None):
    if errs is None: errs=[]
    if isinstance(obj,dict):
        for k,v in obj.items():
            if k in FORBIDDEN_FIELDS: errs.append(f'forbidden field at {path}.{k}')
            scan_forbidden(v,f'{path}.{k}',errs)
    elif isinstance(obj,list):
        for i,v in enumerate(obj): scan_forbidden(v,f'{path}[{i}]',errs)
    elif isinstance(obj,str):
        low=obj.lower()
        for p in FORBIDDEN_PHRASES:
            if p in low: errs.append(f"forbidden language '{p}' at {path}")
    return errs

def deterministic_cache_key(route_type, artifact_id):
    return f"gbif:fauna:{route_type}:{artifact_id}"
