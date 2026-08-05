import abstainFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/abstain-stale.json";
import answerFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json";
import denyFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/deny-sensitive.json";
import errorFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/error-upstream.json";
import { mountEvidenceDrawer } from "../../src/features/evidence_drawer";

const fixtures: Readonly<Record<string, unknown>> = Object.freeze({
  abstain: abstainFixture,
  answer: answerFixture,
  deny: denyFixture,
  error: errorFixture,
});

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("Evidence Drawer fixture root is missing.");

const requestedFixture = new URL(window.location.href).searchParams.get("fixture");
const fixture =
  requestedFixture !== null &&
  Object.prototype.hasOwnProperty.call(fixtures, requestedFixture)
    ? fixtures[requestedFixture]
    : undefined;

mountEvidenceDrawer(root, fixture);
