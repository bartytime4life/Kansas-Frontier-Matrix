# EBIRD Layer 22 Remediation

Layer 22 adds **copy-on-write corrective remediation governance** for public-safe eBird aggregates.

## CLIs
- `kfm-ebird-remediate`
- `kfm-ebird-corrective-release`

## Key rules
- No network calls, no credentials, no real eBird data.
- Apply mode requires `--apply --force`.
- Remediation defaults to copy-on-write.
- Public outputs must keep `public_safe=true`, `exact_points=restricted`, and suppression >= 10.
- Blocked classes (data-affecting, hash recipe changes, governed predicate changes) require full rerun planning.

## IDs
- `remediation_id`: sha256 over canonical remediation inputs (no timestamps), first 16 hex.
- `corrective_release_id`: sha256 over canonical corrective release inputs (no timestamps), first 16 hex.

## Outputs
Remediation writes: plan, manifest, diff report, root cause report, validation report, optional receipt.
Corrective release writes: plan, manifest, validation report, optional approval receipt.

## Safety
Public artifacts must never include exact coordinates, restricted paths, suppression receipt details, suppressed group hashes, raw row numbers, or secrets.
