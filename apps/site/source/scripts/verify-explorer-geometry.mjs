import assert from "node:assert/strict";

const explorerUrl = process.env.KFM_EXPLORER_URL ?? "http://127.0.0.1:4173";
const cdpOrigin = process.env.KFM_CDP_ORIGIN ?? "http://127.0.0.1:9223";
const targets = await (await fetch(`${cdpOrigin}/json/list`)).json();
const target = targets.find((item) => item.type === "page" && item.url.startsWith(explorerUrl));
if (!target) throw new Error(`Open ${explorerUrl} in the CDP browser before running this check.`);

const socket = new WebSocket(target.webSocketDebuggerUrl);
await new Promise((resolve, reject) => {
  socket.addEventListener("open", resolve, { once: true });
  socket.addEventListener("error", reject, { once: true });
});
let sequence = 0;
const pending = new Map();
socket.addEventListener("message", (event) => {
  const message = JSON.parse(event.data);
  if (!message.id || !pending.has(message.id)) return;
  const handler = pending.get(message.id);
  pending.delete(message.id);
  if (message.error) handler.reject(new Error(message.error.message));
  else handler.resolve(message.result);
});
const call = (method, params = {}) => new Promise((resolve, reject) => {
  const id = ++sequence;
  pending.set(id, { resolve, reject });
  socket.send(JSON.stringify({ id, method, params }));
});
const evaluate = async (expression) => {
  const result = await call("Runtime.evaluate", { expression, awaitPromise: true, returnByValue: true });
  if (result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails));
  return result.result.value;
};
const pause = (milliseconds) => new Promise((resolve) => setTimeout(resolve, milliseconds));
const explorerReady = `(() => {
  const trigger = document.querySelector(".data-notices-trigger");
  return Boolean(document.body && document.readyState === "complete"
    && document.querySelector(".topbar") && document.querySelector(".map-chrome-dock")
    && trigger && Object.keys(trigger).some((key) => key.startsWith("__reactProps$")));
})()`;
const waitFor = async (expression, timeoutMs = 20_000) => {
  const deadline = Date.now() + timeoutMs;
  let lastValue;
  let lastError;
  while (Date.now() < deadline) {
    try {
      lastValue = await evaluate(expression);
      if (lastValue) return;
    } catch (error) {
      // A reload can briefly invalidate the prior execution context.
      lastError = error instanceof Error ? error.message : String(error);
    }
    await pause(100);
  }
  throw new Error(`Timed out waiting for browser state: ${expression}\nLast value: ${JSON.stringify(lastValue)}\nLast error: ${lastError ?? "none"}`);
};

const keyDetails = {
  Enter: { code: "Enter", windowsVirtualKeyCode: 13 },
  Escape: { code: "Escape", windowsVirtualKeyCode: 27 },
  Space: { code: "Space", windowsVirtualKeyCode: 32 },
  Tab: { code: "Tab", windowsVirtualKeyCode: 9 },
  ArrowDown: { code: "ArrowDown", windowsVirtualKeyCode: 40 },
  ArrowUp: { code: "ArrowUp", windowsVirtualKeyCode: 38 },
};
const pressKey = async (key) => {
  const details = keyDetails[key];
  assert.ok(details, `Unsupported test key: ${key}`);
  if (key === "Space" || key === "Enter") {
    const dispatchedKey = key === "Space" ? " " : "Enter";
    const text = key === "Space" ? " " : "\r";
    await call("Input.dispatchKeyEvent", { type: "rawKeyDown", key: dispatchedKey, ...details });
    await call("Input.dispatchKeyEvent", { type: "char", key: dispatchedKey, text, unmodifiedText: text, ...details });
    await call("Input.dispatchKeyEvent", { type: "keyUp", key: dispatchedKey, ...details });
    return;
  }
  await call("Input.dispatchKeyEvent", { type: "rawKeyDown", key, ...details });
  await call("Input.dispatchKeyEvent", { type: "keyUp", key, ...details });
};
const pressLetter = async (letter) => {
  assert.match(letter, /^[a-z]$/i);
  const upper = letter.toUpperCase();
  const details = { code: `Key${upper}`, windowsVirtualKeyCode: upper.charCodeAt(0) };
  await call("Input.dispatchKeyEvent", { type: "rawKeyDown", key: letter, ...details });
  await call("Input.dispatchKeyEvent", { type: "char", key: letter, text: letter, unmodifiedText: letter, ...details });
  await call("Input.dispatchKeyEvent", { type: "keyUp", key: letter, ...details });
};
const reloadAt = async (width, height = width === 390 ? 844 : 900) => {
  await call("Emulation.clearDeviceMetricsOverride");
  await call("Emulation.setDeviceMetricsOverride", {
    width, height, screenWidth: width, screenHeight: height,
    deviceScaleFactor: 1, mobile: width === 390,
  });
  await call("Page.navigate", { url: explorerUrl });
  await waitFor(explorerReady, 20_000);
  await pause(250);
};
const focusSelector = async (selector, label) => {
  const result = await evaluate(`(() => {
    const element = document.querySelector(${JSON.stringify(selector)});
    if (!(element instanceof HTMLElement)) return { found: false, visible: false, focused: false };
    const style = getComputedStyle(element);
    const box = element.getBoundingClientRect();
    const visible = style.display !== "none" && style.visibility !== "hidden" && box.width > 0 && box.height > 0;
    element.focus();
    return { found: true, visible, focused: document.activeElement === element };
  })()`);
  assert.deepEqual(result, { found: true, visible: true, focused: true }, `${label} is not keyboard reachable via ${selector}`);
};
const focusMatching = async (containerSelector, elementSelector, text, label) => {
  const result = await evaluate(`(() => {
    const normalize = (value) => (value || "").replace(/\\s+/g, " ").trim();
    const visible = (element) => {
      const style = getComputedStyle(element);
      const box = element.getBoundingClientRect();
      return style.display !== "none" && style.visibility !== "hidden" && box.width > 0 && box.height > 0;
    };
    const candidates = [...document.querySelectorAll(${JSON.stringify(containerSelector)} + " " + ${JSON.stringify(elementSelector)})];
    const expected = ${JSON.stringify(text)};
    const element = candidates.find((candidate) => {
      const semanticCopy = candidate.cloneNode(true);
      semanticCopy.querySelectorAll?.('[aria-hidden="true"]').forEach((decorative) => decorative.remove());
      const primary = normalize(candidate.querySelector("strong")?.textContent || semanticCopy.textContent);
      return visible(candidate) && (primary === expected || primary.startsWith(expected));
    });
    if (!(element instanceof HTMLElement)) return { found: false, visible: false, focused: false };
    element.focus();
    return { found: true, visible: visible(element), focused: document.activeElement === element };
  })()`);
  assert.deepEqual(result, { found: true, visible: true, focused: true }, `${label} is not keyboard reachable`);
};
const activateSelector = async (selector, label, key = "Enter") => {
  await focusSelector(selector, label);
  await pressKey(key);
  await pause(100);
};
const activateMatching = async (containerSelector, elementSelector, text, label, key = "Enter") => {
  await focusMatching(containerSelector, elementSelector, text, label);
  await pressKey(key);
  await pause(100);
};
const openMenu = async (selector, label) => {
  if (!await evaluate(`document.querySelector(${JSON.stringify(selector)})?.open === true`)) {
    await activateSelector(`${selector} > summary`, label, "Space");
  }
  assert.equal(await evaluate(`document.querySelector(${JSON.stringify(selector)})?.open`), true, `${label} did not open`);
};
const activateWorkspace = async (name, label = name) => {
  await openMenu(".header-overflow-menu", "More site actions");
  await activateMatching(".header-overflow-workspaces", "button", name, label);
};
const activateMode = async (width, name, label = name) => {
  const container = width >= 1200 ? ".map-dock-representations" : ".map-dock-menu-representations";
  if (width < 1200) await openMenu(".map-dock-map-menu", "Map views and controls");
  await activateMatching(container, "button", name, label);
  if (width < 1200) assert.equal(await evaluate(`document.querySelector(".map-dock-map-menu")?.open`), false, `${label} must close the Map menu`);
};
const activateStatus = async () => {
  await openMenu(".header-overflow-menu", "More site actions");
  await activateSelector(".status-header-action", "Status");
};
const assertMinimumTarget = async (selector, label) => {
  const box = await evaluate(`(() => {
    const element = document.querySelector(${JSON.stringify(selector)});
    if (!(element instanceof HTMLElement)) return null;
    const rect = element.getBoundingClientRect();
    const style = getComputedStyle(element);
    if (style.display === "none" || style.visibility === "hidden") return null;
    return { width: rect.width, height: rect.height };
  })()`);
  assert.ok(box, `${label} target is not visible`);
  assert.ok(box.width >= 43.5 && box.height >= 43.5,
    `${label} target is ${box.width}×${box.height}, below 44px`);
};
const assertInViewport = async (selector, label) => {
  const found = await evaluate(`(() => {
    const element = document.querySelector(${JSON.stringify(selector)});
    if (!(element instanceof HTMLElement)) return false;
    element.scrollIntoView({ block: "nearest", inline: "nearest" });
    return true;
  })()`);
  assert.equal(found, true, `${label} is missing`);
  await pause(100);
  const position = await evaluate(`(() => {
    const element = document.querySelector(${JSON.stringify(selector)});
    if (!(element instanceof HTMLElement)) return null;
    const rect = element.getBoundingClientRect();
    return { top: rect.top, right: rect.right, bottom: rect.bottom, left: rect.left, width: innerWidth, height: innerHeight };
  })()`);
  assert.ok(position
    && position.top >= -0.5 && position.left >= -0.5
    && position.bottom <= position.height + 0.5 && position.right <= position.width + 0.5,
  `${label} is outside the viewport after scrolling`);
};
const assertNear = (actual, expected, label, tolerance = 1) => {
  assert.ok(Number.isFinite(actual) && Number.isFinite(expected)
    && Math.abs(actual - expected) <= tolerance,
  `${label}: expected ${expected} ± ${tolerance}, received ${actual}`);
};
const interceptLinkActivation = async (selector, label) => {
  const armed = await evaluate(`(() => {
    const element = document.querySelector(${JSON.stringify(selector)});
    if (!(element instanceof HTMLAnchorElement)) return false;
    window.__kfmGeometryLinkActivation = null;
    element.addEventListener("click", (event) => {
      event.preventDefault();
      window.__kfmGeometryLinkActivation = element.getAttribute("href");
    }, { once: true, capture: true });
    element.focus();
    return document.activeElement === element;
  })()`);
  assert.equal(armed, true, `${label} link is not keyboard reachable`);
  await pressKey("Enter");
  await pause(100);
  assert.equal(await evaluate(`window.__kfmGeometryLinkActivation`), await evaluate(`document.querySelector(${JSON.stringify(selector)}).getAttribute("href")`), `${label} did not activate from Enter`);
};

await call("Page.enable");
await call("Runtime.enable");
const observations = [];
const undergroundObservations = [];
for (const width of [1920, 1800, 1799, 1440, 1200, 1199, 1024, 768, 760, 390]) {
  const height = width === 390 ? 844 : 900;
  await call("Emulation.clearDeviceMetricsOverride");
  await call("Emulation.setDeviceMetricsOverride", {
    width, height, screenWidth: width, screenHeight: height,
    deviceScaleFactor: 1, mobile: width === 390,
  });
  await call("Page.reload", { ignoreCache: true });
  await waitFor(explorerReady, 20_000);
  await pause(250);
  let geometry = null;
  const geometryDeadline = Date.now() + 20_000;
  while (!geometry && Date.now() < geometryDeadline) {
    try {
      geometry = await evaluate(`(() => {
    const body = document.body;
    const rootElement = document.documentElement;
    if (!body || !rootElement || document.readyState !== "complete"
      || !document.querySelector(".topbar") || !document.querySelector(".map-chrome-dock")) return null;
    const visible = (element) => {
      if (!element) return false;
      const style = getComputedStyle(element);
      const box = element.getBoundingClientRect();
      return style.display !== "none" && style.visibility !== "hidden" && box.width > 0 && box.height > 0;
    };
    const rect = (selector) => {
      const box = document.querySelector(selector)?.getBoundingClientRect();
      return box ? { left: box.left, top: box.top, right: box.right, bottom: box.bottom, width: box.width, height: box.height } : null;
    };
    const outside = (rootSelector) => {
      const root = document.querySelector(rootSelector)?.getBoundingClientRect();
      if (!root) return ["missing-root"];
      return [...document.querySelectorAll(rootSelector + " > *")]
        .filter(visible)
        .filter((element) => {
          const box = element.getBoundingClientRect();
          return box.top < root.top - .5 || box.bottom > root.bottom + .5;
        })
        .map((element) => element.className || element.tagName);
    };
    const targets = [...document.querySelectorAll(".topbar button, .topbar a, .topbar summary, .global-search label, .map-chrome-dock button, .map-chrome-dock summary, .map-chrome-dock select, .map-tool-rail button, .maplibregl-ctrl-group button")]
      .filter(visible).map((element) => ({
        height: element.getBoundingClientRect().height,
        label: element.getAttribute("aria-label") || element.textContent.trim().replace(/\s+/g, " ") || element.tagName,
      }));
    const headerFocusOrder = [...document.querySelectorAll(".topbar input, .topbar button, .topbar a, .topbar summary")]
      .filter(visible)
      .map((element) => element.getAttribute("aria-label") || element.getAttribute("placeholder") || element.textContent.trim().replace(/\\s+/g, " "));
    const mode = document.querySelector(".map-dock-representations");
    const launcher = rect(".qwen-map-launch");
    const mobileDock = rect(".map-mobile-actions");
    const mapMenu = document.querySelector(".map-dock-map-menu");
    if (mapMenu) mapMenu.open = true;
    return {
      width: innerWidth,
      header: rect(".topbar"),
      dock: rect(".map-chrome-dock"),
      stage: rect(".map-stage"),
      dockInHeader: Boolean(document.querySelector(".topbar > .map-chrome-dock")),
      horizontalOverflow: rootElement.scrollWidth > rootElement.clientWidth || body.scrollWidth > body.clientWidth,
      headerOverflow: outside(".topbar"),
      dockOverflow: outside(".map-chrome-dock"),
      smallestTarget: Math.min(...targets.map((target) => target.height)),
      targetsUnder44: targets.filter((target) => target.height < 43.5),
      headerFocusOrder,
      directModes: visible(mode),
      directQuickControls: visible(document.querySelector(".map-dock-actions > .map-dock-action")),
      menuModes: visible(document.querySelector(".map-dock-menu-representations")),
      menuQuickControls: visible(document.querySelector(".map-dock-menu-quick")),
      directBasemap: visible(document.querySelector(".map-dock-basemap")),
      directControls: visible(document.querySelector(".map-dock-action.map-dock-wide-only")),
      mapOverflow: visible(document.querySelector(".map-dock-map-menu > summary")),
      controlsInOverflow: [...document.querySelectorAll(".map-dock-map-menu button")].some((button) => visible(button) && button.textContent.includes("Map controls")),
      mobileBrand: visible(document.querySelector(".brand-lockup .mark")),
      qwenClearsMobileDock: !launcher || !mobileDock || launcher.bottom <= mobileDock.top - 4,
    };
  })()`);
    } catch {
      // The dev server can reload once more after ready; retry in the new context.
    }
    if (!geometry) await pause(100);
  }
  assert.ok(geometry, `${width}px geometry unavailable after reload`);
  assert.equal(geometry.width, width, `${width}px emulated viewport drifted to ${geometry.width}px`);
  assert.equal(geometry.horizontalOverflow, false, `${width}px page overflow`);
  assert.deepEqual(geometry.headerOverflow, [], `${width}px header child overflow`);
  assert.deepEqual(geometry.dockOverflow, [], `${width}px dock child overflow`);
  assert.ok(geometry.smallestTarget >= 43.5, `${width}px target below 44px: ${JSON.stringify(geometry.targetsUnder44)}`);
  assert.equal(geometry.header.height, 54, `${width}px single toolbar height`);
  assert.equal(geometry.dock.height, 44, `${width}px map control target height`);
  assert.equal(geometry.dockInHeader, true, `${width}px map controls must share the global header`);
  assert.ok(geometry.dock.top >= geometry.header.top && geometry.dock.bottom <= geometry.header.bottom,
    `${width}px map controls escaped the single header row`);
  assertNear(geometry.stage.top, geometry.header.bottom, `${width}px map starts directly below the header`);
  assert.equal(geometry.headerFocusOrder[0], "Search places, layers, official data…");
  assert.equal(geometry.directModes, width >= 1200, `${width}px representation placement`);
  assert.equal(geometry.directQuickControls, width > 760, `${width}px quick control placement`);
  assert.equal(geometry.menuModes, width < 1200, `${width}px menu representations`);
  assert.equal(geometry.menuQuickControls, width <= 760, `${width}px menu quick controls`);
  assert.equal(geometry.directBasemap, width >= 1800, `${width}px direct basemap`);
  assert.equal(geometry.directControls, width >= 1800, `${width}px direct controls`);
  assert.equal(geometry.mapOverflow, width < 1800, `${width}px Map menu`);
  assert.equal(geometry.controlsInOverflow, width < 1800, `${width}px controls in Map menu`);
  if (width === 390) {
    assert.equal(geometry.mobileBrand, true);
    assert.equal(geometry.qwenClearsMobileDock, true);
  }

  await evaluate(`(() => {
    const mapMenu = document.querySelector(".map-dock-map-menu");
    if (mapMenu instanceof HTMLDetailsElement) mapMenu.open = false;
  })()`);
  await activateMode(width, "Underground", `${width}px Underground`);
  await waitFor(`document.querySelector('.map-stage')?.getAttribute('data-underground') === 'true'
    && Boolean(document.querySelector('[aria-label="Underground 2D locator"]'))
    && Boolean(document.querySelector('section[aria-label="Underground workspace"]'))`);
  await pause(500);
  const underground = await evaluate(`(() => {
    const root = document.documentElement;
    const body = document.body;
    const stageElement = document.querySelector(".map-stage");
    const dockElement = document.querySelector(".map-chrome-dock");
    const headerElement = document.querySelector(".topbar");
    const locatorElement = document.querySelector('[aria-label="Underground 2D locator"]');
    const canvasElement = document.querySelector(".map-canvas");
    const effectsElement = document.querySelector(".map-effects");
    const panelElement = document.querySelector('section[aria-label="Underground workspace"]');
    const launcherElement = document.querySelector(".qwen-map-launch");
    const triggerElement = document.querySelector(innerWidth >= 1200
      ? '.map-dock-representations button[aria-label="Underground Logs & sections"]'
      : ".map-dock-map-menu > summary");
    const closeElement = document.querySelector('button[aria-label="Close Underground"]');
    const rect = (element) => {
      if (!(element instanceof Element)) return null;
      const box = element.getBoundingClientRect();
      return { left: box.left, top: box.top, right: box.right, bottom: box.bottom, width: box.width, height: box.height };
    };
    const visible = (element) => {
      if (!(element instanceof Element)) return false;
      const style = getComputedStyle(element);
      const box = element.getBoundingClientRect();
      return style.display !== "none" && style.visibility !== "hidden" && box.width > 0 && box.height > 0;
    };
    const stage = rect(stageElement);
    const dock = rect(dockElement);
    const locator = rect(locatorElement);
    const canvas = rect(canvasElement);
    const effects = rect(effectsElement);
    const panel = rect(panelElement);
    const launcher = rect(launcherElement);
    const target = (element) => {
      const box = rect(element);
      return box ? {
        width: box.width,
        height: box.height,
        label: element.getAttribute("aria-label") || element.textContent.trim().replace(/\\s+/g, " "),
      } : null;
    };
    const undergroundTargets = [
      target(triggerElement),
      ...[...locatorElement.querySelectorAll("button")].map(target),
      target(closeElement),
      target(launcherElement),
    ].filter(Boolean);
    const withinStage = { locator, canvas, effects, panel, launcher };
    const outsideStage = !stage ? ["missing-stage"] : Object.entries(withinStage)
      .filter(([, box]) => !box || box.left < stage.left - 1 || box.right > stage.right + 1 || box.top < stage.top - 1 || box.bottom > stage.bottom + 1)
      .map(([name]) => name);
    return {
      width: innerWidth,
      mode: stageElement?.getAttribute("data-underground"),
      stage, dock, header: rect(headerElement), locator, canvas, effects, panel, launcher,
      resolvedLocatorTop: locatorElement ? parseFloat(getComputedStyle(locatorElement).top) : null,
      resolvedSurfaceTop: canvasElement ? parseFloat(getComputedStyle(canvasElement).top) : null,
      horizontalOverflow: root.scrollWidth > root.clientWidth || body.scrollWidth > body.clientWidth,
      locatorOverflow: locatorElement ? locatorElement.scrollWidth > locatorElement.clientWidth + 1 || locatorElement.scrollHeight > locatorElement.clientHeight + 1 : true,
      outsideStage,
      launcherVisible: visible(launcherElement),
      launcherLabel: launcherElement?.getAttribute("aria-label"),
      undergroundTargets,
      targetsUnder44: undergroundTargets.filter((item) => item.width < 43.5 || item.height < 43.5),
    };
  })()`);
  assert.equal(underground.width, width, `${width}px Underground viewport drifted`);
  assert.equal(underground.mode, "true", `${width}px Underground state was not retained`);
  assert.equal(underground.horizontalOverflow, false, `${width}px Underground page overflow`);
  assert.equal(underground.locatorOverflow, false, `${width}px Underground locator content overflow`);
  assert.deepEqual(underground.outsideStage, [], `${width}px Underground surface escaped the map stage`);
  assert.deepEqual(underground.targetsUnder44, [], `${width}px Underground target below 44px`);
  assert.equal(underground.launcherVisible, true, `${width}px Qwen launcher hidden in Underground`);
  assert.equal(underground.launcherLabel, "Ask Qwen about this map view", `${width}px Qwen launcher lost its accessible name`);
  assertNear(underground.header.bottom, underground.stage.top, `${width}px Underground starts below the single header`);
  assert.ok(underground.dock.top >= underground.header.top && underground.dock.bottom <= underground.header.bottom, `${width}px Underground controls escaped the header`);
  assertNear(underground.locator.top - underground.stage.top, underground.resolvedLocatorTop, `${width}px Underground locator offset`);
  assertNear(underground.canvas.top - underground.stage.top, underground.resolvedSurfaceTop, `${width}px Underground map offset`);
  assert.ok(underground.locator.top >= underground.stage.top + 7.5, `${width}px Underground locator overlaps the header`);
  assert.ok(underground.locator.bottom <= underground.canvas.top + 1, `${width}px Underground locator overlaps the map surface`);
  assertNear(underground.canvas.left, underground.effects.left, `${width}px Underground effect left edge`);
  assertNear(underground.canvas.top, underground.effects.top, `${width}px Underground effect top edge`);
  assertNear(underground.canvas.right, underground.effects.right, `${width}px Underground effect right edge`);
  assertNear(underground.canvas.bottom, underground.effects.bottom, `${width}px Underground effect bottom edge`);
  assertNear(underground.canvas.bottom, underground.panel.top, `${width}px Underground map-to-panel boundary`, 1.5);
  assertNear(underground.panel.bottom, underground.stage.bottom, `${width}px Underground panel bottom`, 1.5);
  assert.ok(underground.canvas.height >= 100, `${width}px Underground locator map is too short`);
  assert.ok(underground.launcher.top >= underground.canvas.top - 1 && underground.launcher.bottom <= underground.panel.top - 12,
    `${width}px Qwen launcher is not reachable in the exposed locator map`);
  for (const [selector, label] of [
    [width >= 1200 ? '.map-dock-representations button[aria-label="Underground Logs & sections"]' : ".map-dock-map-menu > summary", "Underground mode access"],
    ['[aria-label="Underground 2D locator"] button:nth-of-type(1)', "Use map center"],
    ['[aria-label="Underground 2D locator"] button:nth-of-type(2)', "Find selection"],
    ['[aria-label="Underground 2D locator"] button:nth-of-type(3)', "Reset to 2D"],
    ['button[aria-label="Close Underground"]', "Close Underground"],
    [".qwen-map-launch", "Qwen launcher"],
  ]) {
    await assertMinimumTarget(selector, `${width}px ${label}`);
  }
  await focusSelector(".qwen-map-launch", `${width}px Qwen launcher in Underground`);
  await activateSelector('button[aria-label="Close Underground"]', `${width}px Close Underground`);
  await waitFor(`document.querySelector('.map-stage')?.getAttribute('data-underground') !== 'true'
    && !document.querySelector('section[aria-label="Underground workspace"]')`);
  undergroundObservations.push(underground);
  observations.push(geometry);
}

const keyboardCoverage = [];
const covered = (name, width) => keyboardCoverage.push({ name, width });

// Wide desktop: every direct header/dock path remains operable without a pointer.
await reloadAt(1920);
await activateSelector(".data-notices-trigger", "Data & downloads");
await waitFor(`Boolean(document.querySelector("#data-notices-panel"))`);
await assertMinimumTarget(".data-notices-panel header button", "Data panel close");
await assertMinimumTarget('.data-notices-panel footer a[href="/data"]', "Contribute data");
await interceptLinkActivation('.data-notices-panel a[href="/data"]', "Contribute data");
await pressKey("Escape");
await waitFor(`!document.querySelector("#data-notices-panel")`);
assert.equal(await evaluate(`document.activeElement === document.querySelector(".data-notices-trigger")`), true);
covered("Data & downloads / Contribute data", 1920);

await openMenu(".header-overflow-menu", "More site actions");
await activateSelector(".new-from-map-action", "Compose");
await waitFor(`Boolean(document.querySelector("#map-context-card") && document.activeElement?.getAttribute("aria-label") === "Close map context composer")`);
await assertMinimumTarget('#map-context-card button[aria-label="Close map context composer"]', "Compose close");
await pressKey("Escape");
await waitFor(`!document.querySelector("#map-context-card")`);
assert.equal(await evaluate(`document.activeElement === document.querySelector(".new-from-map-action")`), true);
covered("Compose", 1920);

await activateWorkspace("Reports", "Reports workspace");
await waitFor(`document.querySelector('.primary-workspace-surface')?.getAttribute('data-workspace') === 'reports'`);
await activateWorkspace("Stories", "Stories workspace");
await waitFor(`document.querySelector('.primary-workspace-surface')?.getAttribute('data-workspace') === 'stories'`);
await activateWorkspace("Map", "Map workspace");
await waitFor(`!document.querySelector(".primary-workspace-surface")`);
covered("Map / Reports / Stories", 1920);

await activateSelector('.map-dock-representations button[aria-label="Underground Logs & sections"]', "Underground");
await waitFor(`Boolean(document.querySelector('section[aria-label="Underground workspace"]'))`);
await activateSelector('button[aria-label="Close Underground"]', "Close Underground");
await waitFor(`!document.querySelector('section[aria-label="Underground workspace"]')`);
await activateMatching(".map-dock-representations", "button", "2D", "2D Map");
await waitFor(`document.querySelector('.map-dock-representations button:nth-of-type(2)')?.getAttribute('aria-pressed') === 'true'`);
await activateMatching(".map-dock-representations", "button", "Terrain 3D", "Terrain 3D");
await waitFor(`[...document.querySelectorAll('.map-dock-representations button')].some((button) => button.querySelector('b')?.textContent === 'Terrain 3D' && button.getAttribute('aria-pressed') === 'true')`);
await activateMatching(".map-dock-representations", "button", "Globe", "Globe");
await waitFor(`[...document.querySelectorAll('.map-dock-representations button')].some((button) => button.querySelector('b')?.textContent === 'Globe' && button.getAttribute('aria-pressed') === 'true')`);
await activateMatching(".map-dock-representations", "button", "Compare", "Compare A/B");
await waitFor(`document.querySelector('.map-utility-panel')?.getAttribute('data-open') === 'true' && document.querySelector('.map-utility-panel')?.getAttribute('data-view') === 'compare'`);
await pressKey("Escape");
covered("Underground / 2D / Terrain / Globe / Compare", 1920);

await reloadAt(1920);
const desktopBasemapBefore = await evaluate(`document.querySelector('.map-dock-basemap select')?.value`);
await focusSelector('.map-dock-basemap select[aria-label="Choose basemap style"]', "Basemap");
await pressLetter("m");
await pause(100);
assert.notEqual(await evaluate(`document.querySelector('.map-dock-basemap select')?.value`), desktopBasemapBefore, "Basemap did not respond to the keyboard");
covered("Basemap", 1920);

await activateSelector(".map-dock-action.map-dock-wide-only", "Map controls");
await waitFor(`document.querySelector('.map-utility-panel')?.getAttribute('data-open') === 'true'
  && document.querySelector('.map-utility-panel')?.getAttribute('data-view') === 'navigate'
  && document.querySelector('.map-utility-panel')?.contains(document.activeElement)`);
await assertMinimumTarget('.map-utility-panel button[aria-label^="Close "]', "Map controls close");
await pressKey("Escape");
covered("Map controls direct", 1920);

await reloadAt(1920);
await activateMatching(".map-dock-actions", "button", "Time", "Time");
await waitFor(`Boolean(document.querySelector(".timeline-detail"))`);
await assertMinimumTarget('.timeline-detail .timeline-primary-actions a[href="/observatory"]', "Daily archive");
await assertMinimumTarget(".timeline-detail .timeline-close", "Timeline close");
await interceptLinkActivation('.timeline-detail a[href="/observatory"]', "Daily archive");
covered("Time / Daily archive", 1920);

await reloadAt(1920);
await activateMatching(".map-dock-actions", "button", "Layers", "Layers");
await waitFor(`document.querySelector('.layer-panel')?.getAttribute('aria-hidden') === 'false' && document.querySelector('.layer-panel')?.getAttribute('data-panel-mode') === 'layers'`);
await assertMinimumTarget('.layer-panel button[aria-label="Close Explorer navigation"]', "Layers close");
await activateSelector(".layer-panel-explore > summary", "Other map tools", "Space");
assert.equal(await evaluate(`document.querySelector(".layer-panel-explore")?.open`), true);
await assertMinimumTarget(".layer-panel-explore > summary", "Other map tools");
await assertMinimumTarget(".layer-panel-explore nav button:nth-of-type(3)", "Kansas historic maps");
await activateMatching(".layer-panel-explore", "button", "Kansas historic maps", "Kansas historic maps");
await waitFor(`document.querySelector('.map-utility-panel')?.getAttribute('data-open') === 'true' && document.querySelector('.map-utility-panel')?.getAttribute('data-view') === 'history'`);
covered("Layers / Kansas historic maps", 1920);

await reloadAt(1920);
await activateMatching(".map-dock-actions", "button", "Places", "Places");
await waitFor(`document.querySelector('.layer-panel')?.getAttribute('aria-hidden') === 'false' && document.querySelector('.layer-panel')?.getAttribute('data-panel-mode') === 'places'`);
covered("Places", 1920);

// Tablet: Map retains every representation after the inline row folds away.
await reloadAt(1024);
await openMenu(".map-dock-map-menu", "Map views and controls");
await assertInViewport(".map-dock-menu-panel", "Tablet Map menu");
await assertMinimumTarget('.map-dock-menu-representations button[aria-label="Underground Logs & sections"]', "Tablet Underground menu action");
await pressKey("Escape");
assert.deepEqual(await evaluate(`({
  open: document.querySelector(".map-dock-map-menu")?.open,
  focusRestored: document.activeElement === document.querySelector(".map-dock-map-menu > summary"),
})`), { open: false, focusRestored: true });
for (const [name, pressedExpression] of [
  ["2D", `[...document.querySelectorAll('.map-dock-menu-representations button')].some((button) => button.querySelector('b')?.textContent === '2D' && button.getAttribute('aria-pressed') === 'true')`],
  ["Terrain 3D", `[...document.querySelectorAll('.map-dock-menu-representations button')].some((button) => button.querySelector('b')?.textContent === 'Terrain 3D' && button.getAttribute('aria-pressed') === 'true')`],
  ["Globe", `[...document.querySelectorAll('.map-dock-menu-representations button')].some((button) => button.querySelector('b')?.textContent === 'Globe' && button.getAttribute('aria-pressed') === 'true')`],
]) {
  await activateMode(1024, name, `Tablet ${name}`);
  await waitFor(pressedExpression);
}
await activateMode(1024, "Compare", "Tablet Compare A/B");
await waitFor(`document.querySelector('.map-utility-panel')?.getAttribute('data-open') === 'true' && document.querySelector('.map-utility-panel')?.getAttribute('data-view') === 'compare'`);
await pressKey("Escape");
covered("Map menu / 2D / Terrain / Globe / Compare / Escape and focus return", 1024);

// Tablet: overflow replacements, status hand-offs, and the single Qwen launcher.
await reloadAt(1024);
await activateSelector(".header-overflow-menu > summary", "Header overflow", "Space");
assert.equal(await evaluate(`document.querySelector(".header-overflow-menu")?.open`), true);
await pressKey("Escape");
assert.deepEqual(await evaluate(`({
  open: document.querySelector(".header-overflow-menu")?.open,
  focusRestored: document.activeElement === document.querySelector(".header-overflow-menu > summary"),
})`), { open: false, focusRestored: true });

await pressKey("Space");
await activateSelector(".header-overflow-menu .share-action", "Share current view");
await waitFor(`!document.querySelector(".header-overflow-menu")?.open`);
assert.equal(await evaluate(`document.activeElement === document.querySelector(".header-overflow-menu > summary")`), true);
covered("Share", 1024);

await pressKey("Space");
await interceptLinkActivation('.header-overflow-panel a[href="/about"]', "About");
await pressKey("Escape");
assert.equal(await evaluate(`document.activeElement === document.querySelector(".header-overflow-menu > summary")`), true);
covered("About", 1024);

await pressKey("Space");
await activateMatching(".header-overflow-workspaces", "button", "Reports", "Overflow Reports");
await waitFor(`document.querySelector('.primary-workspace-surface')?.getAttribute('data-workspace') === 'reports'`);
await activateSelector(".header-overflow-menu > summary", "Header overflow", "Space");
await activateMatching(".header-overflow-workspaces", "button", "Stories", "Overflow Stories");
await waitFor(`document.querySelector('.primary-workspace-surface')?.getAttribute('data-workspace') === 'stories'`);
await activateSelector(".header-overflow-menu > summary", "Header overflow", "Space");
await activateMatching(".header-overflow-workspaces", "button", "Map", "Overflow Map");
await waitFor(`!document.querySelector(".primary-workspace-surface")`);
covered("Overflow Map / Reports / Stories", 1024);

await activateSelector(".map-dock-map-menu > summary", "Map dock overflow", "Space");
await activateMatching(".map-dock-map-menu", "button", "Style & basemap", "Style & basemap");
await waitFor(`Boolean(document.querySelector('#map-settings[open]') && document.activeElement === document.querySelector('#map-settings > summary'))`);
const renderQualityBefore = await evaluate(`document.querySelector('select[aria-label="Map rendering quality"]')?.value`);
await focusSelector('select[aria-label="Map rendering quality"]', "Rendering quality");
await assertMinimumTarget('select[aria-label="Map rendering quality"]', "Rendering quality");
await pressLetter(renderQualityBefore === "detail" ? "b" : "h");
await pause(100);
assert.notEqual(await evaluate(`document.querySelector('select[aria-label="Map rendering quality"]')?.value`), renderQualityBefore, "Rendering quality did not respond to the keyboard");
covered("Style & basemap / Rendering quality", 1024);

await reloadAt(1024);
await activateSelector(".map-dock-map-menu > summary", "Map dock overflow", "Space");
await activateMatching(".map-dock-map-menu", "button", "Map controls", "Overflow Map controls");
await waitFor(`document.querySelector('.map-utility-panel')?.getAttribute('data-open') === 'true'
  && document.querySelector('.map-utility-panel')?.getAttribute('data-view') === 'navigate'
  && document.querySelector('.map-utility-panel')?.contains(document.activeElement)`);
for (const section of ["Inspect", "Scene", "Measure", "Report", "Export"]) {
  await activateMatching(".map-utility-tabs", "button", section, `${section} map control section`);
  await waitFor(`document.querySelector('.map-utility-panel')?.getAttribute('data-view') === ${JSON.stringify(section.toLowerCase())}`);
}
await activateMatching(".map-utility-tabs", "button", "Measure", "Measure map control section");
for (const mode of ["Point", "Line", "Polygon"]) {
  await assertMinimumTarget(`#map-utility-view-measure button[aria-label="${mode}"]`, `${mode} measurement mode`);
}
await activateSelector('#map-utility-view-measure button[aria-label="Point"]', "Point measurement mode");
assert.equal(await evaluate(`document.querySelector('#map-utility-view-measure button[aria-label="Point"]')?.getAttribute('aria-pressed')`), "true");
await pressKey("Escape");
covered("Map controls overflow / Inspect / Scene / Measure / Report / Export", 1024);

await reloadAt(1024);
await activateStatus();
await waitFor(`Boolean(document.querySelector(".repository-briefing") && !document.querySelector(".repository-overlay").hidden)`);
await activateSelector('.status-map-actions [aria-controls="map-source-status"]', "Source status");
await waitFor(`Boolean(document.querySelector("#map-source-status") && document.activeElement?.getAttribute("aria-label") === "Close source status")`);
await assertMinimumTarget('#map-source-status button[aria-label="Close source status"]', "Source status close");
await pressKey("Escape");
await waitFor(`!document.querySelector("#map-source-status")`);
assert.equal(await evaluate(`document.activeElement === document.querySelector(".header-overflow-menu > summary")`), true);
covered("Status / Source status", 1024);

await activateStatus();
await waitFor(`!document.querySelector(".repository-overlay")?.hidden`);
await activateMatching(".status-map-links", "button", "Live controls", "Live controls");
await waitFor(`document.querySelector(".repository-overlay")?.hidden === true`);
assert.equal(await evaluate(`document.activeElement === document.querySelector("#map-canvas")`), true);
covered("Live controls", 1024);

await reloadAt(1024);
await activateStatus();
await waitFor(`!document.querySelector(".repository-overlay")?.hidden`);
const baselineTimeOrigin = await evaluate(`performance.timeOrigin`);
await focusMatching(".status-map-links", "button", "Today’s baseline", "Today's baseline");
await pressKey("Enter");
await waitFor(`performance.timeOrigin !== ${baselineTimeOrigin}`);
await waitFor(explorerReady, 20_000);
covered("Today's baseline", 1024);

await activateSelector(".qwen-map-launch", "Qwen launcher");
await waitFor(`Boolean(document.querySelector("#qwen-map-panel") && document.activeElement?.getAttribute("aria-label") === "Close Qwen companion")`);
await assertMinimumTarget('#qwen-map-panel button[aria-label="Close Qwen companion"]', "Qwen close");
await pressKey("Escape");
await waitFor(`!document.querySelector("#qwen-map-panel")`);
assert.equal(await evaluate(`document.activeElement === document.querySelector(".qwen-map-launch")`), true);
covered("Qwen", 1024);

// Mobile: the More menu retains workspaces; Map retains modes and quick controls.
// Each 48px bottom-dock route remains independently reachable.
await reloadAt(390);
await activateWorkspace("Reports", "Mobile Reports");
await waitFor(`document.querySelector('.primary-workspace-surface')?.getAttribute('data-workspace') === 'reports'`);
await activateWorkspace("Stories", "Mobile Stories");
await waitFor(`document.querySelector('.primary-workspace-surface')?.getAttribute('data-workspace') === 'stories'`);
await activateWorkspace("Map", "Mobile Map");
await waitFor(`!document.querySelector(".primary-workspace-surface")`);
covered("Mobile Map / Reports / Stories through More", 390);

for (const name of ["Time", "Layers", "Places"]) {
  await reloadAt(390);
  await openMenu(".map-dock-map-menu", "Mobile Map views and controls");
  await assertInViewport(".map-dock-menu-panel", "Mobile Map menu");
  await activateMatching(".map-dock-menu-quick", "button", name, `Mobile Map menu ${name}`);
  assert.equal(await evaluate(`document.querySelector(".map-dock-map-menu")?.open`), false);
  if (name === "Time") {
    await waitFor(`Boolean(document.querySelector(".timeline-detail"))`);
    await pressKey("Escape");
    await waitFor(`!document.querySelector(".timeline-detail")`);
  } else {
    await waitFor(`document.querySelector('.layer-panel')?.getAttribute('aria-hidden') === 'false' && document.querySelector('.layer-panel')?.getAttribute('data-panel-mode') === ${JSON.stringify(name.toLowerCase())}`);
    await pressKey("Escape");
    await waitFor(`document.querySelector('.layer-panel')?.getAttribute('aria-hidden') === 'true'`);
  }
  covered(`Mobile Map menu ${name}`, 390);
}
await reloadAt(390);

await activateMatching(".map-mobile-actions", "button", "Map layers", "Mobile Map layers");
await waitFor(`document.querySelector('.layer-panel')?.getAttribute('aria-hidden') === 'false' && document.querySelector('.layer-panel')?.getAttribute('data-panel-mode') === 'layers'`);
await pressKey("Escape");
await waitFor(`document.querySelector('.layer-panel')?.getAttribute('aria-hidden') === 'true'`);
covered("Mobile Map layers", 390);

await reloadAt(390);
await activateMatching(".map-mobile-actions", "button", "Places", "Mobile Places");
await waitFor(`document.querySelector('.layer-panel')?.getAttribute('aria-hidden') === 'false' && document.querySelector('.layer-panel')?.getAttribute('data-panel-mode') === 'places'`);
await pressKey("Escape");
await waitFor(`document.querySelector('.layer-panel')?.getAttribute('aria-hidden') === 'true'`);
covered("Mobile Places", 390);

await reloadAt(390);
await activateMatching(".map-mobile-actions", "button", "Sources", "Mobile Sources");
await waitFor(`Boolean(document.querySelector("#map-source-status") && document.activeElement?.getAttribute("aria-label") === "Close source status")`);
await pressKey("Escape");
await waitFor(`!document.querySelector("#map-source-status")`);
assert.equal(await evaluate(`document.activeElement === [...document.querySelectorAll('.map-mobile-actions button')].find((button) => button.textContent.trim().startsWith('Sources'))`), true);
covered("Mobile Sources", 390);

await reloadAt(390);
await activateMatching(".map-mobile-actions", "button", "Time", "Mobile Time");
await waitFor(`Boolean(document.querySelector(".timeline-detail"))`);
await pressKey("Escape");
await waitFor(`!document.querySelector(".timeline-detail")`);
covered("Mobile Time", 390);

await reloadAt(390);
await activateMatching(".map-mobile-actions", "button", "Style", "Mobile Style");
await waitFor(`Boolean(document.querySelector('#map-settings[open]') && document.activeElement === document.querySelector('#map-settings > summary'))`);
await pressKey("Escape");
await waitFor(`document.querySelector('.layer-panel')?.getAttribute('aria-hidden') === 'true'`);
covered("Mobile Style", 390);

await reloadAt(390);
await activateSelector(".qwen-map-launch", "Mobile Qwen launcher");
await waitFor(`Boolean(document.querySelector("#qwen-map-panel") && document.activeElement?.getAttribute("aria-label") === "Close Qwen companion")`);
assert.equal(await evaluate(`document.querySelector("#qwen-map-panel")?.getAttribute("aria-modal")`), "true");
await waitFor(`document.querySelector(".topbar")?.inert === true && Boolean(document.querySelector(".map-chrome-dock")?.closest("[inert]")) && document.querySelector(".map-mobile-actions")?.inert === true`);
assert.deepEqual(await evaluate(`(() => {
  const panel = document.querySelector("#qwen-map-panel");
  const outsideButton = document.querySelector(".map-mobile-actions button");
  outsideButton?.focus();
  return {
    panelHasInertAncestor: Boolean(panel?.closest("[inert]")),
    focusStayedInPanel: Boolean(panel?.contains(document.activeElement)),
    topbarInert: document.querySelector(".topbar")?.inert === true,
    dockInert: Boolean(document.querySelector(".map-chrome-dock")?.closest("[inert]")),
    mobileActionsInert: document.querySelector(".map-mobile-actions")?.inert === true,
  };
})()`), {
  panelHasInertAncestor: false,
  focusStayedInPanel: true,
  topbarInert: true,
  dockInert: true,
  mobileActionsInert: true,
});
for (const [selector, label] of [
  ['.qwen-runtime-actions button:first-child', "Qwen Setup"],
  ['.qwen-runtime-actions button:last-child', "Qwen Retry"],
  ['.qwen-form textarea', "Qwen question"],
  ['.qwen-form button[type="submit"]', "Qwen Ask"],
  ['.qwen-panel-footer button', "Copy grounded prompt"],
]) {
  await assertInViewport(selector, label);
  await assertMinimumTarget(selector, label);
}
await activateSelector('.qwen-runtime-actions button:first-child', "Qwen Setup");
await waitFor(`Boolean(document.querySelector("#qwen-setup-guidance"))`);
await assertInViewport("#qwen-setup-guidance", "Qwen setup guidance");
await activateSelector('.qwen-runtime-actions button:first-child', "Close Qwen Setup");
await waitFor(`!document.querySelector("#qwen-setup-guidance")`);
await focusSelector('.qwen-panel-footer button', "Copy grounded prompt");
await pressKey("Tab");
await waitFor(`document.activeElement?.getAttribute("aria-label") === "Close Qwen companion"`);
assert.equal(await evaluate(`document.elementFromPoint(2, 2)?.classList.contains("qwen-modal-backdrop")`), true);
await call("Input.dispatchMouseEvent", { type: "mousePressed", x: 2, y: 2, button: "left", clickCount: 1 });
await call("Input.dispatchMouseEvent", { type: "mouseReleased", x: 2, y: 2, button: "left", clickCount: 1 });
await waitFor(`!document.querySelector("#qwen-map-panel")`);
assert.equal(await evaluate(`document.activeElement === document.querySelector(".qwen-map-launch")`), true);
covered("Mobile Qwen / Setup / Retry / Ask / Copy / modal isolation / focus trap", 390);

process.stdout.write(`${JSON.stringify({ status: "passed", observations, undergroundObservations, keyboardCoverage }, null, 2)}\n`);
socket.close();
