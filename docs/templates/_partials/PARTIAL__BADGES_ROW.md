<!--
PARTIAL: BADGES ROW

Purpose
- Provide a consistent, copy/paste-friendly badges row for KFM docs and README-like pages.

How to use
- Include this partial inside the top-of-file IMPACT block.
- Keep the badge count small (<= ~8) so it stays readable.

Customization
- Replace the TODO_* values below in one place (this partial) OR (preferred) have your template
  generator rewrite this partial at build-time with repo-specific values.

Recommended values
- TODO_STATUS: experimental | active | stable | deprecated
- TODO_POLICY_LABEL: public | restricted | internal | ...
- TODO_LICENSE_SPDX: SPDX identifier (e.g., Apache-2.0, MIT)

Notes
- The static shields.io badges always render.
- Dynamic GitHub badges (CI / release) are provided as an optional block; they require a real
  repo slug + workflow filename.
-->

<p align="left">
  <!-- Core posture badges (static; safe defaults) -->
  <img alt="status" src="https://img.shields.io/badge/status-TODO_STATUS-orange" />
  <img alt="owners" src="https://img.shields.io/badge/owners-TODO_OWNERS-lightgrey" />
  <img alt="policy" src="https://img.shields.io/badge/policy-TODO_POLICY_LABEL-blue" />
  <img alt="evidence discipline" src="https://img.shields.io/badge/evidence-cite--or--abstain-informational" />
  <img alt="governance" src="https://img.shields.io/badge/governance-FAIR%20%2B%20CARE-informational" />
  <img alt="license" src="https://img.shields.io/badge/license-TODO_LICENSE_SPDX-lightgrey" />

  <!-- Optional dynamic badges (uncomment + fill in the TODOs) -->
  <!--
  <a href="https://github.com/TODO_REPO_SLUG/actions/workflows/TODO_CI_WORKFLOW">
    <img alt="CI" src="https://github.com/TODO_REPO_SLUG/actions/workflows/TODO_CI_WORKFLOW/badge.svg" />
  </a>
  <a href="https://github.com/TODO_REPO_SLUG/releases">
    <img alt="Release" src="https://img.shields.io/github/v/release/TODO_REPO_SLUG?sort=semver" />
  </a>
  -->
</p>
