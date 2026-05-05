#!/usr/bin/env python3
import subprocess
allowed=('docs/adr/','docs/architecture/','docs/control-plane/','docs/domains/','docs/registers/','docs/runbooks/','docs/sources/','docs/standards/','docs/tracking/','docs/catalog/','docs/README.md')
files=subprocess.check_output(['git','ls-files','docs/**'],text=True).splitlines()
orph=[f for f in files if not any(f.startswith(a) or f==a for a in allowed)]
print('\n'.join(orph[:50]))
raise SystemExit(1 if orph else 0)
