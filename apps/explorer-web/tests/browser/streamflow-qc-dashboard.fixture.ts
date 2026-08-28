import invalidFixture from "../../../../fixtures/ui/streamflow_qc_dashboard_projection/invalid/extra-raw-flow-field.json";
import heldFixture from "../../../../fixtures/ui/streamflow_qc_dashboard_projection/valid/held.json";
import localReviewFixture from "../../../../fixtures/ui/streamflow_qc_dashboard_projection/valid/local-review.json";
import regionalFixture from "../../../../fixtures/ui/streamflow_qc_dashboard_projection/valid/regional-context.json";
import { mountStreamflowQcDashboard } from "../../src/features/streamflow_qc_dashboard";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) {
  throw new Error("Streamflow QC dashboard fixture root is missing.");
}

const requested = new URL(window.location.href).searchParams.get("fixture");
const fixture =
  requested === "invalid"
    ? invalidFixture
    : requested === "held"
      ? heldFixture
      : requested === "local"
        ? localReviewFixture
        : regionalFixture;

mountStreamflowQcDashboard(root, fixture);
