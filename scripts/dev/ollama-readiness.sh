#!/usr/bin/env bash
# Read-only local Ollama/Qwen readiness probe for KFM development.
# It never sends a prompt, invokes generation, changes KFM runtime posture, or pulls a model.
set -euo pipefail

MODE="inspect"
MODEL="${KFM_LOCAL_OLLAMA_MODEL:-qwen3:14b}"
HOST="${OLLAMA_HOST:-http://127.0.0.1:11434}"
TIMEOUT="3"

usage() {
  cat <<'USAGE'
Usage: scripts/dev/ollama-readiness.sh [--inspect | --verify] [options]

Modes:
  --inspect          Validate configuration and print the planned read-only probe.
  --verify           GET the loopback-only Ollama /api/tags endpoint and check a model.

Options:
  --host URL         Ollama base URL (default: OLLAMA_HOST or http://127.0.0.1:11434)
  --model NAME       Exact local model name (default: qwen3:14b)
  --timeout SECONDS  Network timeout from 1 through 30 (default: 3)
  --help             Show this help.

Exit codes:
  0  SUCCESS or DRY_RUN
  2  INVALID_INPUT
  4  BLOCKED because Ollama or the requested model is unavailable
  5  VALIDATION_FAILED because the local response is malformed or oversized
USAGE
}

while (($# > 0)); do
  case "$1" in
    --inspect)
      MODE="inspect"
      shift
      ;;
    --verify)
      MODE="verify"
      shift
      ;;
    --host)
      (($# >= 2)) || { printf 'KFM_OLLAMA_READINESS: INVALID_INPUT: --host requires a URL\n' >&2; exit 2; }
      HOST="$2"
      shift 2
      ;;
    --model)
      (($# >= 2)) || { printf 'KFM_OLLAMA_READINESS: INVALID_INPUT: --model requires a name\n' >&2; exit 2; }
      MODEL="$2"
      shift 2
      ;;
    --timeout)
      (($# >= 2)) || { printf 'KFM_OLLAMA_READINESS: INVALID_INPUT: --timeout requires seconds\n' >&2; exit 2; }
      TIMEOUT="$2"
      shift 2
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      printf 'KFM_OLLAMA_READINESS: INVALID_INPUT: unknown argument: %s\n' "$1" >&2
      exit 2
      ;;
  esac
done

python3 - "$MODE" "$HOST" "$MODEL" "$TIMEOUT" <<'PY'
from __future__ import annotations

import ipaddress
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request

EXIT_INVALID_INPUT = 2
EXIT_BLOCKED = 4
EXIT_VALIDATION_FAILED = 5
MAX_RESPONSE_BYTES = 2 * 1024 * 1024
MODEL_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._/+-]{0,127}(?::[A-Za-z0-9][A-Za-z0-9._+-]{0,63})?$")


def stop(code: int, outcome: str, detail: str) -> None:
    print(f"KFM_OLLAMA_READINESS: {outcome}: {detail}", file=sys.stderr)
    raise SystemExit(code)


def normalize_base_url(raw: str) -> str:
    try:
        parsed = urllib.parse.urlsplit(raw)
    except ValueError:
        stop(EXIT_INVALID_INPUT, "INVALID_INPUT", "OLLAMA_HOST is not a valid URL")

    if parsed.scheme != "http":
        stop(EXIT_INVALID_INPUT, "INVALID_INPUT", "only loopback HTTP is allowed")
    if parsed.username is not None or parsed.password is not None:
        stop(EXIT_INVALID_INPUT, "INVALID_INPUT", "credentials are forbidden in OLLAMA_HOST")
    if parsed.query or parsed.fragment:
        stop(EXIT_INVALID_INPUT, "INVALID_INPUT", "query strings and fragments are forbidden")
    if parsed.path not in ("", "/"):
        stop(EXIT_INVALID_INPUT, "INVALID_INPUT", "OLLAMA_HOST must not contain an API path")

    hostname = parsed.hostname
    if hostname is None:
        stop(EXIT_INVALID_INPUT, "INVALID_INPUT", "OLLAMA_HOST has no hostname")
    if hostname != "localhost":
        try:
            if not ipaddress.ip_address(hostname).is_loopback:
                stop(EXIT_INVALID_INPUT, "INVALID_INPUT", "Ollama must remain loopback-only")
        except ValueError:
            stop(EXIT_INVALID_INPUT, "INVALID_INPUT", "Ollama hostname must be localhost or a loopback address")

    try:
        port = parsed.port
    except ValueError:
        stop(EXIT_INVALID_INPUT, "INVALID_INPUT", "OLLAMA_HOST port is invalid")
    if port is not None and not 1 <= port <= 65535:
        stop(EXIT_INVALID_INPUT, "INVALID_INPUT", "OLLAMA_HOST port is outside 1..65535")

    display_host = f"[{hostname}]" if ":" in hostname else hostname
    authority = display_host if port is None else f"{display_host}:{port}"
    return f"http://{authority}"


if len(sys.argv) != 5:
    stop(EXIT_INVALID_INPUT, "INVALID_INPUT", "internal argument count mismatch")

mode, host, model, raw_timeout = sys.argv[1:]
if mode not in {"inspect", "verify"}:
    stop(EXIT_INVALID_INPUT, "INVALID_INPUT", "mode must be inspect or verify")
if not MODEL_NAME.fullmatch(model):
    stop(EXIT_INVALID_INPUT, "INVALID_INPUT", "model name is empty or unsafe")
try:
    timeout = int(raw_timeout)
except ValueError:
    stop(EXIT_INVALID_INPUT, "INVALID_INPUT", "timeout must be an integer")
if not 1 <= timeout <= 30:
    stop(EXIT_INVALID_INPUT, "INVALID_INPUT", "timeout must be from 1 through 30 seconds")

base_url = normalize_base_url(host)
tags_url = f"{base_url}/api/tags"

if mode == "inspect":
    print("KFM Ollama/Qwen readiness inspection")
    print("------------------------------------")
    print("Outcome: DRY_RUN")
    print(f"Loopback endpoint: {tags_url}")
    print(f"Requested model: {model}")
    print("Planned request: one bounded GET to /api/tags")
    print("Generation requests: none")
    print("Model downloads: none")
    print("KFM runtime change: none; KFM_MODEL_RUNTIME remains mock")
    raise SystemExit(0)

request = urllib.request.Request(
    tags_url,
    headers={"Accept": "application/json", "User-Agent": "kfm-local-readiness/1"},
    method="GET",
)


class DenyRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # type: ignore[no-untyped-def]
        stop(EXIT_VALIDATION_FAILED, "VALIDATION_FAILED", "local Ollama endpoint returned a redirect")


opener = urllib.request.build_opener(
    urllib.request.ProxyHandler({}),
    DenyRedirects(),
)
try:
    with opener.open(request, timeout=timeout) as response:
        body = response.read(MAX_RESPONSE_BYTES + 1)
except (urllib.error.URLError, TimeoutError, OSError) as error:
    stop(EXIT_BLOCKED, "BLOCKED", f"local Ollama /api/tags is unavailable ({type(error).__name__})")

if len(body) > MAX_RESPONSE_BYTES:
    stop(EXIT_VALIDATION_FAILED, "VALIDATION_FAILED", "local Ollama response exceeded 2 MiB")
try:
    payload = json.loads(body.decode("utf-8"))
except (UnicodeDecodeError, json.JSONDecodeError):
    stop(EXIT_VALIDATION_FAILED, "VALIDATION_FAILED", "local Ollama response is not valid UTF-8 JSON")
if not isinstance(payload, dict) or not isinstance(payload.get("models"), list):
    stop(EXIT_VALIDATION_FAILED, "VALIDATION_FAILED", "local Ollama response has no models array")

names: set[str] = set()
for item in payload["models"]:
    if not isinstance(item, dict):
        stop(EXIT_VALIDATION_FAILED, "VALIDATION_FAILED", "models array contains a non-object")
    for key in ("name", "model"):
        value = item.get(key)
        if isinstance(value, str):
            names.add(value)

if model not in names:
    stop(EXIT_BLOCKED, "BLOCKED", f"model {model} is not installed; operator next step: ollama pull {model}")

print("KFM_OLLAMA_READINESS: SUCCESS")
print(f"Endpoint: {tags_url}")
print(f"Model present: {model}")
print("Generation requests: none")
print("KFM runtime posture: unchanged (mock)")
PY
