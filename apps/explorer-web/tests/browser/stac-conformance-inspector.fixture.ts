import invalidFixture from "../../../../fixtures/ui/stac_conformance_inspector_projection/invalid/extra-field.json";
import conformantFixture from "../../../../fixtures/ui/stac_conformance_inspector_projection/valid/conformant.json";
import nonConformantFixture from "../../../../fixtures/ui/stac_conformance_inspector_projection/valid/non-conformant.json";
import { mountStacConformanceInspector } from "../../src/features/stac_conformance_inspector";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) {
  throw new Error("STAC conformance inspector fixture root is missing.");
}

const requested = new URL(window.location.href).searchParams.get("fixture");
const fixture =
  requested === "invalid"
    ? invalidFixture
    : requested === "non-conformant"
      ? nonConformantFixture
      : conformantFixture;

mountStacConformanceInspector(root, fixture);
