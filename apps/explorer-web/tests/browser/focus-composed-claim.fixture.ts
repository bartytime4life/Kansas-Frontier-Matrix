import abstainFixture from "../../../../fixtures/ui/focus_composed_claim_projection/valid/abstain-unresolved.json";
import qualifiedFixture from "../../../../fixtures/ui/focus_composed_claim_projection/valid/answer-qualified.json";
import supportedFixture from "../../../../fixtures/ui/focus_composed_claim_projection/valid/answer-supported.json";
import denyFixture from "../../../../fixtures/ui/focus_composed_claim_projection/valid/deny-policy.json";
import {
  FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
  mountFocusComposedClaimFixture,
  type FocusComposedClaimFixtureCase,
} from "../../src/features/focus_panel";

const cases: readonly FocusComposedClaimFixtureCase[] = Object.freeze([
  {
    caseId: "supported",
    label: "Ask supported composed claim",
    request: {
      profile: FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
      request_id: "request:focus:soil-context-supported-001",
      claim_id: "claim:synthetic:soil-context-001",
      question: "What does the released synthetic soil evidence support?",
      allowed_evidence_refs: [
        "kfm:evidence:synthetic:soil-static-001",
        "kfm:evidence:synthetic:soil-station-001",
      ],
    },
  },
  {
    caseId: "qualified",
    label: "Ask qualified composed claim",
    request: {
      profile: FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
      request_id: "request:focus:soil-context-qualified-001",
      claim_id: "claim:synthetic:soil-context-002",
      question: "What bounded static soil support is available?",
      allowed_evidence_refs: ["kfm:evidence:synthetic:soil-static-002"],
    },
  },
  {
    caseId: "abstain",
    label: "Ask unresolved composed claim",
    request: {
      profile: FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
      request_id: "request:focus:soil-context-abstain-001",
      claim_id: "claim:synthetic:soil-context-003",
      question: "Can the unresolved synthetic claim be answered?",
      allowed_evidence_refs: ["kfm:evidence:synthetic:soil-static-003"],
    },
  },
  {
    caseId: "deny",
    label: "Ask restricted composed claim",
    request: {
      profile: FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
      request_id: "request:focus:soil-context-deny-001",
      claim_id: "claim:synthetic:soil-context-004",
      question: "Can restricted synthetic detail be shown?",
      allowed_evidence_refs: ["kfm:evidence:synthetic:restricted-004"],
    },
  },
  {
    caseId: "scope-mismatch",
    label: "Ask composed claim outside evidence scope",
    request: {
      profile: FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
      request_id: "request:focus:soil-context-supported-001",
      claim_id: "claim:synthetic:soil-context-001",
      question: "Can evidence outside the request scope be used?",
      allowed_evidence_refs: ["kfm:evidence:synthetic:other"],
    },
  },
  {
    caseId: "resolver-error",
    label: "Ask composed claim with resolver failure",
    request: {
      profile: FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
      request_id: "request:focus:resolver-error-001",
      claim_id: "claim:synthetic:resolver-error-001",
      question: "Can a failed resolver produce an answer?",
      allowed_evidence_refs: ["kfm:evidence:synthetic:resolver-error-001"],
    },
  },
]);

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("Focus composed-claim fixture root is missing.");

mountFocusComposedClaimFixture(root, cases, async (request) => {
  await Promise.resolve();
  switch (request.requestId) {
    case "request:focus:soil-context-qualified-001":
      return qualifiedFixture;
    case "request:focus:soil-context-abstain-001":
      return abstainFixture;
    case "request:focus:soil-context-deny-001":
      return denyFixture;
    case "request:focus:resolver-error-001":
      throw new Error("PRIVATE_BROWSER_FOCUS_RESOLVER_CANARY_c74bd9");
    default:
      return supportedFixture;
  }
});
