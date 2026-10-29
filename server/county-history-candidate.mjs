/** Private operator adapter for checked county WORK reports. No public imports,
 * acquisition, database writes, source admission, signing or release transition.
 */
import { constants } from 'node:fs';
import { open } from 'node:fs/promises';
import { isAbsolute, dirname } from 'node:path';
import { canonical, sha } from './pipeline-contract.mjs';
import { directory } from './pipeline-files.mjs';

export const COUNTY_REPORT_LIMIT = 8 * 1024 * 1024;
export const COUNTY_ARCHIVE_SHA256 = 'a233b4b3bcf3f3d7a52a4c18de76017f0d4f1f421086f95312df4c59a0aa5f02';
const SOURCE_URL = 'https://publications.newberry.org/ahcb/downloads/gis/KS_AtlasHCB.zip';
const FIRST = '1804-10-01', END = '2001-01-01';
const SHAPE = 'KS_AtlasHCB/KS_Historical_Counties/KS_Historical_Counties.';
const EVENTS = 'KS_AtlasHCB/KS_Comprehensive_Database/KS_Comprehensive_Database.txt';
// Compatibility pins for this exact offline qualification, not a source registry.
const MEMBERS = [
  [SHAPE + 'shp', '43026f03b3d1d5a8020c64aa5a17d765687277311e792208c78d3620e98c35b4', 3008116],
  [SHAPE + 'dbf', '25730b7c0ed9bb300f6dd80e833e3c82f95e23b4e8e639fe263f7eeaaefa13ed', 260015],
  [EVENTS, '1be56325d28ea82f512d09b8c005e09a20296b0cde6d5f478f9ed1e38bf832e6', 232811],
  [SHAPE + 'prj', '84cf5b9a3c1a444f83ac30ff76f8c5035990223027ba69b2f4d628388adcbd65', 167],
  [SHAPE + 'shx', 'ee4c1d945d526da5952e35170cbcfd639ae60ac259529d0e04aca34c01111619', 2828],
];
const HASH = /^[a-f0-9]{64}$/;
const ID = /^urn:kfm:work:county-history:[a-f0-9]{64}$/;
const CREDIT = 'Newberry Library · Atlas of Historical County Boundaries';
const LIMIT = 'Unreleased research candidate. Scholarly reconstruction; source labels are unreviewed. Includes predecessor and non-county jurisdictions beyond present Kansas. No legal boundary, sovereignty, ownership or population claim is established.';
const fail = code => { throw new Error('COUNTY_' + code); };
const object = v => { if (!v || typeof v !== 'object' || Array.isArray(v)) fail('SCHEMA_INVALID'); return v; };
const text = (v, max = 512, empty = false) => {
  if (typeof v !== 'string' || v.length > max || (!empty && !v.trim()) || /[\u0000-\u001f\u007f]/u.test(v)) fail('TEXT_INVALID');
  return v;
};
const list = (v, max) => { if (!Array.isArray(v) || v.length > max) fail('LIST_LIMIT'); return v; };
const integer = (v, max) => { if (!Number.isSafeInteger(v) || v < 1 || v > max) fail('RECORD_LOCATOR'); return v; };
const day = v => {
  if (typeof v !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(v) || !Number.isFinite(Date.parse(v + 'T00:00:00Z'))
    || new Date(v + 'T00:00:00Z').toISOString().slice(0, 10) !== v) fail('DATE_INVALID');
  return v;
};
const identity = (kind, ...values) => 'urn:kfm:work:county-history:' + sha(JSON.stringify([COUNTY_ARCHIVE_SHA256, kind, ...values]));
function refs(value, artifacts, expectedPaths) {
  const result = list(value, 3).map(r => {
    object(r);
    const artifact = artifacts[r.artifactId];
    if (!artifact || !expectedPaths.includes(artifact.member)) fail('EVIDENCE_REF');
    const chronology = artifact.member === EVENTS;
    if (r.locatorKind !== (chronology ? 'tsv_data_record_1_based' : 'shape_dbf_record_1_based')) fail('EVIDENCE_LOCATOR');
    return { artifactId: r.artifactId, locatorKind: r.locatorKind, recordNumber: integer(r.recordNumber, chronology ? 945 : 341) };
  });
  if (result.length !== expectedPaths.length || new Set(result.map(r => artifacts[r.artifactId].member)).size !== result.length) fail('EVIDENCE_REF');
  return result;
}
function boundary(value, artifacts, selectedDay) {
  const r = object(value), validFrom = day(r.validFrom), validToExclusive = day(r.validToExclusive);
  const sourceId = text(r.institutionSourceId, 96), version = integer(r.sourceVersion, 1000);
  if (!/^[a-z0-9_]+$/.test(sourceId) || validFrom < FIRST || validToExclusive > END || validFrom >= validToExclusive
    || !(validFrom <= selectedDay && selectedDay < validToExclusive) || r.classificationStatus !== 'unreviewed_source_label'
    || r.id !== identity('boundary_version', sourceId, version, validFrom, validToExclusive)
    || day(r.sourceLastDay) !== new Date(Date.parse(validToExclusive + 'T00:00:00Z') - 86400000).toISOString().slice(0, 10)
    || !(r.fips === null || typeof r.fips === 'string' && /^\d{5}$/.test(r.fips))
    || !(r.sourceState === null || typeof r.sourceState === 'string' && /^[A-Z]{2}$/.test(r.sourceState))) fail('BOUNDARY_RECORD');
  const evidenceRefs = refs(r.evidenceRefs, artifacts, [SHAPE + 'shp', SHAPE + 'dbf', EVENTS]);
  const recordNumber = evidenceRefs.find(e => artifacts[e.artifactId].member === SHAPE + 'shp').recordNumber;
  if (evidenceRefs.find(e => artifacts[e.artifactId].member === SHAPE + 'dbf').recordNumber !== recordNumber) fail('GEOMETRY_LOCATOR_JOIN');
  return { id: r.id, institutionSourceId: sourceId, sourceVersion: version,
    sourceName: text(r.sourceName, 200), sourceFullName: text(r.sourceFullName, 200), sourceState: r.sourceState,
    fips: r.fips, sourceCountyType: text(r.sourceCountyType, 100), classificationStatus: r.classificationStatus,
    validFrom, validToExclusive, sourceLastDay: r.sourceLastDay, change: text(r.change, 6000),
    citation: text(r.citation, 3000), evidenceRefs };
}
function geometry(value, budget) {
  const g = object(value);
  if (!['Polygon', 'MultiPolygon'].includes(g.type)) fail('GEOMETRY_TYPE');
  let count = 0;
  const polygon = rings => list(rings, 1000).map(ring => {
    const points = list(ring, 100000).map(p => {
      if (!Array.isArray(p) || p.length !== 2 || !p.every(v => typeof v === 'number' && Number.isFinite(v))
        || Math.abs(p[0]) > 180 || Math.abs(p[1]) > 90 || ++count > 100000 || ++budget.vertices > 200000) fail('COORDINATES');
      return [...p];
    });
    if (points.length < 4 || points[0][0] !== points.at(-1)[0] || points[0][1] !== points.at(-1)[1]
      || new Set(points.slice(0, -1).map(p => p.join(','))).size < 3) fail('RING_STRUCTURE');
    return points;
  });
  const polygons = (g.type === 'Polygon' ? [g.coordinates] : list(g.coordinates, 1000)).map(polygon);
  if (!polygons.length || polygons.some(p => !p.length)) fail('EMPTY_GEOMETRY');
  // Structural transport checks only; GEOS validity is evidence in the hashed report.
  return { type: g.type, coordinates: g.type === 'Polygon' ? polygons[0] : polygons };
}
function epoch(value) {
  const e = object(value);
  if (day(e.validFrom) < FIRST || day(e.validToExclusive) > END || e.validFrom >= e.validToExclusive
    || typeof e.coverageValid !== 'boolean') fail('EPOCH_INVALID');
  integer(e.featureCount, 107);
  const pairs = list(e.interiorOverlapRecordPairs, 100).map(p => {
    if (!Array.isArray(p) || p.length !== 2 || integer(p[0], 341) >= integer(p[1], 341)) fail('EPOCH_INVALID'); return [...p];
  });
  const invalid = list(e.invalidEdgeRecordNumbers, 341).map(n => integer(n, 341));
  if (e.coverageValid && (pairs.length || invalid.length)) fail('EPOCH_INVALID');
  return { validFrom: e.validFrom, validToExclusive: e.validToExclusive, featureCount: e.featureCount,
    coverageValid: e.coverageValid, interiorOverlapRecordPairs: pairs, invalidEdgeRecordNumbers: invalid };
}
function epochs(value) {
  const result = list(value, 1000).map(epoch);
  if (!result.length || result[0].validFrom !== FIRST || result.at(-1).validToExclusive !== END
    || result.some((e, i) => i && result[i-1].validToExclusive !== e.validFrom)) fail('EPOCH_COVERAGE');
  return result;
}
function operation(value, artifacts) {
  const op = object(value);
  if (op.sourceCrs !== 'EPSG:4269' || op.targetCrs !== 'OGC:CRS84' || op.axisOrder !== 'longitude_latitude'
    || op.operationId !== 'EPSG:1188' || op.operationAccuracyMetres !== 4 || op.networkEnabled !== false || op.ballparkAllowed !== false
    || op.sourceProjectionEvidenceRef?.locatorKind !== 'whole_archive_member'
    || artifacts[op.sourceProjectionEvidenceRef?.artifactId]?.member !== SHAPE + 'prj') fail('COORDINATE_OPERATION');
  return { sourceCrs: op.sourceCrs, targetCrs: op.targetCrs, axisOrder: op.axisOrder, operationId: op.operationId,
    operationAccuracyMetres: 4, accuracyMeaning: 'Coordinate operation metadata; historical boundary accuracy is unknown.',
    sourceProjectionEvidenceRef: { artifactId: op.sourceProjectionEvidenceRef.artifactId, locatorKind: 'whole_archive_member' } };
}

/** expectedSha256 must come from the operator's qualification evidence, outside
 * the report. A matching hash establishes byte integrity, never source approval.
 * Python numeric JSON spelling is not re-hashed as if it were JavaScript JSON.
 */
export function adaptCountyHistoryReport(input, expectedSha256) {
  if (!HASH.test(expectedSha256 ?? '') || !(typeof input === 'string' || Buffer.isBuffer(input) || input instanceof Uint8Array)) fail('REPORT_INPUT');
  if ((typeof input === 'string' ? Buffer.byteLength(input) : input.byteLength) > COUNTY_REPORT_LIMIT) fail('REPORT_LIMIT');
  const bytes = Buffer.from(input);
  if (!bytes.length || bytes.length > COUNTY_REPORT_LIMIT) fail('REPORT_LIMIT');
  if (sha(bytes) !== expectedSha256) fail('REPORT_INTEGRITY');
  let r;
  try { r = JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(bytes)); } catch { fail('REPORT_JSON'); }
  object(r);
  const snapshot = object(r.snapshot), checked = object(r.geometryQualification), source = object(r.source);
  const selectedDay = day(snapshot.selectedDay);
  if (selectedDay < FIRST || selectedDay >= END || r.status !== 'HOLD' || r.releaseEligible !== false
    || source.archiveSha256 !== COUNTY_ARCHIVE_SHA256 || source.bytes !== 2131373 || source.url !== SOURCE_URL || source.coverageStart !== FIRST || source.coverageLastDay !== '2000-12-31'
    || snapshot.format !== 'county_history_date_query_v1' || snapshot.lifecycle !== 'WORK' || snapshot.releaseEligible !== false || snapshot.geometryIncluded !== false
    || checked.format !== 'county_history_geometry_work_v1' || checked.lifecycle !== 'WORK' || checked.releaseEligible !== false || checked.selectedDay !== selectedDay
    || !['WORK','QUARANTINE'].includes(checked.candidateState) || r.counts?.boundaryVersions !== 341
    || r.qualification !== (checked.candidateState === 'WORK' ? 'offline_geometry_passed_for_selected_day' : 'offline_geometry_quarantined_for_selected_day')) fail('REPORT_BINDING');
  if (list(checked.individualSourceInvalid, 341).length || list(checked.individualTransformedInvalid, 341).length
    || list(checked.repairs, 1).length || checked.clipping !== null || checked.simplification !== null
    || canonical(checked.transforms) !== canonical(['EPSG:1188 with longitude/latitude axis order', 'RFC 7946 ring orientation'])) fail('GEOMETRY_CHECKS');
  const receipts = list(r.members, 100), artifacts = {};
  for (const [member, digest, size] of MEMBERS) {
    const matches = receipts.filter(m => m?.path === member);
    if (matches.length !== 1 || matches[0].sha256 !== digest || matches[0].bytes !== size) fail('MEMBER_IDENTITY');
    artifacts['sha256:' + digest] = { member, sha256: digest, bytes: size };
  }
  const bundle = object(snapshot.evidenceBundle);
  if (bundle.lifecycle !== 'WORK' || bundle.archiveSha256 !== COUNTY_ARCHIVE_SHA256 || bundle.sourceUrl !== SOURCE_URL) fail('EVIDENCE_BUNDLE');
  if (Object.keys(object(bundle.artifacts)).sort().join(',') !== MEMBERS.slice(0, 3).map(m => 'sha256:' + m[1]).sort().join(',')) fail('EVIDENCE_BUNDLE');
  for (const key of Object.keys(object(bundle.artifacts))) {
    if (!artifacts[key] || canonical(bundle.artifacts[key]) !== canonical(artifacts[key])) fail('EVIDENCE_BUNDLE');
  }
  const sourceEpochs = epochs(checked.sourceCoverageEpochs), targetEpochs = epochs(checked.transformedCoverageEpochs);
  if (canonical(sourceEpochs) !== canonical(targetEpochs)) fail('SOURCE_TARGET_COVERAGE');
  const selectedEpoch = targetEpochs.find(e => e.validFrom <= selectedDay && selectedDay < e.validToExclusive);
  if (canonical(epoch(checked.selectedEpoch)) !== canonical(selectedEpoch)) fail('SELECTED_EPOCH');
  const op = operation(checked.coordinateOperation, artifacts);
  const records = list(snapshot.boundaryVersions, 107).map(v => boundary(v, artifacts, selectedDay));
  if (records.length !== selectedEpoch.featureCount || new Set(records.map(r => r.id)).size !== records.length
    || new Set(records.map(r => r.evidenceRefs.find(e => e.locatorKind === 'shape_dbf_record_1_based').recordNumber)).size !== records.length) fail('SNAPSHOT_COMPLETENESS');
  records.sort((a, b) => a.id < b.id ? -1 : a.id > b.id ? 1 : 0);
  const events = list(snapshot.eventOnlyRecordsOnDay, 588).map(e => {
    object(e); const evidenceRefs = refs(e.evidenceRefs, artifacts, [EVENTS]);
    if (day(e.eventDate) !== selectedDay || e.id !== identity('event_only', MEMBERS[2][1], evidenceRefs[0].recordNumber)
      || !(e.institutionSourceId === null || typeof e.institutionSourceId === 'string' && /^[a-z0-9_]+$/.test(e.institutionSourceId))) fail('EVENT_IDENTITY');
    return { id: e.id, institutionSourceId: e.institutionSourceId, sourceName: text(e.sourceName, 200, true),
      eventDate: selectedDay, change: text(e.change, 6000), citation: text(e.citation, 3000), evidenceRefs };
  });
  const aliases = list(snapshot.undatedNameCrossReferences, 16).map(a => {
    object(a); const evidenceRefs = refs(a.evidenceRefs, artifacts, [EVENTS]);
    if (a.temporalApplicability !== 'unknown' || a.id !== identity('name_cross_reference', MEMBERS[2][1], evidenceRefs[0].recordNumber)) fail('ALIAS_IDENTITY');
    return { id: a.id, targetInstitutionSourceId: text(a.targetInstitutionSourceId, 96), sourceText: text(a.sourceText, 300), temporalApplicability: 'unknown', evidenceRefs };
  });
  if (new Set(events.map(e => e.id)).size !== events.length || aliases.length !== 16 || new Set(aliases.map(a => a.id)).size !== aliases.length) fail('CHRONOLOGY_COMPLETENESS');
  const candidate = r.geometryCandidate, checkedGeometry = checked.candidateState === 'WORK';
  const features = [], budget = { vertices: 0 };
  if (checkedGeometry) {
    object(candidate);
    if (!selectedEpoch.coverageValid || candidate.type !== 'FeatureCollection' || candidate.lifecycle !== 'WORK' || candidate.releaseEligible !== false
      || candidate.selectedDay !== selectedDay || list(candidate.features, 107).length !== records.length
      || !HASH.test(checked.candidateSha256 ?? '')) fail('CANDIDATE_BINDING');
    const candidateBundle = object(candidate.evidenceBundle);
    if (candidateBundle.lifecycle !== 'WORK' || candidateBundle.archiveSha256 !== COUNTY_ARCHIVE_SHA256 || candidateBundle.sourceUrl !== SOURCE_URL
      || canonical(candidateBundle.artifacts) !== canonical(artifacts)
      || canonical(operation(candidate.coordinateOperation, artifacts)) !== canonical(op)) fail('CANDIDATE_EVIDENCE');
    const byId = new Map(records.map(record => [record.id, record])), seen = new Set();
    for (const feature of candidate.features) {
      object(feature); const record = byId.get(feature.id), p = object(feature.properties);
      const { geometrySha256, ...sourceRecord } = p;
      if (feature.type !== 'Feature' || !record || seen.has(feature.id) || canonical(boundary(sourceRecord, artifacts, selectedDay)) !== canonical(record)
        || !HASH.test(geometrySha256 ?? '')) fail('FEATURE_BINDING');
      seen.add(feature.id);
      features.push({ type: 'Feature', id: record.id, geometry: geometry(feature.geometry, budget),
        properties: { ...record, sourceGeometrySha256: geometrySha256 } });
    }
    features.sort((a, b) => a.id < b.id ? -1 : a.id > b.id ? 1 : 0);
  } else if (candidate !== null || selectedEpoch.coverageValid) fail('QUARANTINE_BINDING');
  const result = { format: 'kfm-county-history-research-v1', lifecycle: 'WORK', releaseEligible: false, publicClientEligible: false,
    selectedDay, geometryState: checkedGeometry ? 'checked-candidate' : 'quarantine',
    source: { url: SOURCE_URL, organization: CREDIT, archiveSha256: COUNTY_ARCHIVE_SHA256, kind: 'historical_reconstruction',
      coverageStart: FIRST, coverageEndExclusive: END, limitation: LIMIT },
    calendar: { selectedEpoch, coverageEpochs: targetEpochs, availableSnapshotDays: checkedGeometry ? [selectedDay] : [], carryForward: false },
    records, eventOnlyRecordsOnDay: events, undatedNameCrossReferences: aliases,
    data: { type: 'FeatureCollection', features }, evidenceBundle: { lifecycle: 'WORK', sourceUrl: SOURCE_URL, archiveSha256: COUNTY_ARCHIVE_SHA256, artifacts },
    provenance: { reportSha256: expectedSha256, upstreamCandidateSha256: checkedGeometry ? checked.candidateSha256 : null,
      upstreamDigestEncoding: 'Python json.dumps(sort_keys=True,separators=(comma,colon),ensure_ascii=True)',
      digestMeaning: 'The supplied report-byte hash is checked. Upstream Python JSON digests are preserved, not recomputed using JavaScript number spelling.',
      coordinateOperation: op, geometryValidation: 'Reported GEOS checks; this adapter rechecks transport structure, not polygon topology.' } };
  return { ...result, adapterSha256: sha(canonical(result)) };
}

export async function readCountyHistoryReport(path, expectedSha256) {
  if (typeof path !== 'string' || !isAbsolute(path) || path.split('/').includes('..') || !HASH.test(expectedSha256 ?? '')) fail('REPORT_PATH');
  await directory(dirname(path));
  const handle = await open(path, constants.O_RDONLY | constants.O_NOFOLLOW | constants.O_NONBLOCK);
  try {
    const before = await handle.stat();
    if (!before.isFile() || before.size < 1 || before.size > COUNTY_REPORT_LIMIT) fail('REPORT_LIMIT');
    const chunks = []; let length = 0;
    while (true) {
      const buffer = Buffer.alloc(Math.min(65536, COUNTY_REPORT_LIMIT + 1 - length));
      const { bytesRead } = await handle.read(buffer);
      if (!bytesRead) break;
      length += bytesRead; if (length > COUNTY_REPORT_LIMIT) fail('REPORT_LIMIT');
      chunks.push(buffer.subarray(0, bytesRead));
    }
    const after = await handle.stat();
    if (length !== before.size || before.size !== after.size || before.mtimeMs !== after.mtimeMs || before.ctimeMs !== after.ctimeMs) fail('REPORT_CHANGED');
    return adaptCountyHistoryReport(Buffer.concat(chunks, length), expectedSha256);
  } finally { await handle.close(); }
}

/** Exact-day private rehearsal for the calendar. Not a public read DTO. */
export function countyHistoryCalendarView(packet, requestedDay) {
  const { adapterSha256, ...content } = object(packet);
  if (packet.format !== 'kfm-county-history-research-v1' || packet.lifecycle !== 'WORK' || packet.releaseEligible !== false
    || packet.publicClientEligible !== false || sha(canonical(content)) !== adapterSha256) fail('ADAPTER_INTEGRITY');
  const selectedDay = day(requestedDay);
  const negative = reason => ({ state: 'held', reason, selectedDay, lifecycle: 'WORK', releaseEligible: false, publicClientEligible: false,
    data: { type: 'FeatureCollection', features: [] } });
  if (selectedDay < FIRST || selectedDay >= END) return negative('OUTSIDE_SOURCE_COVERAGE');
  if (selectedDay !== packet.selectedDay) return negative('SNAPSHOT_NOT_PREPARED');
  if (packet.geometryState !== 'checked-candidate') return negative('QUARANTINED_COVERAGE');
  return { state: 'candidate-only', selectedDay, lifecycle: 'WORK', releaseEligible: false, publicClientEligible: false,
    data: structuredClone(packet.data), evidenceBundle: structuredClone(packet.evidenceBundle) };
}

/** Source-drawer rehearsal: retain cited record context even when geometry is held. */
export function countyHistoryDrawerRecord(packet, recordId, requestedDay) {
  const view = countyHistoryCalendarView(packet, requestedDay);
  if (requestedDay !== packet.selectedDay || !ID.test(recordId ?? '')) return null;
  const record = packet.records.find(r => r.id === recordId);
  if (!record) return null;
  return { id: record.id, title: record.sourceFullName, selectedDay: requestedDay, validFrom: record.validFrom,
    validToExclusive: record.validToExclusive, sourceLastDay: record.sourceLastDay, sourceId: record.institutionSourceId,
    fips: record.fips, sourceState: record.sourceState, sourceType: record.sourceCountyType,
    classificationStatus: record.classificationStatus, change: record.change, citation: record.citation,
    sourceOrganization: CREDIT, sourceUrl: SOURCE_URL, limitation: LIMIT, geometryState: view.state,
    evidenceRefs: structuredClone(record.evidenceRefs), evidenceBundle: structuredClone(packet.evidenceBundle),
    reportSha256: packet.provenance.reportSha256,
    lifecycle: 'WORK', releaseEligible: false, publicClientEligible: false };
}
