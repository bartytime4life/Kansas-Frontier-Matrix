#!/usr/bin/env python3
"""Create source-bound image animations; no downloads or data admission."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

root = Path(__file__).resolve().parents[2]
manifest = json.loads((root / 'scripts/welcome-demos/runtime-assets.json').read_text())
known = {item['path']: item for item in manifest['files']}
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

if len(sys.argv) != 2:
    raise SystemExit('Usage: build-animations.py /path/to/ffmpeg')
output = root / 'public/welcome/animations'
output.mkdir(parents=True, exist_ok=True)
files = []
for source in sorted((root / 'public/welcome/demos').glob('*.webm')):
    public_path = '/' + source.relative_to(root / 'public').as_posix()
    expected = known.get(public_path)
    if not expected or digest(source) != expected['sha256']:
        raise SystemExit('Source integrity mismatch: ' + public_path)
    target = output / (source.stem + '.webp')
    subprocess.run([sys.argv[1], '-v', 'error', '-i', str(source), '-vf',
        'fps=10,scale=960:-1:flags=lanczos', '-c:v', 'libwebp_anim',
        '-quality', '62', '-loop', '0', '-an', '-y', str(target)], check=True)
    files.append({'source': public_path, 'sourceSha256': expected['sha256'],
        'delivery': '/' + target.relative_to(root / 'public').as_posix(),
        'sha256': digest(target), 'bytes': target.stat().st_size})
(output / 'provenance.json').write_text(json.dumps({'kind': 'RECORDED_EXPLORER_DERIVATIVE',
    'authority': 'NONE', 'live': False, 'fps': 10, 'width': 960,
    'sourceRecord': 'scripts/welcome-demos/runtime-assets.json', 'files': files}, indent=2) + '\n')
