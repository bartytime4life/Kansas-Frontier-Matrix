/** Operator launch fragments provision capabilities; HTTP status cannot bootstrap them. */
export type Companion = "downloads" | "intake" | "basemap";
const services: Companion[] = ["downloads", "intake", "basemap"];
const memory = new Map<Companion, string>();
const valid = (value: string | null): value is string => value !== null && value.length === 43 && /^[A-Za-z0-9_-]{43}$/.test(value);

export function companionSession(service: Companion): string {
  if (typeof window === "undefined") return "";
  const params = new URLSearchParams(window.location.hash.slice(1));
  let changed = false;
  for (const name of services) {
    const values = params.getAll(`kfm-${name}`);
    const key = `kfm-${name}-session`;
    if (values.length) {
      changed = true;
      const token = values.length === 1 && valid(values[0]) ? values[0] : "";
      memory.set(name, token);
      params.delete(`kfm-${name}`);
      try { if (token) window.sessionStorage.setItem(key, token); else window.sessionStorage.removeItem(key); } catch { /* Use memory when storage is disabled. */ }
    } else if (!memory.has(name)) {
      try {
        const token = window.sessionStorage.getItem(key);
        memory.set(name, valid(token) ? token : "");
      } catch { memory.set(name, ""); }
    }
  }
  if (changed) window.history.replaceState(null, "", window.location.pathname + window.location.search + (params.size ? `#${params}` : ""));
  return memory.get(service) ?? "";
}
