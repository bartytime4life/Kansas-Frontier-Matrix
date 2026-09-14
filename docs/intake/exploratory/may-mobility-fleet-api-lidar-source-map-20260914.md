# KFM May Mobility Fleet API LiDAR source map

**Checkpoint:** 2026-09-14  
**Provider surface:** [May Mobility Fleet API — LiDAR](https://docs.maymobility.com/docs/fleet-api/topics-channels/lidar/)  
**Repository base:** `main@6c5be18cf8448654be95a6db688d98546cd5276e`  
**Disposition:** `EXPLORATORY_RETAINED / RESTRICTED_PARTNER_TELEMETRY / HOLD / VALIDATED_BRANCH_ONLY`

> This record incorporates the public May Mobility LiDAR interface into KFM's source-role map. It does not provision an account, obtain credentials, call an endpoint, identify a vehicle, request a time interval, create or download a ROS bag, activate a connector, admit a source, open a pull request, release a layer, or publish data.

## Executive decision

May Mobility's Fleet API LiDAR surface is a vehicle-specific, recent-log retrieval service. It is not a public Kansas elevation source, a statewide terrain product, a LiDAR project catalog, or a browser-ready point-cloud service.

Its logical KFM role is narrow:

1. **Restricted partner telemetry:** a possible source of short mobile LiDAR observations from an explicitly authorized May Mobility vehicle and interval.
2. **Mobile reality capture:** a possible input for transportation, streetscape, autonomy-perception, accessibility, or bounded change-analysis research when purpose, rights, consent, sensitivity, and geography are approved.
3. **Transformation source:** a ROS bag may become a derived LAS/LAZ/COPC/EPT point-cloud artifact only after deterministic, offline processing preserves the sensor, time, frame, calibration, pose, rights, and uncertainty lineage.

The service must not be inserted into KFM's general terrain precedence ladder. USGS 3DEP and the responsible public steward remain the preferred authority for terrain and public elevation products. LiDAR Atlas remains a discovery/procurement candidate. GPXZ remains a derived elevation/composite comparison candidate. May Mobility remains vehicle telemetry.

## Source-role separation

| Surface | KFM role | What it must not become |
|---|---|---|
| USGS 3DEP / public LiDAR steward | Terrain and public collection authority for its exact product | A label silently transferred to unrelated mobile scans |
| LiDAR Atlas | Commercial project discovery and optional managed processing | Terrain authority or automatic source selector |
| GPXZ | Derived elevation-value, profile, raster, or composite comparison candidate | Primary Kansas terrain truth |
| May Mobility Fleet API LiDAR | Restricted vehicle-sensor log acquisition | Public terrain catalog, continuous live layer, or direct Explorer feed |
| KFM derived point-cloud pipeline | Deterministic conversion, validation, redaction, tiling, and release preparation | A source-authority substitute |

## Confirmed public behavior

The [LiDAR channel page](https://docs.maymobility.com/docs/fleet-api/topics-channels/lidar/) describes a two-step Batch API flow:

1. initiate generation with an endpoint shaped like `ENDPOINT/lidar?vehicle=...&startTime=...&endTime=...`;
2. receive the generated ROS bag filename;
3. download the named artifact through `ENDPOINT/download?filename=...`.

The page states:

- `vehicle` names the requested vehicle;
- `startTime` is required and must be at least one day old rather than from the current day;
- `endTime` is optional;
- the default interval is 30 seconds after `startTime`;
- the maximum LiDAR interval is 30 seconds;
- requested LiDAR logs cannot be older than five days;
- the generated output is a ROS bag filename;
- generation is estimated to complete within five minutes; and
- the download opportunity lasts ten minutes.

The public page uses placeholders rather than publishing a base hostname, stable versioned route, exact scope, or production service contract.

## Authentication boundary

The [Fleet API connection page](https://docs.maymobility.com/docs/fleet-api/connecting-to-fleet-api/) says May Mobility provisions accounts and supplies client-credential values, token URL, scope, and endpoint details. It documents AWS Cognito client-credentials token acquisition and says Batch REST requests use an OAuth bearer token in the `Authorization` header.

KFM requirements are stricter than the public example:

- credentials exist only in an approved server-side secret store;
- secrets never enter a URL, repository file, fixture, report, receipt, browser state, error message, or log;
- the Realtime API query-token pattern documented elsewhere is prohibited for KFM;
- token acquisition, LiDAR job creation, and download are separate allowlisted operations;
- every operation requires current, purpose-bound authority;
- vehicle identifiers and exact intervals are treated as sensitive even when the access token is absent;
- redirects, returned filenames, response types, sizes, and destination paths are validated before use; and
- public Explorer code never calls May Mobility directly.

## Public-documentation conflicts

The inspected public pages do not describe one internally consistent Batch API contract:

| Page | Public statement | Conflict requiring closure |
|---|---|---|
| [LiDAR](https://docs.maymobility.com/docs/fleet-api/topics-channels/lidar/) | LiDAR requests are at most 30 seconds and no older than five days | More restrictive than the generic Batch description |
| [Types of Data](https://docs.maymobility.com/docs/fleet-api/types-of-data/) | Generic Batch requests can span ten minutes, are split into 30-second pages, and cover a seven-day lookback | It does not explain whether these generic pagination rules apply to LiDAR jobs |
| [Welcome](https://docs.maymobility.com/docs/intro/) | Batch currently retrieves only GPS and POSE for up to ten minutes | This conflicts with the separate LiDAR Batch page |

KFM treats the LiDAR-specific limits as the safest provisional bounds, but it does not claim that the current service is available or that the visible examples form a complete contract. Vendor confirmation and a versioned specification are required before any live evaluation.

## Why the ROS bag is not yet a map layer

The public LiDAR page does not specify:

- ROS 1 versus ROS 2 bag format or bag version;
- message topics, message types, schemas, serialization, compression, or ordering;
- LiDAR make/model, firmware, return mode, scan pattern, range, field of view, intensity semantics, or per-point fields;
- sensor clock, vehicle clock, UTC relationship, leap-second handling, timestamp precision, drift, or synchronization error;
- coordinate-frame identifiers or the TF tree;
- LiDAR-to-vehicle extrinsics, calibration identity, calibration validity interval, or calibration uncertainty;
- whether GPS, pose, IMU, wheel odometry, map frame, or localization data are included or separately authorized;
- horizontal CRS, datum, vertical datum, geoid, epoch, units, or map projection;
- accuracy, precision, covariance, quality flags, occlusion, motion correction, or completeness;
- whether the bag contains a single LiDAR topic or other vehicle data;
- stable job identity, job state, polling contract, idempotency, cancellation, retry, or partial-result behavior; or
- content type, expected byte-size ceiling, digest, signature, malware posture, or download error envelope.

Without these facts, KFM may describe the output only as a provider-generated vehicle LiDAR log candidate. It may not describe it as a georeferenced survey, classified point cloud, DEM, DTM, DSM, nDSM, terrain measurement, or authoritative street model.

## Proposed artifact separation

The following names describe responsibilities only; this checkpoint does not choose a schema home or create machine authority.

| Conceptual object | Responsibility | Initial state |
|---|---|---|
| `MayFleetLidarRequestIntent` | Approved vehicle alias, purpose, interval, geographic/sensitivity classification, ceiling, owner, and authority reference | WORK only |
| `MayFleetLidarJobReceipt` | Secret-free request identity, provider route/version, request and response times, job/filename identity, outcome, cost/quota, and expiry | Receipt candidate |
| `RosBagSourceArtifact` | Exact downloaded bytes, digest, size, media identification, custody, rights, retention, and scan/validation result | QUARANTINE by default |
| `MobileLidarObservationSet` | Parsed topics, messages, clocks, frames, sensor/calibration lineage, and explicit missing dependencies | WORK after validation |
| `DerivedPointCloudArtifact` | Deterministically transformed LAS/LAZ/COPC/EPT plus transform receipt and retained source reference | PROCESSED candidate |
| `ReleasedPointCloudLayer` | Public-safe immutable carrier bound to evidence, policy, attribution, limitations, correction, and rollback | PUBLISHED only after separate promotion |

The raw ROS bag and every derivative keep different identities. Converting to LAS/LAZ/COPC/EPT does not make the result an original public-survey point cloud and does not create classifications that were absent from the sensor stream.

## Required mobile-LiDAR lineage

Any later admitted artifact must preserve or explicitly mark unknown:

- provider and contracting entity;
- stable vehicle alias, with the public identity generalized or suppressed;
- acquisition start/end and timestamp basis;
- requested interval, actual interval, retrieval time, and provider job/download expiry;
- source ROS bag format/version, message/topic inventory, byte count, and digest;
- sensor make/model/firmware and configuration, where disclosure is lawful;
- scan pattern, returns, intensity, range, field of view, and point record semantics;
- sensor, vehicle, odometry, local, map, and earth frame identities;
- complete transformation graph and TF samples used;
- calibration identifiers, validity window, extrinsics, intrinsics, and uncertainty;
- GPS/GNSS, pose, IMU, odometry, localization, correction service, and time-sync inputs;
- native and output CRS, horizontal datum, vertical datum, geoid, epoch, axis order, and units;
- motion compensation, filtering, cropping, decimation, classification, registration, fusion, colorization, and gridding methods;
- software/container versions, configuration, deterministic seed where relevant, and transform digest;
- accuracy/precision/covariance, validation method, control/checkpoint evidence, density, gaps, occlusion, and limitations;
- license, contractual purpose, retention, derivative, redistribution, public-display, training, and deletion rights;
- sensitivity classification, redaction/generalization decision, reviewer, correction path, and rollback target.

If pose, frame, or calibration closure is absent, the data remain a local-frame observation and must not be placed on the Kansas map.

## Privacy, safety, and rights posture

Vehicle LiDAR can encode a precise route and time plus observable people, vehicles, homes, businesses, entrances, infrastructure, work zones, emergency scenes, security features, and other third-party activity. Even without photographic texture, geometry and trajectory can create privacy, safety, contractual, and re-identification risk.

Default controls:

- treat every vehicle, route, time window, filename, bag, frame transform, and exact point cloud as restricted;
- deny requests involving personal residences, schools, care facilities, correctional facilities, critical infrastructure, active incidents, archaeology, protected ecology, or other sensitive targets without explicit policy and steward authority;
- do not use operational May Mobility data for face/person recognition, identity inference, surveillance, law enforcement, insurance, employment, or behavioral scoring;
- do not upload KFM AOIs or other source data to May Mobility through this interface;
- do not publicly expose raw trajectories, timestamps, calibration secrets, vehicle identifiers, or exact restricted geometry;
- require documented collection purpose, contractual access, bystander/passenger treatment, ownership, municipal/partner constraints, derivative rights, redistribution, model-training terms, retention/deletion, subprocessors, hosting region, incident notice, and withdrawal/correction obligations; and
- require a pre-publication sensitivity scan of the actual derived carrier, not only a style-layer hiding rule.

## Bounded connector posture

No connector is created here. A future connector proposal must be server-only, no-network-by-default, operation-scoped, and fail closed.

Minimum live-operation sequence:

1. validate authority, purpose, rights, sensitivity, vehicle alias, and interval before network access;
2. retrieve client credentials from secret storage and obtain a narrowly scoped token;
3. enforce the LiDAR-specific one-day lag, five-day lookback, and 30-second maximum unless a signed current contract establishes tighter limits;
4. cap requests, concurrency, response bytes, generation wait, download attempts, total runtime, storage, and cost;
5. create a secret-free canonical request identity;
6. submit one idempotency-safe request or return `HOLD` if idempotency is not established;
7. validate the response as an expected job/filename result without trusting it as a path or URL;
8. retrieve once through an allowlisted HTTPS route before expiry;
9. stream into a bounded quarantine sink while computing a digest;
10. validate media identity, size, container structure, topic inventory, timestamps, frames, and declared dependencies;
11. emit a finite receipt and hand off only to RAW or QUARANTINE according to the accepted policy decision; and
12. delete or retain source and derived bytes only under the approved contract and retention schedule.

No browser, MapLibre control, Focus Mode, public API route, report exporter, or background watcher receives provider credentials or direct access.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `READY` | The bounded operation is authorized and all pre-network gates pass; it does not mean source admission or release |
| `HOLD` | Contract, schema, currentness, pose/calibration, rights, purpose, quota, or owner decision remains unresolved |
| `DENY` | Policy, sensitivity, prohibited purpose, invalid interval, unapproved vehicle, secret exposure, unsafe redirect/path, or rights restriction prohibits the action |
| `ABSTAIN` | Available evidence cannot establish the identity, frame, location, meaning, or fitness of the data |
| `NO_RESULTS` | A successful, contract-conforming request yields no artifact for the authorized interval |
| `EXPIRED` | The generated download opportunity expired before validated acquisition |
| `ERROR` | Authentication, provider, timeout, malformed response, download, digest, storage, parser, or validation failure occurred |

Empty, expired, denied, and failed outcomes must not become a blank map or an inferred absence of objects.

## MapLibre boundary

Current KFM doctrine lists `maplibre-gl-lidar` as a possible governed plugin for LAS/LAZ/COPC/EPT point-cloud carriers, not ROS bags. The repository's [MapLibre atlas](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/6c5be18cf8448654be95a6db688d98546cd5276e/docs/atlases/maplibre-master.md) and [map-first doctrine](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/6c5be18cf8448654be95a6db688d98546cd5276e/docs/doctrine/map-first.md) require plugin and 3D admission plus sensitivity controls.

Therefore:

- a ROS bag is never a browser carrier;
- conversion and validation occur offline behind governed boundaries;
- application code does not import a point-cloud plugin to bypass source, evidence, policy, or release gates;
- the released layer references the immutable derived carrier and its source/transform evidence;
- point budgets, level of detail, classification/intensity filters, accessible 2D fallback, and explicit degraded states are required; and
- selection and the Evidence Drawer resolve the exact acquisition, transformation, rights, uncertainty, limitations, and release lineage.

## Relationship to connector doctrine

The current [ADR-0012 draft](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/6c5be18cf8448654be95a6db688d98546cd5276e/docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md) and current connector family conventions restrict source-edge output to RAW or QUARANTINE. This record does not accept the ADR or create a May Mobility connector. It applies the existing fail-closed design boundary to the candidate.

## Minimum evaluation package

Before live access, the owner must obtain and approve:

- a versioned LiDAR API reference and change/deprecation policy;
- exact base URLs, OAuth issuer/audience, scopes, token lifetime, and service-account controls;
- request, job, status, response, download, error, pagination, retry, idempotency, cancellation, and expiry schemas;
- confirmed current LiDAR availability and resolution of the public five-day/seven-day and 30-second/ten-minute conflicts;
- a ROS bag/topic/message specification and one contractually shareable sanitized sample;
- sensor, timing, coordinate-frame, calibration, pose, GPS/GNSS/IMU, localization, CRS/datum, units, and uncertainty documentation;
- quotas, rate limits, size ceilings, generation-time behavior, cost/pricing, SLA, outage and support procedures;
- terms, privacy/DPA, security, encryption details, retention/deletion, subprocessors, hosting region, incident notice, audit, and account revocation;
- source ownership, collection authority, bystander/passenger treatment, partner/municipal rights, derivative/redistribution/public-display/model-training terms, attribution, corrections, and withdrawal; and
- an approved non-sensitive purpose, vehicle, route/area, interval, steward, security owner, privacy owner, and data-destruction plan.

The first executable work should use only offline synthetic fixtures that model request validation, filename/path rejection, expiry, malformed job results, oversize artifacts, missing topics, missing TF, clock drift, absent pose, rights denial, and sensitive-geometry denial. A live request remains a later, separately authorized action.

## Promotion gates

- [ ] Product owner, transportation/mobile-mapping steward, security owner, privacy owner, and release authority assigned.
- [ ] May Mobility confirms the current LiDAR service and resolves public-documentation conflicts.
- [ ] Versioned API, OAuth, job, download, errors, idempotency, limits, SLA, and deprecation contract accepted.
- [ ] ROS bag, topic, time, frame, pose, calibration, CRS/datum, accuracy, and uncertainty contract accepted.
- [ ] Contract, collection authority, privacy/DPA, rights, retention, deletion, redistribution, display, training, correction, and withdrawal accepted.
- [ ] Sensitive targets and prohibited purposes are denied before request construction.
- [ ] Secrets, vehicle identifiers, intervals, filenames, routes, and exact geometry are safely handled and redacted.
- [ ] Deterministic offline fixtures prove finite outcomes and zero network by default.
- [ ] Bounded download-to-quarantine behavior, byte identity, media validation, and malicious-container cases pass.
- [ ] Deterministic ROS-bag parsing and point-cloud transformation preserve full lineage.
- [ ] Local-frame data abstain from georeferenced display when pose/frame/calibration evidence is incomplete.
- [ ] 3D/plugin admission, EvidenceBundle resolution, public-carrier sensitivity scanning, accessibility, performance, report/export, correction, and rollback pass.
- [ ] Independent exact-head review and separate source-admission, release, deployment, promotion, and publication decisions are recorded.

## Current disposition

**Retain the concept; hold all live and public behavior.** The API could add value only for an authorized May Mobility partnership or research engagement involving specific vehicle observations. It does not currently add a public Kansas data source or replace USGS, LiDAR Atlas, GPXZ, state, county, municipal, or field-survey authority.

The next owner decision is whether to authorize contact with May Mobility for the private Fleet API contract, ROS bag schema, legal/privacy package, sanitized sample, limits/pricing/SLA, and a discovery/evaluation account. That contact and every credential, query, and download require separate authority.

## Repository delivery boundary

Issue [#4024](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/4024) remains open. This writer path therefore stops at `VALIDATED_BRANCH_ONLY` and does not open a pull request.

Rollback before any reviewed integration is deletion of the feature branch. `main` is not changed.

## Non-effects

No vendor contact, account, client ID, client secret, token, endpoint hostname, scope, vehicle ID, route, interval, API request, response, job, filename, download, ROS bag, point cloud, transformation, connector, SourceDescriptor, registry entry, RAW/QUARANTINE payload, policy change, EvidenceBundle, release artifact, MapLibre layer, Focus Mode action, deployment, promotion, publication, PR transition, merge, or incident closure is created by this checkpoint.

## Sources

### May Mobility public documentation

- [LiDAR Batch API](https://docs.maymobility.com/docs/fleet-api/topics-channels/lidar/)
- [Connecting to Fleet API](https://docs.maymobility.com/docs/fleet-api/connecting-to-fleet-api/)
- [Types of Data](https://docs.maymobility.com/docs/fleet-api/types-of-data/)
- [Fleet API introduction](https://docs.maymobility.com/docs/intro/)

### KFM coordination and implementation context

- [KFM Real-Data Resource Integration hub](https://app.notion.com/p/3d6a92021bf6816cae0ec1ccbd15e21e)
- [KFM USGS TNMAccess source intake](https://app.notion.com/p/3dba92021bf68116a36ac38699a8bf06)
- [KFM GPXZ elevation service intake](https://app.notion.com/p/3dba92021bf6819197a5ff96b9f24a96)
- [KFM LiDAR Atlas API intake](https://app.notion.com/p/3dba92021bf681e395b5e5d6aa2ff6fd)
- [MapLibre atlas at the repository base](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/6c5be18cf8448654be95a6db688d98546cd5276e/docs/atlases/maplibre-master.md)
- [Map-first doctrine at the repository base](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/6c5be18cf8448654be95a6db688d98546cd5276e/docs/doctrine/map-first.md)
- [ADR-0012 draft at the repository base](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/6c5be18cf8448654be95a6db688d98546cd5276e/docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md)

The attached `KFM_Full_Atlas_seed_cards.md` and `maplibre3d.md` research copies informed the LiDAR-lineage and governed point-cloud-rendering analysis. They are supporting research context, not proof of current repository implementation.
