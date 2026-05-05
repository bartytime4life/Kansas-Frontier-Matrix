from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass
from pathlib import Path

from .models import SigningSettings


@dataclass(slots=True)
class CosignResult:
    ok: bool
    command: list[str]
    stdout: str
    stderr: str


def _run(cmd: list[str]) -> CosignResult:
    try:
        proc = subprocess.run(cmd, check=False, text=True, capture_output=True)
        return CosignResult(proc.returncode == 0, cmd, proc.stdout, proc.stderr)
    except FileNotFoundError as exc:
        return CosignResult(False, cmd, "", f"cosign_not_found:{exc}")


def env_overlay(settings: SigningSettings) -> SigningSettings:
    """Allow CI/local env vars to override config without editing JSON."""
    return SigningSettings(
        enabled=settings.enabled or os.environ.get("KFM_SIGN", "").lower() in {"1", "true", "yes"},
        mode=os.environ.get("COSIGN_MODE", settings.mode),
        certificate_identity=os.environ.get("COSIGN_CERTIFICATE_IDENTITY", settings.certificate_identity),
        certificate_identity_regexp=os.environ.get("COSIGN_CERTIFICATE_IDENTITY_REGEXP", settings.certificate_identity_regexp),
        certificate_oidc_issuer=os.environ.get("COSIGN_CERTIFICATE_OIDC_ISSUER", settings.certificate_oidc_issuer),
        key=os.environ.get("COSIGN_KEY", settings.key),
        public_key=os.environ.get("COSIGN_PUBLIC_KEY", settings.public_key),
    )


def sign_blob(path: str | Path, bundle_path: str | Path, settings: SigningSettings) -> CosignResult:
    path = Path(path)
    bundle_path = Path(bundle_path)
    bundle_path.parent.mkdir(parents=True, exist_ok=True)
    cmd = ["cosign", "sign-blob", "--yes", "--bundle", str(bundle_path)]
    if settings.key:
        cmd.extend(["--key", settings.key])
    cmd.append(str(path))
    return _run(cmd)


def verify_blob(path: str | Path, bundle_path: str | Path, settings: SigningSettings) -> CosignResult:
    path = Path(path)
    bundle_path = Path(bundle_path)
    cmd = ["cosign", "verify-blob", str(path), "--bundle", str(bundle_path)]
    if settings.public_key:
        cmd.extend(["--key", settings.public_key])
    else:
        if settings.certificate_identity:
            cmd.append(f"--certificate-identity={settings.certificate_identity}")
        elif settings.certificate_identity_regexp:
            cmd.append(f"--certificate-identity-regexp={settings.certificate_identity_regexp}")
        else:
            return CosignResult(False, cmd, "", "missing_verification_identity")
        if not settings.certificate_oidc_issuer:
            return CosignResult(False, cmd, "", "missing_certificate_oidc_issuer")
        cmd.append(f"--certificate-oidc-issuer={settings.certificate_oidc_issuer}")
    return _run(cmd)


def sign_and_verify(path: str | Path, bundle_path: str | Path, settings: SigningSettings) -> tuple[CosignResult, CosignResult | None]:
    signed = sign_blob(path, bundle_path, settings)
    if not signed.ok:
        return signed, None
    verified = verify_blob(path, bundle_path, settings)
    return signed, verified
