"""Local Google OAuth consent with PKCE, state, expiry, and private KFM credentials."""
from __future__ import annotations
import base64
import hashlib
import json
import re
import secrets
import time
from urllib.parse import urlencode, parse_qs
from urllib.request import Request, urlopen
from tools.local_data.acquisition import save_state
from tools.local_data.file_io import read_regular

SCOPES=["https://www.googleapis.com/auth/earthengine"]
CALLBACK="http://127.0.0.1:8769/oauth/callback"

def credentials(work):
    import ee
    from google.oauth2.credentials import Credentials
    path=work/"credentials.json"
    if not path.exists(): return ee.data.get_persistent_credentials()
    saved=json.loads(read_regular(path,64000))
    return Credentials(None,refresh_token=saved["refresh_token"],token_uri=ee.oauth.TOKEN_URI,
                       client_id=ee.oauth.CLIENT_ID,client_secret=ee.oauth.CLIENT_SECRET,scopes=SCOPES)

class SignIn:
    def __init__(self,work):
        self.work=work
        self.pending=None
        self.phase="idle"
    def status(self):
        if self.pending and self.pending["expires"]<time.monotonic():
            self.pending=None;self.phase="expired"
        return self.phase
    def start(self,value):
        if not isinstance(value,dict) or set(value)!={"project"} or not isinstance(value["project"],str) or not re.fullmatch(r"[a-z][a-z0-9-]{4,61}[a-z0-9]",value["project"]): raise ValueError("PROJECT_ID_REQUIRED")
        self.status()
        if self.phase=="validating": raise ValueError("SIGN_IN_IN_PROGRESS")
        if self.pending and self.pending["project"]==value["project"]:return {"url":self.pending["url"]}
        import ee
        verifier=secrets.token_urlsafe(48)
        challenge=base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).decode().rstrip("=")
        state=secrets.token_urlsafe(32)
        url=ee.oauth.get_authorization_url(challenge,SCOPES,CALLBACK)+"&"+urlencode({"state":state,"access_type":"offline","prompt":"consent select_account"})
        self.pending={"state":state,"verifier":verifier,"project":value["project"],"expires":time.monotonic()+600,"url":url}
        self.phase="waiting"
        return {"url":url}
    def claim(self,query):
        self.status()
        if len(query)>8192:raise ValueError("INVALID_OAUTH_RESPONSE")
        args=parse_qs(query)
        state=args.get("state",[])
        if not self.pending or len(state)!=1 or not secrets.compare_digest(state[0],self.pending["state"]): raise ValueError("INVALID_OAUTH_STATE")
        pending=self.pending;self.pending=None
        if "error" in args:self.phase="declined";return None
        code=args.get("code",[])
        if len(code)!=1 or not 1<=len(code[0])<=4096:self.phase="failed";raise ValueError("INVALID_OAUTH_RESPONSE")
        self.phase="validating"
        return pending,code[0]
    def finish(self,claimed):
        import ee
        from google.oauth2.credentials import Credentials
        pending,code=claimed
        try:
            body=urlencode({"code":code,"code_verifier":pending["verifier"],"client_id":ee.oauth.CLIENT_ID,"client_secret":ee.oauth.CLIENT_SECRET,"redirect_uri":CALLBACK,"grant_type":"authorization_code"}).encode()
            with urlopen(Request(ee.oauth.TOKEN_URI,data=body),timeout=45) as response:
                raw=response.read(64001)
                if len(raw)>64000:raise ValueError("OAUTH_RESPONSE_LIMIT")
                token=json.loads(raw)["refresh_token"]
            if not isinstance(token,str) or not 1<len(token)<16000:raise ValueError("OAUTH_TOKEN_INVALID")
            creds=Credentials(None,refresh_token=token,token_uri=ee.oauth.TOKEN_URI,client_id=ee.oauth.CLIENT_ID,client_secret=ee.oauth.CLIENT_SECRET,scopes=SCOPES)
            ee.data.setDeadline(45000)
            ee.Initialize(credentials=creds,project=pending["project"])
            save_state(self.work/"credentials.json",{"refresh_token":token,"scopes":SCOPES})
            save_state(self.work/"config.json",{"project":pending["project"],"login":"google-oauth-pkce"})
            self.phase="connected"
        except Exception:
            # Provider responses can contain tokens or authorization codes; never log them.
            self.phase="failed"
