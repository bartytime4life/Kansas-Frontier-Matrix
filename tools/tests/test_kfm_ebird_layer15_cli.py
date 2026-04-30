import subprocess

def test_package_help():
    assert subprocess.run(['tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-package','--help'],check=False).returncode==0

def test_package_version():
    assert subprocess.run(['tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-package','--version'],check=False).returncode==0

def test_deploy_help():
    assert subprocess.run(['tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-deploy','--help'],check=False).returncode==0

def test_deploy_version():
    assert subprocess.run(['tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-deploy','--version'],check=False).returncode==0
