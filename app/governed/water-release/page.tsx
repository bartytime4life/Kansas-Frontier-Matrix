import Link from "next/link";
import { requireChatGPTUser } from "../../chatgpt-auth";
import WaterReleaseConsole from "../../water-release-console";
export const dynamic = "force-dynamic";
export const metadata = { title: "Release a water package" };

export default async function Page() {
  await requireChatGPTUser("/governed/water-release");
  return <main style={{ maxWidth: 780, margin: "40px auto", padding: 24, lineHeight: 1.6, display: "grid", gap: 16 }}>
    <Link href="/">← Explorer</Link>
    <h1 style={{ margin: 0 }}>Release a water package</h1>
    <p style={{ margin: 0 }}>Owner-only. Stage a prepared USGS discharge package from your computer, then activate it here with its release decision. The reviewed-water layer serves only the active package, and only while its decision is valid.</p>
    <ol style={{ margin: 0 }}>
      <li>On your computer: <code>tools/release/water_release.py decide</code>, then <code>stage-hosted</code>.</li>
      <li>Paste the decision file below and press <strong>Activate package</strong>.</li>
      <li>If something is wrong, press <strong>Withdraw active package</strong>; the layer stops serving at once.</li>
    </ol>
    <WaterReleaseConsole />
  </main>;
}
