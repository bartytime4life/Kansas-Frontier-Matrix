"""Prepared metadata must remain bound to original bytes, context and real model output."""
import copy
from contextlib import closing
import gzip
import gc
import hashlib
import json
from pathlib import Path
import sqlite3
import tempfile
import sys
import unittest
from unittest.mock import patch

from tools.local_data import ai_acceptance as ai,intake,intake_review,manage,grounded_review as g,prepare_intake
from tools.local_data.review_cache import Cache,CachedQwen,CachedPackets,key_for
from tools.local_data.smart_intake import SmartManager
from tools.local_data.prepare_intake import current_item


class RecordedQwen:
    model='qwen3.5:test-local';digest='a'*64
    def identity(self):return {'model':self.model,'digest':self.digest}
    def review(self,packet):
        self.calls=getattr(self,'calls',0)+1
        selection={'title_ids':[],'passage_ids':[next(iter(g.choices(packet)[1]))],
            'domain':'hydrology','recommendation':'accept_local','confidence':'high','concern_codes':[]}
        inspection=next(json.loads(f['text']) for f in packet['facts'] if f['id']=='gzip_inspection')
        result,self.last_rendering=g.render(selection,packet,inspection)
        self.last_response=json.dumps(selection);self.last_prompt_sha256=hashlib.sha256(g.SYSTEM.encode()).hexdigest()
        return result,hashlib.sha256(self.last_response.encode()).hexdigest()


class ReviewCacheTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)/'store';manage.init_store(self.root)
        p=self.root/'data/raw/sample.csv.gz';p.write_bytes(gzip.compress(b'station,river\nQA,2.4\n'))
        intake.analyze(self.root);self.item=intake.get_item(self.root,intake.item_id('raw','sample.csv.gz'))
        self.packet=ai.packet_for(self.root,self.item);self.client=RecordedQwen();review,sha=self.client.review(self.packet)
        self.cache=Cache(Path(self.temp.name)/'cache.sqlite');self.key=key_for(self.item,self.client)
        self.saved=self.cache.put(self.key,self.packet,review,self.client,sha)

    def test_replay_uses_exact_original_input_response_and_generation_time(self):
        c=CachedQwen(self.client.model,self.client.digest,self.cache)
        builder=CachedPackets(lambda *_:self.fail('cache should supply the recorded input'),c,self.cache)
        packet=builder(self.root,self.item)
        with patch.object(c,'identity'):
            result,sha=c.review(packet)
        self.assertEqual(result,self.saved['review']);self.assertEqual(c.last_response,self.saved['response'])
        self.assertEqual(c.last_generated_at,self.saved['generated_at'])
        self.assertEqual(sha,hashlib.sha256(self.saved['response'].encode()).hexdigest())

    def test_changed_bytes_or_review_context_cannot_reuse_a_packet(self):
        for field in ('sha256','declared'):
            item=copy.deepcopy(self.item);item[field]='b'*64 if field=='sha256' else {'sensitivity':'controlled'}
            self.assertIsNone(self.cache.get(key_for(item,self.client)))

    def test_changed_prompt_cannot_reuse_the_cache(self):
        with patch.object(ai,'PROMPT_VERSION','a different prompt'):
            self.assertIsNone(self.cache.get(key_for(self.item,self.client)))

    def test_corrupt_or_rewritten_parsed_review_is_rejected(self):
        with closing(sqlite3.connect(self.cache.path)) as db,db:
            value=json.loads(db.execute('SELECT body FROM prepared').fetchone()[0]);value['review']['confidence']='low'
            body=json.dumps(value)
            db.execute('UPDATE prepared SET body=?,body_sha=?',(body,hashlib.sha256(body.encode()).hexdigest()))
        with self.assertRaisesRegex(ValueError,'PREPARED_REVIEW_CHANGED'):self.cache.get(self.key)

    def test_model_identity_is_checked_even_for_cached_results(self):
        c=CachedQwen(self.client.model,self.client.digest,self.cache);c.prepared=self.cache.get(self.key)
        with patch.object(c,'identity',side_effect=ai.ProviderError('LOCAL_QWEN_MODEL_PIN_CHANGED')):
            with self.assertRaises(ai.ProviderError):c.review(self.packet)

    def test_native_acceptance_retains_the_prepared_credit_and_source_checks(self):
        c=CachedQwen(self.client.model,self.client.digest,self.cache)
        with patch.object(c,'identity'):
            manager=SmartManager(self.root,c,packet_builder=CachedPackets(ai.packet_for,c,self.cache))
            manager.start({'admin':'Test owner','filters':{},'limit':10,'retryHeld':False})
            manager.thread.join(10)
        self.assertEqual(manager.status()['job']['counts'],{'accepted':1})
        item=intake.get_item(self.root,self.item['id'])
        self.assertEqual(item['ai_review']['attribution']['generated_at'],self.saved['generated_at'])
        self.assertEqual(item['ai_review']['attribution']['response_sha256'],hashlib.sha256(self.saved['response'].encode()).hexdigest())

    def test_source_changes_are_rejected_before_a_cached_acceptance(self):
        (self.root/self.item['store_path']).write_bytes(gzip.compress(b'station,river\nQA,8.4\n'))
        c=CachedQwen(self.client.model,self.client.digest,self.cache)
        with patch.object(c,'identity'):
            manager=SmartManager(self.root,c,packet_builder=CachedPackets(ai.packet_for,c,self.cache))
            manager.start({'admin':'Test owner','filters':{},'limit':10,'retryHeld':False})
            manager.thread.join(10)
        self.assertEqual(manager.status()['job']['counts'],{'failed':1})
        self.assertEqual(intake.get_item(self.root,self.item['id'])['status'],'review')

    def test_large_preparation_scan_closes_connections_without_waiting_for_gc(self):
        ai.Manager(self.root,self.client)
        baseline=len(list(Path('/proc/self/fd').iterdir()))
        gc.disable()
        try:
            for _ in range(600):
                item,_=current_item(self.root,self.item['id'])
                self.assertEqual(item['sha256'],self.item['sha256'])
            self.assertLessEqual(len(list(Path('/proc/self/fd').iterdir())),baseline+2)
        finally:gc.enable()


class PreparationCommandTests(unittest.TestCase):
    def exercise(self,configured):
        with tempfile.TemporaryDirectory() as folder:
            base=Path(folder);root=base/'store';manage.init_store(root)
            source=root/'data/raw/sample.csv.gz';source.write_bytes(gzip.compress(b'station,river\nQA,2.4\n'))
            intake.analyze(root);item=intake.get_item(root,intake.item_id('raw','sample.csv.gz'))
            client=RecordedQwen();ai.Manager(root,client)
            runtime=base/'pc/runtime';runtime.mkdir(parents=True);(runtime.parent/'run').mkdir()
            (runtime/'storage-identity.json').write_text(json.dumps({'root':str(root)}))
            (runtime/'check-data-mount.py').write_text('raise SystemExit(0)\n')
            policy=manage.canonical({'items':{item['id']:{'sha256':item['sha256'],'context':intake_review.context(item)}}})
            policy_path=base/'owner-policy.json';policy_path.write_bytes(policy)
            config={'model':client.model,'model_digest':client.digest,'owner_policy_source':str(policy_path),
                'owner_policy':hashlib.sha256(policy).hexdigest()}
            default=runtime.parent/'run/smart-intake-cache.sqlite'
            expected=base/'configured-cache/prepared.sqlite' if configured else default
            if configured:config['preparation_cache']=str(expected)
            path=runtime/'smart-intake.json';path.write_text(json.dumps(config))
            before=hashlib.sha256((root/'data/work/intake/index.sqlite').read_bytes()).hexdigest()
            with patch.object(sys,'argv',['prepare_intake','--config',str(path)]), \
                    patch.object(prepare_intake.ai,'Qwen',return_value=client),patch.object(prepare_intake.signal,'signal'):
                prepare_intake.main()
            self.assertTrue(expected.is_file())
            if configured:self.assertFalse(default.exists())
            self.assertEqual(client.calls,1)
            self.assertEqual(hashlib.sha256((root/'data/work/intake/index.sqlite').read_bytes()).hexdigest(),before)
            self.assertEqual(intake.get_item(root,item['id'])['status'],'review')
            cache=Cache(expected);saved=cache.get(key_for(item,client));self.assertIsNotNone(saved)
            consumer=CachedQwen(client.model,client.digest,cache)
            builder=CachedPackets(lambda *_:self.fail('recorded input should be used'),consumer,cache)
            with patch.object(consumer,'identity'),patch.object(ai.Qwen,'review',side_effect=AssertionError('unexpected second inference')):
                result,_=consumer.review(builder(root,item))
            self.assertEqual(result,saved['review']);self.assertEqual(consumer.last_generated_at,saved['generated_at'])
            self.assertEqual(client.calls,1)

    def test_preparation_uses_configured_cache_consumed_by_acceptance(self):self.exercise(True)

    def test_preparation_default_cache_remains_consumable(self):self.exercise(False)


if __name__=='__main__':unittest.main()
