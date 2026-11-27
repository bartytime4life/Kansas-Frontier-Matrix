"use client";

import { useEffect, useLayoutEffect, useRef, useState, type ComponentProps } from "react";

type FieldTools = typeof import("./field-decision-tools")["FieldDecisionTools"];
let loadedTools: FieldTools | null = null;

export function FieldDecisionToolsLoader(props: ComponentProps<FieldTools>) {
  const [Tools, setTools] = useState<FieldTools | null>(() => loadedTools);
  const [failed, setFailed] = useState(false);
  const host = useRef<HTMLDivElement>(null);
  const focusWhenReady = useRef<string | null>(null);

  useEffect(() => {
    if (Tools) return;
    let mounted = true;
    void import("./field-decision-tools").then(({ FieldDecisionTools }) => {
      loadedTools = FieldDecisionTools;
      if (!mounted) return;
      const focused = document.activeElement;
      if (focused instanceof HTMLElement && host.current?.contains(focused)) {
        focusWhenReady.current = focused.dataset.categoryToolLoading ?? null;
      }
      setTools(() => FieldDecisionTools);
    }, () => {
      if (mounted) setFailed(true);
    });
    return () => { mounted = false; };
  }, [Tools]);

  useLayoutEffect(() => {
    const tool = focusWhenReady.current;
    focusWhenReady.current = null;
    if (!Tools || !tool || document.activeElement !== document.body) return;
    const summary = host.current?.querySelector<HTMLElement>(`[data-category-tool="${tool}"]`);
    summary?.scrollIntoView({ block: "nearest" });
    summary?.focus({ preventScroll: true });
  }, [Tools]);

  return <div ref={host}>
    {Tools ? <Tools {...props} /> : <section className="field-tool" aria-label="Farm planning tools">
      <p tabIndex={-1} data-category-tool-loading="farm-planning" role={failed ? "alert" : "status"}>
        {failed ? "Farm planning tools could not load." : "Loading farm planning tools…"}
      </p>
      <p tabIndex={-1} data-category-tool-loading="field-almanac">
        {failed ? "Farmers’ Almanac controls are unavailable." : "Loading Farmers’ Almanac controls…"}
      </p>
      {failed && <button type="button" onClick={() => window.location.reload()}>Reload Explorer</button>}
    </section>}
  </div>;
}
