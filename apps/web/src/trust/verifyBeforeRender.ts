import type { VerifyResult } from "./sigstoreVerify.worker";

export async function verifyBeforeRender(manifest: any, expectedArtifactDigest: string): Promise<VerifyResult> {
  const worker = new Worker(new URL("./sigstoreVerify.worker.ts", import.meta.url), { type: "module" });
  return await new Promise((resolve) => {
    worker.onmessage = (event: MessageEvent<VerifyResult>) => { resolve(event.data); worker.terminate(); };
    worker.postMessage({ manifest, expectedArtifactDigest, policyProfile: "public-safe" });
  });
}

export async function guardedRegisterLayer(args: { manifest: any; expectedArtifactDigest: string; register: () => Promise<void> | void; setStatus: (s: string) => void; setEvidenceReceiptRef: (s?: string) => void; }) {
  const result = await verifyBeforeRender(args.manifest, args.expectedArtifactDigest);
  args.setEvidenceReceiptRef(result.receipt_ref);
  if (result.decision !== "ALLOW_RENDER") {
    args.setStatus("Map layer blocked by trust policy.");
    return result;
  }
  await args.register();
  args.setStatus("Map layer verified and loaded.");
  return result;
}
