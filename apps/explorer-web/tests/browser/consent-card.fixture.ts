import abstainFixture from "../../../../fixtures/ui/consent_card_projection/valid/abstain-unresolved.json";
import answerFixture from "../../../../fixtures/ui/consent_card_projection/valid/answer-viewer-choice.json";
import denyFixture from "../../../../fixtures/ui/consent_card_projection/valid/deny-policy.json";
import errorFixture from "../../../../fixtures/ui/consent_card_projection/valid/error-upstream.json";
import { mountConsentCard } from "../../src/features/consent_card";

const fixtures: Readonly<Record<string, unknown>> = Object.freeze({
  abstain: abstainFixture,
  answer: answerFixture,
  deny: denyFixture,
  error: errorFixture,
});

const root = document.querySelector<HTMLElement>("#fixture-root");
const visibility = document.querySelector<HTMLElement>("[data-layer-visible]");
const eventLog = document.querySelector<HTMLElement>("[data-event-log]");
if (root === null || visibility === null || eventLog === null) {
  throw new Error("Consent Card fixture surface is incomplete.");
}

const url = new URL(window.location.href);
if (url.searchParams.get("reset") === "1") {
  window.sessionStorage.clear();
}
const requested = url.searchParams.get("fixture");
const fixture =
  requested !== null && Object.prototype.hasOwnProperty.call(fixtures, requested)
    ? fixtures[requested]
    : undefined;

mountConsentCard(root, fixture, {
  now: "2026-08-08T00:00:00Z",
  onLayerVisibilityChange(visible) {
    visibility.textContent = `Layer visible: ${String(visible)}`;
  },
  onViewerDecision(event) {
    eventLog.textContent = JSON.stringify(event);
  },
  onViewObligations(event) {
    eventLog.textContent = JSON.stringify({
      kind: "VIEW_OBLIGATIONS",
      ...event,
    });
  },
});
