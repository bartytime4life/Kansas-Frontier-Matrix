import invalidFixture from "../../../../fixtures/ui/view_registry_inspector_projection/invalid/extra-direct-store-field.json";
import availableFixture from "../../../../fixtures/ui/view_registry_inspector_projection/valid/available.json";
import heldFixture from "../../../../fixtures/ui/view_registry_inspector_projection/valid/held.json";
import { mountViewRegistryInspector } from "../../src/features/view_registry_inspector";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) {
  throw new Error("View Registry inspector fixture root is missing.");
}

const requested = new URL(window.location.href).searchParams.get("fixture");
const fixture =
  requested === "invalid"
    ? invalidFixture
    : requested === "held"
      ? heldFixture
      : availableFixture;

mountViewRegistryInspector(root, fixture);
