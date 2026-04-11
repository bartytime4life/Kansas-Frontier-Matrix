from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
required = [
    root / "data/catalog/README.md",
    root / "data/catalog/stac/README.md",
    root / "data/catalog/dcat/README.md",
    root / "data/catalog/prov/README.md",
]
missing = [str(p.relative_to(root)) for p in required if not p.exists()]

if missing:
    print("catalog-validate: FAILED")
    for item in missing:
        print(f" - missing {item}")
    sys.exit(1)

print("catalog-validate: OK (catalog README scaffold present)")
