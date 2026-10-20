// A small lifecycle boundary shared by map and dialog videos. Native decoding
// owns frame presentation; React never repaints or warps source frames.
export function bindPlayback(video, { src, paused = false, onBlocked = () => {} } = {}) {
  let disposed = false, held = paused, ticket = 0;
  // React Strict Mode reuses the element after cleanup. Restore its source
  // before rebinding; otherwise the second mount has no media to decode.
  if(src)video.src=src;
  video.muted = true;
  video.playsInline = true;
  const sync = () => {
    const current = ++ticket;
    if (disposed || held) { video.pause(); return; }
    const result = video.play();
    result?.then?.(() => { if (disposed || held) video.pause(); })?.catch?.(error => {
      if (!disposed && !held && current === ticket && error?.name !== 'AbortError') onBlocked(error);
    });
  };
  video.addEventListener('loadeddata', sync);
  sync();
  return {
    setPaused(value) { if (held === value) return; held = value; sync(); },
    dispose() { disposed = true; ticket++; video.removeEventListener('loadeddata', sync); video.pause(); video.removeAttribute('src'); video.load(); },
  };
}

export function fitScene(box, aspect = 16 / 9) {
  const width = Math.min(box.w, box.h * aspect), height = width / aspect;
  return { x: box.x + (box.w - width) / 2, y: box.y + (box.h - height) / 2, w: width, h: height };
}
