#!/usr/bin/python3
"""Start the authenticated local Studio; never replace an older running copy."""
import fcntl
import json
import os
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

if __package__:
    from .intake_server import source_fingerprint
    from . import workspace_config
else:
    from intake_server import source_fingerprint
    import workspace_config

APP = Path(__file__).resolve().parent
URL = 'http://127.0.0.1:8776'


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise urllib.error.HTTPError(req.full_url, code, 'Redirects are not allowed for local identity checks', headers, fp)


def running():
    # Health has no session token or data paths. Legacy detection is only used
    # to preserve/refuse an already-running unprotected instance.
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    for path in ('/auth/health', '/api/session'):
        try:
            with opener.open(URL + path, timeout=1) as response:
                if response.geturl() != URL + path:
                    continue
                raw = response.read(16385)
                if len(raw) > 16384:
                    continue
                value = json.loads(raw)
            if value.get('app') == 'kfm-local-intake-studio':
                return {key:value.get(key) for key in ('app','sourceFingerprint','authentication')}
        except Exception:
            pass
    return None


def require_current(session, expected):
    if session and (session.get('sourceFingerprint') != expected or session.get('authentication') != 'local-accounts-required'):
        raise SystemExit('A different, older, or unauthenticated KFM Studio is already running at ' + URL + '. Its data and process were preserved. Stop it deliberately or test this candidate on a separate port and disposable store. No existing service was replaced.')


def main():
    os.umask(0o077)
    state_dir = Path.home() / '.local/state/kfm-intake-studio'
    state_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
    expected = source_fingerprint()
    # Owner-private Working Data / Library roots saved by studio_admin.py.
    try:
        config = workspace_config.load()
        issues = workspace_config.problems(config)
    except workspace_config.ConfigError as error:
        raise SystemExit('Data workspace settings are invalid: ' + str(error) + '. Fix them with ./tools/local_data/intake_studio/studio-admin.sh workspace show')
    if issues:
        raise SystemExit('Data workspace settings need attention before Studio can start:\n  ' + '\n  '.join(issues) + '\nFix them with ./tools/local_data/intake_studio/studio-admin.sh')
    with (state_dir / 'launch.lock').open('w') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        session = running(); require_current(session, expected)
        reused = session is not None
        if session is None:
            with (state_dir / 'server.log').open('a') as log:
                proc = subprocess.Popen(['/usr/bin/python3', str(APP / 'private_server.py'), *workspace_config.server_args(config)], cwd=APP,
                    stdin=subprocess.DEVNULL, stdout=log, stderr=log, start_new_session=True)
            (state_dir / 'server.pid').write_text(str(proc.pid))
            for _ in range(100):
                session = running(); require_current(session, expected)
                if session is not None: break
                if proc.poll() is not None: raise SystemExit('Could not start private Studio. See ' + str(state_dir / 'server.log'))
                time.sleep(0.1)
            else: raise SystemExit('Private Studio did not become ready. See ' + str(state_dir / 'server.log'))
    # First-owner setup code appears ONLY in this local interactive terminal,
    # never in server logs, URLs, HTTP metadata or source control.
    if sys.stdout.isatty():
        if __package__:
            from .accounts import Accounts
        else:
            from accounts import Accounts
        accounts = Accounts(Path.home() / '.local/share/kfm-intake-studio')
        if not accounts.initialized():
            print('First-owner setup code (10 minutes, one use): ' + accounts.issue_setup_code())
    if reused:
        print('Studio was already running. Data workspace changes apply after: ./tools/local_data/intake_studio/studio-admin.sh stop')
    if not config.get('kfm_root'):
        print('Working Data is not connected, so held reviews cannot be sent to KFM yet. Run: ./tools/local_data/intake_studio/studio-admin.sh workspace setup')
    if '--no-open' not in sys.argv:
        subprocess.Popen(['xdg-open', URL+'/studio'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(URL+'/studio')


if __name__ == '__main__':
    main()
