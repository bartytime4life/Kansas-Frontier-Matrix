#!/usr/bin/env python3
import subprocess,sys
allowed=('docs/adr/','docs/architecture/','docs/control-plane/','docs/domains/','docs/registers/','docs/runbooks/','docs/sources/','docs/standards/','docs/tracking/','docs/README.md')
orph=[p for p in subprocess.check_output(['git','ls-files','docs'],text=True).splitlines() if p.endswith('.md') and not p.startswith(allowed)]
print('\n'.join(orph[:200]))
print(f'orphan_count={len(orph)}')
sys.exit(1 if orph else 0)
