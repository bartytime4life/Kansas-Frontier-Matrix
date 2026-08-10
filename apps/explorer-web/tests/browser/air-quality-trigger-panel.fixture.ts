import invalidFixture from "../../../../fixtures/ui/air_quality_trigger_projection/invalid/extra-raw-field.json";
import deniedFixture from "../../../../fixtures/ui/air_quality_trigger_projection/valid/denied.json";
import noTriggerFixture from "../../../../fixtures/ui/air_quality_trigger_projection/valid/no-trigger.json";
import triggerFixture from "../../../../fixtures/ui/air_quality_trigger_projection/valid/proposed-trigger.json";
import { mountAirQualityTriggerPanel } from "../../src/features/air_quality_trigger_panel";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("Air-quality trigger fixture root is missing.");

const requested = new URL(window.location.href).searchParams.get("fixture");
mountAirQualityTriggerPanel(
  root,
  requested === "invalid"
    ? invalidFixture
    : requested === "denied"
      ? deniedFixture
      : requested === "no-trigger"
        ? noTriggerFixture
        : triggerFixture,
);
