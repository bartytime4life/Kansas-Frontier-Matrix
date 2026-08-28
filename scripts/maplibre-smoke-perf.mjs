#!/usr/bin/env node

const HOLD_EXIT_CODE = 3;

const reasons = [
  "the former harness acquired MapLibre GL JS 5.5.0 and glyphs from public CDNs",
  "its referenced slim and heavy style fixtures do not exist",
  "its browser, performance, screenshot, receipt, and trust-artifact stages are not governed for execution",
];

console.error("WORKFLOW_HOLD: the legacy MapLibre performance harness is retired.");
for (const reason of reasons) {
  console.error(`- ${reason}`);
}
console.error(
  "Use the package-owned MapLibre 6.x Vite browser fixture for bounded runtime smoke evidence; " +
    "performance execution remains NOT_RUN until deterministic fixtures, thresholds, artifact homes, and CI authority close.",
);

process.exitCode = HOLD_EXIT_CODE;
