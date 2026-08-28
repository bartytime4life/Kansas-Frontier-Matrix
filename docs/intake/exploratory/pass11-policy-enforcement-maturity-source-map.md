# Pass 11 Policy-Enforcement Maturity — Source Map

Status: **PROPOSED**, exploratory adaptation only.

The attached *KFM Components Pass 11 — Idea Index, Category Atlas, and Expansion Dossier* identifies OPA/Rego and Conftest as central policy-gate tools while warning that policy design must not be presented as mounted enforcement. Its `OPS-02` expansion direction calls for documenting maturity in five layers: designed, tested, merge-blocking, promotion-blocking, and runtime-enforced.

This slice implements only the evidence vocabulary, fixture matrix, validator, tests, workflow, and generated authoring receipt for those maturity claims. It does not add a Rego rule, change policy meaning, alter branch protection, mark a check required, approve promotion, activate runtime enforcement, release, deploy, or publish.

## Acceptance boundary

- maturity stages are ordered and cumulative;
- each stage requires the matching evidence kind;
- leapfrogged or overstated claims return `DENY`;
- malformed, noncanonical, or identity-incoherent assessments return `ERROR`;
- supported assessments return `PASS`;
- CI remains read-only and the repository-owned tests perform no network access.

Placement follows accepted Directory Rules v2 and ADR-0029. The source dossier remains planning input and does not become policy or runtime authority through this adaptation.
