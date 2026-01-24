# ✅ `api/src/contracts/examples/events/payloads/index.ts` 📦🧾

> **Purpose:** Realistic **payload-only** fixtures for KFM’s event system (no envelope headers).  
> **Design vibe:** **Evidence-first** 🔎, **provenance-first** ⛓️, **policy-gated** 🛡️, **FAIR+CARE** 🌍🤝

---

## 📄 File Contents

```ts
/**
 * KFM (Kansas Frontier Matrix) — Event Payload Examples
 * ----------------------------------------------------
 * Payload-only examples (no event envelope / headers).
 *
 * Why payload-only?
 * - Schemas often wrap these inside an event envelope (id, type, time, source, trace ids, etc.)
 * - Keeping "payloads" separate makes reuse easier across:
 *   - contract/schema docs
 *   - unit tests / fixtures
 *   - local dev seeding / demos
 *
 * Guiding principles reflected here:
 * - Evidence-first: user-facing artifacts reference sources/citations and evidence manifests
 * - Provenance-first: STAC/DCAT/PROV + run manifests + digests show chain-of-custody
 * - Fail-closed policy gates: examples include gate failures and governance logging
 * - Sovereignty/classification propagation: outputs never downgrade sensitivity vs inputs
 */

/** Lightweight “brand” types for readability in examples. */
export type IsoDateTimeString = string;
export type Sha256Digest = `sha256:${string}`;

const RUN_ID = 'run_2026-01-23T01-23-45Z_7f3a2c1d';
const IDEMPOTENCY_KEY: Sha256Digest =
  'sha256:7c0f4e2c4a09f0d9d5f70a0a9af2d5b2fdfb1c4d2f0f7a1a0b7c0e7d6a5b4c3d';

const STAC_COLLECTION_ID = 'kfm-hydro-river-gauges';
const DCAT_DATASET_ID = 'kfm-dcat-usgs-nwis-river-gauges';
const PROV_BUNDLE_ID = 'prov:kfm:activity:ingest:usgs-nwis:river-gauges:2026-01-23';

const EVIDENCE_MANIFEST_URI = `data/evidence/manifests/${RUN_ID}/evidence_manifest.json`;
const RUN_MANIFEST_URI = `data/audits/${RUN_ID}/run_manifest.json`;
const TELEMETRY_REF = `data/telemetry/runs/${RUN_ID}.ndjson`;

const KANSAS_BBOX_WGS84: [number, number, number, number] = [-102.05, 36.99, -94.58, 40.0];

export const EVENT_PAYLOAD_EXAMPLES = {
  /**
   * 🧱 Data Intake — Run Started
   * Reflects: run identifiers, idempotency keys, inputs, expected outputs, and telemetry reference.
   */
  'kfm.pipeline.run.started': {
    runId: RUN_ID,
    startedAt: '2026-01-23T01:23:45.000Z' satisfies IsoDateTimeString,
    idempotencyKey: IDEMPOTENCY_KEY,
    telemetryRef: TELEMETRY_REF,

    pipeline: {
      name: 'data-intake/usgs-nwis/river-gauges',
      version: '1.3.0',
      git: {
        repo: 'Kansas-Frontier-Matrix',
        ref: 'main',
        commit: 'bb86bf1707b50a9d3d43b06896fd387851de92b3',
      },
    },

    trigger: {
      type: 'schedule',
      cron: '*/15 * * * *',
      requestedBy: {
        actorType: 'service',
        actorId: 'kfm-scheduler',
        displayName: 'KFM Scheduler',
      },
    },

    inputs: [
      {
        kind: 'http',
        uri: 'https://waterservices.usgs.gov/nwis/iv/?format=json&sites=06888990',
        contentType: 'application/json',
        observedAt: '2026-01-23T01:20:00.000Z' satisfies IsoDateTimeString,
      },
    ],

    expectedOutputs: {
      stacCollectionId: STAC_COLLECTION_ID,
      dcatDatasetId: DCAT_DATASET_ID,
      provBundleId: PROV_BUNDLE_ID,
      runManifestUri: RUN_MANIFEST_URI,
      evidenceManifestUri: EVIDENCE_MANIFEST_URI,
    },

    classification: {
      level: 'PUBLIC',
      tags: ['FAIR', 'CARE', 'STREAMING_DATA', 'HYDROLOGY'],
      sovereignty: {
        carePrinciplesApplied: true,
        authorityOfLocalKnowledge: true,
        communities: [],
      },
    },

    spatial: {
      bboxWgs84: KANSAS_BBOX_WGS84,
    },
  },

  /**
   * ✅ Data Intake — Run Completed
   * Includes manifest digesting, artifact references, and supply-chain signals (SBOM + signature).
   */
  'kfm.pipeline.run.completed': {
    runId: RUN_ID,
    status: 'success',
    startedAt: '2026-01-23T01:23:45.000Z' satisfies IsoDateTimeString,
    endedAt: '2026-01-23T01:24:32.500Z' satisfies IsoDateTimeString,
    durationMs: 47500,

    idempotencyKey: IDEMPOTENCY_KEY,

    runManifest: {
      uri: RUN_MANIFEST_URI,
      canonicalization: 'RFC8785',
      canonicalDigest: 'sha256:41f2d61d9f9a0afcccb0aef13d4fd5c3d8b6a3a3f7e3c1d7b9c2e1a0f0d9c8b7' as Sha256Digest,
      toolVersions: {
        node: '20.11.0',
        postgres: '16.2',
        postgis: '3.4.1',
        tippecanoe: '2.5.0',
        conftest: '0.50.0',
        opa: '0.63.0',
      },
      sourceUrls: ['https://waterservices.usgs.gov/nwis/iv/?format=json&sites=06888990'],
      summaryCounts: {
        recordsIn: 120,
        recordsOut: 120,
        errors: 0,
        warnings: 1,
      },
    },

    artifacts: {
      stac: {
        collectionId: STAC_COLLECTION_ID,
        collectionUri: 'data/catalog/stac/collections/kfm-hydro-river-gauges.json',
        itemUris: [
          'data/catalog/stac/items/hydro/river-gauges/06888990/2026-01-23T01-15-00Z.json',
          'data/catalog/stac/items/hydro/river-gauges/06888990/2026-01-23T01-30-00Z.json',
        ],
      },
      dcat: {
        datasetId: DCAT_DATASET_ID,
        datasetUri: 'data/catalog/dcat/kfm-dcat-usgs-nwis-river-gauges.jsonld',
        distributions: [
          {
            mediaType: 'application/geo+json',
            uri: 'data/exports/hydro/river-gauges/latest.geojson',
          },
          {
            mediaType: 'application/x-ndjson',
            uri: TELEMETRY_REF,
          },
        ],
      },
      prov: {
        bundleId: PROV_BUNDLE_ID,
        provJsonUri: `data/prov/${RUN_ID}/prov.json`,
        notes: 'STAC + DCAT records include references linking back to PROV activity identifiers.',
      },
      evidenceManifest: {
        uri: EVIDENCE_MANIFEST_URI,
        digest: 'sha256:0b6a9b0f4f0c2a3d8e9f7a1c0d2e3f4a5b6c7d8e9f0a1b2c3d4e5f60718293a4' as Sha256Digest,
      },
    },

    supplyChain: {
      sbom: {
        format: 'spdx-json',
        uri: `oci://ghcr.io/kfm/sbom@sha256:ab12cd34ef56ab12cd34ef56ab12cd34ef56ab12cd34ef56ab12cd34ef56ab12`,
      },
      signature: {
        type: 'cosign',
        signedArtifact: `oci://ghcr.io/kfm/audits/${RUN_ID}@sha256:9a9b9c9d9e9f000111222333444555666777888999aaabbbcccdddeeefff0001`,
        publicKeyRef: 'kfm-kms://keys/provenance-signing/v1',
      },
    },

    classification: {
      level: 'PUBLIC',
      tags: ['FAIR', 'CARE', 'PROVENANCE_ENFORCED', 'CATALOG_DRIVEN'],
      sovereignty: {
        carePrinciplesApplied: true,
        authorityOfLocalKnowledge: true,
        communities: [],
      },
    },
  },

  /**
   * ❌ Data Intake — Run Failed
   * Demonstrates “fail closed” behavior when a required gate is violated.
   */
  'kfm.pipeline.run.failed': {
    runId: 'run_2026-01-23T02-10-00Z_ba7e1c99',
    status: 'failed',
    startedAt: '2026-01-23T02:10:00.000Z' satisfies IsoDateTimeString,
    endedAt: '2026-01-23T02:10:03.200Z' satisfies IsoDateTimeString,
    durationMs: 3200,

    pipeline: {
      name: 'data-intake/external-csv/heritage-sites',
      version: '0.9.2',
    },

    failure: {
      code: 'POLICY_GATE_DENIED',
      gate: 'license-presence',
      message:
        'Dataset rejected: missing required license metadata (fail-closed policy gate). Add SPDX license id and provider info.',
      policy: {
        engine: 'opa/conftest',
        policyPack: 'kfm-policy-pack',
        policyPackVersion: '13.0.0',
        ruleId: 'KFM-LIC-001',
        decision: 'deny',
      },
      remediation: [
        'Add license SPDX id to DCAT record.',
        'Add provider/attribution details.',
        'Re-run validation and ensure provenance completeness.',
      ],
    },

    classification: {
      level: 'INTERNAL',
      tags: ['FAIL_CLOSED', 'GOVERNANCE'],
      sovereignty: {
        carePrinciplesApplied: true,
        authorityOfLocalKnowledge: true,
        communities: ['example:community:heritage-stewards'],
      },
    },
  },

  /**
   * 🗂️ Catalog — STAC Published
   * When catalog artifacts are made available for discovery / indexing.
   */
  'kfm.catalog.stac.published': {
    publishedAt: '2026-01-23T01:25:05.000Z' satisfies IsoDateTimeString,
    stacCollectionId: STAC_COLLECTION_ID,
    collectionUri: 'data/catalog/stac/collections/kfm-hydro-river-gauges.json',
    itemUris: [
      'data/catalog/stac/items/hydro/river-gauges/06888990/2026-01-23T01-15-00Z.json',
      'data/catalog/stac/items/hydro/river-gauges/06888990/2026-01-23T01-30-00Z.json',
    ],
    validation: {
      schema: 'kfm-stac-profile',
      status: 'pass',
      reportUri: `data/audits/${RUN_ID}/reports/stac_validation.json`,
    },
    provenance: {
      provActivityId: PROV_BUNDLE_ID,
      runId: RUN_ID,
      runManifestUri: RUN_MANIFEST_URI,
    },
    classification: {
      level: 'PUBLIC',
      tags: ['STAC', 'CATALOG', 'PROVENANCE_LINKED'],
    },
  },

  /**
   * 🕸️ Graph — Ingest Completed
   * Reflects mirrored evidence graph in Neo4j: Dataset/Asset/Activity nodes, edges, and integrity checks.
   */
  'kfm.graph.ingest.completed': {
    graphCommitId: 'graph_commit_2026-01-23T01:26:00Z_0137aa',
    ingestedAt: '2026-01-23T01:26:00.000Z' satisfies IsoDateTimeString,

    run: {
      runId: RUN_ID,
      runManifestDigest: 'sha256:41f2d61d9f9a0afcccb0aef13d4fd5c3d8b6a3a3f7e3c1d7b9c2e1a0f0d9c8b7' as Sha256Digest,
    },

    nodesUpserted: {
      dataset: 1,
      asset: 2,
      activity: 1,
      agent: 1,
    },

    relationshipsUpserted: {
      used: 2,
      generated: 2,
      wasAssociatedWith: 1,
      hasPart: 2,
    },

    integrity: {
      constraintsChecked: ['unique(kfmDatasetId)', 'no_orphan_assets', 'prov_links_present'],
      violations: [],
      status: 'pass',
    },

    sampleGraphRefs: {
      datasetNodeId: 'neo4j:node:Dataset:kfm-dcat-usgs-nwis-river-gauges',
      activityNodeId: `neo4j:node:Activity:${PROV_BUNDLE_ID}`,
      assetNodeIds: [
        'neo4j:node:Asset:stac:item:06888990:2026-01-23T01-15-00Z',
        'neo4j:node:Asset:stac:item:06888990:2026-01-23T01-30-00Z',
      ],
    },

    classification: {
      level: 'PUBLIC',
      tags: ['GRAPH', 'EVIDENCE_GRAPH', 'PROVENANCE'],
    },
  },

  /**
   * 🛡️ Policy — Gate Failed (OPA/Conftest)
   * Shows policy-as-code enforcement with stable rule IDs and actionable diagnostics.
   */
  'kfm.policy.gate.failed': {
    evaluatedAt: '2026-01-23T03:00:00.000Z' satisfies IsoDateTimeString,
    engine: 'opa/conftest',
    policyPack: {
      name: 'kfm-policy-pack',
      version: '13.0.0',
      ruleset: ['schema-validation', 'license-presence', 'prov-completeness', 'classification-propagation'],
    },

    rule: {
      id: 'KFM-PROV-001',
      title: 'Provenance Completeness',
      decision: 'deny',
      severity: 'error',
    },

    subject: {
      kind: 'pull_request',
      repo: 'Kansas-Frontier-Matrix',
      prNumber: 412,
      ref: 'refs/pull/412/head',
      changedFiles: [
        'data/catalog/dcat/new_dataset.jsonld',
        'data/catalog/stac/items/new_item.json',
        'docs/stories/new_story_node.md',
      ],
    },

    findings: [
      {
        path: 'data/catalog/dcat/new_dataset.jsonld',
        message: 'Missing required dct:license / SPDX identifier.',
        ruleId: 'KFM-LIC-001',
      },
      {
        path: 'data/catalog/stac/items/new_item.json',
        message: 'Missing kfm:prov_activity_id linking item to a PROV activity.',
        ruleId: 'KFM-PROV-001',
      },
      {
        path: 'docs/stories/new_story_node.md',
        message: 'Evidence for narratives rule: missing citations block (fail-closed).',
        ruleId: 'KFM-EVID-001',
      },
      {
        path: 'data/catalog/stac/items/new_item.json',
        message:
          'Classification propagation violation: input classified RESTRICTED but output marked PUBLIC (must not downgrade).',
        ruleId: 'KFM-CLASS-001',
      },
    ],

    remediation: [
      'Add SPDX license to DCAT record and provider attribution.',
      'Add kfm:prov_activity_id to STAC Item and ensure PROV bundle exists.',
      'Add citations/evidence references to story node content.',
      'Ensure output classification >= most restrictive input classification.',
    ],

    classification: {
      level: 'INTERNAL',
      tags: ['POLICY', 'FAIL_CLOSED', 'OPA', 'CONFTST'],
    },
  },

  /**
   * 🧾 Governance — Ledger Entry Appended
   * Immutable, append-only, signed log of AI outputs and key decisions.
   */
  'kfm.governance.ledger.entry.appended': {
    appendedAt: '2026-01-23T03:00:02.000Z' satisfies IsoDateTimeString,
    ledger: {
      ledgerId: 'kfm-governance-ledger-v1',
      entryId: 'ledger_entry_000000000042',
      previousHash: 'sha256:0000000000000000000000000000000000000000000000000000000000000041' as Sha256Digest,
      entryHash: 'sha256:0000000000000000000000000000000000000000000000000000000000000042' as Sha256Digest,
      signature: {
        type: 'ed25519',
        keyId: 'kfm-ledger-signing-key-v1',
        sig: 'MEUCIQDd...example...==',
      },
    },

    recordedDecision: {
      kind: 'policy_gate',
      engine: 'opa/conftest',
      policyPackVersion: '13.0.0',
      ruleIds: ['KFM-PROV-001', 'KFM-LIC-001', 'KFM-EVID-001', 'KFM-CLASS-001'],
      outcome: 'deny',
      subject: { repo: 'Kansas-Frontier-Matrix', prNumber: 412 },
      notes:
        'Fail-closed governance: change rejected until license, provenance linkage, and evidence citations are present.',
    },

    links: {
      auditReportUri: 'data/audits/pr-412/policy_report.json',
      evidenceManifestUri: 'data/evidence/manifests/pr-412/evidence_manifest.json',
    },

    classification: {
      level: 'INTERNAL',
      tags: ['GOVERNANCE', 'IMMUTABLE_LOG', 'SIGNED'],
    },
  },

  /**
   * 📚 Story Nodes — Published
   * Demonstrates narrative payload linking map state + timeline + citations + evidence manifest.
   */
  'kfm.story.node.published': {
    publishedAt: '2026-01-23T04:15:00.000Z' satisfies IsoDateTimeString,

    storyNode: {
      id: 'story:node:topeka-river-gauges-1935-drought',
      version: '1.0.0',
      slug: 'topeka-river-gauges-1935-drought',
      title: 'Hydrology Signals Around Topeka (1930s Context)',
      summary:
        'A provenance-backed narrative connecting hydrology observations with historical drought context, surfaced through map layers and timeline navigation.',
      authors: [
        { actorType: 'user', actorId: 'user_42', displayName: 'KFM Historian' },
        { actorType: 'service', actorId: 'kfm-focus-mode', displayName: 'Focus Mode (AI Assistant)' },
      ],
    },

    uiContext: {
      mapState: {
        center: { lon: -95.689, lat: 39.0558 },
        zoom: 9.2,
        pitch: 0,
        bearing: 0,
        activeLayers: [
          { layerId: 'hydro:river-gauges:latest', opacity: 0.9 },
          { layerId: 'climate:drought-index:historical', opacity: 0.6 },
        ],
      },
      timelineYear: 1935,
    },

    evidence: {
      evidenceManifestUri: 'data/evidence/manifests/story_nodes/topeka-river-gauges-1935-drought/evidence_manifest.json',
      requiredCitations: true,
      citations: [
        {
          id: 'cite:1',
          kind: 'dcat',
          ref: 'data/catalog/dcat/kfm-dcat-usgs-nwis-river-gauges.jsonld',
          label: 'USGS NWIS River Gauge Observations (DCAT)',
        },
        {
          id: 'cite:2',
          kind: 'stac',
          ref: 'data/catalog/stac/collections/kfm-hydro-river-gauges.json',
          label: 'River Gauges Collection (STAC)',
        },
        {
          id: 'cite:3',
          kind: 'prov',
          ref: `data/prov/${RUN_ID}/prov.json`,
          label: 'Ingest Activity Provenance (PROV)',
        },
      ],
    },

    classification: {
      level: 'PUBLIC',
      tags: ['STORY_NODE', 'EVIDENCE_FIRST', 'PROVENANCE_VISIBLE'],
    },
  },

  /**
   * 🧠 Focus Mode — Query Received
   * Captures user query + UI context bundle used for retrieval and reasoning.
   */
  'kfm.focus.query.received': {
    receivedAt: '2026-01-23T04:14:40.000Z' satisfies IsoDateTimeString,
    requestId: 'focus_req_9c2baf12',
    sessionId: 'focus_sess_01HNN2QK8YQW7A2Y9P2Z',
    user: {
      actorType: 'user',
      actorId: 'user_42',
      displayName: 'KFM Historian',
      roles: ['researcher'],
    },

    prompt: {
      text: 'What does this river gauge layer show around Topeka, and how should I interpret it for the 1930s drought context?',
      locale: 'en-US',
    },

    contextBundle: {
      mapState: {
        center: { lon: -95.689, lat: 39.0558 },
        zoom: 9.2,
        activeLayers: ['hydro:river-gauges:latest', 'climate:drought-index:historical'],
      },
      timelineYear: 1935,
      storyNodeId: 'story:node:topeka-river-gauges-1935-drought',
      requestedClassification: 'PUBLIC',
    },

    governance: {
      requireCitations: true,
      failClosedIfUnsourced: true,
      policyPackVersion: '13.0.0',
    },
  },

  /**
   * ✅ Focus Mode — Answer Generated
   * Includes citations, evidence trail, and sustainability telemetry (energy/carbon).
   */
  'kfm.focus.answer.generated': {
    completedAt: '2026-01-23T04:14:57.000Z' satisfies IsoDateTimeString,
    requestId: 'focus_req_9c2baf12',

    answer: {
      format: 'markdown',
      text:
        [
          'The **river gauge layer** shows observation points (stations) where water level/flow readings are recorded.',
          '',
          'For the **1930s drought context**, interpret it as *instrumental hydrology evidence*—not a drought index by itself.',
          'To link it to drought narratives, compare gauge signals with climate/drought layers and documented drought timelines.',
          '',
          '**Provenance & Sources:**',
          '- Gauge dataset metadata (DCAT): cite:1',
          '- Collection of station observations (STAC): cite:2',
          '- Ingest/processing lineage (PROV): cite:3',
        ].join('\n'),
      citations: [
        { id: 'cite:1', ref: 'data/catalog/dcat/kfm-dcat-usgs-nwis-river-gauges.jsonld' },
        { id: 'cite:2', ref: 'data/catalog/stac/collections/kfm-hydro-river-gauges.json' },
        { id: 'cite:3', ref: `data/prov/${RUN_ID}/prov.json` },
      ],
    },

    explainability: {
      auditPanel: {
        keySignals: [
          'Active layers: hydro:river-gauges:latest, climate:drought-index:historical',
          'Timeline year context: 1935',
          'Graph traversal: Dataset → Assets → Activity (PROV) → Agent',
        ],
        governanceFlags: [],
      },
    },

    provenance: {
      usedDatasets: [
        {
          dcatDatasetId: DCAT_DATASET_ID,
          dcatUri: 'data/catalog/dcat/kfm-dcat-usgs-nwis-river-gauges.jsonld',
        },
      ],
      stacRefs: [
        { collectionId: STAC_COLLECTION_ID, collectionUri: 'data/catalog/stac/collections/kfm-hydro-river-gauges.json' },
      ],
      provActivityId: PROV_BUNDLE_ID,
      evidenceManifestUri: EVIDENCE_MANIFEST_URI,
    },

    focusTelemetry: {
      model: { name: 'kfm-focus-llm', version: 'v13.2' },
      latencyMs: 1700,
      tokenUsage: { inputTokens: 620, outputTokens: 310 },
      sustainability: {
        energyWh: 0.42,
        carbonGCo2e: 0.19,
        notes: 'Approximate compute sustainability metrics captured for observability.',
      },
    },

    governance: {
      citationsPresent: true,
      classificationOk: true,
      policyPackVersion: '13.0.0',
      decision: 'allow',
      ledgerEntryId: 'ledger_entry_000000000043',
    },

    classification: {
      level: 'PUBLIC',
      tags: ['FOCUS_MODE', 'CITED', 'XAI', 'TELEMETRY'],
    },
  },

  /**
   * ⛔ Focus Mode — Answer Blocked
   * Example of refusal when citations cannot be provided (policy violation).
   */
  'kfm.focus.answer.blocked': {
    completedAt: '2026-01-23T04:20:12.000Z' satisfies IsoDateTimeString,
    requestId: 'focus_req_1aa2bb3c',

    blocked: {
      reason: 'UNSOURCED_RESPONSE',
      message:
        'Cannot answer as requested because no verified in-domain sources were found to support the claim. Please refine the question or add a specific dataset/layer.',
      policy: {
        ruleId: 'KFM-AI-CITE-001',
        decision: 'deny',
        failClosed: true,
      },
    },

    governance: {
      citationsPresent: false,
      policyPackVersion: '13.0.0',
      decision: 'deny',
      ledgerEntryId: 'ledger_entry_000000000044',
    },

    classification: {
      level: 'PUBLIC',
      tags: ['FOCUS_MODE', 'REFUSAL', 'FAIL_CLOSED'],
    },
  },

  /**
   * 📡 Streaming Observation — Reading Ingested
   * A single observation event aligned with catalog + provenance practices.
   */
  'kfm.streaming.observation.ingested': {
    observedAt: '2026-01-23T01:30:00.000Z' satisfies IsoDateTimeString,
    station: {
      stationId: 'USGS:06888990',
      name: 'Kansas River at Example Station',
      location: {
        type: 'Point',
        coordinates: [-95.689, 39.0558],
        crs: 'EPSG:4326',
      },
    },

    measurement: {
      kind: 'gage_height',
      value: 6.31,
      unit: 'ft',
      quality: { flags: ['provisional'], confidence: 0.86 },
    },

    catalogLinks: {
      dcatDatasetId: DCAT_DATASET_ID,
      stacCollectionId: STAC_COLLECTION_ID,
      stacItemUri: 'data/catalog/stac/items/hydro/river-gauges/06888990/2026-01-23T01-30-00Z.json',
      provActivityId: PROV_BUNDLE_ID,
    },

    classification: {
      level: 'PUBLIC',
      tags: ['STREAMING_DATA', 'OBSERVATION', 'HYDROLOGY'],
    },
  },

  /**
   * ⚖️ AI Monitoring — Drift Alert Triggered
   * Captures model drift signals and recommended action.
   */
  'kfm.ai.drift.alert.triggered': {
    detectedAt: '2026-01-23T05:00:00.000Z' satisfies IsoDateTimeString,
    model: { name: 'kfm-focus-llm', version: 'v13.2' },
    monitors: {
      citationCoverage: {
        baseline: 0.98,
        current: 0.91,
        threshold: 0.95,
        status: 'breach',
      },
      factualityChecks: {
        baseline: 0.97,
        current: 0.96,
        threshold: 0.95,
        status: 'ok',
      },
    },
    recommendation: {
      action: 'human_review_and_eval',
      notes: 'Investigate reduced citation coverage; check retrieval index freshness and policy pack changes.',
    },
    governance: {
      ledgerEntryId: 'ledger_entry_000000000045',
      notify: ['maintainers', 'ai-qa'],
    },
    classification: {
      level: 'INTERNAL',
      tags: ['AI_QA', 'DRIFT', 'ALERT'],
    },
  },

  /**
   * 🗺️ 3D / Virtual Worlds — Tileset Built
   * For Cesium/3D globe workflows: 3D tiles build output and metadata.
   */
  'kfm.tileset.3d.built': {
    builtAt: '2026-01-23T06:30:00.000Z' satisfies IsoDateTimeString,
    tileset: {
      id: 'tileset:kansas:terrain:v1',
      format: '3d-tiles',
      version: '1.1',
      uri: 'data/tilesets/kansas/terrain/v1/tileset.json',
      boundsWgs84: KANSAS_BBOX_WGS84,
    },
    source: {
      inputs: [
        { kind: 'raster', uri: 'data/rasters/dem/kansas_10m.tif' },
        { kind: 'vector', uri: 'data/vectors/hydro/river_network.geojson' },
      ],
      provActivityId: 'prov:kfm:activity:tileset_build:kansas:terrain:v1',
      runManifestUri: 'data/audits/run_tileset_terrain_v1/run_manifest.json',
    },
    classification: {
      level: 'PUBLIC',
      tags: ['3D', 'CESIUM', 'TERRAIN', 'VIRTUAL_WORLDS'],
    },
  },

  /**
   * 🧭 Geospatial Analysis — Route Generated
   * Example payload for PostGIS + pgRouting style routing output in GeoJSON.
   */
  'kfm.map.route.generated': {
    generatedAt: '2026-01-23T07:10:00.000Z' satisfies IsoDateTimeString,
    request: {
      mode: 'driving',
      engine: 'postgis+pgrouting',
      start: { lon: -95.689, lat: 39.0558 },
      end: { lon: -96.609, lat: 39.1836 },
      crs: 'EPSG:4326',
      costModel: 'time_minutes',
    },
    result: {
      distanceKm: 92.4,
      durationMinutes: 58.0,
      geojson: {
        type: 'FeatureCollection',
        features: [
          {
            type: 'Feature',
            properties: { name: 'Route 1', engine: 'pgr_dijkstra' },
            geometry: {
              type: 'LineString',
              coordinates: [
                [-95.689, 39.0558],
                [-96.15, 39.12],
                [-96.609, 39.1836],
              ],
            },
          },
        ],
      },
    },
    provenance: {
      datasetRefs: [
        {
          dcatDatasetId: 'kfm-dcat-kansas-road-network',
          uri: 'data/catalog/dcat/kfm-dcat-kansas-road-network.jsonld',
        },
      ],
      provActivityId: 'prov:kfm:activity:routing:2026-01-23:topeka-to-manhattan',
    },
    classification: {
      level: 'PUBLIC',
      tags: ['ROUTING', 'POSTGIS', 'ANALYSIS'],
    },
  },

  /**
   * 🔐 Privacy / Ethics — Anonymization Applied
   * Example payload reflecting privacy transformations (e.g., k-anonymity) before public release.
   */
  'kfm.privacy.anonymization.applied': {
    appliedAt: '2026-01-23T08:00:00.000Z' satisfies IsoDateTimeString,
    dataset: {
      sourceDcatDatasetId: 'kfm-dcat-sensitive-survey-responses',
      sourceUri: 'data/catalog/dcat/kfm-dcat-sensitive-survey-responses.jsonld',
      outputDcatDatasetId: 'kfm-dcat-sensitive-survey-responses-anon',
      outputUri: 'data/catalog/dcat/kfm-dcat-sensitive-survey-responses-anon.jsonld',
    },
    method: {
      strategy: 'k-anonymity',
      k: 10,
      additional: ['suppression', 'generalization'],
      notes:
        'Applied anonymization transforms to satisfy governance and reduce re-identification risk before publication.',
    },
    classificationPropagation: {
      inputClassification: 'RESTRICTED',
      outputClassification: 'INTERNAL',
      compliant: true,
    },
    governance: {
      policyPackVersion: '13.0.0',
      ruleId: 'KFM-PRIV-001',
      decision: 'allow_with_controls',
      ledgerEntryId: 'ledger_entry_000000000046',
    },
    classification: {
      level: 'INTERNAL',
      tags: ['PRIVACY', 'ETHICS', 'CARE'],
    },
  },

  /**
   * 🤖 Automation — Watcher/Planner/Executor PR Opened
   * Example payload for safe automation that routes changes through PR + governance.
   */
  'kfm.agent.pr.opened': {
    openedAt: '2026-01-23T09:05:00.000Z' satisfies IsoDateTimeString,
    agent: {
      architecture: 'watcher-planner-executor',
      watcherAlertId: 'alert_missing_metadata_00077',
      plannerPlanId: 'plan_patch_dcat_license_00077',
      executorId: 'kfm-agent-executor',
      killSwitchEnabled: false,
    },
    pr: {
      repo: 'Kansas-Frontier-Matrix',
      number: 418,
      branch: 'agent/patch-metadata-license-00077',
      title: 'Add SPDX license + provider metadata to new dataset contract',
      summary:
        'Automated plan created a minimal patch to satisfy license-presence + provenance linkage rules (no auto-merge).',
    },
    governance: {
      requiredReviews: 2,
      policyChecks: [
        { name: 'conftest-policy', status: 'pending' },
        { name: 'schema-validation', status: 'pending' },
      ],
      ledgerEntryId: 'ledger_entry_000000000047',
    },
    classification: {
      level: 'INTERNAL',
      tags: ['AGENT', 'GOVERNED_AUTOMATION', 'PR_WORKFLOW'],
    },
  },
} as const;

export type EventPayloadExampleKey = keyof typeof EVENT_PAYLOAD_EXAMPLES;
export type EventPayloadExample = (typeof EVENT_PAYLOAD_EXAMPLES)[EventPayloadExampleKey];

export function listEventPayloadExampleKeys(): EventPayloadExampleKey[] {
  return Object.keys(EVENT_PAYLOAD_EXAMPLES) as EventPayloadExampleKey[];
}

export function getEventPayloadExample(key: EventPayloadExampleKey): EventPayloadExample {
  return EVENT_PAYLOAD_EXAMPLES[key];
}

export default EVENT_PAYLOAD_EXAMPLES;
```

---
✅ **Done:** This is ready to paste directly into `api/src/contracts/examples/events/payloads/index.ts` 🚀

