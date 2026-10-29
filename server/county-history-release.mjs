// Approved-context projection for the existing signed publication pipeline.
// A product is never approval: handlePipeline owns signing/commit/read gates.
import { canonical, timestamp, fail } from './pipeline-contract.mjs';

export const COUNTY_SOURCE_ID = 'newberry-county-history';
export const COUNTY_SOURCE_URL = 'https://publications.newberry.org/ahcb/downloads/gis/KS_AtlasHCB.zip';
export const COUNTY_ARCHIVE = 'a233b4b3bcf3f3d7a52a4c18de76017f0d4f1f421086f95312df4c59a0aa5f02';
export const COUNTY_RIGHTS_URL = 'https://publications.newberry.org/ahcb/downloads/states.html';
export const COUNTY_LIMITATION = 'Newberry Atlas scholarly reconstruction. Includes predecessor and non-county jurisdictions beyond modern Kansas. Source type labels are unreviewed; no legal boundary, sovereignty, ownership or population inference. EPSG:1188 is a zero-translation NAD83-to-CRS84 display operation; its 4 m operation metadata is not historical boundary accuracy. Exact prepared day only; no continuation after 2000. Approved external context, not admitted KFM evidence.';
const DAY = /^\d{4}-\d{2}-\d{2}$/;
const HASH = /^[a-f0-9]{64}$/;
const record = v => !!v && typeof v === 'object' && !Array.isArray(v);
const text = (v, max, empty = false) => typeof v === 'string' && v.length <= max && (empty || !!v.trim()) && !/[\u0000-\u001f\u007f]/.test(v);
function exactKeys(v, keys) { return record(v) && Object.keys(v).sort().join(',') === [...keys].sort().join(','); }
function day(v) {
  return typeof v === 'string' && DAY.test(v) && v >= '1804-10-01' && v <= '2000-12-31'
    && Number.isFinite(Date.parse(v + 'T00:00:00Z')) && new Date(v + 'T00:00:00Z').toISOString().slice(0, 10) === v;
}
const fid = (p, d) => `ahcb-${COUNTY_ARCHIVE.slice(0,12)}-${p.institutionSourceId}-v${p.sourceVersion}-${d}`;
const FEATURE_KEYS = ['name','institutionSourceId','sourceVersion','sourceState','fips','sourceCountyType','classificationStatus','validFrom','validToExclusive','sourceLastDay','change','citation','sourceDay','sourceLocators'];
const PRODUCT_KEYS = ['format','sourceId','sourceUrl','rightsUrl','archiveSha256','qualificationReportSha256','preparedAt','effectiveDay','partial','evidenceRole','evidenceEligible','limitation','coordinateOperation','data'];
const shapeSha = '43026f03b3d1d5a8020c64aa5a17d765687277311e792208c78d3620e98c35b4';
const dbfSha = '25730b7c0ed9bb300f6dd80e833e3c82f95e23b4e8e639fe263f7eeaaefa13ed';
const tsvSha = '1be56325d28ea82f512d09b8c005e09a20296b0cde6d5f478f9ed1e38bf832e6';
function validateGeometry(g, budget) {
  if (!exactKeys(g,['type','coordinates']) || !['Polygon','MultiPolygon'].includes(g.type)) fail('COUNTY_GEOMETRY_INVALID');
  const polygons = g.type === 'Polygon' ? [g.coordinates] : g.coordinates;
  if (!Array.isArray(polygons) || !polygons.length || polygons.length > 1000) fail('COUNTY_GEOMETRY_INVALID');
  let vertices = 0;
  for (const rings of polygons) {
    if (!Array.isArray(rings) || !rings.length || rings.length > 1000) fail('COUNTY_GEOMETRY_INVALID');
    for (const ring of rings) {
      if (!Array.isArray(ring) || ring.length < 4 || ring.length > 100000) fail('COUNTY_GEOMETRY_INVALID');
      for (const p of ring) if (!Array.isArray(p) || p.length !== 2 || !p.every(Number.isFinite) || Math.abs(p[0]) > 180 || Math.abs(p[1]) > 90 || ++vertices > 100000 || ++budget.vertices > 200000) fail('COUNTY_GEOMETRY_INVALID');
      if (ring[0][0] !== ring.at(-1)[0] || ring[0][1] !== ring.at(-1)[1] || new Set(ring.slice(0,-1).map(p=>p.join(','))).size < 3) fail('COUNTY_GEOMETRY_INVALID');
    }
  }
}

export function validateCountyRelease(p) {
  if (!exactKeys(p,PRODUCT_KEYS) || p.format !== 'kfm-curated-county-history-v1' || p.sourceId !== COUNTY_SOURCE_ID
    || p.sourceUrl !== COUNTY_SOURCE_URL || p.rightsUrl !== COUNTY_RIGHTS_URL || p.archiveSha256 !== COUNTY_ARCHIVE
    || !HASH.test(p.qualificationReportSha256 ?? '') || !day(p.effectiveDay) || p.partial !== false
    || p.evidenceRole !== 'EXTERNAL_CONTEXT_ONLY' || p.evidenceEligible !== false || p.limitation !== COUNTY_LIMITATION
    || canonical(p.coordinateOperation) !== canonical({id:'EPSG:1188',sourceCrs:'EPSG:4269',targetCrs:'OGC:CRS84',operationAccuracyMetres:4})
    || !exactKeys(p.data,['type','features']) || p.data.type !== 'FeatureCollection' || !Array.isArray(p.data.features) || !p.data.features.length || p.data.features.length > 107
    || p.effectiveDay >= '1873-03-20' && p.effectiveDay < '1874-03-18') fail('COUNTY_PRODUCT_INVALID');
  timestamp(p.preparedAt);
  const ids = new Set(), institutions = new Set(), locators = new Set(), budget = {vertices:0};
  for (const f of p.data.features) {
    const r = f?.properties;
    if (!exactKeys(f,['type','id','geometry','properties']) || f.type !== 'Feature' || !exactKeys(r,FEATURE_KEYS)
      || !/^[a-z0-9_]{1,96}$/.test(r.institutionSourceId ?? '') || !Number.isSafeInteger(r.sourceVersion) || r.sourceVersion < 1 || r.sourceVersion > 1000
      || f.id !== fid(r,p.effectiveDay) || ids.has(f.id) || institutions.has(r.institutionSourceId)
      || !text(r.name,200) || !text(r.sourceCountyType,100) || r.classificationStatus !== 'unreviewed_source_label'
      || !(r.sourceState === null || /^[A-Z]{2}$/.test(r.sourceState)) || !(r.fips === null || typeof r.fips === 'string' && /^\d{5}$/.test(r.fips))
      || !day(r.validFrom) || !day(r.sourceLastDay) || r.validToExclusive !== new Date(Date.parse(r.sourceLastDay+'T00:00:00Z')+86400000).toISOString().slice(0,10)
      || !(r.validFrom <= p.effectiveDay && p.effectiveDay < r.validToExclusive) || r.sourceDay !== p.effectiveDay || !text(r.change,6000) || !text(r.citation,3000)
      || !Array.isArray(r.sourceLocators) || r.sourceLocators.length !== 3) fail('COUNTY_RECORD_INVALID');
    for (let i=0;i<3;i++) {
      const ref=r.sourceLocators[i];
      if (!exactKeys(ref,['memberSha256','recordNumber','kind']) || ref.memberSha256 !== [shapeSha,dbfSha,tsvSha][i]
        || !Number.isSafeInteger(ref.recordNumber) || ref.recordNumber < 1 || ref.recordNumber > (i===2?945:341)
        || ref.kind !== (i===2?'tsv_data_record_1_based':'shape_dbf_record_1_based')) fail('COUNTY_LOCATOR_INVALID');
    }
    if (r.sourceLocators[0].recordNumber !== r.sourceLocators[1].recordNumber || locators.has(r.sourceLocators[0].recordNumber)) fail('COUNTY_LOCATOR_INVALID');
    ids.add(f.id); institutions.add(r.institutionSourceId); locators.add(r.sourceLocators[0].recordNumber); validateGeometry(f.geometry,budget);
  }
  return p;
}
