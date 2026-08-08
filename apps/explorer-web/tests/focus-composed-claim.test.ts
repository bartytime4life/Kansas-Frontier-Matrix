import { describe, expect, it, vi } from "vitest";

import abstainFixture from "../../../fixtures/ui/focus_composed_claim_projection/valid/abstain-unresolved.json";
import qualifiedFixture from "../../../fixtures/ui/focus_composed_claim_projection/valid/answer-qualified.json";
import supportedFixture from "../../../fixtures/ui/focus_composed_claim_projection/valid/answer-supported.json";
import denyFixture from "../../../fixtures/ui/focus_composed_claim_projection/valid/deny-policy.json";
import focusPanelSource from "../src/features/focus_panel/panel.ts?raw";
import focusParsersSource from "../src/features/focus_panel/parsers.ts?raw";
import focusResolverSource from "../src/features/focus_panel/resolver.ts?raw";
import {
  FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
  parseFocusComposedClaimProjection,
  parseFocusComposedClaimRequest,
  resolveFocusComposedClaim,
} from "../src/features/focus_panel";

const supportedRequest = Object.freeze({
  profile: FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
  request_id: "request:focus:soil-context-supported-001",
  claim_id: "claim:synthetic:soil-context-001",
  question: "What does the released synthetic soil evidence support?",
  allowed_evidence_refs: [
    "kfm:evidence:synthetic:soil-static-001",
    "kfm:evidence:synthetic:soil-station-001",
  ],
});

function clone<T>(value: T): T {
  return JSON.parse(JSON.stringify(value)) as T;
}

describe("Explorer Focus composed-claim projection", () => {
  it("strictly parses a bounded request without retaining caller mutation", () => {
    const input = {
      ...supportedRequest,
      allowed_evidence_refs: [...supportedRequest.allowed_evidence_refs],
    };
    const parsed = parseFocusComposedClaimRequest(input);
    input.allowed_evidence_refs[0] = "kfm:evidence:mutated";

    expect(parsed).toEqual({
      profile: FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
      requestId: "request:focus:soil-context-supported-001",
      claimId: "claim:synthetic:soil-context-001",
      question: "What does the released synthetic soil evidence support?",
      allowedEvidenceRefs: [
        "kfm:evidence:synthetic:soil-static-001",
        "kfm:evidence:synthetic:soil-station-001",
      ],
    });
  });

  it("rejects unknown fields, duplicate evidence refs, and unsafe questions", () => {
    expect(
      parseFocusComposedClaimRequest({ ...supportedRequest, raw_prompt: "not allowed" }),
    ).toBeNull();
    expect(
      parseFocusComposedClaimRequest({
        ...supportedRequest,
        allowed_evidence_refs: [
          "kfm:evidence:synthetic:soil-static-001",
          "kfm:evidence:synthetic:soil-static-001",
        ],
      }),
    ).toBeNull();
    expect(
      parseFocusComposedClaimRequest({
        ...supportedRequest,
        question: "unsafe\u0000question",
      }),
    ).toBeNull();
  });

  it("parses supported and qualified answer projections with dependency visibility", () => {
    const supported = parseFocusComposedClaimProjection(supportedFixture);
    const qualified = parseFocusComposedClaimProjection(qualifiedFixture);

    expect(supported).toMatchObject({
      outcome: "ANSWER",
      reasonCode: "COMPOSED_CLAIM_SUPPORTED",
      closureOutcome: "SUPPORTED",
      resolvedRoles: ["STATIC_SURVEY", "STATION_OBSERVATION"],
      unavailableRoles: [],
    });
    expect(qualified).toMatchObject({
      outcome: "ANSWER",
      reasonCode: "COMPOSED_CLAIM_QUALIFIED",
      closureOutcome: "QUALIFIED",
      resolvedRoles: ["STATIC_SURVEY"],
      unavailableRoles: ["STATION_OBSERVATION"],
    });
  });

  it("rejects citation drift, drawer drift, and unknown projection fields", () => {
    const citationDrift = clone(supportedFixture);
    citationDrift.citations[0]!.evidence_ref = "kfm:evidence:synthetic:other";
    expect(parseFocusComposedClaimProjection(citationDrift)).toBeNull();

    const drawerDrift = clone(supportedFixture);
    drawerDrift.evidence_drawer.evidence_refs = [
      "kfm:evidence:synthetic:soil-static-001",
    ];
    expect(parseFocusComposedClaimProjection(drawerDrift)).toBeNull();

    expect(
      parseFocusComposedClaimProjection({
        ...supportedFixture,
        private_reasoning: "not allowed",
      }),
    ).toBeNull();
  });

  it("renders a supported composed claim only inside declared EvidenceRef scope", async () => {
    const resolver = vi.fn(async () => supportedFixture);
    const result = await resolveFocusComposedClaim(supportedRequest, resolver);

    expect(resolver).toHaveBeenCalledTimes(1);
    expect(result).toMatchObject({
      code: "COMPOSED_CLAIM_SUPPORTED",
      view: {
        outcome: "ANSWER",
        closureOutcome: "SUPPORTED",
        evidenceRefs: [
          "kfm:evidence:synthetic:soil-static-001",
          "kfm:evidence:synthetic:soil-station-001",
        ],
        dependencyLabels: [
          "Resolved role: STATIC_SURVEY",
          "Resolved role: STATION_OBSERVATION",
        ],
      },
    });
    expect(result.view.aiReceiptLabel).toContain("not release proof");
  });

  it("renders qualified support with an explicit optional-role limitation", async () => {
    const request = {
      profile: FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
      request_id: "request:focus:soil-context-qualified-001",
      claim_id: "claim:synthetic:soil-context-002",
      question: "What bounded static soil support is available?",
      allowed_evidence_refs: ["kfm:evidence:synthetic:soil-static-002"],
    };
    const result = await resolveFocusComposedClaim(request, async () => qualifiedFixture);

    expect(result).toMatchObject({
      code: "COMPOSED_CLAIM_QUALIFIED",
      view: {
        outcome: "ANSWER",
        closureOutcome: "QUALIFIED",
        dependencyLabels: [
          "Resolved role: STATIC_SURVEY",
          "Unavailable optional role: STATION_OBSERVATION",
        ],
      },
    });
  });

  it("abstains without transport when the request has no governed evidence scope", async () => {
    const resolver = vi.fn(async () => supportedFixture);
    const result = await resolveFocusComposedClaim(
      { ...supportedRequest, allowed_evidence_refs: [] },
      resolver,
    );

    expect(resolver).not.toHaveBeenCalled();
    expect(result).toMatchObject({
      code: "MISSING_EVIDENCE_SCOPE",
      view: {
        outcome: "ABSTAIN",
        evidenceRefs: [],
        citations: [],
      },
    });
  });

  it("uses fixed abstain and deny copy without retaining private diagnostics", async () => {
    const abstainRequest = {
      profile: FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
      request_id: "request:focus:soil-context-abstain-001",
      claim_id: "claim:synthetic:soil-context-003",
      question: "Can the unresolved synthetic claim be answered?",
      allowed_evidence_refs: ["kfm:evidence:synthetic:soil-static-003"],
    };
    const denyRequest = {
      profile: FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
      request_id: "request:focus:soil-context-deny-001",
      claim_id: "claim:synthetic:soil-context-004",
      question: "Can restricted synthetic detail be shown?",
      allowed_evidence_refs: ["kfm:evidence:synthetic:restricted-004"],
    };

    const abstain = await resolveFocusComposedClaim(
      abstainRequest,
      async () => abstainFixture,
    );
    const deny = await resolveFocusComposedClaim(denyRequest, async () => denyFixture);

    expect(abstain.view.message).toBe(
      "The composed claim does not have sufficient released evidence support.",
    );
    expect(deny.view.message).toBe(
      "Policy does not permit this composed claim to be shown.",
    );
    expect(JSON.stringify(abstain)).not.toContain(
      "ABSTAIN_PRIVATE_DIAGNOSTIC_CANARY_795a24",
    );
    expect(JSON.stringify(deny)).not.toContain(
      "SENSITIVE_FOCUS_DENIAL_CANARY_36e71b",
    );
    expect(deny.view).toMatchObject({ evidenceRefs: [], citations: [] });
  });

  it("fails closed on response identity or EvidenceRef scope mismatch", async () => {
    const wrongIdentity = clone(supportedFixture);
    wrongIdentity.request_id = "request:focus:other";
    const identityResult = await resolveFocusComposedClaim(
      supportedRequest,
      async () => wrongIdentity,
    );
    expect(identityResult.code).toBe("RESPONSE_SCOPE_MISMATCH");

    const evidenceResult = await resolveFocusComposedClaim(
      {
        ...supportedRequest,
        allowed_evidence_refs: ["kfm:evidence:synthetic:other"],
      },
      async () => supportedFixture,
    );
    expect(evidenceResult).toMatchObject({
      code: "EVIDENCE_OUTSIDE_REQUEST",
      view: { outcome: "ERROR", citations: [], evidenceRefs: [] },
    });
  });

  it("uses fixed no-leak error copy when the governed resolver fails", async () => {
    const result = await resolveFocusComposedClaim(supportedRequest, async () => {
      throw new Error("PRIVATE_FOCUS_RESOLVER_CANARY_a4f6d8");
    });

    expect(result).toMatchObject({
      code: "GOVERNED_RESOLVER_ERROR",
      view: {
        outcome: "ERROR",
        message: "The governed Focus service could not complete the request.",
      },
    });
    expect(JSON.stringify(result)).not.toContain(
      "PRIVATE_FOCUS_RESOLVER_CANARY_a4f6d8",
    );
  });

  it("keeps the feature no-network and outside provider and lifecycle imports", () => {
    const focusSources = [focusParsersSource, focusResolverSource, focusPanelSource].join("\n");
    expect(focusSources).not.toMatch(/\bfetch\s*\(/);
    expect(focusSources).not.toMatch(
      /(?:from\s+|import\s*\()\s*["'](?:openai|ollama|@?anthropic|@google\/generative-ai|maplibre-gl)["']/i,
    );
    expect(focusSources).not.toMatch(
      /(?:from\s+|import\s*\()\s*["'][^"']*data\/(?:raw|work|quarantine|processed|catalog|triplets|published)[^"']*["']/i,
    );
    expect(focusSources).not.toMatch(/\b(?:chain_of_thought|private_reasoning|provider_trace)\b/);
  });
});
