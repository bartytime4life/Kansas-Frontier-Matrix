"""Owner resolution retains the actual earlier generation and all old receipts."""
from contextlib import closing
import gzip
import hashlib
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest.mock import patch

from tools.local_data import ai_acceptance as ai,grounded_review as g,intake,intake_review,manage
from tools.local_data.smart_intake import SmartManager
from tools.local_data.recorded_review import RecordedReviews


class Reviewer:
    model='qwen3.5:test-local';digest='a'*64
    def __init__(self):self.calls=0
    def identity(self):return {'model':self.model,'digest':self.digest}
    def review(self,packet):
        self.calls+=1
        value={'title_ids':[],'passage_ids':[next(iter(g.choices(packet)[1]))],'domain':'atmosphere',
            'recommendation':'hold','confidence':'low','concern_codes':[]}
        result,self.last_rendering=g.render(value,packet,g.inspection_for(packet))
        self.last_response=json.dumps(value);self.last_prompt_sha256=hashlib.sha256(g.SYSTEM.encode()).hexdigest()
        return result,hashlib.sha256(self.last_response.encode()).hexdigest()


class RecordedReviewTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)/'store';manage.init_store(self.root)
        self.path=self.root/'data/raw/weather.csv.gz';self.path.write_bytes(gzip.compress(b'station,wind\nQA,2.4\n'))
        intake.analyze(self.root);self.identity=intake.item_id('raw','weather.csv.gz');self.client=Reviewer()
        original=SmartManager(self.root,self.client)
        original.start({'admin':'Test owner','filters':{},'limit':100,'retryHeld':False});original.thread.join(10)
        self.assertEqual(original.status()['job']['counts'],{'held':1})
        self.item=intake.get_item(self.root,self.identity);self.result=self.item['ai_review'];self.credit=self.result['attribution']
        self.before_receipt=(self.root/self.result['receipt']).read_bytes()
        self.before_metadata=(self.root/self.result['metadata_record']).read_bytes()
        packet=json.loads((self.root/self.credit['input_path']).read_text())
        body=json.dumps({'result':self.result,'packet':packet,'response':self.client.last_response})
        self.cache=Path(self.temp.name)/'recorded.sqlite'
        with closing(sqlite3.connect(self.cache)) as db,db:
            db.execute('CREATE TABLE reviews(id TEXT PRIMARY KEY,sha TEXT,context TEXT,body_sha TEXT,body TEXT)')
            db.execute('INSERT INTO reviews VALUES(?,?,?,?,?)',(self.identity,self.item['sha256'],
                intake_review.context(self.item),hashlib.sha256(body.encode()).hexdigest(),body))
        self.reader=RecordedReviews(self.cache,[{'version':self.credit['prompt_version'],'sha256':self.credit['prompt_sha256']}])
        self.bindings={self.identity:{'sha256':self.item['sha256'],'context':intake_review.context(self.item)}}
        policy={'schema':'kfm-owner-private-reference-v1','scope':'private-reference-only','requested_by':'Test owner',
            'authorized_at':manage.utc_now(),'request':'Retain these exact files as private references.','items':self.bindings}
        raw=manage.canonical(policy);self.policy=hashlib.sha256(raw).hexdigest()
        path=self.root/'data/work/intake/owner-policies'/(self.policy+'.json');path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(raw)

    def manager(self):return SmartManager(self.root,self.client,owner_policy=self.policy,recorded_reviews=self.reader)

    def test_existing_review_is_accepted_with_original_generation_and_new_owner_receipt(self):
        manager=self.manager();self.assertTrue(manager.start_owner_selection(self.bindings));manager.thread.join(10)
        self.assertEqual(manager.status()['job']['counts'],{'accepted':1});self.assertEqual(self.client.calls,1)
        item=intake.get_item(self.root,self.identity);credit=item['decision']['operator_review']['ai_attribution']
        for key in ('generated_at','prompt_version','prompt_sha256','input_sha256','response_sha256','batch_id'):
            self.assertEqual(credit[key],self.credit[key])
        self.assertNotEqual(credit['acceptance_batch_id'],credit['batch_id'])
        self.assertTrue(credit['review_reused']);self.assertEqual(credit['review']['recommendation'],'hold')
        self.assertEqual((self.root/self.result['receipt']).read_bytes(),self.before_receipt)
        self.assertEqual((self.root/self.result['metadata_record']).read_bytes(),self.before_metadata)
        new=item['ai_review']['metadata_record'];self.assertNotEqual(new,self.result['metadata_record'])
        self.assertEqual(json.loads((self.root/new).read_text())['outcome'],'accepted')
        self.assertIn('REVIEWED_LOCAL_ONLY',item['decision']['holds']);self.assertEqual(len(item['review_history']),1)

    def test_metadata_interruption_resumes_without_duplicate_review_or_generation(self):
        manager=self.manager()
        with patch.object(manager,'organize',side_effect=OSError('interrupted')):
            manager.start_owner_selection(self.bindings);manager.thread.join(10)
        self.assertEqual(manager.status()['job']['state'],'paused')
        manager.control('resume');manager.thread.join(10)
        self.assertEqual(manager.status()['job']['counts'],{'accepted':1})
        self.assertEqual(self.client.calls,1);self.assertEqual(len(intake.get_item(self.root,self.identity)['review_history']),1)

    def test_unbound_context_is_not_queued(self):
        self.bindings[self.identity]['context']='b'*64
        self.assertFalse(self.manager().start_owner_selection(self.bindings));self.assertEqual(self.client.calls,1)

    def test_busy_owner_acceptance_pauses_and_reuses_the_recorded_review_on_resume(self):
        manager=self.manager()
        with patch.object(intake_review,'save',side_effect=ValueError('INTAKE_BUSY')):
            manager.start_owner_selection(self.bindings);manager.thread.join(10)
        self.assertEqual(manager.status()['job']['state'],'paused')
        self.assertEqual(manager.status()['job']['error'],'AI_WORKING_DATA_BUSY_RESUME')
        self.assertEqual(manager.status()['job']['counts'],{'pending':1})
        manager.control('resume');manager.thread.join(10)
        self.assertEqual(manager.status()['job']['counts'],{'accepted':1})
        self.assertEqual(self.client.calls,1);self.assertEqual(len(intake.get_item(self.root,self.identity)['review_history']),1)

    def test_changed_source_bytes_are_rejected_before_reusing_review(self):
        self.path.write_bytes(gzip.compress(b'changed source'))
        manager=self.manager();manager.start_owner_selection(self.bindings);manager.thread.join(10)
        self.assertEqual(manager.status()['job']['counts'],{'failed':1})
        self.assertEqual(intake.get_item(self.root,self.identity)['status'],'review');self.assertEqual(self.client.calls,1)

    def test_forged_cached_description_cannot_replace_the_recorded_response(self):
        with closing(sqlite3.connect(self.cache)) as db,db:
            value=json.loads(db.execute('SELECT body FROM reviews').fetchone()[0]);value['result']['title']='Forged title'
            body=json.dumps(value);db.execute('UPDATE reviews SET body=?,body_sha=?',(body,hashlib.sha256(body.encode()).hexdigest()))
        manager=self.manager();manager.start_owner_selection(self.bindings);manager.thread.join(10)
        self.assertEqual(manager.status()['job']['counts'],{'failed':1})
        self.assertEqual(intake.get_item(self.root,self.identity)['status'],'review')

    def test_changed_physical_response_is_rejected(self):
        (self.root/self.credit['response_path']).write_text('{}')
        manager=self.manager();manager.start_owner_selection(self.bindings);manager.thread.join(10)
        self.assertEqual(manager.status()['job']['counts'],{'failed':1})
        self.assertEqual(intake.get_item(self.root,self.identity)['status'],'review')

    def test_trusted_unsupported_extractive_policy_defers_to_current_review_engine(self):
        with closing(sqlite3.connect(self.cache)) as db,db:
            value=json.loads(db.execute('SELECT body FROM reviews').fetchone()[0])
            value['packet']['description_policy']='source-passages-v1'
            raw=manage.canonical(value['packet']);digest=hashlib.sha256(raw).hexdigest()
            path='data/work/intake/ai-context/'+digest+'.json';(self.root/path).write_bytes(raw)
            credit=value['result']['attribution']
            credit.update(input_path=path,input_sha256=digest,prompt_version='legacy-extractive',prompt_sha256='b'*64)
            body=json.dumps(value);db.execute('UPDATE reviews SET body=?,body_sha=?',
                (body,hashlib.sha256(body.encode()).hexdigest()))
        reader=RecordedReviews(self.cache,[{'version':'legacy-extractive','sha256':'b'*64}])
        task=('new-job',0,self.identity,self.item['sha256'],intake_review.context(self.item),'new-cache')
        self.assertIsNone(reader.get(self.root,self.item,task,self.client))
        # Unsupported rendering is not permission to ignore changed evidence.
        (self.root/credit['response_path']).write_text('{}')
        with self.assertRaisesRegex(ValueError,'RECORDED_REVIEW_RECEIPT_CHANGED'):
            reader.get(self.root,self.item,task,self.client)

    def test_whitespace_only_legacy_review_is_regenerated_as_inspection_availability(self):
        self.path.write_bytes(gzip.compress(b' \n\t\r\n'));intake.analyze(self.root)
        def legacy_packet(root,item):
            packet=ai.packet_for(root,item)
            self.assertEqual(packet['description_policy'],g.AVAILABILITY_VERSION)
            packet['description_policy']=g.VERSION
            return packet
        manager=SmartManager(self.root,self.client,packet_builder=legacy_packet)
        manager.start({'admin':'Test owner','filters':{},'limit':100,'retryHeld':False});manager.thread.join(10)
        item=intake.get_item(self.root,self.identity);result=item['ai_review'];credit=result['attribution']
        self.assertIn('Source text (',result['description'])
        packet=json.loads((self.root/credit['input_path']).read_text())
        body=json.dumps({'result':result,'packet':packet})
        with closing(sqlite3.connect(self.cache)) as db,db:
            db.execute('UPDATE reviews SET sha=?,context=?,body_sha=?,body=? WHERE id=?',
                (item['sha256'],intake_review.context(item),hashlib.sha256(body.encode()).hexdigest(),body,self.identity))
        reader=RecordedReviews(self.cache,[{'version':credit['prompt_version'],'sha256':credit['prompt_sha256']}])
        task=('new-job',0,self.identity,item['sha256'],intake_review.context(item),'new-cache')
        self.assertIsNone(reader.get(self.root,item,task,self.client))


if __name__=='__main__':unittest.main()
