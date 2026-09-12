import { describe, expect, it } from "vitest";
import {
  CURRENT_MAPLIBRE_READINESS,
  FEATURE_CATALOG,
  KNOWLEDGE_DOMAINS,
  REPOSITORY_SNAPSHOT,
  filterFeatures,
  findDomain,
  repositoryUrl,
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

  it("binds the website catalog and MapLibre HOLD to the refreshed repository snapshot", () => {
    const runtime = FEATURE_CATALOG.find(
      (entry) => entry.id === "maplibre-runtime",
    );
    expect(runtime?.maturity).toBe("HOLD");
    expect(REPOSITORY_SNAPSHOT).toMatchObject({
      commit: "d25a4c046892aa826ca04da29215f8ae4aae8e51",
      commitRecordedAt: "2026-09-12T01:19:24Z",
      mapLibre: {
        readinessCandidate: "6.7.0",
        readinessState: "HOLD",
        packagePresent: true,
        adapterImplemented: true,
        browserRuntimeActivated: false,
        browserEvidenceComplete: false,
      },
    });
    expect(CURRENT_MAPLIBRE_READINESS).toMatchObject({
      evidenceCommit: "033103a0afe80f85a823973951b3b7d15abb7a8b",
      evidenceRecordedAt: "2026-09-09T02:12:08Z",
      readinessCandidate: "6.7.0",
      readinessState: "HOLD",
      packagePresent: true,
      adapterImplemented: true,
      browserRuntimeActivated: false,
      browserEvidenceComplete: false,
    });
    expect(repositoryUrl("apps/explorer-web")).toContain(
      `/tree/${REPOSITORY_SNAPSHOT.commit}/apps/explorer-web`,
    );
    expect(repositoryUrl("contracts/data/layer_manifest.md", "blob")).toContain(
      `/blob/${REPOSITORY_SNAPSHOT.commit}/contracts/data/layer_manifest.md`,
    );
  });

  it("catalogs the map-first Living Atlas as fixture-first work", () => {
    expect(FEATURE_CATALOG.find((entry) => entry.id === "living-atlas")).toMatchObject({
      maturity: "FIXTURE_FIRST",
      path: "apps/explorer-web/src/features/living_atlas",
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
