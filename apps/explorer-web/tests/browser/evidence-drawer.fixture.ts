import abstainFixture from "../../../../tests/fixtures/ui/evidence_drawer/abstain-stale.json";
import answerFixture from "../../../../tests/fixtures/ui/evidence_drawer/answer.json";
import denyFixture from "../../../../tests/fixtures/ui/evidence_drawer/deny-sensitive.json";
import errorFixture from "../../../../tests/fixtures/ui/evidence_drawer/error-upstream.json";
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
