export type CameraPose = { position: [number, number, number]; target: [number, number, number]; offset: [number, number] };

/** OrbitControls handles arrows without emitting its pointer `start` event. */
export function bindCameraKeyboardInterruption(target: EventTarget, cancel: () => void) {
  const keydown = (event: Event) => {
    if (["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown"].includes((event as KeyboardEvent).key)) cancel();
  };
  target.addEventListener("keydown", keydown);
  return () => target.removeEventListener("keydown", keydown);
}

/** Refit the rotated projection while retaining the user's zoom relative to a full fit. */
export function rotateCutawayCamera(pose: CameraPose, angle: number, fit: (direction: [number, number, number]) => {distance: number; offsetX: number; offsetY: number}): CameraPose {
  const d = pose.position.map((n, i) => n - pose.target[i]) as CameraPose["position"];
  const radius = Math.max(.000001, Math.hypot(...d)), direction = d.map(n => n / radius) as CameraPose["position"];
  const rotated: CameraPose["position"] = [direction[0] * Math.cos(angle) + direction[2] * Math.sin(angle), direction[1], direction[2] * Math.cos(angle) - direction[0] * Math.sin(angle)];
  const before = fit(direction), after = fit(rotated), distance = after.distance * radius / before.distance;
  return { target: [...pose.target], position: rotated.map((n, i) => pose.target[i] + n * distance) as CameraPose["position"], offset: [after.offsetX, after.offsetY] };
}

/** Orbit between poses without taking a straight-line shortcut through the model. */
export function betweenCameraPoses(from: CameraPose, to: CameraPose, progress: number): CameraPose {
  const t = Math.max(0, Math.min(1, progress));
  const spherical = (pose: CameraPose) => {
    const d = pose.position.map((v, i) => v - pose.target[i]);
    const radius = Math.max(.000001, Math.hypot(...d));
    return { radius, theta: Math.atan2(d[0], d[2]), phi: Math.acos(Math.max(-1, Math.min(1, d[1] / radius))) };
  };
  const a = spherical(from), b = spherical(to);
  const yaw = Math.atan2(Math.sin(b.theta - a.theta), Math.cos(b.theta - a.theta));
  const radius = a.radius + (b.radius - a.radius) * t, theta = a.theta + yaw * t, phi = a.phi + (b.phi - a.phi) * t;
  const target = from.target.map((v, i) => v + (to.target[i] - v) * t) as CameraPose["target"];
  return { target, position: [target[0] + radius * Math.sin(phi) * Math.sin(theta), target[1] + radius * Math.cos(phi), target[2] + radius * Math.sin(phi) * Math.cos(theta)],
    offset: from.offset.map((v, i) => v + (to.offset[i] - v) * t) as CameraPose["offset"] };
}

/** One short, interruptible transition. No idle animation loop or accumulated queue. */
export function createCutawayCameraMotion(options: {
  read: () => CameraPose; apply: (pose: CameraPose) => void; reducedMotion: () => boolean;
  request: (callback: (time: number) => void) => number; cancel: (id: number) => void; now: () => number;
}) {
  let frame: number | null = null, generation = 0, disposed = false;
  const cancel = () => { generation++; if (frame !== null) options.cancel(frame); frame = null; };
  const move = (to: CameraPose, duration = 300) => {
    if (disposed) return;
    cancel();
    if (options.reducedMotion() || duration <= 0) { options.apply(to); return; }
    const from = options.read(), started = options.now(), token = generation;
    const tick = (time: number) => {
      if (disposed || token !== generation) return;
      frame = null;
      const t = Math.max(0, Math.min(1, (time - started) / duration));
      options.apply(t === 1 ? to : betweenCameraPoses(from, to, 1 - Math.pow(1 - t, 3)));
      if (t < 1) frame = options.request(tick);
    };
    frame = options.request(tick);
  };
  return { move, cancel, dispose: () => { cancel(); disposed = true; } };
}
