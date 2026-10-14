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

export function TopicGuide({ value, onTool }: {
  value: LayerWorkspace; onTool?: (view: MapUtilityView, element: HTMLButtonElement) => void;
}) {
  const topic = topicDefinition(value);
  if (!topic) return null;
  return <section className="topic-guide" aria-label={`${topic.title} guide`}>
    <h3 className="sr-only">{topic.title}</h3><p>{topic.description}</p>
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
