import invalidFixture from "../../../../fixtures/ui/watcher_registry_browser_projection/invalid/extra-field.json";
import availableFixture from "../../../../fixtures/ui/watcher_registry_browser_projection/valid/available.json";
import { mountWatcherRegistryBrowser } from "../../src/features/watcher_registry_browser";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("Watcher Registry browser fixture root is missing.");

const requested = new URL(window.location.href).searchParams.get("fixture");
mountWatcherRegistryBrowser(
  root,
  requested === "invalid" ? invalidFixture : availableFixture,
);
