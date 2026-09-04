from __future__ import annotations

import contextlib
import json
import re
import subprocess
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Iterator

REPO_ROOT = Path(__file__).resolve().parents[1]
BOOTSTRAP = REPO_ROOT / "scripts" / "dev" / "bootstrap.sh"
OLLAMA_READINESS = REPO_ROOT / "scripts" / "dev" / "ollama-readiness.sh"


def _run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
        timeout=15,
    )


def test_local_shell_helpers_have_valid_bash_syntax() -> None:
    result = _run("bash", "-n", str(BOOTSTRAP), str(OLLAMA_READINESS))
    assert result.returncode == 0, result.stderr


def test_bootstrap_inspect_is_read_only_and_reports_canonical_path() -> None:
    before = _run("git", "status", "--porcelain").stdout
    result = _run(
        "bash",
        str(BOOTSTRAP),
        "--inspect",
        "--repo-root",
        str(REPO_ROOT),
    )
    after = _run("git", "status", "--porcelain").stdout

    assert result.returncode == 0, result.stderr
    assert "Outcome: DRY_RUN" in result.stdout
    assert "~/src/Kansas-Frontier-Matrix" not in result.stdout
    assert f"{Path.home()}/src/Kansas-Frontier-Matrix" in result.stdout
    assert "Model-runtime posture: mock by default" in result.stdout
    assert before == after


def test_bootstrap_rejects_unknown_arguments() -> None:
    result = _run("bash", str(BOOTSTRAP), "--not-a-mode")
    assert result.returncode == 2
    assert "INVALID_INPUT" in result.stderr


def test_bootstrap_has_no_privileged_or_direct_remote_installer_path() -> None:
    text = BOOTSTRAP.read_text(encoding="utf-8")
    forbidden = (
        r"\bsudo\b",
        r"\bcurl\b",
        r"\bwget\b",
        r"npm\s+(?:install|i)\s+-g",
        r"git\s+push",
        r"gh\s+pr",
        r"/usr/(?:local/)?bin/(?!env\b)",
    )
    for pattern in forbidden:
        assert re.search(pattern, text) is None, pattern


def test_bootstrap_guards_ignored_local_state_and_private_environment() -> None:
    text = BOOTSTRAP.read_text(encoding="utf-8")
    assert 'for path in ".venv/" "node_modules/" ".env"' in text
    assert 'git check-ignore -q "$path"' in text
    assert "mode & 0o077 == 0" in text
    assert text.count("require_ignored_local_outputs") >= 3  # definition, apply, verify


def test_local_versions_are_consistent_with_repository_manifests() -> None:
    bootstrap_text = BOOTSTRAP.read_text(encoding="utf-8")
    match = re.search(
        r'^readonly LOCAL_NODE_VERSION="([0-9]+\.[0-9]+\.[0-9]+)"$',
        bootstrap_text,
        re.MULTILINE,
    )
    assert match is not None
    node_version = match.group(1)
    root_manifest = json.loads((REPO_ROOT / "package.json").read_text(encoding="utf-8"))
    explorer_manifest = json.loads(
        (REPO_ROOT / "apps" / "explorer-web" / "package.json").read_text(
            encoding="utf-8"
        )
    )
    maplibre_manifest = json.loads(
        (REPO_ROOT / "packages" / "maplibre" / "package.json").read_text(
            encoding="utf-8"
        )
    )

    major, minor, _patch = (int(item) for item in node_version.split("."))
    assert major == 22 and minor >= 13
    assert root_manifest["engines"]["node"] == ">=22.13 <23"
    assert explorer_manifest["engines"]["node"] == root_manifest["engines"]["node"]
    assert root_manifest["packageManager"] == "pnpm@11.17.0"
    assert maplibre_manifest["dependencies"]["maplibre-gl"] == "6.6.0"


def test_local_package_commands_preserve_loopback_and_governed_api_boundary() -> None:
    scripts = json.loads((REPO_ROOT / "package.json").read_text(encoding="utf-8"))[
        "scripts"
    ]
    assert scripts["local:explorer"].endswith("--host 127.0.0.1 --port 5173")
    assert "KFM_API_BIND=127.0.0.1" in scripts["local:api"]
    assert "KFM_API_PORT=8080" in scripts["local:api"]
    assert "qwen3:14b" in scripts["local:qwen:verify"]
    assert "OLLAMA_HOST" not in scripts["local:explorer"]


def test_ollama_inspect_is_read_only_and_never_uses_generation_endpoint() -> None:
    text = OLLAMA_READINESS.read_text(encoding="utf-8")
    result = _run("bash", str(OLLAMA_READINESS), "--inspect")

    assert result.returncode == 0, result.stderr
    assert "Outcome: DRY_RUN" in result.stdout
    assert "/api/tags" in result.stdout
    assert "Generation requests: none" in result.stdout
    assert "/api/chat" not in text
    assert "ollama pull" in text  # operator guidance only; the helper never executes it


@contextlib.contextmanager
def _fake_ollama(payload: object, *, raw: bytes | None = None) -> Iterator[str]:
    requests: list[str] = []
    body = raw if raw is not None else json.dumps(payload).encode("utf-8")

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802 - stdlib handler API
            requests.append(self.path)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, _format: str, *args: object) -> None:
            return

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        host, port = server.server_address
        yield f"http://{host}:{port}"
        assert requests == ["/api/tags"]
    finally:
        server.shutdown()
        thread.join(timeout=5)
        server.server_close()


def test_ollama_verify_finds_exact_qwen_model_without_generation() -> None:
    payload = {"models": [{"name": "qwen3:14b", "model": "qwen3:14b"}]}
    with _fake_ollama(payload) as host:
        result = _run(
            "bash",
            str(OLLAMA_READINESS),
            "--verify",
            "--host",
            host,
            "--model",
            "qwen3:14b",
        )

    assert result.returncode == 0, result.stderr
    assert "KFM_OLLAMA_READINESS: SUCCESS" in result.stdout
    assert "KFM runtime posture: unchanged (mock)" in result.stdout


def test_ollama_verify_reports_missing_model_as_blocked() -> None:
    with _fake_ollama({"models": []}) as host:
        result = _run(
            "bash",
            str(OLLAMA_READINESS),
            "--verify",
            "--host",
            host,
            "--model",
            "qwen3:14b",
        )

    assert result.returncode == 4
    assert "BLOCKED" in result.stderr
    assert "ollama pull qwen3:14b" in result.stderr


def test_ollama_verify_rejects_malformed_local_response() -> None:
    with _fake_ollama({}, raw=b"not-json") as host:
        result = _run(
            "bash",
            str(OLLAMA_READINESS),
            "--verify",
            "--host",
            host,
        )

    assert result.returncode == 5
    assert "VALIDATION_FAILED" in result.stderr


@contextlib.contextmanager
def _redirecting_local_endpoint() -> Iterator[str]:
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:  # noqa: N802 - stdlib handler API
            self.send_response(302)
            self.send_header("Location", "http://127.0.0.1:9/api/tags")
            self.end_headers()

        def log_message(self, _format: str, *args: object) -> None:
            return

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        host, port = server.server_address
        yield f"http://{host}:{port}"
    finally:
        server.shutdown()
        thread.join(timeout=5)
        server.server_close()


def test_ollama_verify_rejects_redirects_without_following_them() -> None:
    with _redirecting_local_endpoint() as host:
        result = _run(
            "bash",
            str(OLLAMA_READINESS),
            "--verify",
            "--host",
            host,
        )

    assert result.returncode == 5
    assert "redirect" in result.stderr


def test_ollama_non_loopback_host_is_rejected_before_request() -> None:
    result = _run(
        "bash",
        str(OLLAMA_READINESS),
        "--verify",
        "--host",
        "http://0.0.0.0:11434",
    )
    assert result.returncode == 2
    assert "loopback-only" in result.stderr
