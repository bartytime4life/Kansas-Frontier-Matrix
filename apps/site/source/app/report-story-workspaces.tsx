"use client";

import { useEffect, useMemo, useRef, useState } from "react";
import {
  createReportDraft,
  createTrustStory,
  type EvidenceRecord,
  type MapSnapshot,
  type ReportDraft,
  type StoryDraft,
  type StoryScene,
} from "./workspace-model";

import SnapshotMap from "./snapshot-map";
import { readDraft, REPORT_STORAGE_KEY, STORY_STORAGE_KEY } from "./workspace-storage";

type WorkspaceMode = "reports" | "stories";

type ReportStoryWorkspacesProps = Readonly<{
  mode: WorkspaceMode;
  snapshot: MapSnapshot;
  evidenceRecords: readonly EvidenceRecord[];
  onModeChange: (mode: WorkspaceMode) => void;
  onReturnToMap: () => void;
  onInspectEvidence: (record: EvidenceRecord) => void;
  onApplyScene: (scene: StoryScene) => void;
  getCurrentSnapshot: () => MapSnapshot;
}>;

const readStored = <T,>(key: string, snapshotId: string): T | null => {
  const draft = readDraft(key);
  if (!draft) return null;
  const id = "snapshot" in draft ? draft.snapshot.id : draft.baseSnapshot?.id ?? draft.scenes[0]?.snapshot.id.replace(/-(?:supported|corrected|historical|denied)$/, "");
  return id === snapshotId ? draft as T : null;
};

const safeFileName = (value: string, fallback: string) =>
  value.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 72) || fallback;

const downloadText = (fileName: string, text: string, type: string) => {
  const url = URL.createObjectURL(new Blob([text], { type }));
  const anchor = document.createElement("a");
  anchor.href = url;
  anchor.download = fileName;
  document.body.append(anchor);
  anchor.click();
  anchor.remove();
  window.setTimeout(() => URL.revokeObjectURL(url), 0);
};

const replaceReport = (draft: ReportDraft, patch: Partial<ReportDraft>): ReportDraft => ({
  ...draft,
  ...patch,
  status: "DRAFT",
  updatedAt: new Date().toISOString(),
});

const trustTone = (state: string) => state.toLowerCase().replaceAll(" ", "-");

const reportMarkdown = (draft: ReportDraft, evidence: readonly EvidenceRecord[]) => {
  const selectedEvidence = evidence.filter((record) => draft.includedEvidenceIds.includes(record.id));
  const layerLines = draft.snapshot.visibleLayers.map((layer) =>
    `- ${layer.order + 1}. ${layer.title} (${layer.domain}; ${Math.round(layer.opacity * 100)}%; ${layer.trustState})`,
  );
  const evidenceLines = selectedEvidence.length
    ? selectedEvidence.map((record) => `- [${record.id}] ${record.title} — ${record.citation} (${record.trustState})`)
    : ["- No evidence records included."];
  return [
    `# ${draft.title}`,
    "",
    "> DRAFT · NOT PUBLISHED · Generated starter language remains editable.",
    "",
    `**Research question:** ${draft.researchQuestion || "Not set"}`,
    `**Area:** ${draft.snapshot.area.label}`,
    `**Time:** ${draft.snapshot.committedTime.label}`,
    `**Representation:** ${draft.snapshot.representation}`,
    `**Basemap:** ${draft.snapshot.basemap} (display context)` ,
    "**Map attribution:** " + (draft.snapshot.basemap === "standard" ? "OpenFreeMap · OpenMapTiles · © OpenStreetMap contributors" : draft.snapshot.basemap === "imagery" ? "Tiles © Esri" : draft.snapshot.basemap === "streets" ? "© OpenStreetMap contributors" : "KFM local background style"),
    ...(draft.snapshot.representation === "Terrain 3D" ? ["**Display terrain:** AWS Terrain Tiles · Mapzen; not an admitted evidence source."] : []),
    "",
    "## Visible layer stack",
    "",
    ...layerLines,
    "",
    "## Summary",
    "",
    draft.sections.summary,
    "",
    "## Observations",
    "",
    draft.sections.observations,
    "",
    "## Findings",
    "",
    draft.sections.findings,
    "",
    "## Limitations",
    "",
    draft.sections.limitations,
    "",
    "## Open questions",
    "",
    draft.sections.openQuestions,
    "",
    "## Evidence and sources",
    "",
    ...evidenceLines,
    "",
    draft.sections.sources,
    "",
    `Policy outcome: ${draft.snapshot.policy.outcome} — ${draft.snapshot.policy.reason}`,
  ].join("\n");
};

const evidenceForSnapshot = (snapshot: MapSnapshot, evidence: readonly EvidenceRecord[]) => {
  const matching = evidence.filter((record) => snapshot.evidenceRefs.includes(record.citation)
    && (snapshot.inspectableFeatureIds ? snapshot.inspectableFeatureIds.includes(record.featureId) || snapshot.selection?.featureId === record.featureId : snapshot.visibleLayers.some((layer) => layer.id === record.layerId)));
  if (matching.length > 0) return matching;
  return snapshot.selection
    ? evidence.filter((record) => record.featureId === snapshot.selection?.featureId)
    : [];
};

export default function ReportStoryWorkspaces({
  mode,
  snapshot,
  evidenceRecords,
  onModeChange,
  onReturnToMap,
  onInspectEvidence,
  onApplyScene,
  getCurrentSnapshot,
}: ReportStoryWorkspacesProps) {
  const headingRef = useRef<HTMLHeadingElement>(null);
  const [storageState, setStorageState] = useState<"saved" | "saving" | "unavailable">("saving");
  const [report, setReport] = useState<ReportDraft>(() =>
    readStored<ReportDraft>(REPORT_STORAGE_KEY, snapshot.id) ?? createReportDraft(snapshot, evidenceRecords),
  );
  const [story, setStory] = useState<StoryDraft>(() =>
    readStored<StoryDraft>(STORY_STORAGE_KEY, snapshot.id) ?? createTrustStory(snapshot, evidenceRecords),
  );
  const [storyPlaying, setStoryPlaying] = useState(false);
  const [storyPlayIndex, setStoryPlayIndex] = useState(0);
  const [reducedMotion, setReducedMotion] = useState(false);

  useEffect(() => {
    headingRef.current?.focus();
    const handleEscape = (event: KeyboardEvent) => {
      if (event.key === "Escape") onReturnToMap();
    };
    document.addEventListener("keydown", handleEscape);
    return () => document.removeEventListener("keydown", handleEscape);
  }, [mode, onReturnToMap]);

  useEffect(() => {
    const preference = window.matchMedia("(prefers-reduced-motion: reduce)");
    const sync = () => setReducedMotion(preference.matches);
    sync();
    preference.addEventListener("change", sync);
    return () => preference.removeEventListener("change", sync);
  }, []);

  useEffect(() => {
    let active = true;
    try {
      if (mode === "reports") window.localStorage.setItem(REPORT_STORAGE_KEY, JSON.stringify(report));
      else window.localStorage.setItem(STORY_STORAGE_KEY, JSON.stringify(story));
      window.setTimeout(() => { if (active) setStorageState("saved"); }, 0);
    } catch {
      window.setTimeout(() => { if (active) setStorageState("unavailable"); }, 0);
    }
    return () => { active = false; };
  }, [mode, report, story]);

  useEffect(() => {
    if (!storyPlaying || story.scenes.length < 2) return;
    const timer = window.setTimeout(() => {
      setStoryPlayIndex((index) => {
        if (index >= story.scenes.length - 1) {
          setStoryPlaying(false);
          return index;
        }
        return index + 1;
      });
    }, reducedMotion ? 6500 : 4800);
    return () => window.clearTimeout(timer);
  }, [reducedMotion, story.scenes.length, storyPlayIndex, storyPlaying]);

  const snapshotEvidence = useMemo(
    () => evidenceForSnapshot(report.snapshot, evidenceRecords),
    [evidenceRecords, report.snapshot],
  );
  const includedEvidence = useMemo(
    () => snapshotEvidence.filter((record) => report.includedEvidenceIds.includes(record.id)),
    [report.includedEvidenceIds, snapshotEvidence],
  );
  const readinessItems = [
    Boolean(report.title.trim()),
    Boolean(report.researchQuestion.trim()),
    Boolean(report.sections.summary.trim()),
    Boolean(report.sections.limitations.trim()),
    includedEvidence.length > 0,
    report.snapshot.policy.outcome !== "ERROR",
  ];
  const readiness = Math.round(readinessItems.filter(Boolean).length / readinessItems.length * 100);
  const playbackScene = story.scenes[storyPlayIndex] ?? story.scenes[0];
  const activeScene = playbackScene;

  const updateReport = (recipe: (current: ReportDraft) => ReportDraft) => {
    setStorageState("saving");
    setReport(recipe);
  };

  const updateReportSection = (section: keyof ReportDraft["sections"], value: string) => {
    value = value.slice(0, 24000);
    updateReport((current) => replaceReport(current, { sections: { ...current.sections, [section]: value } }));
  };

  const toggleEvidence = (recordId: string) => {
    updateReport((current) => replaceReport(current, {
      includedEvidenceIds: current.includedEvidenceIds.includes(recordId)
        ? current.includedEvidenceIds.filter((id) => id !== recordId)
        : [...current.includedEvidenceIds, recordId],
    }));
  };

  const updateStory = (patch: Partial<StoryDraft>) => {
    setStorageState("saving");
    setStory((current) => ({ ...current, ...patch, status: "DRAFT", updatedAt: new Date().toISOString() }));
  };

  const updateScene = (sceneId: string, patch: Partial<StoryScene>) => {
    updateStory({ scenes: story.scenes.map((scene) => scene.id === sceneId ? { ...scene, ...patch } : scene) });
  };

  const moveScene = (index: number, direction: -1 | 1) => {
    const target = index + direction;
    if (target < 0 || target >= story.scenes.length) return;
    const scenes = [...story.scenes];
    [scenes[index], scenes[target]] = [scenes[target], scenes[index]];
    updateStory({ scenes });
    if (index === storyPlayIndex) setStoryPlayIndex(target);
    else if (target === storyPlayIndex) setStoryPlayIndex(index);
  };

  const duplicateScene = (scene: StoryScene) => {
    if (story.scenes.length >= 64) return;
    const copy: StoryScene = { ...scene, id: `scene-${Date.now()}`, title: `${scene.title} copy` };
    const index = story.scenes.findIndex((candidate) => candidate.id === scene.id);
    const scenes = [...story.scenes];
    scenes.splice(index + 1, 0, copy);
    updateStory({ scenes });
    setStoryPlayIndex(index + 1);
  };

  const addCurrentScene = () => {
    if (story.scenes.length >= 64) return;
    const snapshot = getCurrentSnapshot();
    const scene: StoryScene = {
      id: `scene-current-${Date.now()}`,
      title: snapshot.selection?.title ?? "Current Kansas investigation",
      narrative: "This scene preserves the current map camera, representation, committed time, layer stack, selection, and evidence references.",
      snapshot,
      evidenceRefs: snapshot.evidenceRefs,
      caveats: ["Map appearance and spatial overlap are context, not independent evidence."],
      motion: reducedMotion ? "none" : "ease",
    };
    updateStory({ scenes: [...story.scenes, scene] });
    setStoryPlayIndex(story.scenes.length);
  };

  const deleteScene = (sceneId: string) => {
    if (story.scenes.length <= 1) return;
    const scenes = story.scenes.filter((scene) => scene.id !== sceneId);
    updateStory({ scenes });
    setStoryPlayIndex((index) => Math.min(index, scenes.length - 1));
  };

  const exportReport = (format: "markdown" | "json") => {
    const stem = safeFileName(report.title, "kansas-map-investigation");
    if (format === "json") {
      downloadText(`${stem}.json`, JSON.stringify({ ...report, authority: "DRAFT_NOT_PUBLISHED" }, null, 2), "application/json");
      return;
    }
    downloadText(`${stem}.md`, reportMarkdown(report, snapshotEvidence), "text/markdown");
  };

  const exportStory = () => {
    const stem = safeFileName(story.title, "kansas-guided-story");
    downloadText(`${stem}.json`, JSON.stringify({ ...story, authority: "DRAFT_NOT_PUBLISHED" }, null, 2), "application/json");
  };

  return (
    <section className="primary-workspace-surface" data-workspace={mode} aria-labelledby="primary-workspace-title">
      <header className="primary-workspace-header">
        <div>
          <span>KANSAS FRONTIER MATRIX · DEVICE-LOCAL WORKSPACE</span>
          <h1 id="primary-workspace-title" ref={headingRef} tabIndex={-1}>{mode === "reports" ? "Evidence report builder" : "Guided story builder"}</h1>
          <p>{mode === "reports" ? "Write from the exact inherited map state and keep evidence limits beside every claim." : "Compose ordered map scenes without turning camera motion into evidence."}</p>
        </div>
        <nav aria-label="Report and story workspaces">
          <button type="button" aria-current={mode === "reports" ? "page" : undefined} onClick={() => onModeChange("reports")}>Reports</button>
          <button type="button" aria-current={mode === "stories" ? "page" : undefined} onClick={() => onModeChange("stories")}>Stories</button>
          <button className="return-map" type="button" onClick={onReturnToMap}>Return to map</button>
        </nav>
        <div className="draft-state" role="status"><strong>DRAFT · NOT PUBLISHED</strong><small>{storageState === "saved" ? "Saved on this device" : storageState === "saving" ? "Saving locally…" : "Browser storage unavailable"}</small></div>
      </header>

      {mode === "reports" ? <div className="report-workspace-grid">
        <aside className="snapshot-context" aria-label="Inherited map snapshot">
          <span className="workspace-eyebrow">MAP SNAPSHOT</span>
          <h2>{report.snapshot.area.label}</h2>
          <SnapshotMap snapshot={report.snapshot} label="Inherited report map" />
          <dl>
            <div><dt>Committed time</dt><dd>{report.snapshot.committedTime.label}</dd></div>
            <div><dt>Layer stack</dt><dd>{report.snapshot.visibleLayers.length} visible</dd></div>
            <div><dt>Inspectable</dt><dd>{report.snapshot.inspectableRecordCount} records</dd></div>
            <div><dt>Evidence posture</dt><dd>{report.snapshot.sourceBackedCount} source-backed · {report.snapshot.boundedCount} bounded</dd></div>
            <div><dt>Selection</dt><dd>{report.snapshot.selection?.title ?? "None · viewport scope"}</dd></div>
            <div><dt>Policy</dt><dd>{report.snapshot.policy.outcome}</dd></div>
          </dl>
          <section className="snapshot-layer-stack" aria-labelledby="snapshot-layer-title">
            <h3 id="snapshot-layer-title">Visible layers · draw order</h3>
            <ol>{report.snapshot.visibleLayers.map((layer) => <li key={layer.id}><i style={{ opacity: Math.max(.25, layer.opacity) }} aria-hidden="true" /><span><strong>{layer.title}</strong><small>{layer.domain} · {Math.round(layer.opacity * 100)}%</small></span><b data-trust={trustTone(layer.trustState)}>{layer.trustState}</b></li>)}</ol>
          </section>
        </aside>

        <main className="report-paper" aria-label="Editable report draft">
          <div className="paper-rule"><span>KFM FIELD NOTE</span><strong>DRAFT</strong></div>
          <label className="report-title-field"><span>Report title</span><input value={report.title} maxLength={120} onChange={(event) => updateReport((current) => replaceReport(current, { title: event.target.value }))} /></label>
          <label className="report-question-field"><span>Research question</span><textarea rows={2} value={report.researchQuestion} maxLength={400} onChange={(event) => updateReport((current) => replaceReport(current, { researchQuestion: event.target.value }))} /></label>
          {(Object.keys(report.sections) as Array<keyof ReportDraft["sections"]>).map((section) => <label className="report-section-field" key={section}>
            <span>{section.replace(/([A-Z])/g, " $1")} <small>{report.generatedFields.includes(section) ? "Generated starter · editable" : "Editable"}</small></span>
            <textarea rows={section === "summary" || section === "findings" ? 5 : 4} value={report.sections[section]} onChange={(event) => updateReportSection(section, event.target.value)} />
          </label>)}
          <aside className="report-boundary"><strong>Map pixels do not become findings.</strong><p>Generated starter language records scope and posture only. It does not invent conclusions, admit a source, or clear policy and review gates.</p></aside>
        </main>

        <aside className="report-evidence-column" aria-label="Evidence inclusion and report readiness">
          <section className="readiness-card">
            <div><span>Draft completeness</span><strong>{readiness}%</strong></div>
            <progress max="100" value={readiness}>{readiness}%</progress>
            <p>Completeness measures fields and citations, not factual approval.</p>
          </section>
          <section className="evidence-inclusion" aria-labelledby="evidence-inclusion-title">
            <header><div><span className="workspace-eyebrow">EVIDENCE</span><h2 id="evidence-inclusion-title">Include with the draft</h2></div><small>{includedEvidence.length}/{snapshotEvidence.length}</small></header>
            <div>{snapshotEvidence.map((record) => <article key={record.id} data-trust={trustTone(record.trustState)}>
              <label><input type="checkbox" checked={report.includedEvidenceIds.includes(record.id)} onChange={() => toggleEvidence(record.id)} /><span><strong>{record.title}</strong><small>{record.domain} · {record.trustState}</small></span></label>
              <p>{record.supports}</p>
              <footer><code>{record.citation}</code><button type="button" onClick={() => onInspectEvidence(record)}>Inspect</button></footer>
            </article>)}{snapshotEvidence.length === 0 && <p className="empty-workspace-state">No claim-bearing evidence reference matches this map snapshot. The draft may record the gap, but it cannot publish a fallback claim.</p>}</div>
          </section>
          <div className="workspace-export-actions">
            <button type="button" onClick={() => exportReport("markdown")}>Export Markdown</button>
            <button type="button" onClick={() => exportReport("json")}>Export JSON</button>
            <button type="button" onClick={() => window.print()}>Print clean view</button>
            <button type="button" disabled title="Publication requires evidence, policy, review, and release gates">Publish unavailable</button>
          </div>
        </aside>
      </div> : <div className="story-workspace-grid">
        <aside className="story-scene-list" aria-label="Ordered story scenes">
          <div className="story-draft-fields">
            <label><span>Story title</span><input value={story.title} maxLength={120} onChange={(event) => updateStory({ title: event.target.value })} /></label>
            <label><span>Guiding question</span><textarea rows={3} value={story.researchQuestion} onChange={(event) => updateStory({ researchQuestion: event.target.value })} /></label>
          </div>
          <div className="story-scene-heading"><div><span className="workspace-eyebrow">ORDERED SCENES</span><h2>{story.scenes.length} chapters</h2></div><button type="button" onClick={addCurrentScene} disabled={story.scenes.length >= 64}>Add current map scene</button></div>
          <ol>{story.scenes.map((scene, index) => <li key={scene.id} data-active={scene.id === activeScene?.id}>
            <button className="scene-select" type="button" onClick={() => { setStoryPlayIndex(index); setStoryPlaying(false); }}><span>{String(index + 1).padStart(2, "0")}</span><strong>{scene.title}</strong><small>{scene.snapshot.committedTime.label} · {scene.snapshot.representation}</small></button>
            <div><button type="button" disabled={index === 0} onClick={() => moveScene(index, -1)} aria-label={`Move ${scene.title} earlier`}>Up</button><button type="button" disabled={index === story.scenes.length - 1} onClick={() => moveScene(index, 1)} aria-label={`Move ${scene.title} later`}>Down</button></div>
          </li>)}</ol>
        </aside>

        <main className="story-preview-stage" aria-label="Story preview and player">
          {playbackScene && <>
            <SnapshotMap key={playbackScene.id} snapshot={playbackScene.snapshot} label={`Story scene: ${playbackScene.title}`} />
            <article className="story-transcript" aria-live="polite">
              <span>SCENE {storyPlayIndex + 1} OF {story.scenes.length}</span>
              <h2>{playbackScene.title}</h2>
              <p>{playbackScene.narrative}</p>
              <div>{playbackScene.caveats.map((caveat) => <small key={caveat}>{caveat}</small>)}</div>
            </article>
            <nav className="story-player-controls" aria-label="Story playback">
              <button type="button" disabled={storyPlayIndex === 0} onClick={() => setStoryPlayIndex((index) => Math.max(0, index - 1))}>Previous</button>
              <button type="button" aria-pressed={storyPlaying} onClick={() => {
                if (!storyPlaying && storyPlayIndex === story.scenes.length - 1) setStoryPlayIndex(0);
                setStoryPlaying((current) => !current);
              }}>{storyPlaying ? "Pause" : "Preview full story"}</button>
              <button type="button" disabled={storyPlayIndex === story.scenes.length - 1} onClick={() => setStoryPlayIndex((index) => Math.min(story.scenes.length - 1, index + 1))}>Next</button>
              <button type="button" onClick={() => { setStoryPlaying(false); onApplyScene(playbackScene); }}>Open scene on map</button>
              <button type="button" onClick={() => { setStoryPlaying(false); onReturnToMap(); }}>Exit preview</button>
            </nav>
            <div className="story-text-alternative"><strong>Text alternative</strong><p>{playbackScene.snapshot.representation}; {playbackScene.snapshot.area.label}; {playbackScene.snapshot.committedTime.label}; visible layers: {playbackScene.snapshot.visibleLayers.map((layer) => layer.title).join(", ") || "none"}. Evidence references: {playbackScene.evidenceRefs.join(", ") || "none"}.</p></div>
          </>}
        </main>

        <aside className="scene-editor" aria-label="Selected scene editor">
          {activeScene ? <>
            <div><span className="workspace-eyebrow">SCENE EDITOR</span><h2>{activeScene.title}</h2></div>
            <label><span>Scene title</span><input value={activeScene.title} maxLength={120} onChange={(event) => updateScene(activeScene.id, { title: event.target.value })} /></label>
            <label><span>Narrative</span><textarea rows={8} value={activeScene.narrative} maxLength={1200} onChange={(event) => updateScene(activeScene.id, { narrative: event.target.value })} /></label>
            <label><span>Motion</span><select value={reducedMotion ? "none" : activeScene.motion} disabled={reducedMotion} onChange={(event) => updateScene(activeScene.id, { motion: event.target.value as StoryScene["motion"] })}><option value="none">None</option><option value="ease">Gentle camera ease</option></select><small>{reducedMotion ? "Reduced-motion preference forces no motion." : "Motion guides attention only; it never represents change."}</small></label>
            <section><span>Evidence references</span>{activeScene.evidenceRefs.map((reference) => {
              const record = evidenceRecords.find((candidate) => candidate.citation === reference);
              return <article key={reference}><code>{reference}</code>{record && <button type="button" onClick={() => onInspectEvidence(record)}>Inspect</button>}</article>;
            })}</section>
            <section><span>Caveats</span><ul>{activeScene.caveats.map((caveat) => <li key={caveat}>{caveat}</li>)}</ul></section>
            <div className="scene-editor-actions"><button type="button" onClick={() => duplicateScene(activeScene)} disabled={story.scenes.length >= 64}>Duplicate</button><button type="button" onClick={() => deleteScene(activeScene.id)} disabled={story.scenes.length <= 1}>Delete</button></div>
          </> : <p className="empty-workspace-state">Add a map scene to begin.</p>}
          <div className="workspace-export-actions"><button type="button" onClick={exportStory}>Export story JSON</button><button type="button" disabled title="Publication requires evidence, policy, review, and release gates">Publish unavailable</button></div>
        </aside>
      </div>}
      {mode === "reports" && <article className="report-print-document" aria-label="Print report">
        <h1>{report.title}</h1><strong>DRAFT · NOT PUBLISHED</strong>
        <pre>{reportMarkdown(report, snapshotEvidence)}</pre>
      </article>}
    </section>
  );
}
