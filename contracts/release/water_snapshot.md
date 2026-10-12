# Water snapshot profile v1

Owning root: contracts; machine shapes reuse schemas/contracts/v1/release.
This bounded profile does not replace the general ReleaseManifest contract.
Canonical shapes: water_snapshot_manifest, water_snapshot and water_release_decision.

The immutable snapshot carries exactly four JSON texts: candidate, catalog,
validation and evidence. Exact UTF-8 artifact bytes are hashed; RFC 8785 hashes
the manifest without package_id. The package cannot approve itself. Local Python
and Site Worker preserve these bytes and use shared synthetic conformance fixtures.
Candidate and validation identities retain the existing Python canonical profile;
the Worker verifies exact artifact hashes and their cross-references, while
candidate schema/semantic validation belongs to Python preparation and review.
The local owner staging and activation operations require a caller-supplied
domain validator and compare the embedded validation receipt with its result.
The trusted operator must supply the canonical hydrology validator at both
transitions; the reusable release package does not import a pipeline. Rehashing a
different `PASS` receipt does not satisfy these transitions. The read-only
Python and Site projections retain their bounded carrier checks; this local
operator safeguard does not implement hosted review or authorize release.

Only separately trusted operator metadata can authorize reads. It binds the exact
package, six governance references, distinct reviewer/releaser, ordered UTC review/
release times, expiry, correction state and rollback. Client input never writes
this metadata. Missing evidence, invalid hashes, inactive verification, withdrawal,
expiry and nonpublic/review-required bundles omit response data. A staged package
is not active. Activation is atomic compare-and-swap and retains the previous ID.
Local rehearsal mechanics are separate from read-only API code and acquisition.

Versioned reads compose the unchanged closed RuntimeResponseEnvelope as
`{envelope,data}`. Never add arbitrary payload properties to the envelope.
Positive payloads include approval_expires_at; negative payloads omit data.
The general policy engine, signed remote release operator and hosted administrative
review workflow remain open; this contract does not imply their completion.
See [the runbook](../../docs/runbooks/water-pilot.md) for consumers, tests and rollback.
