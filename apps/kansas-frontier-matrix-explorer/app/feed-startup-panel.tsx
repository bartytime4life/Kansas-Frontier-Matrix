"use client";

import { useEffect } from "react";
import fixtureText from "../fixtures/feed-startup.synthetic.json?raw";
import { mountFeedStartupSurface } from "./feed-startup-surface.mjs";
import "./feed-startup-panel.css";

/** The existing ribbon owns layout. This isolated child neither recreates the
 * map nor patches history, layer selection, evidence or source permissions. */
export default function FeedStartupPanel() {
  useEffect(() => {
    const actions = document.querySelector<HTMLElement>(".kfm-report-ribbon__actions");
    if (!actions) return;
    const host = document.createElement("span");
    host.dataset.kfmFeedStartup = "repository-preview";
    actions.append(host);
    const surface = mountFeedStartupSurface(host, { fixtureText });
    return () => { surface.dispose(); host.remove(); };
  }, []);
  return null;
}
