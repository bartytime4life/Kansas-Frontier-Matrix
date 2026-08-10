import invalidFixture from "../../../../fixtures/ui/pmtiles_range_diagnostics_projection/invalid/extra-field.json";
import availableFixture from "../../../../fixtures/ui/pmtiles_range_diagnostics_projection/valid/available.json";
import { mountPmtilesRangeDiagnostics } from "../../src/features/pmtiles_range_diagnostics";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("PMTiles range diagnostics fixture root is missing.");

const requested = new URL(window.location.href).searchParams.get("fixture");
mountPmtilesRangeDiagnostics(
  root,
  requested === "invalid" ? invalidFixture : availableFixture,
);
