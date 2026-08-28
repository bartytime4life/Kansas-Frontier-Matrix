import invalidFixture from "../../../../fixtures/ui/soil_yearly_change_projection/invalid/extra-field.json";
import availableFixture from "../../../../fixtures/ui/soil_yearly_change_projection/valid/available.json";
import { mountSoilYearlyChangeViewer } from "../../src/features/soil_yearly_change_viewer";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("Soil yearly change fixture root is missing.");

const requested = new URL(window.location.href).searchParams.get("fixture");
mountSoilYearlyChangeViewer(
  root,
  requested === "invalid" ? invalidFixture : availableFixture,
);
