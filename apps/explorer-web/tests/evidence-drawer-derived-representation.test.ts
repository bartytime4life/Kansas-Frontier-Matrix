import { describe, expect, it } from "vitest";

import answerFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json";
import denyFixture from "../../../fixtures/ui/evidence_drawer_payload/valid/deny-sensitive.json";
import evidenceDrawerSource from "../src/features/evidence_drawer/index.tsx?raw";
import {
  DERIVED_REPRESENTATION_DISCLOSURE,
  resolveEvidenceDrawer,
} from "../src/features/evidence_drawer";

describe("Evidence Drawer derived-representation disclosure", () => {
  it("prominently distinguishes supported derived output from source-observed evidence", () => {
    const derivedAnswer = {
      ...answerFixture,
      trust_state: {
        ...answerFixture.trust_state,
        source_role: "derived",
      },
    };

    const result = resolveEvidenceDrawer(derivedAnswer);

    expect(result).toMatchObject({
      outcome: "ANSWER",
      code: "SUPPORTED",
      representationDisclosure: DERIVED_REPRESENTATION_DISCLOSURE,
    });
    expect(result.representationDisclosure?.message).toBe(
      "Computed from upstream evidence; not a source-observed relationship or event.",
    );
    expect(result.trustLabels).toContain("Source role: derived");
  });

  it.each(["authoritative", "official", "context"] as const)(
    "does not falsely label a %s projection as derived",
    (sourceRole: "authoritative" | "official" | "context") => {
      const projection = {
        ...answerFixture,
        trust_state: {
          ...answerFixture.trust_state,
          source_role: sourceRole,
        },
      };

      expect(resolveEvidenceDrawer(projection).representationDisclosure).toBeNull();
    },
  );

  it("never exposes a derived disclosure as a substitute for denied evidence", () => {
    const deniedDerivedProjection = {
      ...denyFixture,
      trust_state: {
        ...denyFixture.trust_state,
        source_role: "derived",
      },
    };

    const result = resolveEvidenceDrawer(deniedDerivedProjection);

    expect(result).toMatchObject({
      outcome: "DENY",
      code: "SENSITIVE_DETAIL_RESTRICTED",
      representationDisclosure: null,
    });
    expect(result.evidenceRefs).toEqual([]);
    expect(result.citations).toEqual([]);
  });

  it("renders the disclosure as a semantic note with stable inspection hooks", () => {
    expect(evidenceDrawerSource).toContain(
      'dataset.component = "derived-representation-disclosure"',
    );
    expect(evidenceDrawerSource).toContain(
      'setAttribute("role", "note")',
    );
    expect(evidenceDrawerSource).toContain(
      'setAttribute("aria-label", "Representation disclosure")',
    );
  });
});
