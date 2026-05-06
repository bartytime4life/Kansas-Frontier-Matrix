#!/usr/bin/env python3
from __future__ import annotations
import re
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
REGISTER = ROOT / "docs/registers/workflow_dependency_register.yaml"
WORKFLOWS = ROOT / ".github/workflows"

SCRIPT_RE = re.compile(r"(?:python\s+|bash\s+|sh\s+|\.\/)([\w./-]+\.(?:py|sh))")
PATH_RE = re.compile(r"([A-Za-z0-9_./-]+\.(?:json|ya?ml|toml|ini|cfg))")
SECRET_RE = re.compile(r"secrets\.([A-Z0-9_]+)")
CTX_RE = re.compile(r"github\.([a-zA-Z_]+)")
PM_RE = re.compile(r"\b(python|pip|pip3|npm|pnpm|yarn|go|cargo|uv|poetry|bash|sh)\b")


def load_yaml(path: Path):
    with path.open() as f:
        return yaml.safe_load(f)


def collect_from_workflow(path: Path):
    data = load_yaml(path)
    txt = path.read_text()
    # Ignore heredoc-embedded scripts (e.g., python <<'PY') when collecting
    # repo path literals; these blocks often contain generated temp-output paths
    # or example names that are not required checkout files.
    txt_for_paths = re.sub(r"<<'?[A-Za-z_][A-Za-z0-9_]*'?\n.*?\n[A-Za-z_][A-Za-z0-9_]*", "", txt, flags=re.DOTALL)
    scripts, cfgs, pms = set(), set(), set()
    for m in SCRIPT_RE.finditer(txt):
        scripts.add(m.group(1).lstrip("./"))
    for m in PATH_RE.finditer(txt_for_paths):
        candidate = m.group(1).lstrip("./")
        if candidate.startswith("github"):
            continue
        cfgs.add(candidate)
    for m in PM_RE.finditer(txt):
        t = m.group(1)
        pms.add("python" if t in {"pip", "pip3"} else ("bash" if t == "sh" else t))
    secrets = {"secrets." + s for s in SECRET_RE.findall(txt)}
    context = {"github." + c for c in CTX_RE.findall(txt) if c != "com"}
    return data, scripts, cfgs, pms, secrets | context


def main() -> int:
    reg = load_yaml(REGISTER)
    entries = {e["workflow_file"]: e for e in reg["workflows"]}
    failures = []

    workflow_files = sorted(p.relative_to(ROOT).as_posix() for p in WORKFLOWS.glob("*.yml"))
    missing_entries = [wf for wf in workflow_files if wf not in entries]
    if missing_entries:
        failures.append(f"Missing register entries: {missing_entries}")

    for wf in workflow_files:
        entry = entries.get(wf)
        if not entry:
            continue
        _, scripts, cfgs, pms, ctx = collect_from_workflow(ROOT / wf)
        documented_scripts = set(entry.get("required_scripts", []))
        documented_paths = set(entry.get("required_repo_paths", []))
        documented_pms = set(entry.get("required_package_managers", []))
        documented_ctx = set(entry.get("required_secrets_or_github_context", []))

        for s in documented_scripts:
            if not (ROOT / s).exists():
                failures.append(f"{wf}: documented script missing: {s}")
        for p in documented_paths:
            if not (ROOT / p).exists():
                failures.append(f"{wf}: documented repo path missing: {p}")

        repo_prefixes=("configs/","contracts/","schemas/","policy/","release/","data/","tests/","tools/","scripts/","apps/",".github/")
        missing_cfg = sorted(c for c in cfgs if c and c.startswith(repo_prefixes) and not (ROOT / c).exists())
        if missing_cfg:
            failures.append(f"{wf}: missing referenced config/files: {missing_cfg[:10]}")

        missing_pm_docs = sorted(pm for pm in pms if pm not in documented_pms)
        if missing_pm_docs:
            failures.append(f"{wf}: package commands undocumented: {missing_pm_docs}")

        undocumented_ctx = sorted(c for c in ctx if c not in documented_ctx)
        if undocumented_ctx:
            failures.append(f"{wf}: undocumented secrets/context: {undocumented_ctx}")

    if failures:
        print("workflow dependency validation FAILED")
        for f in failures:
            print("-", f)
        return 1
    print("workflow dependency validation PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
