from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class SigningSettings:
    enabled: bool = False
    mode: str = "keyless"
    certificate_identity: str = ""
    certificate_identity_regexp: str = ""
    certificate_oidc_issuer: str = "https://token.actions.githubusercontent.com"
    key: str = ""
    public_key: str = ""

    @classmethod
    def from_mapping(cls, data: dict[str, Any] | None) -> "SigningSettings":
        data = data or {}
        return cls(
            enabled=bool(data.get("enabled", False)),
            mode=str(data.get("mode", "keyless")),
            certificate_identity=str(data.get("certificate_identity", "")),
            certificate_identity_regexp=str(data.get("certificate_identity_regexp", "")),
            certificate_oidc_issuer=str(data.get("certificate_oidc_issuer", "https://token.actions.githubusercontent.com")),
            key=str(data.get("key", "")),
            public_key=str(data.get("public_key", "")),
        )


@dataclass(slots=True)
class RunnerSettings:
    max_changes_per_run: int = 10
    batch_size: int = 5
    max_workers: int = 4
    token_rate_per_minute: float = 1.0
    token_burst: int = 3
    max_download_bytes: int = 25 * 1024 * 1024
    max_retries: int = 5
    backoff_base_seconds: int = 2
    backoff_max_seconds: int = 300
    fail_on_missing_http_validators: bool = True
    meta_dir: str = ".last_meta"
    queue_path: str = ".queue/watcher.events.jsonl"
    dlq_path: str = ".queue/dlq.events.jsonl"
    state_dir: str = ".state"
    work_dir: str = "WORK"
    receipts_dir: str = "receipts"
    signing: SigningSettings = field(default_factory=SigningSettings)

    @classmethod
    def from_mapping(cls, data: dict[str, Any] | None) -> "RunnerSettings":
        data = data or {}
        return cls(
            max_changes_per_run=int(data.get("max_changes_per_run", 10)),
            batch_size=int(data.get("batch_size", 5)),
            max_workers=int(data.get("max_workers", 4)),
            token_rate_per_minute=float(data.get("token_rate_per_minute", 1.0)),
            token_burst=int(data.get("token_burst", 3)),
            max_download_bytes=int(data.get("max_download_bytes", 25 * 1024 * 1024)),
            max_retries=int(data.get("max_retries", 5)),
            backoff_base_seconds=int(data.get("backoff_base_seconds", 2)),
            backoff_max_seconds=int(data.get("backoff_max_seconds", 300)),
            fail_on_missing_http_validators=bool(data.get("fail_on_missing_http_validators", True)),
            meta_dir=str(data.get("meta_dir", ".last_meta")),
            queue_path=str(data.get("queue_path", ".queue/watcher.events.jsonl")),
            dlq_path=str(data.get("dlq_path", ".queue/dlq.events.jsonl")),
            state_dir=str(data.get("state_dir", ".state")),
            work_dir=str(data.get("work_dir", "WORK")),
            receipts_dir=str(data.get("receipts_dir", "receipts")),
            signing=SigningSettings.from_mapping(data.get("signing")),
        )


@dataclass(slots=True)
class SourceSpec:
    source_id: str
    url: str
    download_key: str
    source_version: str = "v1"
    domain: str = "unknown"
    policy_label: str = "restricted"
    rights_status: str = "controlled"
    artifact_name: str = ""
    validators: list[str] = field(default_factory=list)
    headers: dict[str, str] = field(default_factory=dict)
    allow_missing_http_validators: bool = False

    @classmethod
    def from_mapping(cls, data: dict[str, Any]) -> "SourceSpec":
        if not data.get("source_id"):
            raise ValueError("source.source_id is required")
        if not data.get("url"):
            raise ValueError(f"source.url is required for {data.get('source_id')}")
        url = str(data["url"])
        return cls(
            source_id=str(data["source_id"]),
            url=url,
            download_key=str(data.get("download_key", url)),
            source_version=str(data.get("source_version", "v1")),
            domain=str(data.get("domain", "unknown")),
            policy_label=str(data.get("policy_label", "restricted")),
            rights_status=str(data.get("rights_status", "controlled")),
            artifact_name=str(data.get("artifact_name", "")),
            validators=list(data.get("validators", [])),
            headers={str(k): str(v) for k, v in dict(data.get("headers", {})).items()},
            allow_missing_http_validators=bool(data.get("allow_missing_http_validators", False)),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class ProbeResult:
    status: int
    etag: str | None = None
    last_modified: str | None = None
    content_length: int | None = None
    content_type: str | None = None
    error: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class ChangeEvent:
    source_id: str
    prev_spec_hash: str | None
    next_spec_hash: str
    material: bool
    reason: str
    high_risk: bool
    seen_at: str
    attempt_count: int = 0
    available_at: str | None = None

    @classmethod
    def from_mapping(cls, data: dict[str, Any]) -> "ChangeEvent":
        return cls(
            source_id=str(data["source_id"]),
            prev_spec_hash=data.get("prev_spec_hash"),
            next_spec_hash=str(data["next_spec_hash"]),
            material=bool(data.get("material", True)),
            reason=str(data.get("reason", "changed")),
            high_risk=bool(data.get("high_risk", False)),
            seen_at=str(data.get("seen_at", "")),
            attempt_count=int(data.get("attempt_count", 0)),
            available_at=data.get("available_at"),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def load_config(path: str | Path) -> tuple[RunnerSettings, dict[str, SourceSpec]]:
    import json

    with Path(path).open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    settings = RunnerSettings.from_mapping(data.get("runner", {}))
    sources = [SourceSpec.from_mapping(item) for item in data.get("sources", [])]
    if not sources:
        raise ValueError("config must include at least one source")
    by_id = {src.source_id: src for src in sources}
    if len(by_id) != len(sources):
        raise ValueError("source_id values must be unique")
    return settings, by_id
