import Link from "next/link";

const ROUTES = [
  ["/", "Explorer map", "Layers, time, Underground and the Evidence Drawer."],
  ["/observatory", "Event Observatory", "Dated radar, smoke, streamflow and weather archives."],
  ["/knowledge", "Kansas knowledge", "Released places, people, events and stories."],
  ["/about", "About the Explorer", "How evidence states, sources and limits work."],
] as const;

/** Shared recovery page for unknown or retired destinations. */
export default function NotFound() {
  return (
    <main className="kfm-not-found">
      <div className="kfm-not-found-card">
        <p className="kfm-not-found-kicker"><span aria-hidden="true">KFM</span> 404 · No record at this address</p>
        <h1>This place isn&apos;t on the map</h1>
        <p>The address may be mistyped, moved, or no longer available. Pick a starting point below.</p>
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
