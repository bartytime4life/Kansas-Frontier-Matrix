import Link from "next/link";
export const metadata = { title: "About the public KFM preview" };
export default function Page() {
 return <main style={{ maxWidth: 780, margin: "40px auto", padding: 24, lineHeight: 1.65 }}>
  <Link href="/">← Explorer</Link><h1>Kansas Frontier Matrix public preview</h1>
  <p>This separate preview preserves the private Explorer. The interactive map and 3D display are available for testing. Data-dependent tools show reviewed releases or a specific unavailable state.</p>
  <h2>Publication status</h2><p>No observational or subsurface package is approved for this preview yet. Real water, weather, and original well-log candidates are prepared privately for review. Preparation and successful tests do not grant public release permission.</p>
  <h2>Display and evidence</h2><p>OpenFreeMap, OpenMapTiles, and OpenStreetMap provide the map backdrop. Terrain is approximate display context. Provider resolution, dates, attribution, and uncertainty remain distinct from observed data and original records. A selected map date does not reconstruct past geology.</p>
  <h2>Sources and unavailable data</h2><p>Approved packages will identify their original sources, units, coverage, retrieval and release times. Missing dates and withheld measurements remain unavailable. Synthetic demonstrations and private libraries are excluded.</p>
  <p><Link href="/topics">Explore by subject</Link> · <Link href="/almanacs">Browse almanac references</Link>. Reference publications retain their source, rights and limitations; they do not authorize observational data delivery.</p>
  <h2>Access and corrections</h2><p>The development preview is restricted. The intended public edition permits exploration and approved exports, with administration limited to the owner. Expired, corrected, or withdrawn releases stop serving. Previously downloaded public copies cannot be recalled.</p>
 </main>;
}
