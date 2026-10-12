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
selector, approval or unrelated smoke-script change from that PR is imported.
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
