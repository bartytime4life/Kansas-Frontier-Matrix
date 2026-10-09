"""Local Google consent and verified Earth Engine access; tokens never leave the operator."""
from __future__ import annotations
import base64
import hashlib
import json
import re
import secrets
import threading
import time
from urllib.parse import urlencode, parse_qs
from urllib.request import Request, build_opener, HTTPRedirectHandler
from tools.local_data.acquisition import save_state
from tools.local_data.file_io import read_regular

EE_SCOPE = "https://www.googleapis.com/auth/earthengine"
PROJECT_SCOPE = "https://www.googleapis.com/auth/cloudplatformprojects.readonly"
SCOPES = [EE_SCOPE, PROJECT_SCOPE, "openid", "https://www.googleapis.com/auth/userinfo.email"]
CALLBACK = "http://127.0.0.1:8769/oauth/callback"
PROJECT = re.compile(r"[a-z][a-z0-9-]{4,61}[a-z0-9]\Z")

class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *_args, **_kwargs):
        raise ValueError("GOOGLE_REDIRECT_REJECTED")

def google_json(url, *, token=None, data=None):
    # Only fixed Google endpoints constructed below call this helper. Never follow a redirect with credentials.
    headers = {"Authorization": "Bearer " + token} if token else {}
    with build_opener(NoRedirect()).open(Request(url, data=data, headers=headers), timeout=30) as response:
        raw = response.read(256001)
        if len(raw) > 256000: raise ValueError("GOOGLE_RESPONSE_LIMIT")
        value = json.loads(raw)
        if not isinstance(value, dict): raise ValueError("GOOGLE_RESPONSE_INVALID")
        return value

def make_credentials(token, scopes):
    import ee
    from google.oauth2.credentials import Credentials
    return Credentials(None, refresh_token=token, token_uri=ee.oauth.TOKEN_URI,
                       client_id=ee.oauth.CLIENT_ID, client_secret=ee.oauth.CLIENT_SECRET, scopes=scopes)

def credentials(work):
    import ee
    path = work / "credentials.json"
    if not path.exists(): return ee.data.get_persistent_credentials()
    saved = json.loads(read_regular(path, 64000))
    return make_credentials(saved["refresh_token"], saved.get("scopes", [EE_SCOPE]))

def refresh_credentials(creds):
    from google.auth.transport.requests import Request as GoogleRequest
    request = GoogleRequest()
    creds.refresh(lambda *args, **kwargs: request(*args, **{**kwargs, "timeout": 30}))

def verify_project(creds, project):
    import ee
    ee.data.setDeadline(30000)
    ee.Initialize(credentials=creds, project=project)
    # Initialization alone can reuse cached algorithms. Exercise this account/project's compute permission.
    if ee.Number(1).getInfo() != 1: raise ValueError("PROJECT_ACCESS_UNVERIFIED")

def discover_projects(creds):
    rows, seen, page = [], set(), ""
    for _ in range(3):
        query = {"pageSize": 50, "filter": "lifecycleState:ACTIVE"}
        if page: query["pageToken"] = page
        result = google_json("https://cloudresourcemanager.googleapis.com/v1/projects?" + urlencode(query), token=creds.token)
        projects = result.get("projects", [])
        if not isinstance(projects, list): raise ValueError("GOOGLE_RESPONSE_INVALID")
        for row in projects:
            if not isinstance(row, dict): continue
            project = row.get("projectId")
            if isinstance(project, str) and PROJECT.fullmatch(project) and project not in seen:
                seen.add(project); rows.append(project)
                if len(rows) == 100: return sorted(rows), True
        page = result.get("nextPageToken", "")
        if not page: return sorted(rows), False
        if not isinstance(page, str) or len(page) > 4096: raise ValueError("GOOGLE_RESPONSE_INVALID")
    return sorted(rows), True

class SignIn:
    def __init__(self, work):
        self.work = work
        self.lock = threading.RLock()
        self.pending = None
        self.phase = "idle"
        self.signed_in = False
        self.account = None
        self.projects = []
        self.project_list = "idle"
        self.project = None
        self.ready = False
        self.error = None
        self.worker = None

    def status(self):
        with self.lock:
            if self.pending and self.pending["expires"] < time.monotonic():
                self.pending = None; self.phase = "expired"
            return self.phase

    def snapshot(self):
        with self.lock:
            return {"authentication": self.status(), "signedIn": self.signed_in, "accountEmail": self.account,
                    "projects": list(self.projects), "projectDiscovery": self.project_list,
                    "project": self.project, "configured": self.ready, "authError": self.error}

    def start(self, value):
        if not isinstance(value, dict) or set(value) - {"project"}: raise ValueError("INVALID_AUTH_REQUEST")
        project = value.get("project") or None
        if "project" in value and (not isinstance(value["project"], str) or project and not PROJECT.fullmatch(project)):
            raise ValueError("PROJECT_ID_REQUIRED")
        with self.lock:
            self.status()
            if self.phase == "validating": raise ValueError("SIGN_IN_IN_PROGRESS")
            if self.pending and self.pending["project"] == project: return {"url": self.pending["url"]}
            import ee
            verifier = secrets.token_urlsafe(48)
            challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).decode().rstrip("=")
            state = secrets.token_urlsafe(32)
            url = ee.oauth.get_authorization_url(challenge, SCOPES, CALLBACK) + "&" + urlencode({"state": state, "access_type": "offline", "prompt": "consent select_account"})
            self.pending = {"state": state, "verifier": verifier, "project": project, "expires": time.monotonic() + 600, "url": url}
            self.phase = "waiting"; self.ready = False; self.signed_in = False; self.account = None; self.error = None
            self.projects = []; self.project_list = "idle"
            return {"url": url}

    def claim(self, query):
        with self.lock:
            self.status()
            if len(query) > 8192: raise ValueError("INVALID_OAUTH_RESPONSE")
            args = parse_qs(query)
            state = args.get("state", [])
            if not self.pending or len(state) != 1 or not secrets.compare_digest(state[0], self.pending["state"]): raise ValueError("INVALID_OAUTH_STATE")
            pending = self.pending; self.pending = None
            if "error" in args: self.phase = "declined"; return None
            code = args.get("code", [])
            if len(code) != 1 or not 1 <= len(code[0]) <= 4096: self.phase = "failed"; raise ValueError("INVALID_OAUTH_RESPONSE")
            self.phase = "validating"
            return pending, code[0]

    def finish(self, claimed):
        import ee
        pending, code = claimed
        try:
            body = urlencode({"code": code, "code_verifier": pending["verifier"], "client_id": ee.oauth.CLIENT_ID,
                              "client_secret": ee.oauth.CLIENT_SECRET, "redirect_uri": CALLBACK, "grant_type": "authorization_code"}).encode()
            result = google_json(ee.oauth.TOKEN_URI, data=body)
            token = result.get("refresh_token")
            if not isinstance(token, str) or not 1 < len(token) < 16000: raise ValueError("OAUTH_TOKEN_INVALID")
            scopes = result.get("scope", " ".join(SCOPES)).split()
            if EE_SCOPE not in scopes: raise ValueError("EARTH_ENGINE_PERMISSION_REQUIRED")
            creds = make_credentials(token, scopes)
            refresh_credentials(creds)
            # Save a valid account grant independently from project permission. Never delete it on a project error.
            save_state(self.work / "credentials.json", {"refresh_token": token, "scopes": scopes})
            save_state(self.work / "config.json", {"project": pending["project"], "login": "google-oauth-pkce"})
            self.inspect(creds, pending["project"])
        except Exception:
            with self.lock:
                self.phase = "failed"; self.ready = False; self.error = "GOOGLE_SIGN_IN_FAILED"

    def inspect(self, creds, project):
        with self.lock:
            self.signed_in = True; self.project = project; self.ready = False; self.account = None
        try:
            identity = google_json("https://openidconnect.googleapis.com/v1/userinfo", token=creds.token)
            email = identity.get("email")
            if identity.get("email_verified") is True and isinstance(email, str) and len(email) <= 254 and re.fullmatch(r"[^\s@]+@[^\s@]+", email):
                with self.lock: self.account = email
        except Exception: pass  # Legacy grants may not include email; never invent an identity.
        try:
            projects, limited = discover_projects(creds)
            with self.lock: self.projects = projects; self.project_list = "limited" if limited else "complete"
        except Exception:
            with self.lock: self.project_list = "unavailable"
        if project:
            try:
                verify_project(creds, project)
                with self.lock: self.ready = True; self.error = None
            except Exception:
                with self.lock: self.error = "PROJECT_ACCESS_REQUIRED"
        with self.lock: self.phase = "connected" if self.ready else "project-required"

    def check(self, value):
        if not isinstance(value, dict) or set(value) - {"project"}: raise ValueError("INVALID_AUTH_REQUEST")
        project = value.get("project")
        if project is not None and (not isinstance(project, str) or not PROJECT.fullmatch(project)): raise ValueError("PROJECT_ID_REQUIRED")
        with self.lock:
            if self.status() in {"waiting", "validating"}: raise ValueError("SIGN_IN_IN_PROGRESS")
            self.ready = False; self.signed_in = False; self.phase = "validating"; self.error = None
            self.worker = threading.Thread(target=self._check, args=(project,), daemon=True, name="kfm-google-access")
            try: self.worker.start()
            except Exception:
                self.phase = "failed"; self.error = "GOOGLE_SIGN_IN_FAILED"
                raise ValueError("GOOGLE_SIGN_IN_FAILED") from None
        return {"checking": True}

    def _check(self, project):
        try:
            if project is None and (self.work / "config.json").exists():
                project = json.loads(read_regular(self.work / "config.json", 64000)).get("project")
            if project is not None and (not isinstance(project, str) or not PROJECT.fullmatch(project)): raise ValueError("PROJECT_ID_REQUIRED")
            creds = credentials(self.work)
            refresh_credentials(creds)
            # Bind the worker's consumed project before publishing readiness.
            save_state(self.work / "config.json", {"project": project, "login": "google-oauth-pkce"})
            self.inspect(creds, project)
        except Exception:
            with self.lock:
                self.phase = "failed"; self.ready = False; self.signed_in = False; self.account = None; self.error = "GOOGLE_SIGN_IN_REQUIRED"
