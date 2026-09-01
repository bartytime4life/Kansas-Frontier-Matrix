import answerFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json";
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
    case "selection:stale":
    case "selection:stale-mismatch":
      return staleFixture;
    case "selection:superseded":
    case "selection:history-mismatch":
      return supersededFixture;
    case "selection:resolver-error":
      throw new Error("PRIVATE_BROWSER_RESOLVER_CANARY_0b10d7");
    default:
      return answerFixture;
  }
});
