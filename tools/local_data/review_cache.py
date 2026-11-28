"""Content-bound Qwen preparation on the runtime disk, before guarded acceptance."""
from contextlib import closing
import hashlib
import json
from pathlib import Path
import sqlite3

from tools.local_data import ai_acceptance as ai, intake_review
from tools.local_data.manage import canonical, utc_now


def key_for(item, client):
    return hashlib.sha256(canonical([item['id'],item['sha256'],intake_review.context(item),
        client.digest,ai.PROMPT_VERSION,ai.prompt_sha()])).hexdigest()


class Cache:
    def __init__(self, path):
        self.path=Path(path);self.path.parent.mkdir(mode=0o700,parents=True,exist_ok=True)
        with closing(sqlite3.connect(self.path)) as db:
            db.execute('CREATE TABLE IF NOT EXISTS prepared(key TEXT PRIMARY KEY,packet_sha TEXT,response_sha TEXT,body_sha TEXT,body TEXT NOT NULL)')
            db.commit()
        self.path.chmod(0o600)

    def get(self, key):
        with closing(sqlite3.connect(self.path)) as db:
            row=db.execute('SELECT packet_sha,response_sha,body_sha,body FROM prepared WHERE key=?',(key,)).fetchone()
        if not row:return None
        if hashlib.sha256(row[3].encode()).hexdigest()!=row[2]:raise ValueError('AI_PREPARED_CACHE_CHANGED')
        value=json.loads(row[3])
        if (hashlib.sha256(canonical(value['packet'])).hexdigest()!=row[0]
                or hashlib.sha256(value['response'].encode()).hexdigest()!=row[1]):
            raise ValueError('AI_PREPARED_CACHE_CHANGED')
        review=ai.validate_output(value['review'],value['packet'])
        raw=json.loads(value['response'])
        if value['packet'].get('description_policy')==ai.grounded_review.VERSION:
            inspection=next(json.loads(f['text']) for f in value['packet']['facts'] if f['id']=='gzip_inspection')
            expected,rendering=ai.grounded_review.render(raw,value['packet'],inspection)
        else:
            facts={f['id']:f['text'] for f in value['packet']['facts']}
            raw['evidence']=[{'source':v,'quote':facts[v][:500]} for v in raw['evidence']]
            expected,rendering=ai.validate_output(raw,value['packet']),None
        if review != expected or rendering != value['rendering']:raise ValueError('AI_PREPARED_REVIEW_CHANGED')
        return value

    def put(self, key, packet, review, client, response_hash):
        response=client.last_response
        if hashlib.sha256(response.encode()).hexdigest()!=response_hash:
            raise ValueError('AI_PREPARED_RESPONSE_CHANGED')
        value={'packet':packet,'review':ai.validate_output(review,packet),
            'response':response,'model':client.model,'digest':client.digest,
            'generated_at':utc_now(),'rendering':getattr(client,'last_rendering',None),
            'generation_prompt_sha256':getattr(client,'last_prompt_sha256',None)}
        body=json.dumps(value)
        with closing(sqlite3.connect(self.path)) as db:
            with db:db.execute('INSERT OR REPLACE INTO prepared VALUES(?,?,?,?,?)',
                (key,hashlib.sha256(canonical(packet)).hexdigest(),response_hash,hashlib.sha256(body.encode()).hexdigest(),body))
        return value


class CachedQwen(ai.Qwen):
    def __init__(self, model, digest, cache):
        super().__init__(model,digest);self.cache=cache;self.prepared=None

    def review(self, packet):
        value=self.prepared;self.prepared=None;self.last_generated_at=None
        if value is None:return super().review(packet)
        self.identity()
        if (value['model']!=self.model or value['digest']!=self.digest
                or canonical(value['packet'])!=canonical(packet)):
            raise ValueError('AI_PREPARED_CONTEXT_CHANGED')
        self.last_response=value['response'];self.last_rendering=value['rendering']
        self.last_prompt_sha256=value['generation_prompt_sha256'];self.last_generated_at=value['generated_at']
        return ai.validate_output(value['review'],packet),hashlib.sha256(self.last_response.encode()).hexdigest()


class CachedPackets:
    def __init__(self, builder, client, cache):
        self.builder,self.client,self.cache=builder,client,cache

    def __call__(self,root,item):
        value=self.cache.get(key_for(item,self.client))
        self.client.prepared=value
        return value['packet'] if value else self.builder(root,item)
