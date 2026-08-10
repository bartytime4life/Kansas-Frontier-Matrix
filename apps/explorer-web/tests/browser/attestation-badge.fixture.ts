import invalidFixture from "../../../../fixtures/ui/attestation_badge_projection/invalid/extra-field.json";
import verifiedFixture from "../../../../fixtures/ui/attestation_badge_projection/valid/verified.json";
import { mountAttestationBadge } from "../../src/features/attestation_badge";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("Attestation badge fixture root is missing.");

const requested = new URL(window.location.href).searchParams.get("fixture");
root.dataset.inspectCalls = "0";
mountAttestationBadge(
  root,
  requested === "invalid" ? invalidFixture : verifiedFixture,
  {
    onInspect: () => {
      const count = Number(root.dataset.inspectCalls ?? "0") + 1;
      root.dataset.inspectCalls = String(count);
      root.dataset.inspectionRequested = "true";
    },
  },
);
