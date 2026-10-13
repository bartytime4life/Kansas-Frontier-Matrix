"use client";
import { useEffect, useRef, useState, type ReactNode } from "react";
import inventory from "./local-map-archive-inventory.json";
import { ARCHIVE_PAGE_SIZE, LocalPdfSession, archiveWarning, editionBasisLabel, filterLocalMaps, type LocalMapSheet } from "./local-map-archive";

const records: readonly LocalMapSheet[] = inventory.records;
const years = [...new Set(records.flatMap(row => row.startYear !== null && row.endYear !== null ? Array.from({ length: row.endYear - row.startYear + 1 }, (_, i) => row.startYear! + i) : []))].sort((a, b) => a - b);
const collections: Record<string, string> = {
  "Kansas bridges": "Bridge sheets", "Kansas Road Maps": "State road maps", "KFM County Roadways": "County roadway plans",
  "KFM Historic County Township Maps": "Historic county & township", "KFM Past Published County Maps": "Past county maps", "KFM Urban Roadways": "Urban roadway plans",
};
export type LocalArchiveBrowserProps = { renderPreparedReview?: (sheet: LocalMapSheet) => ReactNode };
export default function LocalMapArchiveBrowser({ renderPreparedReview }: LocalArchiveBrowserProps = {}) {
  const [collection, setCollection] = useState("all"), [text, setText] = useState(""), [year, setYear] = useState("all"), [issuesOnly, setIssuesOnly] = useState(false), [page, setPage] = useState(0);
  const [selected, setSelected] = useState<LocalMapSheet | null>(null), [preview, setPreview] = useState<string | null>(null), [busy, setBusy] = useState(false);
  const [status, setStatus] = useState("Select a sheet to inspect its source notes and check your local PDF.");
  const [session] = useState(() => new LocalPdfSession());
  const version = useRef(0), mounted = useRef(true), input = useRef<HTMLInputElement | null>(null);
  useEffect(() => {
    const life = mounted, epoch = version; life.current = true;
    return () => { life.current = false; epoch.current++; session.clear(); };
  }, [session]);
  const matching = filterLocalMaps(records, { collection, text, year, issuesOnly });
  const maxPage = Math.max(0, Math.ceil(matching.length / ARCHIVE_PAGE_SIZE) - 1), currentPage = Math.min(page, maxPage);
  const visible = matching.slice(currentPage * ARCHIVE_PAGE_SIZE, (currentPage + 1) * ARCHIVE_PAGE_SIZE);
  const choose = (row: LocalMapSheet | null) => {
    version.current++; session.clear(); setSelected(row); setPreview(null);
    if (input.current) input.current.value = "";
    setStatus(row ? "Choose the matching PDF from your computer. Only its bytes are checked; nothing is uploaded." : "Selection cleared. Any pending file check is cancelled.");
  };
  const inspect = async (file?: File) => {
    if (!file || !selected) return;
    const token = ++version.current; setPreview(null); setBusy(true);
    setStatus(`Checking ${selected.fileName} on this device${file.size > 32 * 1024 * 1024 ? " · large scan" : ""}…`);
    const result = await session.check(file, selected);
    if (mounted.current) {
      setBusy(false);
      if (token === version.current) {
        setPreview(result.state === "matched" ? result.url : null);
        setStatus(result.state === "matched" ? "Filename, size and SHA-256 match this inventory. Source identity, dates, rights and map alignment still require review." : result.message);
      }
    }
  };
  return <section className="local-map-archive" aria-labelledby="local-map-archive-title">
    <header><h4 id="local-map-archive-title">Local road &amp; bridge map archive</h4><span>{records.length} PDF records · 6 collections</span></header>
    <p>Find a source sheet, then check and open the original on your device. These reference PDFs are separate from the map timeline and georeferenced overlays.</p>
    <p><a href="/downloads#public-maps">Browse Kansas mine maps &amp; geologic maps →</a></p>
    <div className="local-archive-filters">
      <label>Collection<select value={collection} onChange={e => { setCollection(e.target.value); setPage(0); }}><option value="all">All collections</option>{inventory.collections.map(name => <option key={name} value={name}>{collections[name]} · {records.filter(row => row.collection === name).length}</option>)}</select></label>
      <label>Find a sheet<input type="search" value={text} onChange={e => { setText(e.target.value); setPage(0); }} placeholder="County, city or filename" /></label>
      <label>Edition-year clue<select value={year} onChange={e => { setYear(e.target.value); setPage(0); }}><option value="all">All years</option><option value="unknown">Unknown or withheld</option>{years.map(value => <option key={value}>{value}</option>)}</select></label>
      <label className="local-archive-issues"><input type="checkbox" checked={issuesOnly} onChange={e => { setIssuesOnly(e.target.checked); setPage(0); }} />Flagged sources only</label>
    </div>
    <p className="local-archive-coverage" role="status">{matching.length} matching sheets. Edition clues are not opening, closure or road-validity dates. A two-year edition can appear under either year.</p>
    <ul className="local-archive-results">{visible.map(row => <li key={row.id}><button type="button" aria-pressed={selected?.id === row.id} onClick={() => choose(row)}><strong>{row.fileName}</strong><span>{collections[row.collection]} · {row.editionLabel ?? "Date unknown / withheld"}</span><small>{editionBasisLabel(row.editionBasis)}{row.flags.length ? " · review flag" : ""}</small></button></li>)}</ul>
    {visible.length === 0 && <p>No sheet matches these filters. Unknown dates remain searchable by filename.</p>}
    <nav className="local-archive-pages" aria-label="Local archive pages"><button type="button" disabled={currentPage === 0} onClick={() => setPage(currentPage - 1)}>Previous</button><span>Page {currentPage + 1} of {maxPage + 1}</span><button type="button" disabled={currentPage === maxPage} onClick={() => setPage(currentPage + 1)}>Next</button></nav>
    {selected && <section className="local-archive-selection" aria-label="Selected local map sheet">
      <h5>{selected.fileName}</h5><p>{selected.collection}</p>
      {selected.flags.map(flag => <p className="local-archive-warning" key={flag}>{archiveWarning(flag)}</p>)}
      {selected.sameBytesAs.length > 0 && <p>Same bytes also recorded as: {selected.sameBytesAs.join("; ")}. A matching hash does not resolve those names.</p>}
      <dl>
        <div><dt>Edition clue</dt><dd>{selected.editionLabel ?? "Unknown / withheld"} · {editionBasisLabel(selected.editionBasis)}</dd></div>
        <div><dt>Georeferencing</dt><dd>{selected.alignment === "embedded-control-unreviewed" ? "Embedded controls found; independent alignment review pending" : "No embedded controls recorded; independent georeferencing needed"}</dd></div>
        <div><dt>Size</dt><dd>{(selected.sizeBytes / 1024 / 1024).toFixed(2)} MiB</dd></div>
        <div><dt>SHA-256</dt><dd><code>{selected.sha256}</code></dd></div>
      </dl>
      {["KFM County Roadways", "KFM Urban Roadways"].includes(selected.collection) && <p className="local-archive-warning">Functional-classification planning maps may include proposed roadways. They do not establish present road conditions.</p>}
      <label>Check selected original<input ref={input} type="file" accept=".pdf,application/pdf" disabled={busy} onChange={e => void inspect(e.target.files?.[0])} /></label>
      {preview && <a className="local-archive-open" href={preview} target="_blank" rel="noreferrer">Open matched original PDF</a>}
      <button type="button" onClick={() => choose(null)}>Clear selected sheet</button>
      {renderPreparedReview?.(selected)}
    </section>}
    <p className="local-archive-status" role="status">{status}</p>
    <small>One file check at a time, up to 100 MiB. Nothing enters uploads, saved workspaces, reports, the evidence catalog or releases. PDFs are not stretched to a county outline.</small>
  </section>;
}
