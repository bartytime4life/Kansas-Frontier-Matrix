import invalidExtraFieldFixture from "../../../../fixtures/ui/time_scrubber_projection/invalid/extra-field.json";
import answerConflictFixture from "../../../../fixtures/ui/time_scrubber_projection/valid/answer-conflict.json";
import answerCurrentFixture from "../../../../fixtures/ui/time_scrubber_projection/valid/answer-current.json";
import answerStaleFixture from "../../../../fixtures/ui/time_scrubber_projection/valid/answer-stale.json";
import denyPolicyFixture from "../../../../fixtures/ui/time_scrubber_projection/valid/deny-policy.json";
import { mountTimeScrubber } from "../../src/features/time_banner";

const fixtures: Readonly<Record<string, unknown>> = Object.freeze({
  answer: answerCurrentFixture,
  conflict: answerConflictFixture,
  deny: denyPolicyFixture,
  invalid: invalidExtraFieldFixture,
  stale: answerStaleFixture,
});

const root = document.querySelector<HTMLElement>("#fixture-root");
const eventStatus = document.querySelector<HTMLElement>("#event-status");
const copiedStatus = document.querySelector<HTMLElement>("#copied-status");
if (root === null || eventStatus === null || copiedStatus === null) {
  throw new Error("Time Scrubber fixture surface is missing.");
}

const requestedFixture = new URL(window.location.href).searchParams.get("fixture");
const fixture =
  requestedFixture !== null &&
  Object.prototype.hasOwnProperty.call(fixtures, requestedFixture)
    ? fixtures[requestedFixture]
    : undefined;

mountTimeScrubber(root, fixture, {
  longPressMs: 300,
  onScrub: (event) => {
    eventStatus.textContent = `scrub:${event.source}:${event.t}`;
  },
  copyText: (text) => {
    copiedStatus.textContent = `copied:${text}`;
  },
});
