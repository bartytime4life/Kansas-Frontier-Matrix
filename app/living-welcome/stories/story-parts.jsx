'use client';
import { Component, useEffect, useRef, useState } from 'react';
import { drawWaitingSketch, hashSeed, useStoryCanvas } from './story-kit.mjs';

// A module once loaded stays here, so that the next render has it at once, without a flash.
const modules = new Map();
export function useStoryModule(story, enabled) {
  const [, loaded] = useState(0);
  useEffect(() => {
    if (!enabled || !story?.load || modules.has(story.id)) return undefined;
    let live = true;
    story.load().then(storyModule => { modules.set(story.id, storyModule); if (live) loaded(count => count + 1); }).catch(() => {});
    return () => { live = false; };
  }, [story, enabled]);
  return (enabled && story && modules.get(story.id)) || null;
}

export function WaitingSketch({ story, held }) {
  const seed = hashSeed(story.id), cache = useRef({});
  const ref = useStoryCanvas({
    animate: true, held, fps: 15, deps: [story.id],
    draw: (ctx, frame) => drawWaitingSketch(ctx, { ...frame, palette: story.palette, seed, cache: cache.current }),
  });
  return <canvas ref={ref} className="story-canvas" aria-hidden="true"/>;
}

/** A story that throws shows its waiting state; the welcome and the other cards are unaffected. */
export class StoryBoundary extends Component {
  state = { failed: false };
  static getDerivedStateFromError() { return { failed: true }; }
  render() { return this.state.failed ? this.props.fallback : this.props.children; }
}
