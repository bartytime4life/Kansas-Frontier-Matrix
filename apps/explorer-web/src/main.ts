import { resolveBaselineShell } from "./features/shell";
import { mountEvidenceDrawer } from "./features/evidence_drawer";

const root = document.querySelector<HTMLElement>("#root");

if (root === null) {
  throw new Error("Explorer Web root element is missing.");
}

const state = resolveBaselineShell();
const main = document.createElement("main");
const heading = document.createElement("h1");
const outcome = document.createElement("p");
const message = document.createElement("p");
const evidence = document.createElement("p");
const drawerHost = document.createElement("div");

heading.id = "explorer-title";
heading.textContent = "Kansas Frontier Matrix Explorer";
main.setAttribute("aria-labelledby", heading.id);

outcome.textContent = `${state.outcome} / ${state.code}`;
message.textContent = state.message;
evidence.textContent = `Evidence references: ${state.evidenceRefs.length}`;

main.replaceChildren(heading, outcome, message, evidence, drawerHost);
root.replaceChildren(main);
mountEvidenceDrawer(drawerHost);
