"""Reuse an audited, unchanged local review without inventing a new generation."""
from contextlib import closing
import hashlib
import json
from pathlib import Path
import re
import sqlite3

from tools.local_data import ai_acceptance as ai,intake_review
from tools.local_data.file_io import read_regular


class RecordedReviews:
    def __init__(self, path, trusted_prompts):
        self.path=Path(path)
        self.trusted={(v['version'],v['sha256']) for v in trusted_prompts}

    def get(self,root,item,task,client):
        with closing(sqlite3.connect(self.path.as_uri()+'?mode=ro',uri=True)) as db:
            row=db.execute('SELECT sha,context,body_sha,body FROM reviews WHERE id=?',(item['id'],)).fetchone()
        if not row:return None
        if row[0]!=item['sha256'] or row[1]!=task[4] or intake_review.context(item)!=task[4]:return None
        if hashlib.sha256(row[3].encode()).hexdigest()!=row[2]:raise ValueError('RECORDED_REVIEW_CACHE_CHANGED')
        value=json.loads(row[3]);result=value['result'];credit=result['attribution']
        if (credit.get('kind')!='local-ai' or credit.get('model')!=client.model
                or credit.get('model_digest')!=client.digest
                or (credit.get('prompt_version'),credit.get('prompt_sha256')) not in self.trusted
                or not result.get('ai_reviewed') or result.get('outcome')!='held'
                or result['sha256']!=task[3] or result['context']!=task[4]):
            raise ValueError('RECORDED_REVIEW_IDENTITY_CHANGED')
        for field,directory,digest in [('input_path','ai-context',credit['input_sha256']),
                                       ('response_path','ai-responses',credit['response_sha256'])]:
            if not re.fullmatch(r'data/work/intake/'+directory+'/'+digest+r'\.json',credit[field]):
                raise ValueError('RECORDED_REVIEW_PATH_INVALID')
            body=read_regular(root/credit[field],131072)
            if hashlib.sha256(body).hexdigest()!=digest:raise ValueError('RECORDED_REVIEW_RECEIPT_CHANGED')
            if field=='input_path':packet=json.loads(body)
            else:response=json.loads(body)
        if packet!=value['packet']:raise ValueError('RECORDED_REVIEW_INPUT_CHANGED')
        # Old empty-text output quoted an inspection note as if it were source
        # text. The new availability policy generates a properly labeled review.
        if any(f['id']=='gzip_inspection' for f in packet['facts']) and not any(f['id'].startswith('gzip_text_') and f['text'].strip() for f in packet['facts']):
            return None
        if ai.grounded_review.is_extractive(packet):
            rendered,_=ai.grounded_review.render(response,packet,ai.grounded_review.inspection_for(packet))
        else:
            facts={f['id']:f['text'] for f in packet['facts']}
            response['evidence']=[{'source':v,'quote':facts[v][:500]} for v in response['evidence']]
            rendered=ai.validate_output(response,packet)
        if rendered!=credit['review'] or any(result[k]!=rendered[k] for k in ai.OUTPUT_SCHEMA['required']):
            raise ValueError('RECORDED_REVIEW_RENDERING_CHANGED')
        result.pop('metadata_record',None)
        result['review_reused']=True
        return result
