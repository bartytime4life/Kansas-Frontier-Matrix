import * as THREE from "three";
import type { CustomLayerInterface, CustomRenderMethodInput, GeoJSONSource, Map as MapLibreMap } from "./maplibre-seam";
import { createTransportCrew } from "./transport-crew-models";
import { routeLengthM, routePose, routeSlice, transportDetail, transportFrame, transportWorkSectionFits, type TransportWork } from "./transport-history";
import type { FeatureCollection, LineString } from "geojson";
export const TRANSPORT_WORK_LAYER = "kfm-local-transport-work-crew";
const SOURCE = "kfm-local-transport-work";
const LINE = "kfm-local-transport-work-line";
const RAD = Math.PI / 180;
const worldPosition = (lng: number, lat: number, zoom: number) => ({
  x: (lng + 180) / 360 * 512 * 2 ** zoom,
  y: (180 - 180 / Math.PI * Math.log(Math.tan(Math.PI / 4 + lat * RAD / 2))) / 360 * 512 * 2 ** zoom,
  scale: 512 * 2 ** zoom / (40_075_016.686 * Math.cos(lat * RAD)),
});
export function transportLineData(works: readonly TransportWork[], date: string): FeatureCollection<LineString> {
  return { type: "FeatureCollection", features: works.flatMap(work => {
    const frame = transportFrame(work, date), length = routeLengthM(work.coordinates);
    const pieces: [number, number, string][] = work.progressMode === "milestones"
      ? [[0, length, "context"]]
      : work.action === "remove"
      ? [[frame.chainageM, length, frame.closed ? "closed" : "existing"], [0, frame.chainageM, "removed"]]
      : [[0, frame.chainageM, frame.closed ? "closed" : "built"], [frame.chainageM, length, frame.closed ? "closed" : "pending"]];
    return pieces.filter(([a, b]) => b - a > .1).map(([a, b, state]) => ({ type: "Feature" as const,
      properties: { id: work.id, title: work.title, state, basis: frame.basis, mode: work.mode, widthM: work.widthM, latitude: work.coordinates[0][1] },
      geometry: { type: "LineString" as const, coordinates: routeSlice(work.coordinates, a, b).map(p => [...p]) } }));
  }) };
}
/** Public custom-layer API, shared WebGL context, no second canvas or hit target. */
export function attachTransportConstruction(map: MapLibreMap, initial: readonly TransportWork[], initialDate: string, animate: boolean) {
  let works = initial, date = initialDate, active = true;
  const crews = new Map<string, ReturnType<typeof createTransportCrew>>();
  let renderer: THREE.WebGLRenderer | null = null;
  const scene = new THREE.Scene(), camera = new THREE.Camera();
  const ambient = new THREE.HemisphereLight(0xf7f4e9, 0x606757, 2.2); ambient.position.set(0, 0, 100); scene.add(ambient);
  const sun = new THREE.DirectionalLight(0xffedcc, 2.7); sun.position.set(-40, -70, 100); scene.add(sun);
  const updateLines = () => {
    if (!active || !map.isStyleLoaded()) return;
    const data = transportLineData(works, date);
    const source = map.getSource(SOURCE) as GeoJSONSource | undefined;
    if (source) source.setData(data); else map.addSource(SOURCE, { type: "geojson", data });
    if (!map.getLayer(LINE)) map.addLayer({ id: LINE, type: "line", source: SOURCE,
      layout: { "line-cap": "butt", "line-join": "round" }, paint: {
        "line-color": ["case", ["all", ["==", ["get", "basis"], "interpolated"], ["!=", ["get", "state"], "closed"]], "#b890cf", ["match", ["get", "state"], "built", "#47555b", "existing", "#87918d", "closed", "#ce6553", "removed", "#866b55", "context", "#9aa7c4", "#d6ad61"]],
        "line-opacity": ["match", ["get", "state"], "pending", .35, "removed", .25, "context", .55, ["case", ["==", ["get", "basis"], "interpolated"], .6, .9]],
        // Physical width when resolvable; a labelled thin overview line below it.
        "line-width": ["interpolate", ["exponential", 2], ["zoom"], 5, ["max", 1.5, ["*", ["get", "widthM"], ["/", 16384, ["*", 40075016.686, ["cos", ["*", ["get", "latitude"], 0.017453292519943295]]]]]], 13, ["max", 1.5, ["*", ["get", "widthM"], ["/", 4194304, ["*", 40075016.686, ["cos", ["*", ["get", "latitude"], 0.017453292519943295]]]]]], 15, ["max", 1.5, ["*", ["get", "widthM"], ["/", 16777216, ["*", 40075016.686, ["cos", ["*", ["get", "latitude"], 0.017453292519943295]]]]]], 18, ["max", 1.5, ["*", ["get", "widthM"], ["/", 134217728, ["*", 40075016.686, ["cos", ["*", ["get", "latitude"], 0.017453292519943295]]]]]], 22, ["max", 1.5, ["*", ["get", "widthM"], ["/", 2147483648, ["*", 40075016.686, ["cos", ["*", ["get", "latitude"], 0.017453292519943295]]]]]]],
      } });
  };
  const custom: CustomLayerInterface = { id: TRANSPORT_WORK_LAYER, type: "custom", renderingMode: "3d",
    onAdd(_map, gl) {
      renderer = new THREE.WebGLRenderer({ canvas: map.getCanvas(), context: gl }); renderer.autoClear = false;
      renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping;
    },
    render(_gl, input: CustomRenderMethodInput) {
      if (!active || !renderer || map.getProjection().type === "globe" || map.getTerrain()) return;
      const now = performance.now(), moving = animate && !document.hidden;
      const wanted = new Set<string>(); let workVisible = false;
      for (const work of works) {
        const frame = transportFrame(work, date);
        if (frame.state !== "working" || work.action === "remove") continue;
        const pose = routePose(work.coordinates, frame.chainageM);
        const detail = transportDetail(map.getZoom(), pose.coordinate[1], work.positionAccuracyM);
        if (detail === "overview" || work.widthM < 6 || frame.chainageM < 45) continue;
        const point = map.project(pose.coordinate as [number, number]);
        if (point.x < -150 || point.y < -150 || point.x > map.getCanvas().clientWidth + 150 || point.y > map.getCanvas().clientHeight + 150) continue;
        // Long rigid machinery cannot straddle a tight bend. Keep a line cue
        // until a locally straight work section is available.
        if (!transportWorkSectionFits(work, frame.chainageM) || wanted.size >= 4) continue;
        wanted.add(work.id); workVisible = true;
        let crew = crews.get(work.id);
        if (!crew) { crew = createTransportCrew(work.mode, Number(work.start.slice(0, 4)), detail === "crew"); crews.set(work.id, crew); }
        // Toggle worker detail on LOD changes by recreating only at that boundary.
        const expected = `${work.mode}:${detail}`;
        if (crew.group.userData.detail && crew.group.userData.detail !== expected) { crew.dispose(); crews.delete(work.id); crew = createTransportCrew(work.mode, Number(work.start.slice(0, 4)), detail === "crew"); crews.set(work.id, crew); }
        crew.group.userData.detail = expected;
        scene.add(crew.group);
        crew.group.rotation.z = Math.PI / 2 - pose.heading;
        // Equipment remains behind the work front; walls/trees are not sampled
        // into a fabricated historical elevation. Terrain is explicitly held.
        crew.group.position.set(-Math.sin(pose.heading) * 6, -Math.cos(pose.heading) * 6, .08);
        crew.update(moving ? now / 1000 : 0);
        const p = worldPosition(...pose.coordinate, map.getZoom());
        const local = new THREE.Matrix4().makeTranslation(p.x, p.y, 0).scale(new THREE.Vector3(p.scale, -p.scale, 1));
        camera.projectionMatrix.fromArray(input.modelViewProjectionMatrix).multiply(local);
        renderer.resetState(); renderer.render(scene, camera); scene.remove(crew.group);
      }
      for (const [id, crew] of crews) if (!wanted.has(id)) { crew.dispose(); crews.delete(id); }
      // Animation clock articulates tools only. Historical advancement is
      // controlled exclusively by the selected source date, never elapsed FPS.
      if (moving && workVisible) map.triggerRepaint();
      renderer.resetState();
    },
    onRemove() { for (const crew of crews.values()) crew.dispose(); crews.clear(); renderer?.dispose(); renderer = null; },
  };
  const install = () => { if (!active || !map.isStyleLoaded()) return; updateLines(); if (!map.getLayer(TRANSPORT_WORK_LAYER)) map.addLayer(custom); };
  const resume = () => { if (!document.hidden) map.triggerRepaint(); };
  try { install(); } catch (error) {
    if (map.getLayer(TRANSPORT_WORK_LAYER)) map.removeLayer(TRANSPORT_WORK_LAYER);
    if (map.getLayer(LINE)) map.removeLayer(LINE);
    if (map.getSource(SOURCE)) map.removeSource(SOURCE);
    throw error;
  }
  map.on("style.load", install); document.addEventListener("visibilitychange", resume);
  return { update(next: readonly TransportWork[], day: string) { works = next; date = day; updateLines(); map.triggerRepaint(); },
    dispose() { active = false; map.off("style.load", install); document.removeEventListener("visibilitychange", resume);
      if (map.getLayer(TRANSPORT_WORK_LAYER)) map.removeLayer(TRANSPORT_WORK_LAYER);
      if (map.getLayer(LINE)) map.removeLayer(LINE); if (map.getSource(SOURCE)) map.removeSource(SOURCE);
    } };
}
