"use client";

import Link from "next/link";
import type { MapUtilityView } from "./map-interface";
import { TOPIC_GROUPS, TOPIC_STRUCTURE, topicDefinition, restoreTopic, type LayerWorkspace } from "./layer-workspaces";

export function TopicSelect({ value, onChange, label }: {
  value: LayerWorkspace; onChange: (value: LayerWorkspace) => void; label: string;
}) {
  return <label className="topic-select"><span className="sr-only">{label}</span>
    <select aria-label={label} value={value} onChange={event => onChange(restoreTopic(event.target.value))}>
      <option value="all">All topics</option>
      {TOPIC_GROUPS.map(group => <optgroup key={group} label={group}>
        {TOPIC_STRUCTURE.filter(topic => topic.group === group).map(topic => <option key={topic.id} value={topic.id}>{topic.title}</option>)}
      </optgroup>)}
    </select>
  </label>;
}

/** The category preset; `active` means its basemap style matches, not that its source layers are selected. */
export type TopicMapLook = Readonly<{ name: string; lede: string; sceneLabel: string; swatch: readonly [string, string, string]; active: boolean }>;

export function TopicGuide({ value, onTool, mapLook, onOpenMap }: {
  value: LayerWorkspace; onTool?: (view: MapUtilityView, element: HTMLButtonElement) => void;
  mapLook?: TopicMapLook | null; onOpenMap?: () => void;
}) {
  const topic = topicDefinition(value);
  if (!topic) return null;
  return <section className="topic-guide" aria-label={`${topic.title} guide`}>
    <h3 className="sr-only">{topic.title}</h3><p>{topic.description}</p>
    {mapLook && <div className="topic-map-look" style={{ "--m0": mapLook.swatch[0], "--m1": mapLook.swatch[1], "--m2": mapLook.swatch[2] } as React.CSSProperties}>
      <span className="topic-map-look-swatch" aria-hidden="true" />
      <div><strong>{mapLook.name}</strong><small>{mapLook.sceneLabel}{mapLook.active ? " · map style in use" : ""}</small><p>Default view: {mapLook.lede}</p></div>
      {onOpenMap && <button type="button" onClick={onOpenMap}>Open this map</button>}
    </div>}
    <details key={topic.id}><summary>Subtopics &amp; coverage</summary><small>{topic.group}</small>
      <ul aria-label={`${topic.title} subtopics`}>{topic.facets.map(facet => <li key={facet}>{facet}</li>)}</ul>
      <p>{topic.limitation}</p>
    </details>
    <nav aria-label={`${topic.title} tools`}>{topic.resources.map(resource => {
      const tool = resource.href.startsWith("/?maptab=") ? new URLSearchParams(resource.href.slice(2)).get("maptab") as MapUtilityView : null;
      return tool && onTool
        ? <button key={resource.href} type="button" onClick={event => onTool(tool, event.currentTarget)}>{resource.title}</button>
        : <Link key={resource.href} href={resource.href} prefetch={false}>{resource.title} ↗</Link>;
    })}</nav>
  </section>;
}
