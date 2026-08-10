import validFixture from "../../../../fixtures/ui/denial_reason_projection/valid/all-source-codes.json";
import invalidFixture from "../../../../fixtures/ui/denial_reason_projection/invalid/extra-field.json";
import { mountDenialReasonExplorer } from "../../src/features/denial_reason_explorer";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) {
  throw new Error("Denial reason explorer fixture root is missing.");
}

const requested = new URL(window.location.href).searchParams.get("fixture");
mountDenialReasonExplorer(
  root,
  requested === "invalid" ? invalidFixture : validFixture,
);
