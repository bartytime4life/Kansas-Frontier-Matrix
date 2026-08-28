"""Placeholder verifier for perf metrics computed from frame captures."""

from pathlib import Path
import sys


if __name__ == '__main__':
    files = [Path(arg) for arg in sys.argv[1:]]
    if not files:
        print('No files provided', file=sys.stderr)
        raise SystemExit(2)
    for fp in files:
        if not fp.exists():
            print(f'FAIL {fp}: file does not exist')
            raise SystemExit(1)
        print(f'OK {fp}')
