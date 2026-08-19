import { describe, expect, it } from "vitest";
import {
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

  it("keeps the concrete MapLibre runtime explicitly held", () => {
    const runtime = FEATURE_CATALOG.find(
      (entry) => entry.id === "maplibre-runtime",
    );
    expect(runtime?.maturity).toBe("HOLD");
    expect(REPOSITORY_SNAPSHOT.mapLibre.dependencyAdmitted).toBe(false);
    expect(REPOSITORY_SNAPSHOT.mapLibre.runtimeImplemented).toBe(false);
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
