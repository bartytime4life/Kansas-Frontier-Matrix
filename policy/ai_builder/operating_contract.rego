# KFM AI Build Operating Contract — OPA policy stub
#
# Status: PROPOSED v3.0 (companion to docs/doctrine/ai-build-operating-contract.md §47)
# Engine: Open Policy Agent (Rego v1)
# Purpose: Encode the contract's MUST and MUST-NOT rules as machine-checkable predicates so
#          CI can fail a PR that violates them without relying on reviewer judgment alone.
#
# This file is a stub. Each rule below is a starting point; stewards SHOULD refine the
# predicates against the actual repo evidence before treating any CI signal as authoritative.
#
# Inputs (PROPOSED shape — to be finalized by ADR; see §49 Q3 / §50 item 30):
#   input.pr.files              list of changed file paths
#   input.pr.diff_stat          { added, modified, deleted, renamed }
#   input.pr.is_ai_authored     boolean
#   input.pr.generated_receipt  GENERATED_RECEIPT.json object (or null)
#   input.pr.body               PR body text
#   input.pr.labels             list of PR labels
#   input.repo.adrs             list of accepted ADR ids
#   input.repo.directory_rules  parsed directory-rules.md metadata
#   input.repo.contract_version current pinned CONTRACT_VERSION

package kfm.ai_builder.operating_contract

import rego.v1

contract_version := "3.0.0"

# ─────────────────────────────────────────────────────────────────────────────
# §1.7 / §11 — Directory and placement
# ─────────────────────────────────────────────────────────────────────────────

# §11.3: parallel-home prohibition. New top-level folders that look like
# duplicate authority homes for schemas/contracts/policy/data are denied
# unless an ADR explicitly authorizes them.
forbidden_root_prefixes := {
    "jsonschema/",
    "policies/",
    "source-registry/",
    "releases-new/",
    "proofs-new/",
}

deny contains msg if {
    some f in input.pr.files
    some prefix in forbidden_root_prefixes
    startswith(f, prefix)
    not adr_authorizes_parallel_home(prefix)
    msg := sprintf("§11.3 parallel-home prohibition: file %q under %q lacks an authorizing ADR", [f, prefix])
}

# §11.1: domain-named root folders are denied. Topics live INSIDE responsibility roots.
domain_topics := {
    "hydrology", "soil", "fauna", "flora", "archaeology", "roads", "hazards",
    "settlements", "atmosphere", "agriculture", "geology", "habitat", "people",
    "DNA", "land", "rail", "trade",
}

deny contains msg if {
    some f in input.pr.files
    parts := split(f, "/")
    count(parts) > 1
    topic := lower(parts[0])
    topic in domain_topics
    msg := sprintf("§11.1 topic-as-root: %q starts with topic folder %q — choose a responsibility root", [f, parts[0]])
}

# §11.4: schema home convention.
warn contains msg if {
    some f in input.pr.files
    endswith(f, ".schema.json")
    not startswith(f, "schemas/contracts/v1/")
    msg := sprintf("§11.4 schema-home: %q is not under schemas/contracts/v1/; confirm ADR if intentional", [f])
}

adr_authorizes_parallel_home(prefix) if {
    some adr in input.repo.adrs
    adr.scope.parallel_home == prefix
    adr.status == "accepted"
}

# ─────────────────────────────────────────────────────────────────────────────
# §34 — GENERATED_RECEIPT contract
# ─────────────────────────────────────────────────────────────────────────────

# §34.2: AI-authored PRs MUST carry a GENERATED_RECEIPT.json.
deny contains msg if {
    input.pr.is_ai_authored == true
    input.pr.generated_receipt == null
    msg := "§34.2 receipt required: AI-authored PR lacks a GENERATED_RECEIPT.json"
}

# §34.3: receipt MUST pin contract_version, and it MUST match what the repo expects.
deny contains msg if {
    receipt := input.pr.generated_receipt
    receipt != null
    receipt.contract_version != contract_version
    msg := sprintf(
        "§34.3 contract_version mismatch: receipt declares %q, repo expects %q",
        [receipt.contract_version, contract_version]
    )
}

# §34.4: receipt is mergeable only when human_review.state is approved OR override_record is set.
deny contains msg if {
    receipt := input.pr.generated_receipt
    receipt != null
    receipt.human_review.state != "approved"
    receipt.override_record == null
    msg := "§34.4 unmergeable receipt: human_review.state is not approved and no override_record present"
}

# §34.4 cont'd: if any artifact touches policy/schemas/registry/release, policy_decisions MUST be non-empty.
policy_significant_prefixes := {
    "policy/",
    "schemas/contracts/v1/",
    "data/registry/",
    "release/",
}

deny contains msg if {
    receipt := input.pr.generated_receipt
    receipt != null
    some artifact in receipt.artifact_paths
    some prefix in policy_significant_prefixes
    startswith(artifact, prefix)
    count(receipt.policy_decisions) == 0
    msg := sprintf(
        "§34.4 policy_decisions required: artifact %q touches policy-significant lane %q but receipt lists no PolicyDecisions",
        [artifact, prefix]
    )
}

# §34.7: model identity must include provider, model, and version (no generic names).
deny contains msg if {
    receipt := input.pr.generated_receipt
    receipt != null
    not receipt.model_identity.version
    msg := "§34.7 anti-pattern: receipt model_identity missing version"
}

# ─────────────────────────────────────────────────────────────────────────────
# §27 — PR discipline
# ─────────────────────────────────────────────────────────────────────────────

# §27.1: PR body MUST contain the required preflight block. We check for a few load-bearing tokens.
required_pr_tokens := {
    "Goal:",
    "Status labels:",
    "Directory Rules basis:",
    "Validation:",
    "Rollback:",
}

deny contains msg if {
    some token in required_pr_tokens
    not contains(input.pr.body, token)
    msg := sprintf("§27.1 PR body missing required token: %q", [token])
}

# §27.2: PR MUST NOT mix unrelated roots without explanation. Heuristic: changes in
# 3+ different top-level responsibility roots without a "Cross-cutting:" note in the body.
deny contains msg if {
    roots := {root |
        some f in input.pr.files
        parts := split(f, "/")
        root := parts[0]
    }
    count(roots) >= 3
    not contains(input.pr.body, "Cross-cutting:")
    msg := sprintf("§27.2 cross-root sprawl: PR touches %d top-level roots without a Cross-cutting: note", [count(roots)])
}

# ─────────────────────────────────────────────────────────────────────────────
# §15 — Denied AI actions (selected machine-checkable rules)
# ─────────────────────────────────────────────────────────────────────────────

# §15.8: parallel canonical homes (already covered above for known prefixes).

# §15.13: no direct model client paths in browser-served code.
deny contains msg if {
    some f in input.pr.files
    startswith(f, "apps/web/")
    diff_contains_model_client(f)
    msg := sprintf("§15.13 trust membrane: %q appears to call a model runtime directly from browser code", [f])
}

# Placeholder predicate — wire to real diff inspection in CI.
diff_contains_model_client(_) if false

# §15.10: no RAW/WORK/QUARANTINE moves into PUBLISHED.
forbidden_source_to_published_moves := [
    {"from": "data/raw/", "to": "data/published/"},
    {"from": "data/work/", "to": "data/published/"},
    {"from": "data/quarantine/", "to": "data/published/"},
]

deny contains msg if {
    some r in forbidden_source_to_published_moves
    some f in input.pr.diff_stat.renamed
    startswith(f.from, r.from)
    startswith(f.to, r.to)
    msg := sprintf("§15.10 lifecycle violation: rename %s → %s bypasses promotion", [f.from, f.to])
}

# ─────────────────────────────────────────────────────────────────────────────
# §28 — ADR requirements (advisory: warn, don't deny)
# ─────────────────────────────────────────────────────────────────────────────

adr_triggers := {
    "data/raw":           "lifecycle phase boundary",
    "schemas/contracts/": "schema-home authority",
    "policy/sensitivity": "sensitive-location posture",
}

warn contains msg if {
    some trigger, reason in adr_triggers
    some f in input.pr.files
    startswith(f, trigger)
    not pr_has_adr_label
    msg := sprintf("§28 ADR check: %q touches %q (%s) without an ADR-XXXX label or linked ADR", [f, trigger, reason])
}

pr_has_adr_label if {
    some label in input.pr.labels
    startswith(label, "adr-")
}

# ─────────────────────────────────────────────────────────────────────────────
# Aggregation
# ─────────────────────────────────────────────────────────────────────────────

# A PR is admissible if and only if no deny messages fire.
admissible if count(deny) == 0

# CI summary helper — collect all messages into a single object.
report := {
    "admissible": admissible,
    "deny": deny,
    "warn": warn,
    "contract_version": contract_version,
}
