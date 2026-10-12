<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-infra-readme
title: tests/infra/ — Infrastructure Static-Test Boundary
type: README
version: v0.4
status: repository-grounded; one-module-inventory; static-only; non-authoritative
owners: OWNER_TBD — Infrastructure steward · QA steward · Security reviewer · CI steward · Release steward
created: 2026-07-29
updated: 2026-09-25
policy_label: repository-facing; tests; infrastructure; docker; compose; static; local-files-only; non-publisher
owning_root: tests/
responsibility: executable static checks for bounded Docker and Compose review inputs without becoming infrastructure, security, runtime, deployment, release, or publication authority
truth_posture: CONFIRMED one direct static test module, three source-defined unittest methods, one Compose workflow binding, and one related security workflow / UNKNOWN runtime parity and operational deployment
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
evidence_base_ref: main
evidence_base_commit: 5d835798e09a4dd14735779cb44206a8a3e8b2d3
evidence_prior_blob: cf59e18a27f90d8bdb015bd92fc6a45614c9ab83
direct_test_module_count: 1
source_defined_test_count: 3
direct_workflow_binding_count: 1
related:
  - ../README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../infra/README.md
  - ../../infra/compose/README.md
  - ../../infra/docker/README.md
  - ./test_compose_static.py
  - ../../.github/workflows/infra-compose-smoke.yml
  - ../../.github/workflows/security.yml
notes:
  - "Counts describe the current source-defined static checks, not runtime or deployment evidence."
  - "KFM_NO_NETWORK records intent; the module reads local files only."
  - "Passing tests or workflows do not authorize review, release, deployment, promotion, publication, or public exposure."
[/KFM_META_BLOCK_V2] -->

# Infrastructure static tests

The remaining [`test_compose_static.py`](test_compose_static.py) tests the
payload-free Governed API Compose placeholder. It checks that the declared
build context and Dockerfile exist, the final image user is non-root, the
published port is loopback-only, and selected privileged or sensitive inputs
are absent. The former Explorer Web image test was retired with that app.

Run from the repository root:

```bash
python -m unittest discover --start-directory tests/infra --pattern 'test_*.py' --verbose
```

The [`infra-compose-smoke`](../../.github/workflows/infra-compose-smoke.yml)
workflow runs this static suite, renders Compose, and builds the remaining
review image. The [`security`](../../.github/workflows/security.yml) workflow
scans the image. Neither workflow starts an application or proves deployed
behavior, source admission, release, or publication.
