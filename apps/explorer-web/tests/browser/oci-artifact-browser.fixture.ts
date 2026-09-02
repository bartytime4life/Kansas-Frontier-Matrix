import invalidFixture from "../../../../fixtures/ui/oci_artifact_browser_projection/invalid/extra-field.json";
import availableFixture from "../../../../fixtures/ui/oci_artifact_browser_projection/valid/available.json";
import { mountOciArtifactBrowser } from "../../src/features/oci_artifact_browser";

const root = document.querySelector<HTMLElement>("#fixture-root");
if (root === null) throw new Error("OCI artifact browser fixture root is missing.");

const requested = new URL(window.location.href).searchParams.get("fixture");
mountOciArtifactBrowser(
  root,
  requested === "invalid" ? invalidFixture : availableFixture,
);
