"""Owner scope is exact, private, auditable and recoverable after an interrupted write."""
import gzip
import hashlib
import json
from pathlib import Path
import tempfile
import threading
import sqlite3
import unittest
from unittest.mock import patch

from tools.local_data import intake, intake_review, manage, ai_acceptance as ai
from tools.local_data.smart_intake import SmartManager, export_catalog,operator_stopped
from tests.local_data.test_ai_acceptance import FakeQwen


class SmartIntakeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)/'store';manage.init_store(self.root)
        self.path = self.root/'data/raw/hydrology.csv.gz'
        self.path.write_bytes(gzip.compress(b'station,river_level_m\nQA,2.4\n'))
        intake.analyze(self.root);self.identity = intake.item_id('raw','hydrology.csv.gz')
        self.client = FakeQwen();self.client.hold = True
        self.item = intake.get_item(self.root,self.identity)

    def authorize(self, identity=None, sha=None):
        policy = {'schema':'kfm-owner-private-reference-v1','scope':'private-reference-only',
            'requested_by':'Test owner','authorized_at':manage.utc_now(),'request':'Retain these exact files as private references.',
            'items':{identity or self.identity:{'sha256':sha or self.item['sha256'],'context':intake_review.context(self.item)}}}
        body = manage.canonical(policy);digest = hashlib.sha256(body).hexdigest()
        p=self.root/'data/work/intake/owner-policies'/(digest+'.json');p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(body)
        return digest

    def run_job(self, policy=None):
        manager = SmartManager(self.root,self.client,owner_policy=policy)
        manager.start({'admin':'Test owner','filters':{},'limit':100,'retryHeld':False})
        manager.thread.join(10);self.assertFalse(manager.thread.is_alive())
        return manager,manager.status()['job']

    def test_compressed_csv_is_read_without_an_owner_exception(self):
        self.client.hold=False
        _,job=self.run_job()
        self.assertEqual(job['counts'],{'accepted':1})
        result=intake.get_item(self.root,self.identity)['ai_review']
        self.assertTrue(result['attribution']['text_extraction']['crc_validated'])

    def test_exact_owner_request_retains_model_disagreement_and_sharing_holds(self):
        original=self.path.read_bytes();_,job=self.run_job(self.authorize())
        self.assertEqual(job['counts'],{'accepted':1})
        item=intake.get_item(self.root,self.identity)
        self.assertEqual(item['status'],'reviewed');self.assertEqual(item['ai_review']['recommendation'],'hold')
        self.assertEqual(item['ai_review']['attribution']['acceptance_basis'],'owner_requested_private_reference')
        self.assertIn('REVIEWED_LOCAL_ONLY',item['decision']['holds'])
        self.assertEqual(item['review_history'][0]['rights'],'unknown')
        self.assertEqual(original,self.path.read_bytes());export_catalog(self.root)
        self.assertTrue((self.root/'data/work/intake/smart-catalog/CATALOG.csv').exists())

    def test_another_file_or_digest_is_not_authorized(self):
        _,job=self.run_job(self.authorize(sha='f'*64))
        self.assertEqual(job['counts'],{'held':1})
        self.assertEqual(intake.get_item(self.root,self.identity)['status'],'review')

    def test_interrupted_metadata_write_resumes_without_a_second_review(self):
        manager=SmartManager(self.root,self.client,owner_policy=self.authorize())
        with patch.object(manager,'organize',side_effect=OSError('interrupted')):
            manager.start({'admin':'Test owner','filters':{},'limit':100,'retryHeld':False})
            manager.thread.join(10)
        self.assertEqual(manager.status()['job']['state'],'paused')
        manager.control('resume');manager.thread.join(10)
        self.assertEqual(manager.status()['job']['counts'],{'accepted':1})
        self.assertEqual(self.client.calls,1)
        self.assertEqual(len(intake.get_item(self.root,self.identity)['review_history']),1)

    def test_studio_pause_reaches_a_separate_worker_instance(self):
        entered=threading.Event();release=threading.Event()
        self.client.before=lambda packet:(entered.set(),release.wait(5))
        worker=SmartManager(self.root,self.client)
        worker.start({'admin':'Test owner','filters':{},'limit':100,'retryHeld':False})
        self.assertTrue(entered.wait(5))
        studio=ai.Manager(self.root,FakeQwen())
        studio.control('pause');release.set();worker.thread.join(10)
        self.assertFalse(worker.thread.is_alive())
        self.assertEqual(worker.status()['job']['state'],'paused')
        self.assertTrue(operator_stopped(worker.status()['job']))
        worker.control('resume');worker.thread.join(10)
        self.assertFalse(operator_stopped(worker.status()['job']))

    def test_operator_pause_and_maintenance_pause_are_distinct(self):
        self.assertTrue(operator_stopped({'state':'paused','error':'ADMIN_PAUSED'}))
        self.assertTrue(operator_stopped({'state':'cancelled','error':'ADMIN_CANCELLED'}))
        self.assertFalse(operator_stopped({'state':'paused','error':'INTERRUPTED_RESTART'}))
        self.assertFalse(operator_stopped({'state':'paused','error':None}))

    def test_existing_studio_catalog_opens_while_another_connection_writes(self):
        first=ai.Manager(self.root,FakeQwen())
        writer=sqlite3.connect(self.root/'data/work/intake/index.sqlite')
        try:
            writer.execute('BEGIN IMMEDIATE')
            reader=ai.Manager(self.root,FakeQwen())
            self.assertIsNone(reader.status()['job'])
        finally:
            writer.rollback();writer.close()

    def test_data_maintenance_blocks_acceptance_without_losing_the_pending_task(self):
        phase=Path(self.temp.name)/'phase.json';phase.write_text(json.dumps({'phase':'verifying'}))
        manager=SmartManager(self.root,self.client,maintenance_file=phase)
        with self.assertRaisesRegex(ai.ProviderError,'AI_DATA_MAINTENANCE'):
            manager.start({'admin':'Test owner','filters':{},'limit':10,'retryHeld':False})
        self.assertTrue(manager.status()['maintenance'])
        self.assertEqual(intake.get_item(self.root,self.identity)['status'],'review')

    def test_backup_activation_blocks_workspace_acceptance(self):
        manager=SmartManager(self.root,self.client,backup_units=('test-backup.service',))
        with patch('tools.local_data.smart_intake.subprocess.check_output',return_value='activating\n'):
            with self.assertRaisesRegex(ai.ProviderError,'AI_BACKUP_RUNNING'):
                manager.start({'admin':'Test owner','filters':{},'limit':10,'retryHeld':False})
            self.assertEqual(manager.status()['maintenanceReason'],'backup')
        self.assertEqual(self.client.calls,0)
        self.assertEqual(intake.get_item(self.root,self.identity)['status'],'review')

    def test_backup_starting_during_inference_saves_the_draft_for_resume(self):
        self.client.hold=False
        running=[False]
        self.client.before=lambda packet:running.__setitem__(0,True)
        manager=SmartManager(self.root,self.client,backup_units=('test-backup.service',))
        with patch('tools.local_data.smart_intake.backup_running',side_effect=lambda units:running[0]):
            manager.start({'admin':'Test owner','filters':{},'limit':10,'retryHeld':False})
            manager.thread.join(10)
            self.assertEqual(manager.status()['job']['counts'],{'pending':1})
            self.assertEqual(manager.status()['job']['error'],'AI_BACKUP_RUNNING')
            self.assertEqual(intake.get_item(self.root,self.identity)['status'],'review')
            running[0]=False;self.client.before=None
            manager.control('resume');manager.thread.join(10)
            self.assertEqual(manager.status()['job']['counts'],{'accepted':1})
        self.assertEqual(self.client.calls,1)

    def test_unavailable_backup_status_does_not_allow_acceptance(self):
        manager=SmartManager(self.root,self.client,backup_units=('test-backup.service',))
        with patch('tools.local_data.smart_intake.backup_running',side_effect=OSError('service bus unavailable')):
            with self.assertRaisesRegex(ai.ProviderError,'AI_BACKUP_STATE_UNAVAILABLE'):
                manager.start({'admin':'Test owner','filters':{},'limit':10,'retryHeld':False})
        self.assertEqual(self.client.calls,0)


if __name__=='__main__':unittest.main()
