import abstainFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/abstain-stale.json";
import answerFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json";
import denyFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/deny-sensitive.json";
import errorFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/error-upstream.json";
import { mountEvidenceTooltip } from "../../src/features/evidence_tooltip";

const fixtures: Readonly<Record<string, unknown>> = Object.freeze({
  abstain: abstainFixture,
  answer: answerFixture,
  deny: denyFixture,
  error: errorFixture,
});

const root = document.querySelector<HTMLElement>("#fixture-root");
const drawerStatus = document.querySelector<HTMLElement>("#drawer-status");
if (root === null || drawerStatus === null) {
  throw new Error("Evidence Tooltip fixture surface is missing.");
}

const requestedFixture = new URL(window.location.href).searchParams.get("fixture");
const fixture =
  requestedFixture !== null &&
  Object.prototype.hasOwnProperty.call(fixtures, requestedFixture)
    ? fixtures[requestedFixture]
    : undefined;

mountEvidenceTooltip(root, fixture, {
  onOpenDrawer: (payload) => {
    drawerStatus.textContent = `drawer:open:${payload.outcome}`;
  },
});
