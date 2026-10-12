# Site v252 mirror and review-image repair

This candidate starts from main `62479504bba719ca5da066b93febb8e37ab3faf8`.
Current-main water conformance rejected seven files whose bytes no longer
matched the selected v251 receipt: README, five Qwen scripts and the Qwen
knowledge test. The older receipt remains unchanged. This follow-up selects
an append-only receipt generated from the actual current mirror and exact
owner-private Site v252 source `190d16acb2f866cb9c2eb108dbd204ca30465269`.

## Reconciliation and boundaries

The authoritative v252 archive-authorization changes are copied exactly into
the mirror. They overlap eleven Site paths in open #5088; no obsolete receipt,
selector or approval from that PR is imported. The dependent smoke checks are
aligned with v252 owner authorization as described below.
Existing Qwen, companion-session, governed water/weather/soil/storm-event/
earthquake and release overlays remain in the repository. No file is deleted.
The receipt records 953 identical application paths, 29 inherited overlays,
67 repository-only paths and two canonical tool mappings. No Site path is
missing. Content parity does not approve the receipt or establish deployment
of repository-only overlays, data admission, activation or hosted equivalence.

Source geometry, public data, aquifer/Underground renderer, 2048/4096 detail,
units, source time and uncertainty semantics are unchanged. Site v252 remains
owner-only with the same project and DB/BUCKET declarations, deployment
`appgdep_6acc55fe0bb08191b36cbde3d61c1986`, environment revision 6. This follow-up
neither edits nor republishes its authoritative source or runtime settings.

## Container repair

The failing image is the application-free security-review placeholder, not a
running API or Site deployment. The reported packages are bundled inside pip;
the current PyPI pip wheel still names the reported versions in vendor.txt.
The top-level setuptools lock therefore does not repair those bundled copies.
After the hash-locked build-tool installation, remove pip and ensurepip's
bundled wheel from the final filesystem. The build checks both installers are
absent and that the locked setuptools/wheel/packaging versions remain installed.
Non-root execution, digest-pinned base, OS repair floors and the existing
HIGH/CRITICAL vulnerability/secret failure policy remain intact.

Pip remains a build-time bootstrap input. This final-image repair does not
claim every build-time dependency or historical image layer was remediated.
No scan ignore, severity reduction or baseline waiver is used. Local Docker
could not resolve the registry, so an actual hosted image build and the existing
Trivy scan are required before calling container verification complete.

## Validation and recovery

Standalone v252: build, TypeScript and 1,138 tests pass. Composed mirror: build,
TypeScript and 1,196 tests pass. Both lint runs have zero errors and 66 existing
warnings. Current-source parity, Python checks, browser and exact-head hosted
CI outcomes are recorded separately in the new receipt and accompanying PR.
No fresh exhaustive Site security scan or broad physical-device acceptance
is asserted.

The local copy uses a fresh v252 folder through the existing current alias and
port 4173 service. All 984 tracked source files and prepared build files are
checksum verified. The v251 folder and earlier recovery copies remain in place;
old immutable client assets are retained for open tabs. The v109 persisted
store is retained without a migration, reseed, capture or data activation.
Rollback points the alias back to v251 and restarts the existing service using
that store. Repository rollback reverts this follow-up and its selector;
container rollback reverts the Docker change and rebuilds the previous review
image. These operations do not roll back a governed data release.

Placement follows adopted Directory Rules v2 / ADR-0029: application mirror
under apps/site/source, exposure/build-image configuration under infra/docker,
review documentation under docs/reports and immutable recorded comparison
under data/receipts/generated, consumed by existing tools/qa/site_mirror.py.


Fresh installed-local browser verification rendered 50 records, 28 plotted
columns, one aquifer region and a complete 2048 × 1718 surface at zoom 13.4.
Partial coverage and one withheld unbounded class remain visible. No captured
console warnings or errors were returned. A bounded anonymous archive GET
returns 401, preserving v252 authorization rather than serving private content.
Twenty-three mirror/infra Python checks pass. The topology ratchet passes with
zero new drift/invariants and 93 inherited warnings; its baseline is unchanged.
The local copy includes 428 prepared build files and 44 retained prior assets.
Actual container repair verification remains the hosted exact-head scan.


Hosted Site CI initially failed only the local Worker smoke: the old script
expected an anonymous archive GET to return an empty catalog (200) and POST to
return its old CSRF denial (403). v252 denies both before storage access (401).
The script now requires that status and the explicit owner-access error text.
This repairs the dependent test rather than weakening archive authorization.
The actual hosted image build/scan and water conformance already passed at
head ac9ecf2891542c9475cf2ac76a490cb9eab1fd39; final-head execution is separate.


The isolated local Worker smoke passes all 103 checks across 74 routes after
the expectation fix (port 4189, fresh empty test store, no operator-store changes).
Owner merged #5097 at ac9ecf2891542c9475cf2ac76a490cb9eab1fd39 while that
fix was being pushed. That exact head had 108 successes, two skipped and one
Site smoke failure; do not call it fully passing. Its image build, container
scan, security-result and water-conformance passed. The small follow-up retains
that merge and updates only the dependent smoke expectations and this evidence.
Final follow-up CI execution is separate from the earlier successful scans.
