#!/usr/bin/env bash
# Bounded KFM developer bootstrap for Ubuntu 24.04.
#
# This script is local convenience only. It does not grant policy, evidence,
# release, deployment, or publication authority.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
MODE="apply"
PYTHON_ENABLED=1
NODE_ENABLED=1
OFFLINE=0
INSTALL_SYSTEM=0
INSTALL_HOOKS=1
JSON_OUTPUT=0

usage() {
  cat <<'EOF'
Usage: scripts/dev/bootstrap.sh [options]

Options:
  --check             Verify prerequisites without writing or installing.
  --python-only       Configure only the Python environment.
  --node-only         Configure only the Node/pnpm environment.
  --offline           Forbid network-backed dependency resolution.
  --install-system    Explicitly allow apt-get installation of missing base tools.
  --no-hooks          Do not install pre-commit hooks.
  --json              Emit a machine-readable environment receipt.
  -h, --help          Show this help.

Default apply mode creates/updates .venv, installs repository-pinned Python and
Node dependencies, and installs pre-commit hooks when pre-commit is available.
This script never invokes sudo. System packages change only when --install-system
is supplied from an already-root shell.
EOF
}

die() {
  printf 'bootstrap: %s\n' "$*" >&2
  exit 2
}

log() {
  if [[ "$JSON_OUTPUT" -eq 0 ]]; then
    printf 'bootstrap: %s\n' "$*"
  fi
}

command_path() {
  command -v "$1" 2>/dev/null || true
}

version_check() {
  local kind="$1"
  local version="$2"
  python3 - "$kind" "$version" <<'PY'
import re
import sys

kind, raw = sys.argv[1:3]
match = re.search(r"(\d+)\.(\d+)(?:\.(\d+))?", raw)
if not match:
    raise SystemExit(2)
version = tuple(int(part or 0) for part in match.groups())
if kind == "python":
    ok = version >= (3, 11, 0)
elif kind == "node":
    ok = (22, 13, 0) <= version < (23, 0, 0)
elif kind == "pnpm":
    ok = version == (11, 17, 0)
else:
    raise SystemExit(2)
raise SystemExit(0 if ok else 1)
PY
}

while (($#)); do
  case "$1" in
    --check) MODE="check" ;;
    --python-only) PYTHON_ENABLED=1; NODE_ENABLED=0 ;;
    --node-only) PYTHON_ENABLED=0; NODE_ENABLED=1 ;;
    --offline) OFFLINE=1 ;;
    --install-system) INSTALL_SYSTEM=1 ;;
    --no-hooks) INSTALL_HOOKS=0 ;;
    --json) JSON_OUTPUT=1 ;;
    -h|--help) usage; exit 0 ;;
    *) die "unknown argument: $1" ;;
  esac
  shift
done

[[ "$PYTHON_ENABLED" -eq 1 || "$NODE_ENABLED" -eq 1 ]] || die "no runtime selected"
cd "$ROOT"

OS_ID="unknown"
OS_VERSION="unknown"
if [[ -r /etc/os-release ]]; then
  # shellcheck disable=SC1091
  source /etc/os-release
  OS_ID="${ID:-unknown}"
  OS_VERSION="${VERSION_ID:-unknown}"
fi

if [[ "$OS_ID" != "ubuntu" || "$OS_VERSION" != "24.04" ]]; then
  die "supported bootstrap host is Ubuntu 24.04; observed ${OS_ID} ${OS_VERSION}"
fi

missing=()
for tool in git; do
  [[ -n "$(command_path "$tool")" ]] || missing+=("$tool")
done
if [[ "$PYTHON_ENABLED" -eq 1 && -z "$(command_path python3)" ]]; then
  missing+=("python3")
fi
if [[ "$NODE_ENABLED" -eq 1 && -z "$(command_path node)" ]]; then
  missing+=("nodejs")
fi

if ((${#missing[@]})); then
  if [[ "$INSTALL_SYSTEM" -ne 1 ]]; then
    die "missing base tools: ${missing[*]}; rerun with --install-system only after review"
  fi
  [[ "$EUID" -eq 0 ]] || die "--install-system requires an already-root shell; this script never invokes sudo"
  [[ "$OFFLINE" -eq 0 ]] || die "--install-system is incompatible with --offline"
  apt-get update
  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends "${missing[@]}"
fi

GIT_VERSION="$(git --version)"
PYTHON_VERSION="disabled"
NODE_VERSION="disabled"
PNPM_VERSION="disabled"

if [[ "$PYTHON_ENABLED" -eq 1 ]]; then
  PYTHON_VERSION="$(python3 --version 2>&1)"
  version_check python "$PYTHON_VERSION" || die "Python >=3.11 is required; observed $PYTHON_VERSION"
fi

if [[ "$NODE_ENABLED" -eq 1 ]]; then
  NODE_VERSION="$(node --version 2>&1)"
  version_check node "$NODE_VERSION" || die "Node >=22.13 and <23 is required; observed $NODE_VERSION"

  if [[ -z "$(command_path pnpm)" ]]; then
    if [[ "$MODE" == "check" || "$OFFLINE" -eq 1 ]]; then
      die "pnpm 11.17.0 is required and was not found"
    fi
    [[ -n "$(command_path corepack)" ]] || die "corepack is required to activate pnpm"
    corepack prepare pnpm@11.17.0 --activate
  fi
  PNPM_VERSION="$(pnpm --version 2>&1)"
  version_check pnpm "$PNPM_VERSION" || die "pnpm 11.17.0 is required; observed $PNPM_VERSION"
fi

if [[ "$MODE" == "apply" ]]; then
  if [[ "$PYTHON_ENABLED" -eq 1 ]]; then
    if [[ ! -x .venv/bin/python ]]; then
      python3 -m venv .venv
    fi
    pip_args=(install --require-virtualenv -e ".[test]")
    if [[ "$OFFLINE" -eq 1 ]]; then
      pip_args+=(--no-index)
    fi
    .venv/bin/python -m pip "${pip_args[@]}"
    if [[ "$INSTALL_HOOKS" -eq 1 ]]; then
      if [[ -x .venv/bin/pre-commit ]]; then
        .venv/bin/pre-commit install
      else
        die "pre-commit is not installed in .venv; use --no-hooks or add it to the accepted dev dependencies"
      fi
    fi
  fi

  if [[ "$NODE_ENABLED" -eq 1 ]]; then
    pnpm_args=(install --frozen-lockfile)
    if [[ "$OFFLINE" -eq 1 ]]; then
      pnpm_args+=(--offline)
    fi
    pnpm "${pnpm_args[@]}"
  fi
fi

if [[ "$JSON_OUTPUT" -eq 1 ]]; then
  python3 - "$MODE" "$OS_ID" "$OS_VERSION" "$GIT_VERSION" "$PYTHON_VERSION" "$NODE_VERSION" "$PNPM_VERSION" "$OFFLINE" "$PYTHON_ENABLED" "$NODE_ENABLED" <<'PY'
import json
import sys

(
    mode,
    os_id,
    os_version,
    git_version,
    python_version,
    node_version,
    pnpm_version,
    offline,
    python_enabled,
    node_enabled,
) = sys.argv[1:]
print(
    json.dumps(
        {
            "schema": "kfm.dev-bootstrap-receipt/v1",
            "mode": mode,
            "host": {"id": os_id, "version": os_version},
            "tools": {
                "git": git_version,
                "python": python_version,
                "node": node_version,
                "pnpm": pnpm_version,
            },
            "offline": offline == "1",
            "python_enabled": python_enabled == "1",
            "node_enabled": node_enabled == "1",
            "authority": "local-development-only",
        },
        sort_keys=True,
    )
)
PY
else
  log "completed ${MODE} mode for Ubuntu 24.04"
fi
