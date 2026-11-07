#!/usr/bin/python3
"""Start this exact local studio on demand; preserve any existing instance."""

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
else:
    from intake_server import source_fingerprint

APP = Path(__file__).resolve().parent
URL = "http://127.0.0.1:8776"


def running():
    try:
        with urllib.request.urlopen(URL + "/api/session", timeout=1) as response:
            session = json.load(response)
        if session.get("app") == "kfm-local-intake-studio":
            return session
    except Exception:
        pass
    return None


def require_current(session, expected):
    if session and session.get("sourceFingerprint") != expected:
        raise SystemExit(
            "A different or older KFM studio is already running at " + URL + ". "
            "Your inbox and running process were preserved. Close that instance "
            "before launching this copy, or test this checkout on a separate port "
            "with a disposable inbox. See docs/runbooks/local-intake-studio.md."
        )


def main():
    os.umask(0o077)
    state_dir = Path.home() / ".local/state/kfm-intake-studio"
    state_dir.mkdir(parents=True, exist_ok=True, mode=0o700)
    expected = source_fingerprint()
    with (state_dir / "launch.lock").open("w") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        session = running()
        require_current(session, expected)
        if session is None:
            with (state_dir / "server.log").open("a") as log:
                proc = subprocess.Popen(
                    ["/usr/bin/python3", str(APP / "intake_server.py")],
                    cwd=APP,
                    stdin=subprocess.DEVNULL,
                    stdout=log,
                    stderr=log,
                    start_new_session=True,
                )
            (state_dir / "server.pid").write_text(str(proc.pid))
            for _ in range(100):
                session = running()
                require_current(session, expected)
                if session is not None:
                    break
                if proc.poll() is not None:
                    raise SystemExit(
                        "Could not start local intake. See "
                        + str(state_dir / "server.log")
                    )
                time.sleep(0.1)
            else:
                raise SystemExit(
                    "Local intake did not become ready. See "
                    + str(state_dir / "server.log")
                )
    if "--no-open" not in sys.argv:
        subprocess.Popen(
            ["xdg-open", URL], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
    print(URL)


if __name__ == "__main__":
    main()
