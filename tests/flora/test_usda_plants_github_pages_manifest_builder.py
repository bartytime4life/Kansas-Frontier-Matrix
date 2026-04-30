from pathlib import Path
import json,subprocess,tempfile

def test_github_pages_manifest_defaults_to_no_deploy_and_required_guards():
    with tempfile.TemporaryDirectory() as d:
        base=Path(d);out=base/'manifest.json'
        subprocess.check_call(['python','tools/deploy/flora/usda_plants_github_pages_manifest_builder.py','--snapshot-date','2026-01-01','--generated-at','2026-01-01T00:00:00Z','--deployment-plan-ref','/tmp/exec.json','--site-bundle-manifest-ref','/tmp/site/static_site_bundle_manifest.json','--artifact-path','site/flora/usda_plants/2026-01-01','--out',str(out)])
        m=json.loads(out.read_text())
        assert m['deploys'] is False
        assert m['required_permissions']=={'contents':'read','pages':'write','id-token':'write'}
        assert m['requires_environment_protection'] is True
        assert m['uses_long_lived_secrets'] is False
        assert m['claims']['auto_merge'] is False
