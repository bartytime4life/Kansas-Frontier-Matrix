"""Mandatory authentication gateway for the shared private Studio entrypoint.

Wraps established handlers without granting HTTP access to an OS shell, recovery
execution, credentials database, or public deployment. Only the sign-in shell
and minimal process health are anonymous.
"""
from __future__ import annotations
import io
import json
import re
import secrets
import sqlite3
from http.cookies import SimpleCookie, CookieError
from pathlib import Path
from urllib.parse import urlsplit
from .accounts import Accounts, AccessError, ABSOLUTE_SECONDS
from .recovery import RecoveryStore

WEB = Path(__file__).resolve().parent / 'local-web'
COOKIE = 'kfm_studio_session'
PUBLIC = {'/sign-in', '/auth/ui.js', '/auth/ui.css', '/auth/status', '/auth/health'}
PAGES = {'/studio', '/recovery', '/users', '/account/password'}
ASSETS = {'/auth/ui.js': ('studio-ui.js','application/javascript'), '/auth/ui.css': ('studio-ui.css','text/css')}


def cookie_token(headers):
    raw = headers.get_all('Cookie', [])
    if len(raw) > 1: return ''
    raw = raw[0] if raw else ''
    if len(raw) > 4096 or len(re.findall(r'(?:^|;)\s*'+COOKIE+r'=',raw)) != 1: return ''
    try:
        cookies=SimpleCookie();cookies.load(raw)
        return cookies[COOKIE].value if COOKIE in cookies else ''
    except CookieError: return ''


def body_json(request, maximum=65536):
    if request.headers.get('Content-Type') != 'application/json' or request.headers.get('Transfer-Encoding'):
        raise AccessError('BOUNDED_JSON_REQUIRED',415)
    values=request.headers.get_all('Content-Length',[])
    if len(values)!=1 or not re.fullmatch(r'[0-9]{1,8}',values[0]): raise AccessError('ONE_CONTENT_LENGTH_REQUIRED',400)
    size=int(values[0])
    if not 0 < size <= maximum: raise AccessError('REQUEST_BYTE_LIMIT',413)
    request.connection.settimeout(10)
    raw=request.rfile.read(size)
    if len(raw)!=size: raise AccessError('INTERRUPTED_REQUEST')
    from .acceptance import decode
    value=decode(raw)
    if not isinstance(value,dict): raise AccessError('JSON_OBJECT_REQUIRED')
    return value


class AccessMixin:
    """First MRO entry before the legacy Studio Handler. Not an optional route check."""
    principal=None
    session_token=''
    _response_cookie=None

    def end_headers(self):
        if self._response_cookie:
            self.send_header('Set-Cookie', self._response_cookie)
        super().end_headers()

    def respond(self, code, body, kind='application/json', attachment=None):
        if isinstance(body,dict) and 'token' in body and self.principal:
            body={**body,'token':self.principal['csrf'],'user':{k:v for k,v in self.principal.items() if k!='csrf'}}
        return super().respond(code,body,kind,attachment)

    def _host(self):
        if self.client_address[0] != '127.0.0.1' or self.headers.get_all('Host',[]) != [self.server.origin[7:]]:
            raise AccessError('EXACT_LOOPBACK_HOST_REQUIRED',403)
        if any(self.headers.get(k) for k in ('Forwarded','X-Forwarded-For','X-Forwarded-Host','X-Forwarded-Proto')):
            raise AccessError('PROXY_EXPOSURE_NOT_SUPPORTED',403)
        if self.headers.get('Origin') not in (None,self.server.origin) or self.headers.get('Sec-Fetch-Site') not in (None,'same-origin','none'):
            raise AccessError('SAME_ORIGIN_REQUIRED',403)
        parts=urlsplit(self.path)
        if parts.scheme or parts.netloc or '%' in parts.path or '\\' in parts.path or '//' in parts.path or '..' in parts.path:
            raise AccessError('INVALID_REQUEST_PATH')
        return parts.path

    def _redirect(self, destination):
        self.send_response(303);self.send_header('Location',destination)
        self.send_header('Cache-Control','no-store');self.send_header('Content-Length','0')
        self.send_header('Referrer-Policy','no-referrer');self.end_headers()

    def _csrf(self):
        values=[]
        for name in ('X-KFM-Token','X-KFM-Session','X-KFM-CSRF'):
            values += self.headers.get_all(name,[])
        if len(values)!=1 or not secrets.compare_digest(values[0],self.principal['csrf']):
            raise AccessError('SESSION_REQUEST_TOKEN_REQUIRED',403)

    def _legacy_headers(self):
        # Translate only after cookie, role, Origin and per-session CSRF checks.
        # The legacy bearer never leaves this authenticated gateway.
        for name in ('X-KFM-Token','X-KFM-Session'):
            if self.headers.get(name) is not None:
                self.headers.replace_header(name,self.server.token)
            else:
                self.headers[name]=self.server.token

    def _page(self, path):
        content=(WEB/'studio-shell.html').read_text()
        return self.respond(200,content.replace('data-page="studio"','data-page="'+path.strip('/')+'"'),'text/html')

    def _authenticate(self, path):
        self.session_token=cookie_token(self.headers)
        self.principal=self.server.accounts.session(self.session_token)
        if not self.principal:
            if path in PAGES or path in {'/','/index.html','/working-data','/library','/api/workspace/acceptance/page'}:
                self._redirect('/sign-in');return False
            raise AccessError('SIGN_IN_REQUIRED',401)
        if self.principal['mustChangePassword'] and path not in {'/account/password','/auth/session','/auth/password','/auth/logout'}:
            if path in PAGES or path=='/': self._redirect('/account/password');return False
            raise AccessError('PASSWORD_CHANGE_REQUIRED',403)
        return True

    def do_GET(self):
        self.principal=None;self._response_cookie=None
        try:
            path=self._host()
            if path in ASSETS:
                name,mime=ASSETS[path];return self.respond(200,(WEB/name).read_bytes(),mime)
            if path=='/sign-in': return self._page(path)
            if path=='/auth/health':
                return self.respond(200,{'app':'kfm-local-intake-studio','sourceFingerprint':self.server.source_fingerprint,'authentication':'local-accounts-required'})
            if path=='/auth/status': return self.respond(200,{'setupRequired':not self.server.accounts.initialized()})
            if not self._authenticate(path):return
            if path=='/auth/session':
                desks=getattr(getattr(self.server,'workspace',None),'desks',{})
                return self.respond(200,{'user':self.principal,'csrf':self.principal['csrf'],
                    'workspace':{'workingData':'working' in desks,'library':'library' in desks}})
            if path=='/users' and self.principal['role']!='admin':raise AccessError('ADMIN_REQUIRED',403)
            if path in PAGES:return self._page(path)
            if path=='/auth/users':return self.respond(200,{'users':self.server.accounts.users(self.principal)})
            if path=='/auth/audit':return self.respond(200,{'events':self.server.accounts.audit(self.principal)})
            if path=='/api/recovery/state':return self.respond(200,self.server.recovery.snapshot())
            if path=='/api/recovery/export':return self.respond(200,self.server.recovery.export(),'application/json','kfm-recovery-evidence.json')
            if re.fullmatch(r'/api/workspace/(working|library)/session',path):raise AccessError('USE_AUTHENTICATED_STUDIO_SESSION',404)
            public_legacy_assets={'/api/workspace/acceptance/page','/api/workspace/acceptance/app.js','/api/workspace/acceptance/style.css'}
            if path.startswith('/api/') and path!='/api/session' and path not in public_legacy_assets:
                self._csrf();self._legacy_headers()
            return super().do_GET()
        except (AccessError,ValueError,TypeError,KeyError,sqlite3.Error,OSError) as error:
            self._error(error)

    def _error(self,error):
        self.close_connection=True
        if isinstance(error,AccessError):code,status=str(error),error.status
        else:code,status='PRIVATE_WORKSPACE_REQUEST_FAILED',503
        return self.respond(status,{'error':code})

    def do_POST(self):
        self.principal=None;self._response_cookie=None
        try:
            path=self._host()
            if self.headers.get('Origin')!=self.server.origin:raise AccessError('EXACT_ORIGIN_REQUIRED',403)
            lengths=self.headers.get_all('Content-Length',[])
            if self.headers.get('Transfer-Encoding') or len(lengths)!=1 or not re.fullmatch(r'[0-9]{1,8}',lengths[0]):
                raise AccessError('ONE_BOUNDED_CONTENT_LENGTH_REQUIRED',400)
            accounts=self.server.accounts
            if path in {'/auth/login','/auth/bootstrap'}:
                value=body_json(self,4096)
                allowed={'username','password'}|({'setupCode'} if path.endswith('bootstrap') else set())
                if set(value)!=allowed:raise AccessError('INVALID_SIGN_IN_REQUEST')
                if path.endswith('bootstrap'):
                    result=accounts.bootstrap(value['setupCode'],value['username'],value['password'])
                    return self.respond(201,result)
                token=accounts.login(value['username'],value['password'])
                self._response_cookie=f'{COOKIE}={token}; HttpOnly; SameSite=Strict; Path=/; Max-Age={ABSOLUTE_SECONDS}'
                user=accounts.session(token)
                return self.respond(200,{'next':'/account/password' if user['mustChangePassword'] else '/studio'})
            if not self._authenticate(path):return
            self._csrf()
            if path=='/auth/logout':
                accounts.logout(self.session_token)
                self._response_cookie=f'{COOKIE}=; HttpOnly; SameSite=Strict; Path=/; Max-Age=0'
                return self.respond(200,{'signedOut':True})
            if path=='/auth/password':
                value=body_json(self,4096)
                if set(value)!={'currentPassword','newPassword'}:raise AccessError('INVALID_PASSWORD_REQUEST')
                result=accounts.change_password(self.principal,value['currentPassword'],value['newPassword'])
                self._response_cookie=f'{COOKIE}=; HttpOnly; SameSite=Strict; Path=/; Max-Age=0'
                return self.respond(200,result)
            if path=='/auth/users':
                if self.principal['role']!='admin':raise AccessError('ADMIN_REQUIRED',403)
                return self.respond(200,accounts.manage(self.principal,body_json(self,8192)))
            if path=='/api/recovery/events':
                value=body_json(self);self.server.store.check_volume()
                return self.respond(200,self.server.recovery.append(self.principal,value))
            if self.principal['role']=='viewer':raise AccessError('READ_ONLY_ACCOUNT',403)
            if path=='/api/workspace/acceptance/events':
                value=body_json(self)
                if value.get('kind')=='review' and self.principal['role']!='admin':raise AccessError('ADMIN_REQUIRED',403)
                value['actor']=self.principal['username']
                raw=json.dumps(value,ensure_ascii=False).encode()
                self.rfile=io.BytesIO(raw);self.headers.replace_header('Content-Length',str(len(raw)))
            elif (path in {'/api/upload','/api/uploads','/api/workspace/acceptance/import'}
                  or re.fullmatch(r'/api/uploads/[a-f0-9]{32}/(chunk|complete|cancel)',path)):
                pass  # Existing byte/type/volume bounds remain authoritative.
            elif re.fullmatch(r'/api/files/[a-f0-9]{32}/review',path):
                if self.principal['role']!='admin':raise AccessError('ADMIN_REQUIRED',403)
                value=body_json(self,150000);value['reviewer']=self.principal['username']
                raw=json.dumps(value,ensure_ascii=False).encode();self.rfile=io.BytesIO(raw)
                self.headers.replace_header('Content-Length',str(len(raw)))
            elif re.fullmatch(r'/api/files/[a-f0-9]{32}/send',path) or path.startswith('/api/workspace/working/'):
                if self.principal['role']!='admin':raise AccessError('ADMIN_REQUIRED',403)
            else:raise AccessError('ACTION_NOT_ALLOWED',403)
            self._legacy_headers()
            return super().do_POST()
        except (AccessError,ValueError,TypeError,KeyError,sqlite3.Error,OSError) as error:
            self._error(error)


def secure_server_class(base_server, base_handler):
    """Preserve the existing storage/extraction/Workspace implementations."""
    class PrivateHandler(AccessMixin,base_handler):
        pass
    class PrivateServer(base_server):
        def __init__(self,port,store):
            self.accounts=Accounts(store.root)
            self.recovery=RecoveryStore(store.root)
            super().__init__(port,store)
            self.RequestHandlerClass=PrivateHandler
    return PrivateServer
