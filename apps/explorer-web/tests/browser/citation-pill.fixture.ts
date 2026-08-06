import abstainFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/abstain-stale.json";
import answerFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/answer-corrected.json";
import denyFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/deny-sensitive.json";
import errorFixture from "../../../../fixtures/ui/evidence_drawer_payload/valid/error-upstream.json";
import { mountCitationPill } from "../../src/features/citation_pill";

const fixtures: Readonly<Record<string, unknown>> = Object.freeze({
  abstain: abstainFixture,
  answer: answerFixture,
  deny: denyFixture,
  error: errorFixture,
});

const root = document.querySelector<HTMLElement>("#fixture-root");
const copyProbe = document.querySelector<HTMLElement>("#copy-probe");
if (root === null || copyProbe === null) {
  throw new Error("Citation Pill fixture surface is missing.");
}

const requestedFixture = new URL(window.location.href).searchParams.get("fixture");
const fixture =
  requestedFixture !== null &&
  Object.prototype.hasOwnProperty.call(fixtures, requestedFixture)
    ? fixtures[requestedFixture]
    : undefined;

mountCitationPill(root, fixture, {
  timestamp: "1850-06-01T00:00:00Z",
  view: "focus",
  copyText: (text) => {
    copyProbe.textContent = text;
  },
});
