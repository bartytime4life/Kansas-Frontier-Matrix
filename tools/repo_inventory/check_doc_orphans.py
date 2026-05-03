#!/usr/bin/env python3
from __future__ import annotations
import subprocess,sys
ALLOWED=('docs/adr/','docs/architecture/','docs/control-plane/','docs/domains/','docs/registers/','docs/runbooks/','docs/sources/','docs/standards/','docs/tracking/','docs/catalog/','docs/governance/','docs/runtime/','docs/README.md')
files=subprocess.check_output(['git','ls-files','*.md'],text=True).splitlines()
orphan=[f for f in files if f.startswith('docs/') and not any(f==a or f.startswith(a) for a in ALLOWED)]
if orphan:
    print('\n'.join(orphan)); sys.exit(1)
print('OK no doc orphans in docs/')
