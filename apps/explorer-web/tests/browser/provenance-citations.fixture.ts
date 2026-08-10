import invalidFixture from "../../../../fixtures/ui/provenance_citations_projection/invalid/extra-field.json";
import availableFixture from "../../../../fixtures/ui/provenance_citations_projection/valid/available.json";
import { mountProvenanceCitations } from "../../src/features/provenance_citations";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("Provenance citations fixture root is missing.");

const requested = new URL(window.location.href).searchParams.get("fixture");
mountProvenanceCitations(
  root,
  requested === "invalid" ? invalidFixture : availableFixture,
);
