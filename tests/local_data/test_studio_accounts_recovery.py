"""Synthetic account/recovery tests. Reduced KDF cost is test-only; see real-cost test."""
import copy
from email.message import Message
import http.client
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
import json
import os
from pathlib import Path
import sqlite3
import tempfile
import threading
import unittest
from unittest.mock import patch

from tools.local_data.intake_studio import accounts as a
from tools.local_data.intake_studio.recovery import RecoveryStore
from tools.local_data.intake_studio.studio_access import secure_server_class,COOKIE

PASS='Synthetic passphrase 82! only'
NEW='Another synthetic phrase 41!'


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name);self.root.chmod(0o700)
        # Never a supported runtime configuration. Only unit fixtures use this patch.
        self.patch=patch.dict(a.KDF,{'n':1024,'r':8,'p':1});self.patch.start();self.addCleanup(self.patch.stop)
        self.now=[1_800_000_000.0]
        self.acc=a.Accounts(self.root,clock=lambda:self.now[0])
        self.acc.bootstrap(self.acc.issue_setup_code(),'owner',PASS)
        self.owner_token=self.acc.login('owner',PASS)
        self.owner=self.acc.session(self.owner_token)
    def create(self,name='tester',role='operator'):
        self.acc.manage(self.owner,{'action':'create','username':name,'password':PASS,'role':role,'currentPassword':PASS})
        t=self.acc.login(name,PASS); actor=self.acc.session(t)
        self.acc.change_password(actor,PASS,NEW)
        t=self.acc.login(name,NEW)
        return self.acc.session(t),t


class AccountTests(Base):
    def test_no_plaintext_password_or_raw_session_in_database(self):
        raw=self.acc.path.read_bytes()
        self.assertNotIn(PASS.encode(),raw);self.assertNotIn(self.owner_token.encode(),raw)
        self.assertEqual(self.acc.path.stat().st_mode&0o777,0o600)
    def test_owner_bootstrap_one_time(self):
        with self.assertRaisesRegex(a.AccessError,'OWNER_ALREADY_CONFIGURED'):self.acc.bootstrap('anything','second',PASS)
        with self.assertRaisesRegex(a.AccessError,'OWNER_ALREADY_CONFIGURED'):self.acc.issue_setup_code()
    def test_generic_login_failure(self):
        for name,secret in [('owner','wrong'),('missing',PASS)]:
            with self.assertRaisesRegex(a.AccessError,'INVALID_USERNAME_OR_PASSWORD'):self.acc.login(name,secret)
    def test_usernames_are_normalized(self):self.assertEqual(self.acc.session(self.acc.login('OWNER',PASS))['username'],'owner')
    def test_password_minimum(self):
        for p in ['short','x'*20,'1234567890123456','kansasfrontiermatrix']:
            with self.subTest(p=p),self.assertRaises(a.AccessError):a.password(p,'owner',True)
    def test_unicode_normalization(self):self.assertEqual(a.password('e\u0301'+'X'*14),a.password('é'+'X'*14))
    def test_password_maximum_and_null(self):
        for p in ['a'*129,'hello\x00world',None]:
            with self.assertRaises(a.AccessError):a.password(p)
    def test_sessions_expire_idle(self):
        self.now[0]+=a.IDLE_SECONDS+1;self.assertIsNone(self.acc.session(self.owner_token))
    def test_sessions_expire_absolute_despite_activity(self):
        for _ in range(17):self.now[0]+=1700;result=self.acc.session(self.owner_token)
        self.assertIsNone(result)
    def test_restart_invalidates_browser_sessions(self):self.assertIsNone(a.Accounts(self.root,clock=lambda:self.now[0]).session(self.owner_token))
    def test_csrf_is_not_session_secret(self):self.assertNotEqual(self.owner['csrf'],self.owner_token)
    def test_invalid_session_syntax(self):
        for t in ['',None,'x'*400,'../secret']:self.assertIsNone(self.acc.session(t))
    def test_logout_revokes(self):self.acc.logout(self.owner_token);self.assertIsNone(self.acc.session(self.owner_token))
    def test_temporary_password_blocks_until_changed(self):
        self.acc.manage(self.owner,{'action':'create','username':'newuser','password':PASS,'role':'viewer','currentPassword':PASS})
        t=self.acc.login('newuser',PASS);u=self.acc.session(t);self.assertTrue(u['mustChangePassword'])
        self.acc.change_password(u,PASS,NEW);self.assertIsNone(self.acc.session(t))
        self.assertFalse(self.acc.session(self.acc.login('newuser',NEW))['mustChangePassword'])
    def test_change_password_requires_current_password(self):
        with self.assertRaisesRegex(a.AccessError,'CURRENT_PASSWORD_INCORRECT'):self.acc.change_password(self.owner,'wrong',NEW)
    def test_password_change_revokes_all_sessions(self):
        other=self.acc.login('owner',PASS);self.acc.change_password(self.owner,PASS,NEW)
        self.assertIsNone(self.acc.session(other));self.assertIsNone(self.acc.session(self.owner_token))
    def test_password_reuse_rejected(self):
        with self.assertRaisesRegex(a.AccessError,'CHOOSE_A_NEW'):self.acc.change_password(self.owner,PASS,PASS)
    def test_disabled_user_cannot_login(self):
        actor,t=self.create();self.acc.manage(self.owner,{'action':'update','username':'tester','enabled':False,'currentPassword':PASS})
        self.assertIsNone(self.acc.session(t))
        with self.assertRaisesRegex(a.AccessError,'INVALID_USERNAME_OR_PASSWORD'):self.acc.login('tester',NEW)
    def test_role_change_revokes_sessions(self):
        actor,t=self.create();self.acc.manage(self.owner,{'action':'update','username':'tester','role':'viewer','currentPassword':PASS});self.assertIsNone(self.acc.session(t))
    def test_reset_is_temporary_and_revokes(self):
        actor,t=self.create();self.acc.manage(self.owner,{'action':'reset','username':'tester','password':PASS,'currentPassword':PASS})
        self.assertIsNone(self.acc.session(t));self.assertTrue(self.acc.session(self.acc.login('tester',PASS))['mustChangePassword'])
    def test_last_owner_cannot_be_disabled_demoted_or_reset(self):
        for changes in [{'action':'update','enabled':False},{'action':'update','role':'viewer'},{'action':'reset','password':NEW}]:
            with self.assertRaisesRegex(a.AccessError,'LAST_ACTIVE_ADMIN'):self.acc.manage(self.owner,{'username':'owner','currentPassword':PASS,**changes})
    def test_temporary_admin_does_not_justify_disabling_last_owner(self):
        self.acc.manage(self.owner,{'action':'create','username':'second','password':PASS,'role':'admin','currentPassword':PASS})
        with self.assertRaisesRegex(a.AccessError,'LAST_ACTIVE_ADMIN'):self.acc.manage(self.owner,{'action':'update','username':'owner','role':'viewer','currentPassword':PASS})
    def test_operator_cannot_manage_accounts(self):
        actor,_=self.create()
        with self.assertRaisesRegex(a.AccessError,'ADMIN_REQUIRED'):self.acc.manage(actor,{'action':'create','username':'third','role':'admin','password':PASS,'currentPassword':NEW})
    def test_current_admin_password_required(self):
        with self.assertRaisesRegex(a.AccessError,'CURRENT_PASSWORD_INCORRECT'):self.acc.manage(self.owner,{'action':'create','username':'third','role':'admin','password':PASS,'currentPassword':'wrong'})
    def test_no_password_material_in_admin_listing_or_audit(self):
        text=json.dumps(self.acc.users(self.owner))+json.dumps(self.acc.audit(self.owner))
        for s in [PASS,self.owner_token,'password_hash','scrypt-v1']:self.assertNotIn(s,text)
    def test_failures_throttle_and_persist(self):
        for _ in range(5):
            with self.assertRaises(a.AccessError):self.acc.login('owner','wrong')
        with self.assertRaisesRegex(a.AccessError,'SIGN_IN_TEMPORARILY_LIMITED'):self.acc.login('owner',PASS)
        other=a.Accounts(self.root,clock=lambda:self.now[0])
        with self.assertRaisesRegex(a.AccessError,'SIGN_IN_TEMPORARILY_LIMITED'):other.login('owner',PASS)
        self.now[0]+=31;self.assertIsNotNone(self.acc.login('owner',PASS))
    def test_missing_database_does_not_reopen_signup(self):
        self.acc.path.unlink()
        with self.assertRaisesRegex(a.AccessError,'ACCOUNT_DATABASE_MISSING'):a.Accounts(self.root)
    def test_wrong_database_identity_denied(self):
        self.acc.marker.write_text('wrong')
        with self.assertRaisesRegex(a.AccessError,'ACCOUNT_DATABASE_IDENTITY_MISMATCH'):a.Accounts(self.root)
    def test_unsafe_permissions_refused(self):
        self.acc.path.chmod(0o644)
        with self.assertRaisesRegex(a.AccessError,'UNSAFE_ACCOUNT_STORAGE'):self.acc.initialized()
    def test_symlink_refused(self):
        target=self.root/'safe';self.acc.path.rename(target);self.acc.path.symlink_to(target)
        with self.assertRaisesRegex(a.AccessError,'UNSAFE_ACCOUNT_STORAGE'):a.Accounts(self.root)
    def test_local_break_glass_resets_existing_admin_only(self):
        self.acc.local_reset('owner',NEW);self.assertIsNone(self.acc.session(self.owner_token))
        self.assertTrue(self.acc.login('owner',NEW))
        with self.assertRaises(a.AccessError):self.acc.local_reset('missing',NEW)
    def test_setup_code_expires_and_bad_codes_limited(self):
        with tempfile.TemporaryDirectory() as d:
            acc=a.Accounts(d,clock=lambda:self.now[0]);code=acc.issue_setup_code();self.now[0]+=601
            with self.assertRaisesRegex(a.AccessError,'SETUP_CODE_INVALID'):acc.bootstrap(code,'owner',PASS)
            for _ in range(4):
                with self.assertRaises(a.AccessError):acc.bootstrap('wrong','owner',PASS)
            with self.assertRaisesRegex(a.AccessError,'SIGN_IN_TEMPORARILY_LIMITED'):acc.bootstrap('wrong','owner',PASS)
    def test_account_count_limit(self):
        with patch.object(a,'MAX_USERS',1),self.assertRaisesRegex(a.AccessError,'ACCOUNT_LIMIT'):self.acc.manage(self.owner,{'action':'create','username':'third','role':'viewer','password':PASS,'currentPassword':PASS})


class ProductionKDFTest(unittest.TestCase):
    def test_real_production_scrypt_roundtrip(self):
        self.assertEqual((a.KDF['n'],a.KDF['r'],a.KDF['p']),(2**17,8,1))
        encoded=a.hash_password(PASS)
        self.assertTrue(a.verify_password(PASS,encoded));self.assertFalse(a.verify_password(NEW,encoded))


def storage_record():
    return {'kind':'storage','requestId':'storage-1','observedAt':'2026-11-15T21:00:00Z','notes':'Synthetic fixtures; not actual drives.',
            'devices':{role:{'serial':role+'-serial','uuid':role+'-uuid','filesystem':'ext4','mountpoint':'/fixtures/'+role,'totalBytes':1000,'freeBytes':400,'floorBytes':200} for role in ['source','backup']}}

def check_record(**kw):
    return {'kind':'observation','requestId':'check-1','observedAt':'2026-11-15T21:01:00Z','storageRevision':1,'gate':'device_identity','result':'HOLD','steps':'Read fixture','expected':'Match identity','observed':'Review pending','evidence':'fixture record','risk':'Synthetic only',**kw}

def review_record(**kw):
    return {'kind':'review','requestId':'review-1','observedAt':'2026-11-15T21:02:00Z','observation':2,'decision':'ACCEPT_EVIDENCE','reason':'Synthetic evidence only',**kw}


class RecoveryTests(Base):
    def setUp(self):super().setUp();self.store=RecoveryStore(self.root)
    def test_empty_read_creates_nothing(self):
        before=set(self.root.iterdir());state=self.store.snapshot();self.assertEqual(before,set(self.root.iterdir()));self.assertEqual(len(state['gates']),7)
    def test_initial_roles_do_not_claim_drive_identity(self):
        s=self.store.snapshot();self.assertIsNone(s['storage']);self.assertEqual(s['operationalDecision'],'HOLD');self.assertFalse(any(s['authority'].values()))
    def test_storage_observation_review(self):
        self.store.append(self.owner,storage_record());self.store.append(self.owner,check_record(result='PASS'));self.store.append(self.owner,review_record())
        state=self.store.snapshot();self.assertEqual(state['gates'][0]['status'],'REVIEWED_EVIDENCE');self.assertEqual(state['operationalDecision'],'HOLD')
    def test_actor_is_bound_to_authenticated_identity(self):
        x=storage_record();x['actor']='pretend-owner'
        with self.assertRaisesRegex(a.AccessError,'UNKNOWN_STORAGE_FIELDS'):self.store.append(self.owner,x)
    def test_duplicate_idempotent(self):
        self.store.append(self.owner,storage_record());self.assertTrue(self.store.append(self.owner,storage_record())['duplicate']);self.assertEqual(len(self.store.snapshot()['events']),1)
    def test_conflicting_request_id_refused(self):
        self.store.append(self.owner,storage_record());x=storage_record();x['notes']='different'
        with self.assertRaisesRegex(a.AccessError,'REQUEST_ID_CONFLICT'):self.store.append(self.owner,x)
    def test_same_physical_identity_rejected(self):
        for key in ['serial','uuid','mountpoint']:
            x=storage_record();x['devices']['backup'][key]=x['devices']['source'][key]
            with self.assertRaisesRegex(a.AccessError,'BACKUP_MUST_BE_DISTINCT'):self.store.append(self.owner,x)
    def test_negative_capacity_rejected(self):
        x=storage_record();x['devices']['source']['freeBytes']=-1
        with self.assertRaisesRegex(a.AccessError,'INVALID_CAPACITY'):self.store.append(self.owner,x)
    def test_storage_change_invalidates_old_checks(self):
        self.store.append(self.owner,storage_record());self.store.append(self.owner,check_record(result='PASS'));self.store.append(self.owner,review_record())
        x=storage_record();x['requestId']='storage-2';x['devices']['source']['uuid']='new-uuid';self.store.append(self.owner,x)
        self.assertEqual(self.store.snapshot()['gates'][0]['status'],'UNVERIFIED')
        with self.assertRaisesRegex(a.AccessError,'STORAGE_CHANGED'):self.store.append(self.owner,check_record(requestId='new-check'))
    def test_old_pass_cannot_be_accepted_after_new_failure(self):
        self.store.append(self.owner,storage_record());self.store.append(self.owner,check_record(result='PASS'));self.store.append(self.owner,check_record(requestId='check2',result='FAIL',retestOf=2))
        with self.assertRaisesRegex(a.AccessError,'SUPERSEDED_OBSERVATION'):self.store.append(self.owner,review_record())
    def test_nonpass_not_accepted(self):
        self.store.append(self.owner,storage_record());self.store.append(self.owner,check_record())
        with self.assertRaisesRegex(a.AccessError,'CURRENT_PASS_EVIDENCE_REQUIRED'):self.store.append(self.owner,review_record())
    def test_pass_requires_identity(self):
        x=storage_record();x['devices']['source']['serial']='';self.store.append(self.owner,x)
        with self.assertRaisesRegex(a.AccessError,'POSITIVE_DEVICE_IDENTITY_REQUIRED'):self.store.append(self.owner,check_record(result='PASS'))
    def test_pass_requires_evidence(self):
        self.store.append(self.owner,storage_record())
        with self.assertRaisesRegex(a.AccessError,'PASS_REQUIRES_EVIDENCE'):self.store.append(self.owner,check_record(result='PASS',evidence=''))
    def test_capacity_floor(self):
        x=storage_record();x['devices']['backup']['floorBytes']=500;self.store.append(self.owner,x)
        with self.assertRaisesRegex(a.AccessError,'CAPACITY_FLOOR_NOT_ESTABLISHED'):self.store.append(self.owner,check_record(gate='mount_capacity',result='PASS'))
    def test_operator_records_but_cannot_review_or_set_identity(self):
        operator,_=self.create();self.store.append(self.owner,storage_record());self.store.append(operator,check_record(result='PASS'))
        with self.assertRaisesRegex(a.AccessError,'ADMIN_REQUIRED'):self.store.append(operator,review_record())
        with self.assertRaisesRegex(a.AccessError,'ADMIN_REQUIRED'):self.store.append(operator,storage_record())
    def test_viewer_cannot_write(self):
        viewer,_=self.create(role='viewer')
        with self.assertRaisesRegex(a.AccessError,'OPERATOR_REQUIRED'):self.store.append(viewer,storage_record())
    def test_chain_corruption_detected(self):
        self.store.append(self.owner,storage_record())
        with sqlite3.connect(self.store.path) as db:db.execute("UPDATE events SET previous='bad'")
        with self.assertRaisesRegex(a.AccessError,'RECOVERY_CHAIN_INTEGRITY_FAILURE'):self.store.export()
    def test_deterministic_export_excludes_account_secrets(self):
        self.store.append(self.owner,storage_record());one=self.store.export();self.assertEqual(one,self.store.export());self.assertNotIn(PASS.encode(),one);self.assertNotIn(b'password_hash',one)
        envelope=json.loads(one);self.assertEqual(a.digest(__import__('tools.local_data.intake_studio.acceptance',fromlist=['canonical']).canonical(envelope['payload'])),envelope['digest'])
    def test_invalid_time_rejected(self):
        x=storage_record();x['observedAt']='2026-11-15'
        with self.assertRaises(a.AccessError):self.store.append(self.owner,x)
    def test_execution_request_has_no_api_model(self):
        x={'kind':'execute','requestId':'run-shell','observedAt':'2026-11-15T21:00:00Z','command':'true'}
        with self.assertRaisesRegex(a.AccessError,'UNKNOWN_RECOVERY_ACTION'):self.store.append(self.owner,x)
    def test_missing_first_storage_blocks_observations(self):
        with self.assertRaisesRegex(a.AccessError,'STORAGE_CHANGED'):self.store.append(self.owner,check_record())


# HTTP protocol harness uses the real gateway, account DB, and recovery DB.
# The legacy data response is deliberately a stub: not a full Studio E2E claim.
class LegacyHandler(BaseHTTPRequestHandler):
    def log_message(self,*args):pass
    def respond(self,code,body,kind='application/json',attachment=None):
        kind=(kind or 'application/octet-stream').replace('\r','').replace('\n','')
        if isinstance(body,(dict,list)):body=json.dumps(body).encode()
        if isinstance(body,str):body=body.encode()
        self.send_response(code);self.send_header('Content-Type',kind);self.send_header('Content-Length',str(len(body)));self.send_header('Cache-Control','no-store');self.end_headers();self.wfile.write(body)
    def do_GET(self):
        if self.path=='/api/session':return self.respond(200,{'token':self.server.token,'app':'kfm-local-intake-studio'})
        return self.respond(200,{'private':'sentinel','sessionHeader':self.headers.get('X-KFM-Session')})
    def do_POST(self):
        raw=self.rfile.read(int(self.headers.get('Content-Length','0')))
        return self.respond(200,{'legacy':True,'body':json.loads(raw) if raw else {},'sessionHeader':self.headers.get('X-KFM-Session')})
class LegacyServer(ThreadingHTTPServer):
    def __init__(self,port,store):
        self.store=store;self.token='internal-legacy-token';self.source_fingerprint='fixture'
        super().__init__(('127.0.0.1',port),LegacyHandler);self.origin='http://127.0.0.1:'+str(self.server_port)


@unittest.skipIf(os.environ.get("KFM_NO_NETWORK") == "1", "Loopback gateway checks run separately; preserve the repository no-network guard")
class GatewayTests(Base):
    def setUp(self):
        super().setUp()
        from types import SimpleNamespace
        Server=secure_server_class(LegacyServer,LegacyHandler)
        self.server=Server(0,SimpleNamespace(root=self.root,check_volume=lambda:None))
        self.thread=threading.Thread(target=self.server.serve_forever,daemon=True);self.thread.start()
        self.addCleanup(self.stop)
        self.acc=self.server.accounts
        self.owner_token=self.acc.login('owner',PASS);self.owner=self.acc.session(self.owner_token)
    def stop(self):self.server.shutdown();self.server.server_close();self.thread.join(2)
    def call(self,path,method='GET',body=None,auth=True,headers=None):
        h={}
        if auth:h={'Cookie':COOKIE+'='+self.owner_token,'X-KFM-CSRF':self.owner['csrf']}
        if method=='POST':h.update({'Origin':self.server.origin,'Content-Type':'application/json'})
        h.update(headers or {})
        raw=json.dumps(body).encode() if body is not None else None
        conn=http.client.HTTPConnection('127.0.0.1',self.server.server_port,timeout=5)
        conn.request(method,path,body=raw,headers=h);r=conn.getresponse();data=r.read();result=(r.status,dict(r.getheaders()),data);conn.close();return result
    def test_anonymous_health_has_no_data_or_token(self):
        status,h,body=self.call('/auth/health',auth=False);self.assertEqual(status,200);self.assertNotIn(b'token',body);self.assertNotIn(str(self.root).encode(),body)
    def test_all_private_data_requires_account(self):
        for path in ['/api/session','/api/files','/api/files/'+'a'*32+'/original','/api/workspace/working/overview','/api/workspace/acceptance/state','/api/recovery/state','/api/recovery/export','/auth/users','/auth/audit']:
            with self.subTest(path=path):self.assertEqual(self.call(path,auth=False)[0],401)
    def test_private_pages_redirect_anonymous(self):
        for path in ['/','/studio','/working-data','/library','/recovery','/users','/api/workspace/acceptance/page']:
            status,h,_=self.call(path,auth=False);self.assertEqual(status,303);self.assertEqual(h['Location'],'/sign-in')
    def test_signin_shell_and_assets_are_public_no_records(self):
        for path in ['/sign-in','/auth/ui.js','/auth/ui.css']:
            self.assertEqual(self.call(path,auth=False)[0],200)
    def test_signin_sets_httponly_strict_cookie(self):
        status,h,_=self.call('/auth/login','POST',{'username':'owner','password':PASS},auth=False)
        self.assertEqual(status,200);self.assertIn('HttpOnly',h['Set-Cookie']);self.assertIn('SameSite=Strict',h['Set-Cookie'])
    def test_wrong_origin(self):self.assertEqual(self.call('/auth/login','POST',{'username':'owner','password':PASS},auth=False,headers={'Origin':'https://evil.invalid'})[0],403)
    def test_missing_origin(self):
        conn=http.client.HTTPConnection('127.0.0.1',self.server.server_port,timeout=5);conn.request('POST','/auth/login',body=b'{}',headers={'Content-Type':'application/json'});r=conn.getresponse();self.assertEqual(r.status,403);r.read();conn.close()
    def test_forwarded_headers_rejected(self):self.assertEqual(self.call('/auth/health',auth=False,headers={'X-Forwarded-For':'192.0.2.1'})[0],403)
    def test_wrong_host_rejected(self):self.assertEqual(self.call('/auth/health',auth=False,headers={'Host':'evil.invalid'})[0],403)
    def test_cross_site_fetch_rejected(self):self.assertEqual(self.call('/auth/status',auth=False,headers={'Sec-Fetch-Site':'cross-site'})[0],403)
    def test_legacy_session_token_not_exposed(self):
        status,_,body=self.call('/api/session');self.assertEqual(status,200);data=json.loads(body);self.assertEqual(data['token'],self.owner['csrf']);self.assertNotIn(self.server.token,body.decode())
    def test_old_bearer_alone_does_not_authenticate(self):self.assertEqual(self.call('/api/files',auth=False,headers={'X-KFM-Token':self.server.token})[0],401)
    def test_wrong_csrf_rejected(self):self.assertEqual(self.call('/api/upload','POST',{},headers={'X-KFM-CSRF':'wrong'})[0],403)
    def test_multiple_csrf_headers_rejected(self):self.assertEqual(self.call('/api/upload','POST',{},headers={'X-KFM-Token':self.owner['csrf']})[0],403)
    def test_duplicate_session_cookie_rejected(self):self.assertEqual(self.call('/api/files',headers={'Cookie':COOKIE+'='+self.owner_token+'; '+COOKIE+'='+self.owner_token})[0],401)
    def test_per_session_token_compatibility(self):
        status,_,body=self.call('/api/files',headers={'X-KFM-CSRF':self.owner['csrf']});self.assertEqual(status,200);self.assertEqual(json.loads(body)['sessionHeader'],self.server.token)
        status,_,body=self.call('/api/files',auth=False,headers={'Cookie':COOKIE+'='+self.owner_token,'X-KFM-Session':self.owner['csrf']});self.assertEqual(json.loads(body)['sessionHeader'],self.server.token)
    def test_viewer_cannot_write_or_list_users(self):
        actor,t=self.create(role='viewer');self.owner,self.owner_token=actor,t
        self.assertEqual(self.call('/api/upload','POST',{})[0],403);self.assertEqual(self.call('/auth/users')[0],403)
    def test_operator_cannot_approve(self):
        actor,t=self.create();self.owner,self.owner_token=actor,t
        self.assertEqual(self.call('/api/workspace/acceptance/events','POST',{'kind':'review'})[0],403)
    def test_acceptance_actor_cannot_be_spoofed(self):
        status,_,body=self.call('/api/workspace/acceptance/events','POST',{'kind':'observation','actor':'fake'})
        self.assertEqual(status,200);self.assertEqual(json.loads(body)['body']['actor'],'owner')
    def test_unknown_mutation_denied(self):self.assertEqual(self.call('/api/restore','POST',{})[0],403)
    def test_password_reset_required_before_private_data(self):
        self.acc.manage(self.owner,{'action':'create','username':'temporary','password':PASS,'role':'viewer','currentPassword':PASS})
        self.owner_token=self.acc.login('temporary',PASS);self.owner=self.acc.session(self.owner_token)
        self.assertEqual(self.call('/api/recovery/state')[0],403);self.assertEqual(self.call('/auth/session')[0],200)
    def test_logout_revokes_cookie(self):
        status,h,_=self.call('/auth/logout','POST',{});self.assertEqual(status,200);self.assertIn('Max-Age=0',h['Set-Cookie']);self.assertEqual(self.call('/api/files')[0],401)
    def test_encoded_paths_rejected(self):self.assertEqual(self.call('/api/%66iles')[0],400)
    def test_recovery_export_is_private(self):self.assertEqual(self.call('/api/recovery/export')[0],200)
    def test_no_remote_password_reset(self):self.assertEqual(self.call('/auth/reset-admin','POST',{})[0],403)
    def test_session_reports_workspace_connection_without_paths(self):
        status,_,body=self.call('/auth/session');value=json.loads(body)
        self.assertEqual(status,200);self.assertEqual(value['workspace'],{'workingData':False,'library':False})
        self.assertNotIn(str(self.root).encode(),body)
        self.assertEqual(self.call('/auth/session',auth=False)[0],401)
    def test_public_status_returns_only_setup_state(self):self.assertEqual(json.loads(self.call('/auth/status',auth=False)[2]),{'setupRequired':False})
    def test_transfer_encoding_refused_before_legacy_upload(self):
        self.assertEqual(self.call('/api/upload','POST',{},headers={'Transfer-Encoding':'chunked'})[0],400)
    def test_legacy_upload_requires_single_length(self):
        conn=http.client.HTTPConnection('127.0.0.1',self.server.server_port,timeout=5)
        conn.putrequest('POST','/api/upload');conn.putheader('Origin',self.server.origin)
        conn.putheader('Cookie',COOKIE+'='+self.owner_token);conn.putheader('X-KFM-CSRF',self.owner['csrf'])
        conn.putheader('Content-Length','2');conn.putheader('Content-Length','2');conn.endheaders(b'{}')
        r=conn.getresponse();self.assertEqual(r.status,400);r.read();conn.close()
    def test_malformed_body_never_reaches_legacy(self):
        self.assertEqual(self.call('/auth/login','POST',{'username':'owner','password':PASS},auth=False,headers={'Content-Type':'text/plain'})[0],415)


if __name__=='__main__':unittest.main()
