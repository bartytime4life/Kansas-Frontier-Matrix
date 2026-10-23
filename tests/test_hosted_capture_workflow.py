"""Execute the scheduler command with a local curl fixture; never contact production."""
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = yaml.safe_load((ROOT / '.github/workflows/godaddy-hosted-capture.yml').read_text())

class HostedCaptureWorkflowTest(unittest.TestCase):
    def test_scheduler_is_disabled_and_has_no_repository_or_deployment_authority(self):
        self.assertEqual(WORKFLOW['permissions'], {})
        self.assertEqual(set(WORKFLOW['on']), {'schedule', 'workflow_dispatch'})
        job = WORKFLOW['jobs']['capture']
        self.assertIn("github.ref == 'refs/heads/main'", job['if'])
        self.assertIn("vars.KFM_HOSTED_CAPTURE_ENABLED == 'true'", job['if'])
        self.assertEqual(job['environment'], {'name': 'kfm-hosted-capture', 'deployment': False})
        self.assertEqual(job['timeout-minutes'], 4)
        self.assertEqual(len(job['steps']), 1)
        self.assertNotIn('uses', job['steps'][0])

    def command(self, token, exit_code=0):
        with tempfile.TemporaryDirectory(prefix='kfm-capture-workflow-') as directory:
            temp = Path(directory)
            curl = temp / 'curl'
            curl.write_text('#!/usr/bin/env python3\nimport json,os,sys\nfrom pathlib import Path\nPath(os.environ["FIXTURE_RECORD"]).write_text(json.dumps({"argv":sys.argv[1:],"header":sys.stdin.read()}))\nsys.exit(int(os.environ["FIXTURE_EXIT"]))\n')
            curl.chmod(0o700)
            record = temp / 'record.json'
            environment = {**os.environ, 'PATH': str(temp)+os.pathsep+os.environ['PATH'], 'CAPTURE_TOKEN': token, 'FIXTURE_RECORD': str(record), 'FIXTURE_EXIT': str(exit_code)}
            result = subprocess.run(['bash', '-c', WORKFLOW['jobs']['capture']['steps'][0]['run']], env=environment, capture_output=True, text=True, timeout=5)
            return result, json.loads(record.read_text()) if record.exists() else None

    def test_capture_token_is_only_on_stdin_and_destination_cannot_follow_redirects(self):
        token = 'fixture-only-not-a-credential'
        result, record = self.command(token)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(record['header'], 'Authorization: Bearer '+token+'\n')
        self.assertNotIn(token, ' '.join(record['argv'])+result.stdout+result.stderr)
        self.assertEqual(record['argv'][-1], 'https://kansasfrontiermatrix.com/api/source-pipeline/run')
        self.assertIn('--fail-with-body', record['argv'])
        self.assertEqual(record['argv'][record['argv'].index('--max-time')+1], '150')
        self.assertEqual(record['argv'][record['argv'].index('--proto')+1], '=https')
        self.assertNotIn('--location', record['argv'])
        self.assertNotIn('-L', record['argv'])

    def test_missing_token_blocks_network_and_provider_failure_fails_the_job(self):
        result, record = self.command('')
        self.assertNotEqual(result.returncode, 0)
        self.assertIsNone(record)
        result, _ = self.command('fixture-only', exit_code=22)
        self.assertEqual(result.returncode, 22)

if __name__ == '__main__':
    unittest.main()
