import invalidFixture from "../../../../fixtures/ui/evidence_drawer_payload/invalid/extra-field.json";
import abstainFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/abstain-stale.json";
import answerFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json";
import denyFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/deny-sensitive.json";
import errorFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/error-upstream.json";
import { mountTrustHeader } from "../../src/features/trust_header";

const fixtures: Readonly<Record<string, unknown>> = Object.freeze({
  abstain: abstainFixture,
  answer: answerFixture,
  deny: denyFixture,
  error: errorFixture,
  invalid: invalidFixture,
});

const root = document.querySelector<HTMLElement>("#fixture-root");
const drawerStatus = document.querySelector<HTMLElement>("#drawer-status");
if (root === null || drawerStatus === null) {
  throw new Error("Trust Header fixture surface is missing.");
}

const parameters = new URL(window.location.href).searchParams;
const requestedFixture = parameters.get("fixture");
const fixture =
  requestedFixture !== null &&
  Object.prototype.hasOwnProperty.call(fixtures, requestedFixture)
    ? fixtures[requestedFixture]
    : undefined;

mountTrustHeader(root, fixture, {
  compact: parameters.get("compact") === "true",
  onOpenDrawer: (payload) => {
    drawerStatus.textContent = `drawer:open:${payload.outcome}`;
  },
});
