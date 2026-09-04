#!/usr/bin/env bash
# KFM local workstation bootstrap.
# Local convenience only: no truth, release, deployment, or publication authority.
set -euo pipefail

readonly EXIT_OK=0
readonly EXIT_INVALID_INPUT=2
readonly EXIT_UNSUPPORTED=3
readonly EXIT_BLOCKED=4
readonly EXIT_VALIDATION_FAILED=5
readonly CANONICAL_REPOSITORY="https://github.com/bartytime4life/Kansas-Frontier-Matrix.git"
readonly RECOMMENDED_INSTALL_ROOT="${HOME}/src/Kansas-Frontier-Matrix"
readonly LOCAL_NODE_VERSION="22.23.2"

MODE="inspect"
REPO_ROOT=""

usage() {
  cat <<'USAGE'
Usage: scripts/dev/bootstrap.sh [--inspect | --apply | --verify] [--repo-root PATH]

Modes:
  --inspect   Read-only prerequisite and plan report. This is the default.
  --apply     Install repository-local dependencies after explicit review.
  --verify    Run the bounded local verification profile without installing.
  --help      Show this help.

Exit codes:
  0  SUCCESS, NO_CHANGE, or DRY_RUN
  2  INVALID_INPUT
  3  UNSUPPORTED platform or runtime
  4  BLOCKED by a missing prerequisite
  5  VALIDATION_FAILED

Recommended clone location:
  ~/src/Kansas-Frontier-Matrix
USAGE
}

fail() {
  local code="$1"
  shift
  printf 'KFM_LOCAL_BOOTSTRAP: %s\n' "$*" >&2
  exit "$code"
}

while (($# > 0)); do
  case "$1" in
    --inspect)
      MODE="inspect"
      shift
      ;;
    --apply)
      MODE="apply"
      shift
      ;;
    --verify)
      MODE="verify"
      shift
      ;;
    --repo-root)
      (($# >= 2)) || fail "$EXIT_INVALID_INPUT" "INVALID_INPUT: --repo-root requires a path"
      REPO_ROOT="$2"
      shift 2
      ;;
    --help|-h)
      usage
      exit "$EXIT_OK"
      ;;
    *)
      fail "$EXIT_INVALID_INPUT" "INVALID_INPUT: unknown argument: $1"
      ;;
  esac
done

if [[ -z "$REPO_ROOT" ]]; then
  REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || true)"
fi
[[ -n "$REPO_ROOT" ]] || fail "$EXIT_INVALID_INPUT" "INVALID_INPUT: run inside a KFM checkout or pass --repo-root"
REPO_ROOT="$(cd "$REPO_ROOT" 2>/dev/null && pwd -P)" || fail "$EXIT_INVALID_INPUT" "INVALID_INPUT: repository path does not exist"

required_paths=(
  "package.json"
  "pnpm-lock.yaml"
  "pnpm-workspace.yaml"
  "pyproject.toml"
  "apps/explorer-web/package.json"
  "packages/maplibre/package.json"
  ".env.example"
)
for relative_path in "${required_paths[@]}"; do
  [[ -f "$REPO_ROOT/$relative_path" ]] || fail "$EXIT_INVALID_INPUT" "INVALID_INPUT: missing repository marker $relative_path"
done

cd "$REPO_ROOT"

read_pnpm_version() {
  local value
  value="$(sed -nE 's/.*"packageManager"[[:space:]]*:[[:space:]]*"pnpm@([^"]+)".*/\1/p' package.json | head -n 1)"
  [[ -n "$value" ]] || return 2
  printf '%s\n' "$value"
}

version_at_least() {
  local actual="$1"
  local minimum="$2"
  python3 - "$actual" "$minimum" <<'PY'
import sys

def parts(value: str) -> tuple[int, ...]:
    try:
        return tuple(int(item) for item in value.split("."))
    except ValueError:
        raise SystemExit(2)

raise SystemExit(0 if parts(sys.argv[1]) >= parts(sys.argv[2]) else 1)
PY
}

load_nvm() {
  export NVM_DIR="${NVM_DIR:-$HOME/.nvm}"
  if [[ -s "$NVM_DIR/nvm.sh" ]]; then
    # shellcheck source=/dev/null
    . "$NVM_DIR/nvm.sh"
  fi
}

command_version_or_missing() {
  local command_name="$1"
  shift
  if command -v "$command_name" >/dev/null 2>&1; then
    "$command_name" "$@" 2>/dev/null | head -n 1
  else
    printf 'MISSING'
  fi
}

inspect() {
  local node_target pnpm_target node_actual python_actual git_origin
  node_target="$LOCAL_NODE_VERSION"
  pnpm_target="$(read_pnpm_version)" || fail "$EXIT_INVALID_INPUT" "INVALID_INPUT: packageManager must be pnpm@<exact-version>"
  load_nvm
  node_actual="$(command_version_or_missing node --version)"
  python_actual="$(command_version_or_missing python3 --version)"
  git_origin="$(git remote get-url origin 2>/dev/null || printf 'UNSET')"

  cat <<EOF_PLAN
KFM local workstation inspection
--------------------------------
Outcome: DRY_RUN
Repository: $REPO_ROOT
Recommended path: $RECOMMENDED_INSTALL_ROOT
Canonical remote: $CANONICAL_REPOSITORY
Current origin: $git_origin
Platform: $(uname -s 2>/dev/null || printf 'UNKNOWN')
Target Node: $node_target
Current Node: $node_actual
Target pnpm: $pnpm_target
Current pnpm shim: $(command -v pnpm >/dev/null 2>&1 && printf 'PRESENT (version check deferred)' || printf 'MISSING')
Python requirement: >=3.11
Current Python: $python_actual
Virtual environment: $([[ -x .venv/bin/python ]] && printf 'PRESENT' || printf 'ABSENT')
Locked Node dependencies: $([[ -d node_modules ]] && printf 'PRESENT' || printf 'ABSENT')
Local environment file: $([[ -f .env ]] && printf 'PRESENT' || printf 'ABSENT (will copy safe template)')
Ollama command: $(command -v ollama >/dev/null 2>&1 && printf 'PRESENT' || printf 'MISSING')
Model-runtime posture: mock by default; Ollama remains subordinate to the Governed API

Apply effects (only with --apply):
- may use the network through nvm, Corepack/pnpm, and pip;
- may install Node $node_target inside the existing user-owned nvm directory;
- enables Corepack shims inside that user-owned Node installation;
- creates or updates repository-local node_modules and .venv;
- copies .env.example to ignored .env only when .env is absent;
- never commits, pushes, opens a pull request, changes system packages, or exposes a service.
EOF_PLAN
}

require_linux() {
  [[ "$(uname -s)" == "Linux" ]] || fail "$EXIT_UNSUPPORTED" "UNSUPPORTED: this bootstrap currently supports Linux only"
}

require_python() {
  command -v python3 >/dev/null 2>&1 || fail "$EXIT_BLOCKED" "BLOCKED: python3 is required"
  local python_version
  python_version="$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:3])))')"
  version_at_least "$python_version" "3.11" || fail "$EXIT_UNSUPPORTED" "UNSUPPORTED: Python >=3.11 is required; found $python_version"
}

require_git_checkout() {
  command -v git >/dev/null 2>&1 || fail "$EXIT_BLOCKED" "BLOCKED: git is required"
  git rev-parse --is-inside-work-tree >/dev/null 2>&1 || fail "$EXIT_INVALID_INPUT" "INVALID_INPUT: repository root is not a Git checkout"
}

require_clean_tracked_tree() {
  local status
  status="$(git status --porcelain --untracked-files=no)" || fail "$EXIT_BLOCKED" "BLOCKED: Git could not inspect the tracked worktree"
  if [[ -n "$status" ]]; then
    fail "$EXIT_BLOCKED" "BLOCKED: commit or stash tracked changes before --apply"
  fi
}

reject_local_root_symlinks() {
  local path
  for path in .venv node_modules .env; do
    [[ ! -L "$path" ]] || fail "$EXIT_BLOCKED" "BLOCKED: $path must not be a symbolic link"
  done
}

require_ignored_local_outputs() {
  local path
  for path in ".venv/" "node_modules/" ".env"; do
    git check-ignore -q "$path" || fail "$EXIT_BLOCKED" "BLOCKED: $path must remain ignored before local setup"
  done
}

require_private_env() {
  .venv/bin/python - <<'PY_PERMISSIONS' || fail "$EXIT_BLOCKED" "BLOCKED: .env must deny group and other permissions"
from pathlib import Path
import stat

mode = stat.S_IMODE(Path(".env").stat().st_mode)
raise SystemExit(0 if mode & 0o077 == 0 else 1)
PY_PERMISSIONS
}

activate_node() {
  local target="$1"
  local allow_install="$2"
  load_nvm

  if command -v nvm >/dev/null 2>&1; then
    if [[ "$allow_install" == "yes" ]]; then
      nvm install "$target" || fail "$EXIT_BLOCKED" "BLOCKED: nvm could not install Node $target"
    fi
    nvm use --silent "$target" >/dev/null 2>&1 || fail "$EXIT_BLOCKED" "BLOCKED: Node $target is not installed in nvm; run --apply"
  fi

  command -v node >/dev/null 2>&1 || fail "$EXIT_BLOCKED" "BLOCKED: Node is missing; install nvm in your user account, then rerun --apply"
  local actual
  actual="$(node --version)"
  actual="${actual#v}"
  [[ "$actual" == "$target" ]] || fail "$EXIT_UNSUPPORTED" "UNSUPPORTED: expected Node $target, found $actual; use the local bootstrap pin"
}

activate_pnpm() {
  local target="$1"
  local allow_download="$2"
  command -v corepack >/dev/null 2>&1 || fail "$EXIT_BLOCKED" "BLOCKED: Corepack is missing from the selected Node installation"

  if [[ "$allow_download" == "yes" ]]; then
    corepack enable || fail "$EXIT_BLOCKED" "BLOCKED: Corepack could not enable the pnpm shim"
  fi

  command -v pnpm >/dev/null 2>&1 || fail "$EXIT_BLOCKED" "BLOCKED: pnpm shim is missing; run --apply"
  local actual
  if [[ "$allow_download" == "yes" ]]; then
    actual="$(pnpm --version)" || fail "$EXIT_BLOCKED" "BLOCKED: Corepack could not resolve the pinned pnpm version"
  else
    actual="$(COREPACK_ENABLE_NETWORK=0 pnpm --version)" || fail "$EXIT_BLOCKED" "BLOCKED: pinned pnpm is not available offline; run --apply"
  fi
  [[ "$actual" == "$target" ]] || fail "$EXIT_UNSUPPORTED" "UNSUPPORTED: expected pnpm $target, found $actual"
}

install_python_dependencies() {
  python3 -m venv .venv || fail "$EXIT_BLOCKED" "BLOCKED: Python venv support is unavailable"
  mapfile -t requirements < <(
    .venv/bin/python - <<'PY'
from pathlib import Path
import tomllib

project = tomllib.loads(Path("pyproject.toml").read_text(encoding="utf-8"))["project"]
for requirement in project.get("dependencies", []):
    print(requirement)
for requirement in project.get("optional-dependencies", {}).get("test", []):
    print(requirement)
PY
  )
  ((${#requirements[@]} > 0)) || fail "$EXIT_INVALID_INPUT" "INVALID_INPUT: no Python dependencies found in pyproject.toml"
  .venv/bin/python -m pip install --disable-pip-version-check "${requirements[@]}" || fail "$EXIT_BLOCKED" "BLOCKED: Python dependency installation failed"
}

apply() {
  require_linux
  require_git_checkout
  require_clean_tracked_tree
  reject_local_root_symlinks
  require_ignored_local_outputs
  require_python

  local node_target pnpm_target
  node_target="$LOCAL_NODE_VERSION"
  pnpm_target="$(read_pnpm_version)" || fail "$EXIT_INVALID_INPUT" "INVALID_INPUT: packageManager must be pnpm@<exact-version>"

  printf 'KFM_LOCAL_BOOTSTRAP: APPLY repository=%s\n' "$REPO_ROOT"
  printf 'KFM_LOCAL_BOOTSTRAP: network-enabled package installation was explicitly selected\n'
  activate_node "$node_target" "yes"
  activate_pnpm "$pnpm_target" "yes"

  install_python_dependencies
  pnpm install --frozen-lockfile || fail "$EXIT_BLOCKED" "BLOCKED: locked pnpm installation failed"

  if [[ ! -e .env ]]; then
    install -m 600 .env.example .env || fail "$EXIT_BLOCKED" "BLOCKED: could not create .env"
    printf 'KFM_LOCAL_BOOTSTRAP: created ignored .env from .env.example\n'
  else
    printf 'KFM_LOCAL_BOOTSTRAP: preserved existing .env\n'
  fi

  printf 'KFM_LOCAL_BOOTSTRAP: APPLY_COMPLETE; running bounded verification\n'
  verify
}

verify() {
  require_linux
  require_git_checkout
  reject_local_root_symlinks
  require_ignored_local_outputs
  require_python

  local node_target pnpm_target
  node_target="$LOCAL_NODE_VERSION"
  pnpm_target="$(read_pnpm_version)" || fail "$EXIT_INVALID_INPUT" "INVALID_INPUT: packageManager must be pnpm@<exact-version>"
  activate_node "$node_target" "no"
  activate_pnpm "$pnpm_target" "no"

  [[ -x .venv/bin/python ]] || fail "$EXIT_BLOCKED" "BLOCKED: .venv is missing; run --apply"
  [[ -d node_modules ]] || fail "$EXIT_BLOCKED" "BLOCKED: node_modules is missing; run --apply"
  [[ -f .env ]] || fail "$EXIT_BLOCKED" "BLOCKED: .env is missing; run --apply or copy .env.example"
  require_private_env

  .venv/bin/python - <<'PY' || fail "$EXIT_VALIDATION_FAILED" "VALIDATION_FAILED: one or more declared Python modules are unavailable"
import importlib
for module in ("jsonschema", "rfc3339_validator", "rfc8785", "yaml", "hypothesis", "pytest"):
    importlib.import_module(module)
PY

  export COREPACK_ENABLE_NETWORK=0
  set +e
  bash -n scripts/dev/bootstrap.sh scripts/dev/ollama-readiness.sh && \
    .venv/bin/python -m pytest -q tests/test_local_dev_bootstrap.py apps/governed-api/tests && \
    pnpm --filter @kfm/maplibre test && \
    pnpm --filter explorer-web build && \
    pnpm --filter explorer-web test:unit && \
    git diff --check
  local status=$?
  set -e

  ((status == 0)) || fail "$EXIT_VALIDATION_FAILED" "VALIDATION_FAILED: one or more bounded local checks failed"
  printf 'KFM_LOCAL_BOOTSTRAP: SUCCESS\n'
  printf 'Explorer: pnpm run local:explorer -> http://127.0.0.1:5173/\n'
  printf 'Governed API: pnpm run local:api -> http://127.0.0.1:8080/\n'
  printf 'Qwen readiness: pnpm run local:qwen:verify (diagnostic only; runtime remains mock)\n'
}

case "$MODE" in
  inspect)
    inspect
    ;;
  apply)
    apply
    ;;
  verify)
    verify
    ;;
  *)
    fail "$EXIT_INVALID_INPUT" "INVALID_INPUT: unsupported mode"
    ;;
esac
