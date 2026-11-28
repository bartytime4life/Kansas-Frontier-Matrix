"""The unified origin preserves native desk permissions and private sessions."""
from email.message import Message
import io
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock

from tools.local_data import intake, manage
from tools.local_data.intake_studio.intake_server import Store, Handler
from tools.local_data.intake_studio.workspace import Workspace, page, asset
from tools.local_data.intake_studio.accounts import Accounts
from tests.local_data.studio_auth import signed_in_headers


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        for name in ("working", "library"):
            root = self.base / name
            manage.init_store(root)
            (root / "data/raw/sample.csv").write_text("name,latitude,longitude\nsynthetic,38.5,-98.5\n")
            intake.analyze(root)
        self.store = Store(self.base / "studio", self.base / "runtime", kfm_root=self.base / "working",
                           library_root=self.base / "library")
        self.server = SimpleNamespace(origin="http://127.0.0.1:18776", token="synthetic-session", store=self.store)
        self.server.workspace = Workspace(self.store, 18776, self.server.token)
        self.server.accounts = Accounts(self.store.root)
        self.account_headers = signed_in_headers(self, self.server.accounts)

    def request(self, path, *, method="GET", headers=None, body=None):
        h = Handler.__new__(Handler)
        h.path = path
        h.client_address = ("127.0.0.1", 32123)
        h.headers = Message()
        data = json.dumps(body or {}).encode()
        for key, value in {"Host": "127.0.0.1:18776", "Content-Length": str(len(data)),
                           "Content-Type": "application/json", **(headers or {})}.items():
            h.headers[key] = value
        h.rfile, h.wfile = io.BytesIO(data), io.BytesIO()
        h.connection = SimpleNamespace(settimeout=Mock())
        h.server = self.server
        h.close_connection = True
        result = {}
        h.send_response = lambda code: result.update(code=code)
        h.send_header = lambda key, value: result.setdefault('headers', {}).update({key:value})
        h.end_headers = lambda: None
        getattr(h, "do_" + method)()
        return result["code"], h.wfile.getvalue(), result.get("headers", {})

    @property
    def auth(self):
        return {**self.account_headers, "Origin": self.server.origin}

    def test_configured_studio_resumes_with_the_same_smart_worker_policy(self):
        from tools.local_data.smart_intake import SmartManager
        self.store.qwen_model='qwen3.5:test';self.store.qwen_digest='a'*64
        self.store.automation_config=self.base/'smart-intake.json'
        self.store.automation_config.write_text(json.dumps({'model':self.store.qwen_model,'model_digest':self.store.qwen_digest,'owner_policy':None}))
        workspace=Workspace(self.store,18776,self.server.token)
        self.assertIsInstance(workspace.ai,SmartManager)

    def test_studio_refuses_a_different_automation_model_pin(self):
        self.store.qwen_model='qwen3.5:test';self.store.qwen_digest='a'*64
        self.store.automation_config=self.base/'smart-intake.json'
        self.store.automation_config.write_text(json.dumps({'model':self.store.qwen_model,'model_digest':'b'*64}))
        with self.assertRaisesRegex(ValueError,'AI_AUTOMATION_MODEL_PIN_MISMATCH'):
            Workspace(self.store,18776,self.server.token)

    def test_preparation_is_visible_but_maintenance_still_blocks_acceptance(self):
        from tools.local_data.review_cache import CachedQwen
        self.store.qwen_model='qwen3.5:test';self.store.qwen_digest='a'*64
        self.store.automation_config=self.base/'smart-intake.json'
        maintenance=self.base/'maintenance';maintenance.mkdir();(maintenance/'phase.json').write_text(json.dumps({'phase':'verifying'}))
        preparation=self.base/'preparation.json';preparation.write_text(json.dumps({'state':'preparing','prepared':3,'cached':2}))
        self.store.automation_config.write_text(json.dumps({'model':self.store.qwen_model,'model_digest':self.store.qwen_digest,
            'preparation_cache':str(self.base/'cache.sqlite'),'preparation_status':str(preparation),
            'maintenance_directory':str(maintenance)}))
        workspace=Workspace(self.store,18776,self.server.token)
        self.assertIsInstance(workspace.ai.client,CachedQwen)
        self.assertTrue(workspace.ai.status()['maintenance'])
        self.assertEqual(workspace.ai.status()['preparation']['prepared'],3)

    def test_shared_shell_navigation_uses_one_origin_without_frames(self):
        for route, active in (("/working-data", "working-nav"), ("/library", "library-nav")):
            code, body, headers = self.request(route, headers=self.auth)
            self.assertEqual(code, 200)
            text = body.decode()
            self.assertIn('href="/working-data"', text)
            self.assertIn('href="/library"', text)
            self.assertIn('aria-current="page" id="' + active + '"', text)
            self.assertNotIn('<iframe', text)
            self.assertNotIn(self.server.token, text)
            self.assertEqual(headers['Content-Type'], 'text/html')

    def test_workspace_data_require_session_host_and_origin(self):
        for route in ("/api/workspace/working/overview", "/api/workspace/library/items?limit=1"):
            self.assertEqual(self.request(route)[0], 401)
            self.assertEqual(self.request(route, headers={"X-KFM-Session": self.server.token})[0], 401)
            for bad in ({**self.auth,"X-KFM-CSRF":"wrong"}, {**self.auth,"Host":"example.org"},
                        {**self.auth,"Origin":"https://example.org"}):
                self.assertEqual(self.request(route, headers=bad)[0], 403)
            self.assertEqual(self.request(route, headers=self.auth)[0], 200)

    def test_working_and_library_keep_distinct_permissions(self):
        for name, writable in (("working", True), ("library", False)):
            code, body, _ = self.request('/api/workspace/' + name + '/status', headers=self.auth)
            self.assertEqual(code, 200)
            status = json.loads(body)
            self.assertEqual(status['analysisAllowed'], writable)
            self.assertEqual(status['reviewAllowed'], writable)
            self.assertEqual(status['catalogBrowsingAllowed'], not writable)
        for endpoint in ('analyze','apply','review'):
            self.assertEqual(self.request('/api/workspace/library/' + endpoint, method='POST', headers=self.auth)[0], 403)

    def test_readonly_catalog_is_unchanged_by_browsing_and_rejected_writes(self):
        path = self.base / 'library/data/work/intake/index.sqlite'
        before = path.read_bytes()
        for route in ('overview','items?limit=1','extents','release-plan'):
            self.assertEqual(self.request('/api/workspace/library/'+route, headers=self.auth)[0], 200)
        self.request('/api/workspace/library/analyze', method='POST', headers=self.auth)
        self.assertEqual(path.read_bytes(), before)

    def test_item_details_and_filters_use_native_queries(self):
        code, body, _ = self.request('/api/workspace/working/items?text=sample&limit=1', headers=self.auth)
        item = json.loads(body)['items'][0]
        self.assertEqual(code, 200)
        code, body, _ = self.request('/api/workspace/working/items/'+item['id'], headers=self.auth)
        self.assertEqual(code, 200)
        self.assertEqual(json.loads(body)['sha256'], item['sha256'])

    def test_workspace_does_not_add_arbitrary_file_or_api_routes(self):
        for route in ('/api/workspace/other/overview', '/api/workspace/working/not-a-route'):
            self.assertEqual(self.request(route, headers=self.auth)[0], 404)
        for route in ('/workspace/../../intake_server.py', '/api/workspace/working/../../files'):
            self.assertEqual(self.request(route, headers=self.auth)[0], 400)

    def test_revoked_account_cannot_read_workspace(self):
        route = '/api/workspace/working/overview'
        self.assertEqual(self.request(route, headers=self.auth)[0], 200)
        token = self.account_headers['Cookie'].split('=', 1)[1]
        self.server.accounts.logout(token)
        self.assertEqual(self.request(route, headers=self.auth)[0], 401)

    def test_native_assets_are_scoped_and_explicit(self):
        css, mime = asset('/workspace/desk.css')
        self.assertEqual(mime, 'text/css')
        self.assertIn('@scope (.data-workspace)', css)
        self.assertNotIn(':root', css)
        self.assertIn('class="data-workspace"', page('working'))
        with self.assertRaises(KeyError):
            asset('/workspace/other.js')

    def test_unconfigured_view_reports_unavailable(self):
        self.server.workspace.handlers.pop('library')
        self.assertEqual(self.request('/api/workspace/library/status', headers=self.auth)[0], 503)

    def test_inbox_configuration_rejects_missing_or_nested_directories(self):
        for inbox in (self.base / 'not-present', self.base / 'working/data/raw', self.base):
            self.store.inbox = inbox
            with self.assertRaisesRegex(ValueError, 'INBOX_MUST_BE_SEPARATE'):
                Workspace(self.store, 18776, self.server.token)

    def test_post_refuses_missing_data_volume_before_mutation(self):
        self.store.store_check = self.base / 'missing-check.py'
        code, body, _ = self.request('/api/workspace/working/analyze', method='POST', headers=self.auth)
        self.assertEqual(code, 409)
        self.assertIn('data volume', json.loads(body)['error'])

    def test_handoff_link_stays_inside_workspace_and_targets_the_item(self):
        self.assertEqual(self.store.working_url(), '/working-data')
        self.assertEqual(self.store.working_url('a'*32), '/working-data?item='+'a'*32)
        self.assertEqual(self.store.working_url('https://example.org'), '/working-data')

    def ai_manager(self):
        from tools.local_data.ai_acceptance import Manager
        from tests.local_data.test_ai_acceptance import FakeQwen
        self.server.workspace.ai = Manager(self.base/'working',FakeQwen())
        def finish():
            manager = self.server.workspace.ai
            if manager.thread:
                manager.stop.set();manager.thread.join(5)
        self.addCleanup(finish)
        return self.server.workspace.ai

    def test_ai_endpoints_need_session_and_exact_origin_and_refuse_library(self):
        self.ai_manager()
        route='/api/workspace/working/ai-review/start'
        value={'admin':'QA admin','filters':{},'limit':1,'retryHeld':False}
        self.assertEqual(self.request(route,method='POST',body=value)[0],403)
        self.assertEqual(self.request(route,method='POST',body=value,headers={'X-KFM-Session':self.server.token})[0],403)
        self.assertEqual(self.request('/api/workspace/library/ai-review/start',method='POST',body=value,headers=self.auth)[0],403)
        self.assertIsNone(self.server.workspace.ai.status()['job'])

    def test_ai_batch_is_explicit_and_cannot_request_public_acceptance(self):
        manager=self.ai_manager()
        route='/api/workspace/working/ai-review/start'
        value={'admin':'QA admin','filters':{},'limit':1,'retryHeld':False}
        self.assertEqual(self.request(route,method='POST',body={**value,'decision':'public'},headers=self.auth)[0],400)
        self.assertEqual(manager.client.calls,0)
        self.assertEqual(self.request(route,method='POST',body=value,headers=self.auth)[0],200)
        manager.thread.join(5)
        self.assertEqual(manager.status()['job']['counts'],{'accepted':1})

    def test_unconfigured_ai_is_reported_without_starting_a_model(self):
        code,body,_=self.request('/api/workspace/working/ai-review/status',headers=self.auth)
        self.assertEqual(code,200)
        self.assertFalse(json.loads(body)['enabled'])
        self.assertEqual(self.request('/api/workspace/working/ai-review/start',method='POST',headers=self.auth)[0],403)


if __name__ == '__main__':
    unittest.main()
