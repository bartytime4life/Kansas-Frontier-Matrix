import withdrawnFixture from "../../../../fixtures/ui/focus_composed_claim_projection/valid/abstain-withdrawn.json";
import answerFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json";
import heldFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/abstain-source-drift-review.json";
import revokedFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/abstain-revoked.json";
import staleFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/abstain-stale.json";
import supersededFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/abstain-superseded.json";
import denyFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/deny-sensitive.json";
import {
  MAP_FEATURE_SELECTION_PROFILE,
  mountMapFeatureEvidenceFixture,
  type MapEvidenceFixtureCase,
} from "../../src/features/map_runtime";

const cases: readonly MapEvidenceFixtureCase[] = Object.freeze([
  {
    caseId: "answer",
    label: "Select supported map feature",
    selection: {
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selection_id: "selection:flow-001",
      layer_id: "layer:synthetic-streamflow",
      feature_id: "feature:flow-001",
      evidence_refs: [
        "kfm:evidence:synthetic:flow-001",
        "kfm:evidence:synthetic:flow-000",
      ],
    },
  },
  {
    caseId: "missing",
    label: "Select feature without governed evidence",
    selection: {
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selection_id: "selection:missing-evidence",
      layer_id: "layer:synthetic-streamflow",
      feature_id: "feature:missing-evidence",
      evidence_refs: [],
    },
  },
  {
    caseId: "deny",
    label: "Select policy-restricted map feature",
    selection: {
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selection_id: "selection:restricted",
      layer_id: "layer:synthetic-restricted",
      feature_id: "feature:restricted",
      evidence_refs: ["kfm:evidence:synthetic:restricted"],
    },
  },
  {
    caseId: "held",
    label: "Select held evidence history",
    selection: {
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selection_id: "selection:held",
      layer_id: "layer:synthetic-streamflow",
      feature_id: "feature:held",
      evidence_refs: ["kfm:evidence:synthetic:source-drift-held-001"],
    },
  },
  {
    caseId: "held-mismatch",
    label: "Select feature with mismatched held evidence",
    selection: {
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selection_id: "selection:held-mismatch",
      layer_id: "layer:synthetic-streamflow",
      feature_id: "feature:held-mismatch",
      evidence_refs: ["kfm:evidence:synthetic:other"],
    },
  },
  {
    caseId: "stale",
    label: "Select stale map evidence",
    selection: {
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selection_id: "selection:stale",
      layer_id: "layer:synthetic-streamflow",
      feature_id: "feature:stale",
      evidence_refs: ["kfm:evidence:synthetic:stale-001"],
    },
  },
  {
    caseId: "stale-mismatch",
    label: "Select feature with mismatched stale evidence",
    selection: {
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selection_id: "selection:stale-mismatch",
      layer_id: "layer:synthetic-streamflow",
      feature_id: "feature:stale-mismatch",
      evidence_refs: ["kfm:evidence:synthetic:other"],
    },
  },
  {
    caseId: "withdrawn",
    label: "Select withdrawn evidence history",
    selection: {
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selection_id: "selection:withdrawn",
      layer_id: "layer:synthetic-streamflow",
      feature_id: "feature:withdrawn",
      evidence_refs: [
        "kfm:evidence:synthetic:withdrawn-soil-summary-001",
      ],
    },
  },
  {
    caseId: "withdrawn-mismatch",
    label: "Select feature with mismatched withdrawn evidence",
    selection: {
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selection_id: "selection:withdrawn-mismatch",
      layer_id: "layer:synthetic-streamflow",
      feature_id: "feature:withdrawn-mismatch",
      evidence_refs: ["kfm:evidence:synthetic:other"],
    },
  },
  {
    caseId: "revoked",
    label: "Select revoked evidence history",
    selection: {
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selection_id: "selection:revoked",
      layer_id: "layer:synthetic-streamflow",
      feature_id: "feature:revoked",
      evidence_refs: ["kfm:evidence:synthetic:revoked-001"],
    },
  },
  {
    caseId: "revoked-mismatch",
    label: "Select feature with mismatched revoked evidence",
    selection: {
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selection_id: "selection:revoked-mismatch",
      layer_id: "layer:synthetic-streamflow",
      feature_id: "feature:revoked-mismatch",
      evidence_refs: ["kfm:evidence:synthetic:other"],
    },
  },
  {
    caseId: "superseded",
    label: "Select superseded evidence history",
    selection: {
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selection_id: "selection:superseded",
      layer_id: "layer:synthetic-streamflow",
      feature_id: "feature:superseded",
      evidence_refs: ["kfm:evidence:synthetic:superseded-001"],
    },
  },
  {
    caseId: "history-mismatch",
    label: "Select feature with mismatched evidence history",
    selection: {
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selection_id: "selection:history-mismatch",
      layer_id: "layer:synthetic-streamflow",
      feature_id: "feature:history-mismatch",
      evidence_refs: ["kfm:evidence:synthetic:flow-001"],
    },
  },
  {
    caseId: "mismatch",
    label: "Select feature with mismatched evidence",
    selection: {
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selection_id: "selection:mismatch",
      layer_id: "layer:synthetic-streamflow",
      feature_id: "feature:mismatch",
      evidence_refs: ["kfm:evidence:synthetic:other"],
    },
  },
  {
    caseId: "error",
    label: "Select feature with resolver failure",
    selection: {
      profile: MAP_FEATURE_SELECTION_PROFILE,
      selection_id: "selection:resolver-error",
      layer_id: "layer:synthetic-streamflow",
      feature_id: "feature:resolver-error",
      evidence_refs: ["kfm:evidence:synthetic:flow-001"],
    },
  },
]);

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("Map evidence fixture root is missing.");

mountMapFeatureEvidenceFixture(root, cases, async (selection) => {
  await Promise.resolve();
  switch (selection.selectionId) {
    case "selection:restricted":
      return denyFixture;
    case "selection:held":
    case "selection:held-mismatch":
      return heldFixture;
    case "selection:stale":
    case "selection:stale-mismatch":
      return staleFixture;
    case "selection:withdrawn":
    case "selection:withdrawn-mismatch":
      return withdrawnFixture.evidence_drawer;
    case "selection:revoked":
    case "selection:revoked-mismatch":
      return revokedFixture;
    case "selection:superseded":
    case "selection:history-mismatch":
      return supersededFixture;
    case "selection:resolver-error":
      throw new Error("PRIVATE_BROWSER_RESOLVER_CANARY_0b10d7");
    default:
      return answerFixture;
  }
});
