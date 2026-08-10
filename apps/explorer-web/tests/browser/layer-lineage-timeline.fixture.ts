import invalidFixture from "../../../../fixtures/ui/layer_lineage_projection/invalid/extra-field.json";
import availableFixture from "../../../../fixtures/ui/layer_lineage_projection/valid/available.json";
import { mountLayerLineageTimeline } from "../../src/features/layer_lineage_timeline";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("Layer lineage fixture root is missing.");

const requested = new URL(window.location.href).searchParams.get("fixture");
mountLayerLineageTimeline(
  root,
  requested === "invalid" ? invalidFixture : availableFixture,
);
