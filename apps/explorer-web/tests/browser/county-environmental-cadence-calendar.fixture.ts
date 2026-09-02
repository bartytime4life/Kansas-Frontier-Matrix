import invalidFixture from "../../../../fixtures/ui/county_environmental_cadence_projection/invalid/extra-field.json";
import holdFixture from "../../../../fixtures/ui/county_environmental_cadence_projection/valid/hold.json";
import { mountCountyEnvironmentalCadenceCalendar } from "../../src/features/county_environmental_cadence_calendar";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("County cadence fixture root is missing.");

const requested = new URL(window.location.href).searchParams.get("fixture");
mountCountyEnvironmentalCadenceCalendar(
  root,
  requested === "invalid" ? invalidFixture : holdFixture,
);
