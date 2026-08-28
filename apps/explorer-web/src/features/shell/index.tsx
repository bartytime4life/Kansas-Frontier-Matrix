export type BaselineShellState =
  | Readonly<{
      outcome: "ABSTAIN";
      code: "NO_GOVERNED_RESPONSE";
      message: "No governed response is available.";
      evidenceRefs: readonly [];
    }>
  | Readonly<{
      outcome: "ERROR";
      code: "UNSUPPORTED_BASELINE_INPUT";
      message: "This baseline does not accept input.";
      evidenceRefs: readonly [];
    }>;

const EMPTY_EVIDENCE_REFS = Object.freeze([]) as readonly [];

const NO_GOVERNED_RESPONSE: BaselineShellState = Object.freeze({
  outcome: "ABSTAIN",
  code: "NO_GOVERNED_RESPONSE",
  message: "No governed response is available.",
  evidenceRefs: EMPTY_EVIDENCE_REFS,
});

const UNSUPPORTED_BASELINE_INPUT: BaselineShellState = Object.freeze({
  outcome: "ERROR",
  code: "UNSUPPORTED_BASELINE_INPUT",
  message: "This baseline does not accept input.",
  evidenceRefs: EMPTY_EVIDENCE_REFS,
});

export function resolveBaselineShell(
  ...input: readonly [] | readonly [unknown]
): BaselineShellState {
  return input.length === 0
    ? NO_GOVERNED_RESPONSE
    : UNSUPPORTED_BASELINE_INPUT;
}
