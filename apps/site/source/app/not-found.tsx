import Link from "next/link";

const ROUTES = [
  ["/", "Explorer map", "Layers, time, Underground and the Evidence Drawer."],
  ["/observatory", "Event Observatory", "Dated radar, smoke, streamflow and weather archives."],
  ["/knowledge", "Kansas knowledge", "Released places, people, events and stories."],
  ["/data", "Data commons", "Propose a source or follow a submission."],
  ["/about", "About the Explorer", "How evidence states, sources and limits work."],
] as const;

/**
 * Shared 404 for unknown paths and for routes that deliberately answer
 * "not found" (for example owner-only tools when signed out). The copy does
 * not say which case applied.
 */
export default function NotFound() {
  return (
    <main className="kfm-not-found">
      <div className="kfm-not-found-card">
        <p className="kfm-not-found-kicker"><span aria-hidden="true">KFM</span> 404 · No record at this address</p>
        <h1>This place isn&apos;t on the map</h1>
        <p>The address may be mistyped, moved, or unavailable to this session. Pick a starting point below.</p>
        <nav aria-label="Where to go next">
          <ul>
            {ROUTES.map(([href, title, body]) => (
              <li key={href}>
                <Link href={href}><strong>{title}</strong><small>{body}</small><span aria-hidden="true">→</span></Link>
              </li>
            ))}
          </ul>
        </nav>
      </div>
    </main>
  );
}
