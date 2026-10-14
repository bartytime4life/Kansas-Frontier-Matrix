import Link from "next/link";
import { requireChatGPTUser } from "../../chatgpt-auth";
import { ReleaseConsole } from "../../water-release-console";
export const dynamic = "force-dynamic";
export const metadata = { title: "Release a soil package" };

export default async function Page() {
  await requireChatGPTUser("/governed/soil-release");
  return <main style={{ maxWidth: 780, margin: "40px auto", padding: 24, lineHeight: 1.6, display: "grid", gap: 16 }}>
    <Link href="/">← Explorer</Link>
    <h1 style={{ margin: 0 }}>Release a soil package</h1>
    <p style={{ margin: 0 }}>Owner-only (ADR-0046). Stage a prepared NOAA USCRN daily soil package from your computer, then activate it here with its release decision. The reviewed-soil layer serves only the active package, and only while its decision is valid. Soil, weather and water packages, decisions and routes are separate.</p>
    <ol style={{ margin: 0 }}>
      <li>On your computer: <code>tools/release/soil_release.py cycle --site-url</code> (captures, packages, decides and stages here).</li>
      <li>Paste the decision file below and press <strong>Activate package</strong>.</li>
      <li>If something is wrong, press <strong>Withdraw active package</strong>; the layer stops serving at once.</li>
    </ol>
    <ReleaseConsole kind="soil" />
  </main>;
}
