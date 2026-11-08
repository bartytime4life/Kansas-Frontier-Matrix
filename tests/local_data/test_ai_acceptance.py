"""Local AI batches preserve provenance, guarded acceptance and restartability."""
import hashlib
import json
import os
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch

from tools.local_data import ai_acceptance as ai, intake, intake_review, intake_route, manage


class FakeQwen:
    model = "qwen3.5:test-local"
    digest = "a"*64
    def __init__(self):
        self.calls = 0
        self.before = lambda packet:None
        self.hold = False
    def identity(self):
        return {"model":self.model,"digest":self.digest}
    def review(self,packet):
        self.calls += 1
        self.before(packet)
        review = {"title":"Hydrology CSV for private local review",
            "description":"The inspected metadata identifies a CSV table with hydrology fields. The bounded text sample is a local QA fixture; it does not establish real observations or public-use rights.",
            "domain":"hydrology","recommendation":"hold" if self.hold else "accept_local","confidence":"high",
            "evidence":[{"source":"format","quote":packet["facts"][1]["text"][:60]}],"concerns":[]}
        return review,hashlib.sha256(manage.canonical(review)).hexdigest()


class AcceptanceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)/"store"
        manage.init_store(self.root)
        self.path = self.root/"data/raw/hydrology.csv"
        self.path.write_text("station,river_level_m\nQA,2.4\n")
        intake.analyze(self.root)
        self.id = intake.item_id("raw","hydrology.csv")
        self.client = FakeQwen()
        self.manager = ai.Manager(self.root,self.client)
        self.addCleanup(self.finish)
    def finish(self):
        if self.manager.thread:
            self.manager.stop.set()
            self.manager.thread.join(5)
    def request(self,**patches):
        return {"admin":"Test admin","filters":{},"limit":100,"retryHeld":False,**patches}
    def run_batch(self,**patches):
        self.manager.start(self.request(**patches))
        self.manager.thread.join(10)
        self.assertFalse(self.manager.thread.is_alive())
        return self.manager.status()["job"]

    def test_accepted_file_has_ai_description_and_separate_admin_credit(self):
        original = self.path.read_bytes()
        job = self.run_batch()
        self.assertEqual(job["state"],"completed")
        self.assertEqual(job["counts"],{"accepted":1})
        item = intake.get_item(self.root,self.id)
        self.assertEqual(item["status"],"reviewed")
        self.assertEqual(item["ai_review"]["attribution"]["requested_by"],"Test admin")
        review = item["review_history"][0]
        self.assertEqual(review["reviewer"],"Local AI: "+self.client.model)
        self.assertEqual(review["ai_attribution"]["model_digest"],self.client.digest)
        self.assertEqual(review["rights"],"unknown")
        self.assertEqual(review["sensitivity"],"unknown")
        self.assertIn("REVIEWED_LOCAL_ONLY",item["decision"]["holds"])
        self.assertFalse(any(p["action"] in {"candidate","metadata_card"} for p in item["decision"]["placements"]))
        self.assertEqual(original,self.path.read_bytes())
        self.assertTrue((self.root/review["receipt"]).is_file())
        self.assertIn("ai_review",intake.list_items(self.root)["items"][0])
        intake.analyze(self.root)
        self.assertEqual(intake.get_item(self.root,self.id)["ai_review"]["outcome"],"accepted")

    def test_held_review_describes_file_without_accepting_or_repeating(self):
        self.client.hold = True
        job = self.run_batch()
        self.assertEqual(job["counts"],{"held":1})
        item = intake.get_item(self.root,self.id)
        self.assertEqual(item["status"],"review")
        self.assertTrue(item["ai_review"]["description"])
        with self.assertRaisesRegex(ValueError,"NO_NEW_PENDING"):
            self.manager.start(self.request())
        self.run_batch(retryHeld=True)
        self.assertEqual(self.client.calls,2)

    def test_sensitive_flags_cannot_be_cleared_by_ai(self):
        with intake.open_index(self.root) as db:
            body = json.loads(db.execute("SELECT decision_json FROM items WHERE id=?",(self.id,)).fetchone()[0])
            body["review_flags"]=["sensitive_location"]
            db.execute("UPDATE items SET decision_json=? WHERE id=?",(json.dumps(body),self.id))
        self.assertEqual(self.run_batch()["counts"],{"held":1})
        self.assertEqual(intake.get_item(self.root,self.id)["status"],"review")

    def test_personal_content_is_held_even_when_model_says_accept(self):
        self.path.write_text('patient_id,medical_note\nSYNTHETIC,test only\n')
        intake.analyze(self.root)
        self.assertEqual(self.run_batch()['counts'],{'held':1})
        self.assertIn('CONTENT_SENSITIVITY_REQUIRES_ADMIN',intake.get_item(self.root,self.id)['ai_review']['holds'])

    def test_changed_original_is_not_sent_to_ai_or_accepted(self):
        self.path.write_text("changed original bytes\n")
        job = self.run_batch()
        self.assertEqual(job["counts"],{"failed":1})
        self.assertEqual(self.client.calls,0)
        self.assertEqual(intake.get_item(self.root,self.id)["status"],"review")

    def test_instructions_or_claims_outside_schema_are_not_actions(self):
        old = self.client.review
        def unsafe(packet):
            review,digest = old(packet)
            review["recommendation"]="publish"
            return review,digest
        self.client.review = unsafe
        self.assertEqual(self.run_batch()["counts"],{"failed":1})
        self.assertEqual(intake.get_item(self.root,self.id)["status"],"review")

    def test_evidence_quotes_must_match_the_referenced_source(self):
        packet = ai.packet_for(self.root,intake.get_item(self.root,self.id))
        review,_ = self.client.review(packet)
        review["evidence"][0]["quote"]="Invented field observation"
        with self.assertRaisesRegex(ValueError,"QUOTE_INVALID"):
            ai.validate_output(review,packet)

    def test_manual_review_during_inference_is_never_overwritten(self):
        def human(packet):
            item = intake.get_item(self.root,self.id)
            intake_review.save(self.root,{"id":self.id,"sha256":item["sha256"],"revision":0,
                "decision":"local","domain":"hydrology","rights":"unknown","sensitivity":"unknown",
                "reference":"","reviewer":"Human reviewer","note":"Human checked the local source.","confirmed":True},intake_route.load_budget())
        self.client.before = human
        self.run_batch()
        self.assertEqual(intake.get_item(self.root,self.id)["review_history"][0]["reviewer"],"Human reviewer")

    def test_provider_failure_pauses_without_changing_review(self):
        self.client.before = lambda packet:(_ for _ in ()).throw(ai.ProviderError("LOCAL_QWEN_UNAVAILABLE_OR_INVALID"))
        self.assertEqual(self.run_batch()["state"],"paused")
        self.assertEqual(intake.get_item(self.root,self.id)["status"],"review")
        self.client.before = lambda packet:None
        self.manager.control("resume");self.manager.thread.join(10)
        self.assertEqual(self.manager.status()["job"]["counts"],{"accepted":1})

    def test_pause_after_current_file_and_resume_keeps_progress(self):
        (self.root/"data/raw/hydrology2.csv").write_text("station,river_level_m\nQA,3.1\n")
        intake.analyze(self.root)
        started,release = threading.Event(),threading.Event()
        self.client.before = lambda packet:(started.set(),release.wait(5))
        self.manager.start(self.request());self.assertTrue(started.wait(5))
        self.manager.control("pause");release.set();self.manager.thread.join(10)
        job = self.manager.status()["job"]
        self.assertEqual(job["state"],"paused")
        self.assertEqual(job["counts"],{"accepted":1,"pending":1})
        self.client.before = lambda packet:None
        self.manager.control("resume");self.manager.thread.join(10)
        self.assertEqual(self.manager.status()["job"]["counts"],{"accepted":2})

    def test_busy_writer_resumes_saved_draft_without_second_model_call(self):
        held = []
        def lock_writer(packet):
            lock = intake.writer_lock(self.root);lock.__enter__();held.append(lock)
        self.client.before = lock_writer
        self.assertEqual(self.run_batch()["state"],"paused")
        held[0].__exit__(None,None,None)
        self.client.before = lambda packet:None
        self.manager.control("resume");self.manager.thread.join(10)
        self.assertEqual(self.client.calls,1)
        self.assertEqual(self.manager.status()["job"]["counts"],{"accepted":1})

    def test_recovery_after_acceptance_before_task_commit_does_not_duplicate_review(self):
        with patch.object(self.manager,"launch",side_effect=lambda job,fd:__import__('os').close(fd)):
            self.manager.start(self.request())
        job = self.manager.status()["job"]
        with self.manager.db() as db:
            task = db.execute("SELECT job,seq,item,sha,context,cache_key FROM ai_acceptance_tasks WHERE job=?",(job["id"],)).fetchone()
            db.execute("UPDATE ai_acceptance_tasks SET state='working' WHERE job=?",(job["id"],))
        self.manager.process(job,task)
        restarted = ai.Manager(self.root,self.client)
        self.assertEqual(restarted.status()["job"]["state"],"paused")
        restarted.control("resume");restarted.thread.join(10)
        self.assertEqual(restarted.status()["job"]["counts"],{"accepted":1})
        self.assertEqual(self.client.calls,1)
        self.assertEqual(len(intake.get_item(self.root,self.id)["review_history"]),1)

    def test_selection_snapshots_all_pages_without_a_500_file_cap(self):
        for n in range(500):
            (self.root/f'data/raw/hydrology-{n:04d}.csv').write_text("station,value\nQA,1\n")
        intake.analyze(self.root)
        with patch.object(self.manager,"launch",side_effect=lambda job,fd:__import__('os').close(fd)):
            self.manager.start(self.request(limit=0))
        self.assertEqual(self.manager.status()["job"]["total"],501)

    def test_invalid_filters_limits_and_admin_cannot_start(self):
        for patches in ({"admin":""},{"admin":"a\nb"},{"limit":True},{"limit":-1},{"filters":{"path":"/etc/passwd"}}, {"filters":{"bbox":[0,0,float('nan'),1]}}):
            with self.assertRaises(ValueError): self.manager.start(self.request(**patches))

    def test_fixed_local_endpoint_rejects_unpinned_models(self):
        with self.assertRaises(ValueError): ai.Qwen("other-model","a"*64)
        with self.assertRaises(ValueError): ai.Qwen("qwen3.5:4b","bad-digest")
        with self.assertRaises(ai.ProviderError): ai.NoRedirect().redirect_request(None,None,None,None,None,None)

    def test_qwen_selects_evidence_ids_and_server_supplies_exact_fact_text(self):
        packet=ai.packet_for(self.root,intake.get_item(self.root,self.id))
        value,_=self.client.review(packet);value['evidence']=['format']
        client=ai.Qwen(self.client.model,self.client.digest)
        replies=[{'models':[{'name':client.model,'digest':client.digest}]},
                 {'model':client.model,'done':True,'message':{'content':json.dumps(value)}}]
        with patch.object(client,'call',side_effect=replies) as call:
            result,_=client.review(packet)
        self.assertEqual(result['evidence'],[{'source':'format','quote':packet['facts'][1]['text'][:500]}])
        self.assertIn('format',call.call_args_list[1].args[1]['format']['properties']['evidence']['items']['enum'])

    def test_orphaned_job_recovers_without_a_service_restart(self):
        with patch.object(self.manager,'launch',side_effect=lambda job,fd:os.close(fd)):
            self.manager.start(self.request())
        with self.manager.db() as db:
            db.execute("UPDATE ai_acceptance_jobs SET state='running'")
            db.execute("UPDATE ai_acceptance_tasks SET state='working'")
        job=self.manager.status()['job']
        self.assertEqual(job['state'],'paused')
        self.assertEqual(job['counts'],{'pending':1})


if __name__ == '__main__':
    unittest.main()
