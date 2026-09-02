import invalidFixture from "../../../../fixtures/ui/environmental_anomaly_scorecard_projection/invalid/extra-field.json";
import holdFixture from "../../../../fixtures/ui/environmental_anomaly_scorecard_projection/valid/hold.json";
import { mountEnvironmentalAnomalyScorecard } from "../../src/features/environmental_anomaly_scorecard";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("Environmental scorecard fixture root is missing.");

const requested = new URL(window.location.href).searchParams.get("fixture");
mountEnvironmentalAnomalyScorecard(
  root,
  requested === "invalid" ? invalidFixture : holdFixture,
);
