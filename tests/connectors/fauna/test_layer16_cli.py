from subprocess import run


def test_certify_help():
    r = run(["python3", "tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_certify.py", "--help"], check=False)
    assert r.returncode == 0


def test_certify_version():
    r = run(["python3", "tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_certify.py", "--version"], check=False)
    assert r.returncode == 0


def test_support_help():
    r = run(["python3", "tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_support.py", "--help"], check=False)
    assert r.returncode == 0


def test_support_version():
    r = run(["python3", "tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_support.py", "--version"], check=False)
    assert r.returncode == 0
