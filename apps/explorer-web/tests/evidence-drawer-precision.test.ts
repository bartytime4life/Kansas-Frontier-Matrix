import { describe, expect, it } from "vitest";

import answerFixture from "../../../fixtures/contracts/v1/runtime/runtime_response_envelope/valid/valid_2.json";
import {
  parsePrecisionDisclosure,
  precisionDisclosureLabels,
} from "../src/features/evidence_drawer/precision";

describe("Runtime precision-actually-used projection", () => {
  it("renders the three evidence-supported precision dimensions", () => {
    expect(precisionDisclosureLabels(answerFixture.precision_actually_used)).toEqual([
      "Spatial: 250-meter gridded support",
      "Temporal: Daily observation support",
      "Attribute: One decimal place in the cited measurement",
    ]);
  });

  it("preserves evidence/source/transform basis without treating it as proof", () => {
    const parsed = parsePrecisionDisclosure(answerFixture.precision_actually_used);
    expect(parsed?.basis.evidence_refs).toEqual([
      { ref: "obs:1", kind: "measurement" },
    ]);
    expect(parsed?.basis.source_refs).toEqual([
      "fixture:source:runtime-precision",
    ]);
    expect(parsed?.basis.transform_refs).toEqual([]);
  });

  it("fails closed on missing basis evidence", () => {
    const malformed = structuredClone(answerFixture.precision_actually_used);
    malformed.basis.evidence_refs = [];
    expect(parsePrecisionDisclosure(malformed)).toBeNull();
    expect(precisionDisclosureLabels(malformed)).toBeNull();
  });

  it("fails closed on unexpected diagnostic fields", () => {
    const malformed = {
      ...structuredClone(answerFixture.precision_actually_used),
      internal_precision_reason: "PRIVATE_CANARY",
    };
    expect(parsePrecisionDisclosure(malformed)).toBeNull();
    expect(JSON.stringify(precisionDisclosureLabels(malformed))).not.toContain(
      "PRIVATE_CANARY",
    );
  });
});
