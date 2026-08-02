import { resolveBaselineShell } from "./features/shell";
import { resolveEvidenceDrawer } from "./features/evidence_drawer";

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
const drawer = document.createElement("aside");
const drawerHeading = document.createElement("h2");
const drawerMessage = document.createElement("p");
const drawerTrust = document.createElement("ul");

heading.id = "explorer-title";
heading.textContent = "Kansas Frontier Matrix Explorer";
main.setAttribute("aria-labelledby", heading.id);

outcome.textContent = `${state.outcome} / ${state.code}`;
message.textContent = state.message;
evidence.textContent = `Evidence references: ${state.evidenceRefs.length}`;

const drawerState = resolveEvidenceDrawer();
drawerHeading.id = "evidence-drawer-title";
drawerHeading.textContent = drawerState.title;
drawer.setAttribute("role", drawerState.landmarkRole);
drawer.setAttribute("aria-labelledby", drawerHeading.id);
drawer.setAttribute("aria-label", drawerState.accessibilityLabel);
drawer.setAttribute("aria-live", drawerState.ariaLive);
drawer.dataset.outcome = drawerState.outcome;
drawerMessage.textContent = drawerState.message;

for (const label of drawerState.trustLabels) {
  const item = document.createElement("li");
  item.textContent = label;
  drawerTrust.append(item);
}

drawer.replaceChildren(drawerHeading, drawerMessage, drawerTrust);

main.replaceChildren(heading, outcome, message, evidence, drawer);
root.replaceChildren(main);
