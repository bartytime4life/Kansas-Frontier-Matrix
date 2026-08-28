import invalidFixture from "../../../../fixtures/ui/redaction_preview_projection/invalid/extra-restricted-geometry.json";
import readyFixture from "../../../../fixtures/ui/redaction_preview_projection/valid/ready.json";
import { mountRedactionPreview } from "../../src/features/redaction_preview";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("Redaction preview fixture root is missing.");

const requested = new URL(window.location.href).searchParams.get("fixture");
root.dataset.inspectCalls = "0";
mountRedactionPreview(
  root,
  requested === "invalid" ? invalidFixture : readyFixture,
  {
    onInspectReceipt: () => {
      const count = Number(root.dataset.inspectCalls ?? "0") + 1;
      root.dataset.inspectCalls = String(count);
      root.dataset.receiptInspectionRequested = "true";
    },
  },
);
