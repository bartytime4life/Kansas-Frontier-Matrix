import invalidFixture from "../../../../fixtures/ui/planning_scenario_projection/invalid/extra-field.json";
import availableFixture from "../../../../fixtures/ui/planning_scenario_projection/valid/available.json";
import deniedFixture from "../../../../fixtures/ui/planning_scenario_projection/valid/denied.json";
import { mountPlanningScenarioReview } from "../../src/features/planning_scenario_review";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("Planning scenario fixture root is missing.");

const requested = new URL(window.location.href).searchParams.get("fixture");
mountPlanningScenarioReview(
  root,
  requested === "invalid"
    ? invalidFixture
    : requested === "denied"
      ? deniedFixture
      : availableFixture,
);
