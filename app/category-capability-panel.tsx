"use client";

import Link from "next/link";
import { categoryCapabilityGroups, CATEGORY_TOOL_DETAILS } from "./category-capabilities";
import type { CategoryTool } from "./category-maps";
import type { LayerWorkspace, TopicId } from "./layer-workspaces";

export function CategoryCapabilityPanel({ topic, query, onTool }: Readonly<{
  topic: LayerWorkspace; query: string; onTool: (topic: TopicId, tool: CategoryTool) => void;
}>) {
  const groups = categoryCapabilityGroups(topic, query);
  if (!groups.length) return null;
  const count = groups.reduce((sum, group) => sum + group.tools.length + group.workbenches.length, 0);
  return <details key={`${topic}:${Boolean(query.trim())}`} className="category-capabilities" open={topic !== "all" || Boolean(query.trim())}>
    <summary>Tools &amp; workbenches <span>{count}</span></summary>
    <p>Choose a tool to open its controls on your current map. Turn layers on when you need them.</p>
    {groups.map(group => <section key={group.topic} aria-label={`${group.title} capabilities`}>
      {topic === "all" && <h3>{group.title}</h3>}
      <ul>{group.tools.map(id => <li key={id}><button type="button" onClick={() => onTool(group.topic, id)}>
        <strong>{CATEGORY_TOOL_DETAILS[id][0]}</strong><small>{CATEGORY_TOOL_DETAILS[id][1]}</small><span>Map controls →</span>
      </button></li>)}
      {group.workbenches.map(link => <li key={link.href}><Link href={link.href} target="_blank" rel="noreferrer" prefetch={false}>
        <strong>{link.title}</strong><small>{link.detail}</small><span>Open workbench ↗</span>
      </Link></li>)}</ul>
    </section>)}
  </details>;
}
