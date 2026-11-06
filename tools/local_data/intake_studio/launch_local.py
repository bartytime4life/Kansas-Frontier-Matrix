#!/usr/bin/python3
"""Start local intake on demand; no login service or public listener."""

import fcntl, json, os, subprocess, sys, time, urllib.request
from pathlib import Path

APP = Path(__file__).resolve().parent
os.umask(0o077)
STATE = Path.home() / ".local/state/kfm-intake-studio"
STATE.mkdir(parents=True, exist_ok=True, mode=0o700)
URL = "http://127.0.0.1:8776"


def running():
    try:
        with urllib.request.urlopen(URL + "/api/session", timeout=1) as r:
            d = json.load(r)
        return d.get("app") == "kfm-local-intake-studio"
    except Exception:
        return False


with (STATE / "launch.lock").open("w") as lock:
    fcntl.flock(lock, fcntl.LOCK_EX)
    if not running():
        log = (STATE / "server.log").open("a")
        proc = subprocess.Popen(
            ["/usr/bin/python3", str(APP / "intake_server.py")],
            cwd=APP,
            stdin=subprocess.DEVNULL,
            stdout=log,
            stderr=log,
            start_new_session=True,
        )
        (STATE / "server.pid").write_text(str(proc.pid))
        log.close()
        for _ in range(100):
            if running():
                break
            if proc.poll() is not None:
                raise SystemExit(
                    "Could not start local intake. See " + str(STATE / "server.log")
                )
            time.sleep(0.1)
        else:
            raise SystemExit(
                "Local intake did not become ready. See " + str(STATE / "server.log")
            )
if "--no-open" not in sys.argv:
    subprocess.Popen(
        ["xdg-open", URL], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )
print(URL)
