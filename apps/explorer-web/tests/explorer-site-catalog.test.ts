import { describe, expect, it } from "vitest";
import {
  CURRENT_MAPLIBRE_READINESS,
  FEATURE_CATALOG,
  KNOWLEDGE_DOMAINS,
  REPOSITORY_SNAPSHOT,
  filterFeatures,
  findDomain,
} from "../src/site/catalog";

describe("Explorer repository catalog", () => {
  it("keeps feature and domain identifiers unique", () => {
    expect(new Set(FEATURE_CATALOG.map((entry) => entry.id)).size).toBe(
      FEATURE_CATALOG.length,
    );
    expect(new Set(FEATURE_CATALOG.map((entry) => entry.path)).size).toBe(
      FEATURE_CATALOG.length,
    );
    expect(new Set(KNOWLEDGE_DOMAINS.map((entry) => entry.id)).size).toBe(
      KNOWLEDGE_DOMAINS.length,
    );
  });

  it("represents every domain as repository-owned Explorer knowledge", () => {
    expect(KNOWLEDGE_DOMAINS).toHaveLength(13);
    expect(
      KNOWLEDGE_DOMAINS.every((entry) =>
        entry.path.startsWith("apps/explorer-web/src/features/domains/"),
      ),
    ).toBe(true);
  });

  it("keeps the current MapLibre runtime explicitly held without rewriting the snapshot", () => {
    const runtime = FEATURE_CATALOG.find(
      (entry) => entry.id === "maplibre-runtime",
    );
    expect(runtime?.maturity).toBe("HOLD");
    expect(REPOSITORY_SNAPSHOT.mapLibre.readinessCandidate).toBe("6.4.0");
    expect(REPOSITORY_SNAPSHOT.mapLibre.dependencyAdmitted).toBe(false);
    expect(REPOSITORY_SNAPSHOT.mapLibre.runtimeImplemented).toBe(false);
    expect(CURRENT_MAPLIBRE_READINESS).toMatchObject({
      evidenceCommit: "1a3a4075537ea47b7b87b3e2dccbb044b6a62e0f",
      readinessCandidate: "6.6.0",
      readinessState: "HOLD",
      packagePresent: true,
      adapterImplemented: true,
      browserRuntimeActivated: false,
      browserEvidenceComplete: false,
    });
  });

  it("finds cross-domain and maturity-filtered feature slices", () => {
    expect(filterFeatures({ text: "hydrology" }).length).toBeGreaterThan(0);
    expect(
      filterFeatures({ maturity: "VERIFIED_SLICE" }).every(
        (entry) => entry.maturity === "VERIFIED_SLICE",
      ),
    ).toBe(true);
    expect(
      filterFeatures({ area: "Evidence and trust", text: "citation" }).length,
    ).toBeGreaterThan(0);
  });

  it("preserves strong safeguards for sensitive identity-adjacent knowledge", () => {
    const domain = findDomain("people_dna_land");
    expect(domain).not.toBeNull();
    expect(domain?.safeguard.toLocaleLowerCase()).toContain(
      "default deny",
    );
  });
});
