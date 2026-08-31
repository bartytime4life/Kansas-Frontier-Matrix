export const governedLayerResponse = Object.freeze({
  profile: "kfm.governed-api.synthetic-layer-slice.v1",
  scope: "slice-local",
  outcome: "ANSWER",
  reason_code: "SUPPORTED",
  layers: Object.freeze([
    Object.freeze({
      source_id: "source:synthetic-streamflow",
      layer_id: "layer:synthetic-streamflow",
      kind: "circle",
      title: "Synthetic streamflow demonstration",
      description:
        "One generalized, fixture-only Kansas streamflow feature for the bounded governed map slice.",
      geojson: Object.freeze({
        type: "FeatureCollection",
        features: Object.freeze([
          Object.freeze({
            type: "Feature",
            id: "feature:flow-001",
            geometry: Object.freeze({
              type: "Point",
              coordinates: Object.freeze([-98.5, 38.5]),
            }),
            properties: null,
          }),
        ]),
      }),
      selection: Object.freeze({
        profile: "kfm.explorer.map-feature-selection.v1",
        selection_id: "selection:flow-001",
        layer_id: "layer:synthetic-streamflow",
        feature_id: "feature:flow-001",
        evidence_refs: Object.freeze(["kfm:evidence:synthetic:flow-001"]),
      }),
    }),
  ]),
  limitations: Object.freeze([
    "Fixture-only synthetic demonstration; not live data, release authority, or life-safety guidance.",
  ]),
});

const baseTrust = Object.freeze({
  source_role: "official",
  policy: "ALLOW",
  review: "REVIEWED",
  release: "RELEASED",
  freshness: "CURRENT",
  correction: "NONE",
});

export const governedAnswerResponse = Object.freeze({
  profile: "kfm.explorer.evidence-drawer.public-safe.v1",
  id: "kfm:ui:evidence-drawer:answer-001",
  outcome: "ANSWER",
  reason_code: "SUPPORTED",
  title: "Synthetic streamflow observation",
  summary:
    "A synthetic, generalized flow observation is supported by the cited fixture evidence.",
  evidence_refs: Object.freeze(["kfm:evidence:synthetic:flow-001"]),
  citations: Object.freeze([
    Object.freeze({
      label: "Synthetic fixture evidence",
      href: "https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/d1f7ed51cf4d9c9c2fdf94cdc81644744ae464ce/fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json",
    }),
  ]),
  limitations: Object.freeze([
    "Fixture-only demonstration; not a live observation or life-safety instruction.",
  ]),
  trust_state: Object.freeze({ ...baseTrust, correction: "CORRECTED" }),
  history: Object.freeze({
    negative_outcomes: Object.freeze([
      Object.freeze({
        evidence_ref: "kfm:evidence:synthetic:flow-000",
        state: "SUPERSEDED",
        reason_code: "SUPERSEDED_EVIDENCE",
        recorded_at: "2026-08-01T00:00:00Z",
        visible_in_runtime: true,
        resolvable_as_current: false,
      }),
    ]),
    corrections: Object.freeze([
      Object.freeze({
        prior_evidence_ref: "kfm:evidence:synthetic:flow-000",
        active_evidence_ref: "kfm:evidence:synthetic:flow-001",
        status: "ACTIVE_CORRECTION",
        recorded_at: "2026-08-01T00:00:00Z",
      }),
    ]),
  }),
});

export const governedDenyResponse = Object.freeze({
  profile: "kfm.explorer.evidence-drawer.public-safe.v1",
  id: "kfm:ui:evidence-drawer:deny-001",
  outcome: "DENY",
  reason_code: "SENSITIVE_DETAIL_RESTRICTED",
  title: "PRIVATE_DENIAL_CANARY",
  summary: "PRIVATE_DENIAL_CANARY",
  evidence_refs: Object.freeze([]),
  citations: Object.freeze([]),
  limitations: Object.freeze(["PRIVATE_DENIAL_CANARY"]),
  trust_state: Object.freeze({
    source_role: "context",
    policy: "DENY",
    review: "PENDING",
    release: "UNRELEASED",
    freshness: "UNKNOWN",
    correction: "NONE",
  }),
  history: Object.freeze({
    negative_outcomes: Object.freeze([]),
    corrections: Object.freeze([]),
  }),
});

export const governedErrorResponse = Object.freeze({
  profile: "kfm.explorer.evidence-drawer.public-safe.v1",
  id: "kfm:ui:evidence-drawer:error-001",
  outcome: "ERROR",
  reason_code: "UPSTREAM_ERROR",
  title: "PRIVATE_ERROR_CANARY",
  summary: "PRIVATE_ERROR_CANARY",
  evidence_refs: Object.freeze([]),
  citations: Object.freeze([]),
  limitations: Object.freeze(["PRIVATE_ERROR_CANARY"]),
  trust_state: Object.freeze({
    source_role: "context",
    policy: "ERROR",
    review: "NOT_APPLICABLE",
    release: "UNRELEASED",
    freshness: "UNKNOWN",
    correction: "NONE",
  }),
  history: Object.freeze({
    negative_outcomes: Object.freeze([]),
    corrections: Object.freeze([]),
  }),
});
