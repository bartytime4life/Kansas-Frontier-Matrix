import { describe, expect, it } from "vitest";

import invalidExtraField from "../../../fixtures/ui/watcher_registry_browser_projection/invalid/extra-field.json";
import invalidPlaceholder from "../../../fixtures/ui/watcher_registry_browser_projection/invalid/placeholder-with-endpoint.json";
import availableFixture from "../../../fixtures/ui/watcher_registry_browser_projection/valid/available.json";
import deniedFixture from "../../../fixtures/ui/watcher_registry_browser_projection/valid/denied.json";
import errorFixture from "../../../fixtures/ui/watcher_registry_browser_projection/valid/error.json";
import heldFixture from "../../../fixtures/ui/watcher_registry_browser_projection/valid/held.json";
import adapterSource from "../src/adapters/WatcherRegistryBrowserProjection.ts?raw";
import featureSource from "../src/features/watcher_registry_browser/index.ts?raw";
import { parseWatcherRegistryBrowserProjection } from "../src/adapters/WatcherRegistryBrowserProjection";
import { resolveWatcherRegistryBrowser } from "../src/features/watcher_registry_browser";

describe("Explorer Watcher Registry browser", () => {
  it("shows inactive watcher metadata from a closed projection", () => {
    const result = resolveWatcherRegistryBrowser(availableFixture);

    expect(result).toMatchObject({
      outcome: "AVAILABLE",
      code: "REGISTRY_AVAILABLE",
      registryId: "kfm://control-plane/watcher-registry/v1",
      registryStatus: "PROPOSED_INACTIVE",
      canReadRegistry: false,
      canRunWatcher: false,
      canActivateSource: false,
      canWriteLifecycle: false,
      canEvaluatePolicy: false,
      canRelease: false,
      canPublish: false,
      accessibilityLabel: "Watcher Registry browser: available",
    });
    expect(result.watchers).toHaveLength(2);
    expect(result.watchers[0]).toMatchObject({
      watcherId: "kfm.watcher.shared.plants_drift.placeholder",
      state: "PLACEHOLDER",
      pollMode: "MANUAL_ONLY",
      endpointRef: null,
      outputTypes: [],
    });
    expect(result.watchers[1]).toMatchObject({
      watcherId: "kfm.watcher.soil.ssurgo_gnatsgo.candidate",
      state: "INACTIVE",
      outputTypes: ["SOIL_CHANGE_CANDIDATE", "SOIL_WATCHER_HOLD"],
    });
  });

  it("preserves abstain, deny, and error without watcher detail", () => {
    expect(resolveWatcherRegistryBrowser(heldFixture)).toMatchObject({
      outcome: "ABSTAIN",
      code: "REGISTRY_UNAVAILABLE",
      registryId: null,
      watchers: [],
    });
    expect(resolveWatcherRegistryBrowser(deniedFixture)).toMatchObject({
      outcome: "DENY",
      code: "POLICY_DENIED",
      registryId: null,
      watchers: [],
    });
    expect(resolveWatcherRegistryBrowser(errorFixture)).toMatchObject({
      outcome: "ERROR",
      code: "UPSTREAM_ERROR",
      registryId: null,
      watchers: [],
      ariaLive: "assertive",
    });
  });

  it("rejects unknown fields without reflecting their canary", () => {
    expect(parseWatcherRegistryBrowserProjection(invalidExtraField)).toEqual({
      ok: false,
      code: "MALFORMED_WATCHER_REGISTRY_BROWSER_PROJECTION",
    });
    const result = resolveWatcherRegistryBrowser(invalidExtraField);
    expect(result).toMatchObject({
      outcome: "ERROR",
      code: "INVALID_PAYLOAD",
      registryId: null,
      watchers: [],
    });
    expect(JSON.stringify(result)).not.toContain(
      "WATCHER_REGISTRY_INTERNAL_CANARY_9c45a1",
    );
  });

  it("fails closed when a placeholder carries endpoint or schedule claims", () => {
    expect(parseWatcherRegistryBrowserProjection(invalidPlaceholder)).toEqual({
      ok: false,
      code: "MALFORMED_WATCHER_REGISTRY_BROWSER_PROJECTION",
    });
  });

  it("rejects entry order, duplicate canonical identity, and unsafe governance", () => {
    const reversed = JSON.parse(JSON.stringify(availableFixture));
    reversed.watchers.reverse();

    const duplicateCanonical = JSON.parse(JSON.stringify(availableFixture));
    duplicateCanonical.watchers[1].canonical_id =
      duplicateCanonical.watchers[0].canonical_id;

    const unsafeGovernance = JSON.parse(JSON.stringify(availableFixture));
    unsafeGovernance.governance.watcher_execution_allowed = true;

    for (const candidate of [reversed, duplicateCanonical, unsafeGovernance]) {
      expect(parseWatcherRegistryBrowserProjection(candidate)).toEqual({
        ok: false,
        code: "MALFORMED_WATCHER_REGISTRY_BROWSER_PROJECTION",
      });
    }
  });

  it("uses an explicit abstention when no governed projection exists", () => {
    expect(resolveWatcherRegistryBrowser()).toMatchObject({
      outcome: "ABSTAIN",
      code: "NO_GOVERNED_RESPONSE",
      watchers: [],
      canRunWatcher: false,
      canActivateSource: false,
      canRelease: false,
      canPublish: false,
    });
  });

  it("contains no transport, persistence, direct-store, or mutation seam", () => {
    const source = `${adapterSource}\n${featureSource}`;
    expect(source).not.toMatch(/\bfetch\s*\(|XMLHttpRequest|WebSocket/);
    expect(source).not.toMatch(/\b(?:localStorage|sessionStorage)\b/);
    expect(source).not.toMatch(
      /data\/(?:raw|work|quarantine|processed|catalog|triplets|published)/i,
    );
    expect(source).not.toMatch(
      /\b(?:runWatcher|activateSource|writeLifecycle|approve|release|publish)\s*\(/i,
    );
  });
});
