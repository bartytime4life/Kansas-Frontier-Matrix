import invalidFixture from "../../../../fixtures/ui/county_ndvi_change_projection/invalid/extra-field.json";
import candidateFixture from "../../../../fixtures/ui/county_ndvi_change_projection/valid/candidate.json";
import deniedFixture from "../../../../fixtures/ui/county_ndvi_change_projection/valid/denied.json";
import { mountCountyNdviChangePanel } from "../../src/features/county_ndvi_change_panel";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("County NDVI fixture root is missing.");

const requested = new URL(window.location.href).searchParams.get("fixture");
mountCountyNdviChangePanel(
  root,
  requested === "invalid"
    ? invalidFixture
    : requested === "denied"
      ? deniedFixture
      : candidateFixture,
);
