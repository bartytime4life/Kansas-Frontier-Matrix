<div align="center">
Kansas Frontier Matrix — Automation &
Governance
.github/workflows/README.md
Mission: Document the GitHub-based automation (CI/CD) and project governance practices for the
Kansas Frontier Matrix (KFM). This includes continuous integration workflows, branch management
strategy, compliance checks, and roles/responsibilities — ensuring all code, data, and documentation
changes are validated, auditable, and aligned with MCP principles.
Build & Deploy
STAC Validated
CodeQL Passed
Trivy 🛡 Passed
Pre-Commit
Docs · MCP-DL v6.3
License: MIT | CC-BY 4.0
</div>
<details><summary>📚 Table of Contents</summary>
• Overview
• CI/CD Workflow Overview
• Validation Flow (CI Lifecycle)
• ⚙ Core Workflows
• 🛡 Governance & Roles
•
•
•
•
•
MCP Compliance Matrix
Contribution Notes
Metadata & Provenance
Related Documentation
Version History
</details>
1Overview
The Automation & Governance system of KFM ensures that every change to code, data, or documentation
is automatically validated, securely reviewed, and transparently recorded. It comprises a suite of
GitHub Actions workflows for continuous integration/deployment (CI/CD), combined with rigorous branch
policies and role-based reviews. Key goals of this system are to:
• Maintain integrity – CI workflows check data checksums, STAC metadata compliance, and test
results for every pull request 1 2 .
• Enforce reproducibility – All pipelines and builds are deterministic, with environment consistency
and Makefile targets to reproduce any CI run locally 2 3 .
• 🔒 Ensure security – Automated CodeQL and Trivy scans detect vulnerabilities in code and
dependencies 4 5 . Protected branches and secret scanning prevent unauthorized changes 6 .
• Track provenance – Every workflow outputs logs and artifacts (e.g. validation reports, build logs)
archived under version control for auditability 7 8 .
• 🏛 Uphold governance – Branch protections (required reviews, semantic commits, signed commits)
and CODEOWNERS rules involve the right experts for each change, aligning with MCP governance
standards 9 10 .
All automation is implemented via GitHub Actions workflows in this repository, with results visible through
status badges (above) and in the GitHub Actions console. The sections below detail each workflow, the
branch strategy for changes, and how these enforce the Master Coder Protocol (MCP) principles.
CI/CD Workflow Overview
flowchart TD
A[" Commit / Pull Request"] --> B["⚙ Pre-Commit Hooks\n(code style & lint
checks)"]
B --> C["
CI Validation\n(STAC metadata, Checksums, Tests)"]
C --> D[" Security Scanning\n(CodeQL analysis, Trivy audit)"]
D --> E["📦 Build & Deploy\n(Static site docs, web viewer)"]
E --> F["Publish Artifacts\n(GitHub Pages site, Data Catalog)"]
F --> G["Logs & Reports\nstored under version control"]
style A fill:#f8f9fa,stroke:#777;
style B fill:#eef7ff,stroke:#0077cc;
style C fill:#fff0f5,stroke:#cc0088;
style D fill:#ecf9f0,stroke:#33aa33;
style E fill:#fffbea,stroke:#e8a500;
style F fill:#f0e8ff,stroke:#8844cc;
style G fill:#f9f9f9,stroke:#555;
<!-- END OF MERMAID -->
2Workflow Pipeline: Every push or pull request triggers a sequence of automated checks.
Pre-commit hooks run first (linting, formatting), followed by CI validation jobs (checksums
verification, STAC metadata validation, etc.), then security scans, and finally if on the main
branch, a build and deployment of documentation and the web app 11 12 . All results are
logged and any failure will prevent promotion of the code change.
Validation Flow (CI Lifecycle)
sequenceDiagram
participant Dev as Developer (PR)
participant GA as GitHub Actions
participant CI as CI Workflows
participant CD as CD Deploy
Dev->>GA: Push commits / Open Pull Request
GA->>CI: Run **Pre-Commit** checks (lint & format)
CI-->>Dev:
Failures block merge (fix & commit)
CI->>CI: Run **Checksums** workflow (data integrity)
CI->>CI: Run **STAC Validate** workflow (metadata)
CI->>CI: Run **CodeQL** and **Trivy** security scans
CI->>CD: Run **Site Build & Deploy** on `main` branch
CD->>GA: Upload site, artifacts & logs
GA->>Dev: Report status checks & results
<!-- END OF MERMAID -->
Lifecycle: On each PR, the system ensures code and data quality before any merge. All
required checks (✔ pre-commit, data validation, security scans) must pass on the
development branch PR. Only then can changes be merged, after which the deployment
workflow publishes updates for end-users 2 13 . This guarantees that the main branch is
always in a deployable, validated state.
⚙ Core Workflows
All CI/CD automation is defined in the .github/workflows/ directory (YAML files). Key workflows
include:
WorkflowRoleTrigger
Pre-
CommitEnforces code style,
linting, and formatting.On every PR
commit
3
Validation / Tasks
Runs pre-commit hooks
( black , ruff , etc.) to ensure
coding standards
2
.WorkflowRoleTriggerValidation / Tasks
STAC
ValidateValidates all STAC Items,
Collections, and JSON
metadata.On PRs and
pushesUses stac-validator and JSON
Schema to check dataset metadata
compliance 14 .
ChecksumsComputes & verifies
SHA-256 hashes for all
processed data files.On data updatescompares outputs to detect any
data tampering 14 .
Scheduled (daily/
CRON) or manual
dispatchDownloads sources listed in data/
Fetch DataFetches raw data from
external sources as
defined in manifests.Site BuildBuilds and deploys the
documentation site and
web application.On merge to
mainExecutes static site generator
(MkDocs/Jekyll) and publishes to
GitHub Pages 16 .
CodeQLPerforms static code
analysis for vulnerabilities.Weekly and on
PRsGitHub CodeQL scans the
repository for security issues
(OWASP queries, etc.) 17 .
TrivyScans container images
and dependencies for
known CVEs.Weekly (cron)Trivy CLI audits dependency
manifests and Docker images for
vulnerabilities 18 .
Auto MergeAutomatically merges PRs
that pass all required
checks.After CI success
on PR
Runs make checksums and
sources/*.json and validates
manifest structure 15
2
.
Uses GitHub Actions to auto-merge
approved PRs into target branch
(e.g. dev ), if all status checks are
green.
.github/workflows/
├── README.md# Workflow documentation index (this file)
├── pre-commit.yml# Lint & format checks on PRs
├── stac-validate.yml# STAC metadata validation pipeline
├── checksums.yml# Data integrity verification pipeline
├── fetch.yml# Data acquisition from external sources
├── site.yml# Build & deploy static docs and web app
├── codeql.yml# Static analysis security scan
├── trivy.yml# Container and dependency vulnerability scan
└── auto-merge.yml# Auto-merge bot for PRs after checks
Workflow Catalog: The above directory structure outlines all automated workflows. Each
workflow is isolated but orchestrated together through triggers and sequential dependencies
(e.g. CI must pass before Auto Merge). Detailed logs for these runs are saved under data/
work/logs/ci/ for posterity
7
8
equivalent Makefile targets (e.g.
site ) to reproduce CI results
3
. Contributors can also run these tasks locally via the
make checksums ,
.
4
make stac-validate ,
make🛡 Governance & Roles
Effective governance of the KFM project is achieved by combining automation with clear human roles and
responsibilities:
• Branch Strategy: The repository uses a two-tier branch model. All development happens on the
dev branch, via feature or fix branches merged into dev through pull requests. The main
branch is protected for release – only updated from
dev
after thorough testing and
documentation of a release. Both dev and main are protected branches (require pull requests,
approved reviews, and passing checks for any merge) 19
pipeline from initial code to production release.
20 .
This strategy ensures an audited
• Protected Commits: Branch protection rules enforce “quality gates”:
• At least 1 approved review by a code owner or maintainer is required to merge into dev or main
.
• All required CI checks (see above workflows) must succeed before merging.
• Signed commits are required on protected branches (GPG or SSH signature)
9
9
.
• Semantic commit messages (Conventional Commits style) are encouraged and in some cases
required for certain subsystems, to feed into changelogs and provenance tracking 21 22 .
• CODEOWNERS & Reviews: The repository defines a CODEOWNERS policy mapping areas to
responsible teams. For example, changes under /docs/standards/ must be approved by the
Documentation Team and Security Team, while any change to .github/** (CI workflows)
requires approval from the Security Team 23 . This ensures domain experts review critical changes.
GitHub will automatically request reviews from these owners on each PR.
• Role Structure: Project contributors are organized into teams, each with distinct responsibilities in
the governance process:
Role / TeamResponsibilities
Project MaintainersOversee repository health, approve and merge pull requests, and cut
releases on main . Ensure that development policies are followed and
coordinate across teams.
Security Team (@kfm-
security)
Documentation Team
(@kfm-docs)
Review all security-sensitive changes (code, workflows, dependencies). Must
approve CI workflow edits, dependency updates, and any potential security
impact. Implements branch protection and monitors vulnerability scan
results.
Ensure all changes are accompanied by updated documentation. Review
edits to docs/ and metadata. Enforce the MCP documentation standards
(proper front-matter, version history, etc.).
5Role / TeamResponsibilities
Core Developers
(@kfm-core)Implement new features and fixes in code and data pipelines. Write tests,
adhere to coding standards, and participate in peer code reviews.
QA / Data Team (@qa-
team, @data-team)Validate data outputs and pipeline results. Cross-check that new data or
models meet quality standards. This team may also own specific domain
pipelines (e.g. Data Engineering Team for ETL jobs) and ensure their
correctness.
Governance
CommitteeCross-functional group (lead maintainers from each team) that periodically
audits compliance with MCP, reviews the backlog 24 25 , and plans releases.
They ensure that the project as a whole remains transparent, well-
documented, and aligned with its mission.
Governance Checks: In addition to automated CI checks, there are regular human-in-the-
loop checks. For example, the Governance Committee conducts a biweekly backlog review
and a quarterly audit of documentation and metadata to ensure everything has proper
provenance 24 25 . Prior to a release, maintainers follow a checklist verifying that version
numbers are updated, license attributions are in place, and all datasets are accounted for in
the STAC catalog. These governance practices complement automation to uphold KFM’s
standards.
MCP Compliance Matrix
The Kansas Frontier Matrix’s automation and governance are designed from the ground up to comply with
the Master Coder Protocol (MCP) principles. The table below summarizes how each MCP principle is
implemented in practice:
MCP PrincipleImplementation in Workflows & Governance
Documentation-
firstEvery workflow and config change is accompanied by updated documentation or
inline comments. PR templates require documenting any user-facing change. All
modules have up-to-date READMEs before code merges 22 26 .
ReproducibilityCI pipelines use pinned versions for dependencies and provide Makefile targets
for local replication of all steps 3 . Data artifacts include checksums; anyone can
fetch and validate datasets via the same scripts used in CI.
Open StandardsWorkflows and data formats rely on open standards: pipeline definitions in YAML,
metadata in JSON/STAC, diagrams in Mermaid, etc. 27 28 . This maximizes
transparency and interoperability of the processes.
Every CI run logs outputs to versioned files (e.g., ci_build.log , validation
Provenance
reports) with timestamps and commit hashes 8 . The git history and backlog
link each change to an author and purpose 24 29 . CODEOWNERS ensure
authoritative sign-off. All documents carry authorship, date, and version info (see
below).
6MCP Principle
Auditability
Implementation in Workflows & Governance
Strict branch protections and required checks mean every change is reviewed and
traceable. CI artifacts (logs, reports, SBOMs) are retained under data/work/
logs/ for external audit
8
. Regular governance audits (e.g., verifying all STAC
entries and checksums quarterly) provide additional oversight.
Each principle is thus not only a philosophy but a concrete part of the KFM development workflow. This
alignment with MCP guarantees that the system remains maintainable, trustworthy, and verifiable over
time 30
31 .
Contribution Notes
We welcome contributions from team members and the community. To maintain the quality and
consistency of the KFM project, please observe the following guidelines:
• Development Branch: Fork or create a feature branch off of dev for your work. Submit Pull
Requests targeting the dev branch (not main ). Ensure your branch is up-to-date with the latest
dev to avoid merge conflicts.
• Issue Tracking: If your contribution addresses an existing issue or backlog item, mention it in your
PR description (e.g., “Closes #123” or references a B-2025-XYZ backlog ID). New significant
features should ideally have a corresponding issue or backlog entry for traceability.
• Coding Standards: Follow the project’s coding conventions and style. Run pre-commit locally to
catch lint and format issues before pushing 9 . Code should be accompanied by tests when
applicable.
• Documentation: All changes must include updates to relevant documentation. This could mean
updating a README, architecture doc, or code comments. Remember that KFM follows a
documentation-first approach – if adding a new module or dataset, add docs (or at least an outline)
for it as part of your PR.
• Semantic Commits: Use descriptive commit messages. We prefer Conventional Commit style (e.g.,
feat: add new climate data pipeline or fix: correct checksum validation
logic ). This helps with auto-generating changelogs and understanding history. Squash small fix
commits into logical units before merge.
• Pull Request Template: Fill out the PR template (if provided) to detail the purpose of your change,
how to test it, and any impacts on docs or data. This helps reviewers follow your thought process
and verify all aspects.
Pull Request Checklist: Before requesting a review or merging, double-check the following (our PR
template includes similar items):
• [ ] All pre-commit hooks pass locally (formatting, linting, security checks).
• [ ] Documentation is updated (relevant README or docs sections) to reflect your changes.
• [ ] Tests (unit tests or manual run-through of workflows) have been added or updated for any new/
changed functionality.
• [ ] CI checks are all green. (You can click on the details of each status check at the bottom of your PR to
see logs.)
7• [ ] Reviewers assigned: Ensure appropriate team members (based on CODEOWNERS or expertise)
are requested for review.
• [ ] Semantic commit messages: Squash or amend commits to follow conventions if needed, and
ensure commits are signed (if you have signing set up).
• [ ] Linked issues/backlog: Include references to issue IDs or backlog entries that your PR addresses,
for traceability.
Following these guidelines helps speed up the review process and maintains the high standard of quality
and reproducibility for the Kansas Frontier Matrix. Thank you for contributing!
Metadata & Provenance
This document is maintained under the Master Coder Protocol Documentation Lifecycle (MCP-DL v6.3)
compliance rules. All changes to it are tracked in version control for full transparency. Key metadata:
• License: Code portions of this repository are released under the MIT License, and documentation
content is released under CC-BY 4.0. See the LICENSE file for details.
• Version: This document is currently at v1.1 (as of 2025-10-16), reflecting the latest format and
compliance updates.
• Changelog: See the Version History section below for a summary of changes. All historical revisions
of this file can be explored via the Git history in GitHub.
By adhering to MCP-DL standards, we ensure that this README (and all documentation) remains auditable,
versioned, and linked to the broader provenance chain of the project.
Related Documentation
PathDescription
docs/architecture/ci-
cd.mdCI/CD Architecture – in-depth overview of pipelines and automation.
docs/standards/
security.mdSecurity & Access Standards – details on branch protection, secrets, etc.
docs/notes/backlog.mdProject Backlog – tasks and enhancements tracked with provenance
(governance in action).
.github/CODEOWNERSCODEOWNERS file – defines code ownership and required reviewers for
different parts of the repo.
8Version History
Version
Date
v1.1
v1.0
AuthorSummary
2025-10-16KFM Documentation
& Governance TeamStyle overhaul – Reformatted README to KFM house
style (emoji headers, centered title block, TOC).
Added Metadata & Provenance and Contribution
Notes sections; improved badge labels and relative
links for consistency.
2025-10-04KFM Documentation
& Governance TeamInitial release of GitHub Automation & Governance
README, describing all CI workflows, branch
strategy, and compliance standards.
<div align="center">
Kansas Frontier Matrix — “Automation with Integrity. Validation with Provenance.”
.github/workflows/README.md · GitHub workflows & project governance documentation for the
Kansas Frontier Matrix.
</div>
1
2
3
4
5
6
7
8
11
12
13
14
15
16
17
18
19
20
31
ci-cd.md
https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/9fcfe24783aab696f5ea160eb79d230c1666a60b/docs/architecture/
ci-cd.md
9
10
23
security.md
https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/9fcfe24783aab696f5ea160eb79d230c1666a60b/docs/standards/
security.md
21
28
30
ARCHITECTURE.md
https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/9fcfe24783aab696f5ea160eb79d230c1666a60b/
ARCHITECTURE.md
22
README.md
https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/9fcfe24783aab696f5ea160eb79d230c1666a60b/docs/README.md
24
25
29
backlog.md
https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/9fcfe24783aab696f5ea160eb79d230c1666a60b/docs/notes/
backlog.md
26
27
documentation.md
https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/9fcfe24783aab696f5ea160eb79d230c1666a60b/docs/standards/
documentation.md
9
