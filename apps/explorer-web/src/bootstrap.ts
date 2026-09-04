import "./main";

import { isMapLibre3DFixtureLabEnabled } from "./site/maplibre-3d-fixture-lab/activation";
import type { MountedMapLibre3DFixtureLab } from "./site/maplibre-3d-fixture-lab/mount";

let fixtureLab: MountedMapLibre3DFixtureLab | null = null;
let fixtureLabDisposed = false;

function renderFixtureLoadFailure(host: HTMLElement): void {
  const status = host.ownerDocument.createElement("p");
  status.className = "maplibre-3d-fixture__status";
  status.dataset.state = "ERROR";
  status.setAttribute("role", "alert");
  status.textContent =
    "ERROR / MODULE_LOAD_FAILED — the opt-in synthetic MapLibre 3D fixture lab failed closed.";
  host.replaceChildren(status);
}

if (isMapLibre3DFixtureLabEnabled(window.location.href)) {
  const mapSection = document.querySelector<HTMLElement>("#map");
  if (mapSection !== null) {
    const host = document.createElement("div");
    host.dataset.component = "maplibre-3d-fixture-lab-loading";
    host.setAttribute("aria-label", "Synthetic MapLibre 3D fixture lab");
    const loading = document.createElement("p");
    loading.setAttribute("role", "status");
    loading.setAttribute("aria-live", "polite");
    loading.textContent =
      "Loading the disabled-by-default synthetic MapLibre 3D fixture lab.";
    host.append(loading);
    mapSection.append(host);

    void import("./site/maplibre-3d-fixture-lab/mount")
      .then(({ mountMapLibre3DFixtureLab }) =>
        mountMapLibre3DFixtureLab(host),
      )
      .then((mounted) => {
        if (fixtureLabDisposed) {
          mounted.destroy();
          return;
        }
        fixtureLab = mounted;
      })
      .catch(() => {
        if (!fixtureLabDisposed) renderFixtureLoadFailure(host);
      });
  }
}

window.addEventListener(
  "pagehide",
  () => {
    fixtureLabDisposed = true;
    fixtureLab?.destroy();
    fixtureLab = null;
  },
  { once: true },
);
