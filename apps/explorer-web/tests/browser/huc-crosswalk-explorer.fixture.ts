import invalidFixture from "../../../../fixtures/ui/huc_crosswalk_projection/invalid/extra-field.json";
import ambiguousFixture from "../../../../fixtures/ui/huc_crosswalk_projection/valid/ambiguous.json";
import verifiedFixture from "../../../../fixtures/ui/huc_crosswalk_projection/valid/verified-exact.json";
import { mountHucCrosswalkExplorer } from "../../src/features/huc_crosswalk_explorer";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) {
  throw new Error("HUC crosswalk explorer fixture root is missing.");
}

const requested = new URL(window.location.href).searchParams.get("fixture");
const fixture =
  requested === "invalid"
    ? invalidFixture
    : requested === "ambiguous"
      ? ambiguousFixture
      : verifiedFixture;
mountHucCrosswalkExplorer(root, fixture);
