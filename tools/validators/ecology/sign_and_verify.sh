#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'EOF'
Usage:
  tools/validators/ecology/sign_and_verify.sh sign [repo-root]
  tools/validators/ecology/sign_and_verify.sh verify [repo-root]

Environment for keyless verification:
  COSIGN_CERT_IDENTITY       e.g. name@example.com
  COSIGN_CERT_OIDC_ISSUER    e.g. https://accounts.google.com or https://github.com/login/oauth

Optional key mode:
  COSIGN_KEY                 path or KMS URI for signing/verifying with --key
EOF
}

cmd="${1:-}"
root="${2:-.}"
proof_dir="$root/data/proofs"
bundle_dir="$proof_dir/cosign"
validator="$root/tools/validators/ecology/validate_run.py"

require_bin() {
  command -v "$1" >/dev/null 2>&1 || { echo "missing required command: $1" >&2; exit 127; }
}

case "$cmd" in
  sign)
    require_bin cosign
    mkdir -p "$bundle_dir"
    if [[ -n "${COSIGN_KEY:-}" ]]; then
      cosign sign-blob "$proof_dir/evidencebundle.json" --key "$COSIGN_KEY" --bundle "$bundle_dir/evidencebundle.bundle"
      cosign sign-blob "$proof_dir/decision_log.json" --key "$COSIGN_KEY" --bundle "$bundle_dir/decision_log.bundle"
      signed_by="key:$COSIGN_KEY"
    else
      cosign sign-blob "$proof_dir/evidencebundle.json" --bundle "$bundle_dir/evidencebundle.bundle"
      cosign sign-blob "$proof_dir/decision_log.json" --bundle "$bundle_dir/decision_log.bundle"
      signed_by="${COSIGN_CERT_IDENTITY:-keyless-oidc}"
    fi
    python3 "$validator" record-signature --root "$root" --signed-by "$signed_by"
    ;;
  verify)
    require_bin cosign
    if [[ -n "${COSIGN_KEY:-}" ]]; then
      cosign verify-blob "$proof_dir/evidencebundle.json" --key "$COSIGN_KEY" --bundle "$bundle_dir/evidencebundle.bundle"
      cosign verify-blob "$proof_dir/decision_log.json" --key "$COSIGN_KEY" --bundle "$bundle_dir/decision_log.bundle"
    else
      : "${COSIGN_CERT_IDENTITY:?set COSIGN_CERT_IDENTITY for keyless verification}"
      : "${COSIGN_CERT_OIDC_ISSUER:?set COSIGN_CERT_OIDC_ISSUER for keyless verification}"
      cosign verify-blob "$proof_dir/evidencebundle.json" --bundle "$bundle_dir/evidencebundle.bundle" \
        --certificate-identity "$COSIGN_CERT_IDENTITY" \
        --certificate-oidc-issuer "$COSIGN_CERT_OIDC_ISSUER"
      cosign verify-blob "$proof_dir/decision_log.json" --bundle "$bundle_dir/decision_log.bundle" \
        --certificate-identity "$COSIGN_CERT_IDENTITY" \
        --certificate-oidc-issuer "$COSIGN_CERT_OIDC_ISSUER"
    fi
    python3 "$validator" validate --root "$root"
    ;;
  -h|--help|help|"")
    usage
    ;;
  *)
    usage >&2
    exit 64
    ;;
esac
