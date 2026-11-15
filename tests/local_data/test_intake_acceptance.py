"""Synthetic evidence-ledger and request-dispatch tests; no providers or private files."""
import importlib.util
import io
import json
from pathlib import Path
import sqlite3
import tempfile
from types import SimpleNamespace, ModuleType
import unittest
from unittest.mock import patch

from tools.local_data.intake_studio import acceptance as a


def wrapped(payload):
    return {"algorithm": "SHA-256", "canonicalization": "test fixture",
            "digest": a.sha(a.canonical(payload)), "payload": payload}


def receipt(marker="fixture"):
    return wrapped({"schema": a.SCHEMA, "candidateSha": "a" * 40, "runId": marker,
                    "sourceInventory": [{"id": f"source-{i}", "title": f"Source {i}",
                         "category": "Test", "testCase": {"steps": ["Inspect"], "expected": ["Match"]}}
                        for i in range(59)],
                    "candidateEvidence": wrapped({"scope": "synthetic"}),
                    "downloadEvidence": wrapped({"results": [{"sourceId": f"source-{i}"} for i in range(13)]}),
                    "overallAcceptance": "VERIFIED"})  # Imported labels grant no local authority.


def observation(identity, **changes):
    value = {"kind": "observation", "receiptId": identity, "actor": "Synthetic observer",
             "observedAt": "2026-11-15T19:00:00Z", "sourceId": "source-0", "lane": "repository",
             "environment": "candidate", "result": "HOLD", "runId": "fixture-run-1",
             "steps": "Inspect exact revision", "expected": "Category matches",
             "observed": "Review pending"}
    value.update(changes)
    return value


def review(identity, observation_id="1", **changes):
    value = {"kind": "review", "receiptId": identity, "actor": "Synthetic reviewer",
             "observedAt": "2026-11-15T19:01:00Z", "observation": observation_id,
             "decision": "HOLD", "reason": "Await rendered evidence"}
    value.update(changes)
    return value


class ReceiptTests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(len(a.validate_receipt(a.canonical(receipt()))["payload"]["sourceInventory"]), 59)

    def test_payload_change_without_digest_rejected(self):
        value = receipt(); value["payload"]["candidateSha"] = "b" * 40
        with self.assertRaisesRegex(ValueError, "DIGEST_MISMATCH"):
            a.validate_receipt(a.canonical(value))

    def test_nested_digest_rejected(self):
        value = receipt()["payload"]; value["candidateEvidence"]["digest"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "DIGEST_MISMATCH"):
            a.validate_receipt(a.canonical(wrapped(value)))

    def test_duplicate_json_keys(self):
        with self.assertRaisesRegex(ValueError, "DUPLICATE_JSON_KEY"):
            a.decode(b'{"a":1,"a":2}')

    def test_nan_and_infinity(self):
        for raw in (b'{"a":NaN}', b'{"a":Infinity}', b'{"a":1e309}'):
            with self.subTest(raw=raw), self.assertRaises(ValueError): a.decode(raw)

    def test_empty_oversize_and_binary(self):
        for raw in (b'', b'a' * (a.MAX_BYTES + 1), b'\xff\xfe', b'PK\x03\x04'):
            with self.subTest(size=len(raw)), self.assertRaises(ValueError): a.validate_receipt(raw)

    def test_schema_and_revision(self):
        for changes in ({"schema":"unknown"}, {"candidateSha":"short"}, {"candidateSha":int("1" * 40)}):
            value = receipt()["payload"]; value.update(changes)
            with self.subTest(changes=changes), self.assertRaises(ValueError): a.validate_receipt(a.canonical(wrapped(value)))

    def test_source_inventory_unique_and_exact(self):
        for change in (lambda s:s.pop(), lambda s:s.append(s[0]), lambda s:s.__setitem__(1,s[0]), lambda s:s[0].update(id='../escape'), lambda s:s[0].update(id=123)):
            value=receipt()["payload"]; change(value["sourceInventory"])
            with self.subTest(change=change), self.assertRaises(ValueError): a.validate_receipt(a.canonical(wrapped(value)))

    def test_source_plan_shape(self):
        value = receipt()["payload"]; value["sourceInventory"][0]["testCase"]["steps"] = "not a list"
        with self.assertRaisesRegex(ValueError, "INVALID_SOURCE_CASE"): a.validate_receipt(a.canonical(wrapped(value)))

    def test_download_inventory(self):
        for change in (lambda s:s.pop(), lambda s:s.__setitem__(1,s[0]), lambda s:s[0].update(sourceId='missing')):
            value=receipt()["payload"]; downloads=value["downloadEvidence"]["payload"]; change(downloads["results"])
            value["downloadEvidence"]=wrapped(downloads)
            with self.subTest(change=change), self.assertRaises(ValueError): a.validate_receipt(a.canonical(wrapped(value)))

    def test_scriptlike_strings_are_data(self):
        value=receipt()["payload"]; value["sourceInventory"][0]["title"]='<script>alert(1)</script>'
        self.assertIn('<script>', a.validate_receipt(a.canonical(wrapped(value)))["payload"]["sourceInventory"][0]["title"])


class StoreTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name); self.store=a.EvidenceStore(self.root)
        self.raw=json.dumps(receipt(), ensure_ascii=False, indent=2).encode()
        self.id=self.store.import_receipt(self.raw)["id"]

    def test_original_bytes_preserved_and_duplicate_import(self):
        self.assertEqual(self.store.raw(self.id),self.raw)
        self.assertTrue(self.store.import_receipt(self.raw)["duplicate"])
        self.assertEqual(len(self.store.snapshot()["receipts"]),1)

    def test_imported_verified_label_never_promotes(self):
        state=self.store.snapshot(); self.assertEqual(state["overallAcceptance"],"HOLD")
        self.assertEqual(state["receipts"][0]["importStatus"],"UNREVIEWED")
        self.assertFalse(any(state["authority"].values()))
        self.assertEqual(state["events"],[])

    def test_deterministic_export_and_digest(self):
        before=self.store.export(); self.assertEqual(before,self.store.export())
        value=json.loads(before); self.assertEqual(a.sha(a.canonical(value["payload"])),value["digest"])

    def test_restart(self):
        self.store.append(observation(self.id))
        self.assertEqual(self.store.export(),a.EvidenceStore(self.root).export())

    def test_observation_review_retest_preserve_history(self):
        self.store.append(observation(self.id,result="PASS",evidence="fixture.txt sha256:recorded",buildIdentity="test build"))
        self.store.append(review(self.id,decision="ACCEPT_EVIDENCE"))
        self.store.append(review(self.id,decision="RETEST"))
        self.store.append(observation(self.id,runId="fixture-run-2",retestOf="1"))
        state=self.store.snapshot(); self.assertEqual(len(state["events"]),4)
        self.assertEqual(state["events"][0]["event"]["result"],"PASS")
        self.assertEqual(state["events"][3]["event"]["result"],"HOLD")
        self.assertEqual(state["overallAcceptance"],"HOLD")

    def test_observation_retry_is_idempotent(self):
        value=observation(self.id); first=self.store.append(value); again=self.store.append(value)
        self.assertTrue(again["duplicate"]); self.assertEqual(first["sequence"],again["sequence"])
        self.assertEqual(len(self.store.snapshot()["events"]),1)

    def test_run_id_conflict_rejected(self):
        self.store.append(observation(self.id))
        with self.assertRaisesRegex(ValueError,"RUN_ID_CONFLICT"):
            self.store.append(observation(self.id,observed="Different result"))

    def test_unknown_clearance_fields_denied(self):
        for field in ("sensitivityClearance","publication","sourceAdmission","reviewerApproval"):
            with self.subTest(field=field), self.assertRaisesRegex(ValueError,"UNKNOWN_OBSERVATION_FIELDS"):
                self.store.append(observation(self.id,**{field:True}))

    def test_pass_requires_evidence_and_build(self):
        for changes in ({"result":"PASS"},{"result":"PASS","evidence":"record"},{"result":"PASS","buildIdentity":"build"}):
            with self.subTest(changes=changes),self.assertRaisesRegex(ValueError,"PASS_EVIDENCE_REQUIRED"):
                self.store.append(observation(self.id,**changes))

    def test_rendered_pass_requires_revision_and_target_webgl(self):
        base={"result":"PASS","lane":"rendered_browser","evidence":"screenshot","buildIdentity":"build"}
        with self.assertRaisesRegex(ValueError,"PASS_REVISION_REQUIRED"): self.store.append(observation(self.id,**base))
        for webgl in ('unknown','unavailable','not_applicable',''):
            with self.subTest(webgl=webgl),self.assertRaisesRegex(ValueError,"RENDERED_BROWSER_EVIDENCE_REQUIRED"):
                self.store.append(observation(self.id,**base,revision='b'*40,browser='test browser',viewport='800x600',webgl2=webgl))
        self.store.append(observation(self.id,**base,revision='b'*40,browser='test browser',viewport='800x600',webgl2='available'))

    def test_hold_can_record_unknown_revision(self):
        self.store.append(observation(self.id,lane="rendered_browser",environment="public",webgl2="unavailable"))
        self.assertEqual(self.store.snapshot()["events"][0]["event"]["revision"],"")

    def test_invalid_scope_timestamp_and_source(self):
        for changes in ({"lane":"magic"},{"environment":"production-maybe"},{"result":"VERIFIED"},
                        {"sourceId":"unregistered"},{"revision":"abc"},{"observedAt":"2026-11-15T19:00:00"},
                        {"intakeFileId":"../escape"},{"runId":""},{"steps":""},{"actor":""}):
            with self.subTest(changes=changes),self.assertRaises(ValueError): self.store.append(observation(self.id,**changes))

    def test_intake_reference_never_edits_intake(self):
        intake_file=self.root/'sentinel.json'; intake_file.write_text('{"sensitivity":"held"}')
        before=intake_file.read_bytes()
        self.store.append(observation(self.id,intakeFileId='a'*32))
        self.assertEqual(intake_file.read_bytes(),before)

    def test_non_pass_cannot_be_accepted(self):
        self.store.append(observation(self.id))
        with self.assertRaisesRegex(ValueError,"ONLY_PASS_EVIDENCE_CAN_BE_ACCEPTED"):
            self.store.append(review(self.id,decision="ACCEPT_EVIDENCE"))

    def test_cross_receipt_reference_denied(self):
        self.store.append(observation(self.id))
        other=self.store.import_receipt(a.canonical(receipt('other')))["id"]
        with self.assertRaisesRegex(ValueError,"REFERENCE_NOT_IN_THIS_RECEIPT"):
            self.store.append(review(other))

    def test_retest_scope_mismatch_denied(self):
        self.store.append(observation(self.id))
        for changes in ({"environment":"public"},{"lane":"focused_tests"},{"sourceId":"source-1"}):
            with self.subTest(changes=changes),self.assertRaisesRegex(ValueError,"RETEST_SCOPE_MISMATCH"):
                self.store.append(observation(self.id,runId='next',retestOf='1',**changes))

    def test_review_cannot_point_at_review(self):
        self.store.append(observation(self.id));self.store.append(review(self.id))
        with self.assertRaisesRegex(ValueError,"OBSERVATION_REFERENCE_REQUIRED"):
            self.store.append(review(self.id,'2'))

    def test_receipt_corruption_refused(self):
        with sqlite3.connect(self.store.path) as db: db.execute('UPDATE receipts SET body=?',(b'{}',))
        with self.assertRaisesRegex(ValueError,"STORED_EVIDENCE_CORRUPT"):self.store.raw(self.id)
        with self.assertRaisesRegex(ValueError,"STORED_EVIDENCE_CORRUPT"):self.store.export()

    def test_orphaned_event_refused(self):
        self.store.append(observation(self.id))
        with sqlite3.connect(self.store.path) as db: db.execute("DELETE FROM receipts")
        with self.assertRaisesRegex(ValueError,"ORPHANED_EVIDENCE_EVENT"):self.store.snapshot()

    def test_event_chain_corruption_refused(self):
        self.store.append(observation(self.id))
        with sqlite3.connect(self.store.path) as db: db.execute("UPDATE events SET previous=?",('f'*64,))
        with self.assertRaisesRegex(ValueError,"LEDGER_INTEGRITY_FAILURE"):self.store.snapshot()
        with self.assertRaisesRegex(ValueError,"LEDGER_INTEGRITY_FAILURE"):self.store.append(observation(self.id,runId='next'))

    def test_quota_failure_is_atomic(self):
        before=self.store.export()
        with patch.object(a,'MAX_TOTAL_BYTES',len(self.raw)):
            with self.assertRaisesRegex(ValueError,"EVIDENCE_STORAGE_LIMIT"):self.store.append(observation(self.id))
        self.assertEqual(before,self.store.export())

    def test_receipt_and_event_count_limits(self):
        with patch.object(a,'MAX_RECEIPTS',1):
            with self.assertRaisesRegex(ValueError,"RECEIPT_COUNT_LIMIT"):self.store.import_receipt(a.canonical(receipt('next')))
        with patch.object(a,'MAX_EVENTS',0):
            with self.assertRaisesRegex(ValueError,"EVENT_COUNT_LIMIT"):self.store.append(observation(self.id))

    def test_read_does_not_initialize(self):
        with tempfile.TemporaryDirectory() as tmp:
            store=a.EvidenceStore(tmp);self.assertEqual(store.snapshot()["receipts"],[])
            self.assertEqual(list(Path(tmp).iterdir()),[])

    def test_symlink_storage_refused(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)/'acceptance.sqlite3';path.symlink_to(self.store.path)
            with self.assertRaisesRegex(ValueError,"UNSAFE_EVIDENCE_STORAGE"):a.EvidenceStore(tmp).snapshot()


class Request:
    def __init__(self,path,raw=b'',headers=None,allowed=True):
        self.path=path;self.rfile=io.BytesIO(raw);self.response=None;self.guards=[];self.allowed=allowed
        self.server=SimpleNamespace(origin='http://127.0.0.1:8777')
        self.connection=SimpleNamespace(settimeout=lambda _:None)
        self.headers={"Origin":self.server.origin,"Content-Type":"application/json","Content-Length":str(len(raw))}
        if headers:self.headers.update(headers)
    def guard(self,**kwargs):
        self.guards.append(kwargs)
        if not self.allowed:self.respond(403,{"error":"test guard denied"})
        return self.allowed
    def respond(self,*args):self.response=args;return args


class DispatchTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.store=SimpleNamespace(root=Path(self.tmp.name),check_volume=lambda:None)
    def call(self,suffix,method='GET',raw=b'',headers=None,allowed=True):
        r=Request(a.PREFIX+suffix,raw,headers,allowed);a.dispatch(r,method,self.store);return r
    def test_guard_denial(self):
        r=self.call('/state',allowed=False);self.assertEqual(r.response[0],403)
        self.assertEqual(list(self.store.root.iterdir()),[])
    def test_api_requires_workspace_session(self):
        r=self.call('/state');self.assertEqual(r.guards,[{"token":True,"header":"X-KFM-Session"}])
    def test_page_and_assets_use_existing_guard_without_token(self):
        for path in ('/page','/app.js','/style.css'):
            r=self.call(path);self.assertEqual(r.response[0],200);self.assertFalse(r.guards[0]['token'])
        self.assertIn('aria-current="page" id="acceptance-nav"',self.call('/page').response[1])
    def test_assets_reject_post(self):self.assertEqual(self.call('/app.js','POST',b'{}').response[0],405)
    def test_unknown_route_rejected(self):self.assertEqual(self.call('/publish','POST',b'{}').response[0],404)
    def test_wrong_and_missing_origin(self):
        for origin in ('https://external.example',None):
            self.assertEqual(self.call('/import','POST',a.canonical(receipt()),{'Origin':origin}).response[0],403)
    def test_mime_and_transfer_encoding(self):
        for headers in ({'Content-Type':'text/plain'},{'Transfer-Encoding':'chunked'}):
            self.assertEqual(self.call('/import','POST',a.canonical(receipt()),headers).response[0],415)
    def test_empty_and_oversized_requests(self):
        for length in ('0',str(a.MAX_BYTES+1)):
            self.assertEqual(self.call('/import','POST',b'{}',{'Content-Length':length}).response[0],413)
    def test_truncated_body(self):
        r=self.call('/import','POST',b'{}',{'Content-Length':'10'});self.assertEqual(r.response[1]['error'],'INTERRUPTED_EVIDENCE_REQUEST')
    def test_volume_failure_no_write(self):
        def fail():raise RuntimeError('VOLUME_NOT_VERIFIED')
        self.store.check_volume=fail
        r=self.call('/import','POST',a.canonical(receipt()));self.assertEqual(r.response[1]['error'],'VOLUME_NOT_VERIFIED')
        self.assertEqual(list(self.store.root.iterdir()),[])
    def test_import_state_original_and_export_routes(self):
        raw=a.canonical(receipt());r=self.call('/import','POST',raw);self.assertEqual(r.response[0],200)
        identity=r.response[1]['id'];self.assertEqual(self.call('/original/'+identity).response[1],raw)
        self.assertEqual(len(self.call('/state').response[1]['receipts']),1)
        self.assertEqual(self.call('/export').response[1],self.call('/export').response[1])
    def test_event_route(self):
        identity=self.call('/import','POST',a.canonical(receipt())).response[1]['id']
        r=self.call('/events','POST',a.canonical(observation(identity)));self.assertEqual(r.response[0],200)
    def test_failed_import_preserves_existing(self):
        self.call('/import','POST',a.canonical(receipt()));before=self.call('/export').response[1]
        self.assertEqual(self.call('/import','POST',b'{}').response[0],400)
        self.assertEqual(before,self.call('/export').response[1])
    def test_existing_workspace_dispatch_mount(self):
        # Execute the exact adapter, isolating unrelated Desk dependencies. This
        # is a dispatch harness, not a full Studio server or browser test.
        path=Path(a.__file__).with_name('workspace.py')
        spec=importlib.util.spec_from_file_location('acceptance_workspace_harness',path)
        module=importlib.util.module_from_spec(spec)
        stubs={name:ModuleType(name) for name in ('tools.local_data.intake','tools.local_data.intake_service')}
        with patch.dict('sys.modules',stubs):spec.loader.exec_module(module)
        workspace=module.Workspace.__new__(module.Workspace);workspace.store=self.store
        r=Request(a.PREFIX+'/state');workspace.dispatch(r,'GET');self.assertEqual(r.response[0],200)
    def test_client_uses_text_nodes_not_html_insertion(self):
        script=(a.WEB/'acceptance.js').read_text()
        for forbidden in ('innerHTML','outerHTML','insertAdjacentHTML','eval('):self.assertNotIn(forbidden,script)
        self.assertIn("fetch(root + path",script);self.assertIn("fetch('/api/session'",script)
        self.assertIn("previousId !== selectedId",script)
        self.assertIn("observation.reset(); review.reset();",script)


if __name__=='__main__':unittest.main()
