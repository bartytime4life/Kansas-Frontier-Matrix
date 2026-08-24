import { describe, expect, it, vi } from "vitest";

import qualifiedFixture from "../../../fixtures/ui/focus_composed_claim_projection/valid/answer-qualified.json";
import workspaceSource from "../src/site/mount-synthetic-focus-workspace.ts?raw";
import {
  FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
  resolveFocusComposedClaim,
} from "../src/features/focus_panel";
import { resolveSyntheticFocusWorkspaceProjection } from "../src/site/mount-synthetic-focus-workspace";

const request = Object.freeze({
  profile: FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
  request_id: "request:focus:soil-context-qualified-001",
  claim_id: "claim:synthetic:soil-context-002",
  question: "What endorsed synthetic support remains after policy withholding?",
  allowed_evidence_refs: ["kfm:evidence:synthetic:soil-static-002"],
});

function clone<T>(value: T): T {
  return JSON.parse(JSON.stringify(value)) as T;
}

describe("Focus workspace governed boundary", () => {
  it("keeps machine-only withheld context outside the public projection", async () => {
    const machineOnlyContext = Object.freeze({
      role: "RESTRICTED_CONTEXT",
      raw: "RAW_GOVERNED_CONTEXT_CANARY_3373",
    });
    const projection = clone(qualifiedFixture);
    projection.unavailable_roles = [machineOnlyContext.role];
    projection.limitations = [
      "One synthetic restricted-context role is withheld by policy; no protected detail is exposed.",
    ];
    projection.evidence_drawer.limitations = [...projection.limitations];

    const resolver = vi.fn(async () => {
      expect(machineOnlyContext.raw).toBe("RAW_GOVERNED_CONTEXT_CANARY_3373");
      return projection;
    });
    const result = await resolveFocusComposedClaim(request, resolver);

    expect(resolver).toHaveBeenCalledTimes(1);
    expect(result).toMatchObject({
      code: "COMPOSED_CLAIM_QUALIFIED",
      projection: {
        policy: "ALLOW",
        unavailableRoles: ["RESTRICTED_CONTEXT"],
      },
      view: {
        outcome: "ANSWER",
        evidenceRefs: ["kfm:evidence:synthetic:soil-static-002"],
        citations: [
          {
            evidenceRef: "kfm:evidence:synthetic:soil-static-002",
            label: "Synthetic static soil survey fixture",
          },
        ],
      },
    });
    expect(JSON.stringify(result)).not.toContain(machineOnlyContext.raw);

    const rejected = await resolveFocusComposedClaim(request, async () => ({
      ...projection,
      raw_governed_context: machineOnlyContext.raw,
    }));
    expect(rejected.code).toBe("PROJECTION_INVALID");
    expect(JSON.stringify(rejected)).not.toContain(machineOnlyContext.raw);
  });

  it("keeps the normal-workspace mount no-network and outside raw data or providers", () => {
    expect(workspaceSource).not.toMatch(/\bfetch\s*\(/);
    expect(workspaceSource).not.toMatch(
      /(?:from\s+|import\s*\()\s*["'](?:openai|ollama|@?anthropic|@google\/generative-ai|maplibre-gl)["']/i,
    );
    expect(workspaceSource).not.toMatch(
      /(?:from\s+|import\s*\()\s*["'][^"']*data\/(?:raw|work|quarantine|processed|catalog|triplets|published)[^"']*["']/i,
    );
    expect(workspaceSource).not.toContain("RAW_GOVERNED_CONTEXT_CANARY_3373");
    expect(workspaceSource).not.toContain("raw_governed_context");
  });

  it("binds the corrected workspace answer to active evidence while retaining history", async () => {
    const result = await resolveFocusComposedClaim(
      {
        profile: FOCUS_COMPOSED_CLAIM_REQUEST_PROFILE,
        request_id: "request:focus:corrected-evidence-001",
        claim_id: "claim:synthetic:corrected-evidence-001",
        question: "What does the corrected synthetic summary support?",
        allowed_evidence_refs: [
          "kfm:evidence:synthetic:corrected-soil-summary-001",
        ],
      },
      resolveSyntheticFocusWorkspaceProjection,
    );

    expect(result).toMatchObject({
      code: "COMPOSED_CLAIM_SUPPORTED",
      projection: {
        evidenceDrawer: {
          trustLabels: expect.arrayContaining(["Correction: CORRECTED"]),
          historyLabels: expect.arrayContaining([
            "Correction lineage: kfm:evidence:synthetic:superseded-soil-summary-001 → kfm:evidence:synthetic:corrected-soil-summary-001 (2026-08-20T00:00:00Z)",
          ]),
        },
      },
      view: {
        evidenceRefs: [
          "kfm:evidence:synthetic:corrected-soil-summary-001",
        ],
      },
    });
    expect(result.view.evidenceRefs).not.toContain(
      "kfm:evidence:synthetic:superseded-soil-summary-001",
    );
  });
});
