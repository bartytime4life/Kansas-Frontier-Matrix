# Development-tooling Zod collection validation correction

The mirror's eslint-plugin-react-hooks 7.1.1 dependency and its error formatter
resolve Zod 4.4.3. GHSA-mrhx-c7xc-m3w5 identifies versions below 4.6.6 as affected.
The selected caller is development lint tooling; this investigation does not
establish an application-request path to it or claim deployed-server protection.

Pin only that consumer's Zod resolution to official 4.6.6 through an
eslint-plugin-react-hooks override. Other package records, React 19.2.9,
framework versions and vendor archives are retained. There is no blanket 3.x
upgrade or unrelated audit-fix operation.

Four tiny local regressions exercise early upper-size gates for array max/length,
Set max and Map max. A preprocessing counter must remain zero for an oversized
collection; the error must be the single size error. They reproduce on 4.4.3.
Ordinary constrained values and the existing zod-validation-error formatter
are compatibility controls. Tests use two or three local items, without stress
payloads, server requests, private records, provider/model calls or memory-load
claims. Upstream patch: colinhacks/zod@a0ebf970f2d752e5f58527cd2942ff48be4f46bd.

The PR records the fresh audit, clean install, lint/build/type checks and test
results at its exact candidate. A clean lockfile audit is not a comprehensive
security assessment, alert dismissal or hosted/installed remediation evidence.

This follow-up builds on the mirror Flight binary-normalization correction so
its append-only receipt succeeds that exact inventory. Historical receipts,
original Site identity, all 262 withheld carriers, canonical mappings and
pending-review/false hosted-equivalence declarations remain. Implementations,
tests and docs stay in apps/site/source; receipt/selector/regression responsibilities
stay in data/receipts/generated, tools/qa and tests/qa under ADR-0029 and ADR-0048.

Revert this consumer override, lock entry, regression/document and successor
selector/QA as one unit, retaining all immutable receipts. That restores the
affected dependency and is not a security resolution. No merge, Site sync,
service install, configuration/data admission or publication is performed here.

Sources:
- https://github.com/advisories/GHSA-mrhx-c7xc-m3w5
- https://github.com/colinhacks/zod/commit/a0ebf970f2d752e5f58527cd2942ff48be4f46bd
