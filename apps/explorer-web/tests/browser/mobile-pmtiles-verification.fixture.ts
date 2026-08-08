import fixtureSuite from "../../../../fixtures/pmtiles/mobile_verification/cases.json";
import {
  decodeMobilePmtilesArchive,
  verifyMobilePmtilesFixture,
  type MobilePmtilesRenderAdapter,
  type MobilePmtilesVerificationResult,
} from "../../src/features/map_runtime/mobile_pmtiles_verification";

type FixtureBundle = typeof fixtureSuite.base;

declare global {
  interface Window {
    __kfmMobilePmtilesVerification?: Readonly<{
      runValid: () => Promise<MobilePmtilesVerificationResult>;
      runTampered: () => Promise<MobilePmtilesVerificationResult>;
      getLastResult: () => MobilePmtilesVerificationResult | null;
    }>;
  }
}

function requireElement<T extends Element>(selector: string): T {
  const value = document.querySelector<T>(selector);
  if (value === null) {
    throw new Error(`Mobile PMTiles fixture element is missing: ${selector}`);
  }
  return value;
}

const verifyButton = requireElement<HTMLButtonElement>(
  "#verify-mobile-pmtiles",
);
const tamperedButton = requireElement<HTMLButtonElement>(
  "#verify-tampered-pmtiles",
);
const status = requireElement<HTMLElement>("#mobile-pmtiles-status");
const canvas = requireElement<HTMLCanvasElement>("#mobile-pmtiles-canvas");
const holds = requireElement<HTMLUListElement>("#mobile-pmtiles-holds");

function clone<T>(value: T): T {
  return JSON.parse(JSON.stringify(value)) as T;
}

function encodeBase64(bytes: Uint8Array): string {
  let binary = "";
  for (const value of bytes) binary += String.fromCharCode(value);
  return btoa(binary);
}

const renderTile: MobilePmtilesRenderAdapter = async (tileBytes, mediaType) => {
  const bitmap = await createImageBitmap(
    new Blob([tileBytes], { type: mediaType }),
  );
  canvas.width = bitmap.width;
  canvas.height = bitmap.height;
  const context = canvas.getContext("2d", {
    alpha: true,
    willReadFrequently: true,
  });
  if (context === null) {
    bitmap.close();
    throw new Error("Canvas 2D context is unavailable.");
  }
  context.clearRect(0, 0, canvas.width, canvas.height);
  context.drawImage(bitmap, 0, 0);
  const pixel = Array.from(context.getImageData(0, 0, 1, 1).data);
  const result = {
    decoded: true,
    rendered: true,
    width: bitmap.width,
    height: bitmap.height,
    pixelRgba: pixel,
  };
  bitmap.close();
  return result;
};

let lastResult: MobilePmtilesVerificationResult | null = null;

function renderResult(result: MobilePmtilesVerificationResult): void {
  lastResult = result;
  status.textContent = `${result.outcome} / ${result.code}`;
  status.dataset.outcome = result.outcome;
  status.dataset.code = result.code;
  status.dataset.maplibreBootState = result.maplibreBootState;
  status.dataset.authority = result.authority;
  holds.replaceChildren(
    ...result.holds.map((hold) => {
      const item = document.createElement("li");
      item.textContent = hold;
      return item;
    }),
  );
}

async function run(bundle: FixtureBundle): Promise<MobilePmtilesVerificationResult> {
  verifyButton.disabled = true;
  tamperedButton.disabled = true;
  status.textContent = "Verifying synthetic PMTiles fixture...";
  try {
    const result = await verifyMobilePmtilesFixture(bundle, renderTile);
    if (result.outcome !== "PASS") {
      const context = canvas.getContext("2d");
      context?.clearRect(0, 0, canvas.width, canvas.height);
    }
    renderResult(result);
    return result;
  } finally {
    verifyButton.disabled = false;
    tamperedButton.disabled = false;
  }
}

async function runValid(): Promise<MobilePmtilesVerificationResult> {
  return run(clone(fixtureSuite.base));
}

async function runTampered(): Promise<MobilePmtilesVerificationResult> {
  const bundle = clone(fixtureSuite.base);
  const archive = decodeMobilePmtilesArchive(bundle.archive_base64);
  if (archive === null) throw new Error("Fixture archive cannot be decoded.");
  archive[archive.length - 1] ^= 0x01;
  bundle.archive_base64 = encodeBase64(archive);
  return run(bundle);
}

verifyButton.addEventListener("click", () => {
  void runValid();
});
tamperedButton.addEventListener("click", () => {
  void runTampered();
});

window.__kfmMobilePmtilesVerification = Object.freeze({
  runValid,
  runTampered,
  getLastResult: () => lastResult,
});
