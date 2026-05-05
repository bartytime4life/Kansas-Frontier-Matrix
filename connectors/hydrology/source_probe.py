import os

def run_probe(source_id:str,dry_run:bool=True)->dict:
    if os.getenv('KFM_ALLOW_NETWORK')!='1':
        return {'outcome':'ABSTAIN','reason':'network disabled','source_id':source_id}
    if dry_run:
        return {'outcome':'ABSTAIN','reason':'dry-run metadata only','source_id':source_id}
    return {'outcome':'ERROR','reason':'live probing disabled by policy','source_id':source_id}
