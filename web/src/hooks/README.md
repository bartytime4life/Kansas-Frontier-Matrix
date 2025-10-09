<div align="center">

# ⚓ Kansas Frontier Matrix — Web Frontend Hooks  
`web/src/hooks/`

**Custom React Hooks · State Management · Lifecycle Utilities**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../../.github/workflows/ci.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/codeql.yml?label=CodeQL)](../../../../.github/workflows/codeql.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../docs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../LICENSE)

</div>

---

## 🧭 Overview

The `web/src/hooks/` directory provides **custom React Hooks** that encapsulate reusable logic for  
data fetching, global state synchronization, event handling, and responsive UI behaviors across  
the **Kansas Frontier Matrix** web application.

These hooks simplify component logic and maintain consistent data flow between the **Map**,  
**Timeline**, and **AI Assistant** interfaces.  

Each hook follows the **Master Coder Protocol (MCP)** principles:
- Fully documented via JSDoc comments.
- Deterministic and side-effect aware.
- Tested via Jest/React Testing Library.
- Explicit dependencies (no hidden global state).

---

## 🧱 Directory Structure

```text
web/src/hooks/
├── useFetch.js              # Handles API requests with loading/error states
├── useDebounce.js           # Debounces user input (e.g., search bar)
├── useResizeObserver.js     # Observes DOM element resize for responsive layouts
├── useTimelineRange.js      # Manages global timeline state (start/end)
├── useMapInteraction.js     # Map click/hover events and layer sync
├── useKeyboardShortcuts.js  # Keyboard navigation and focus accessibility
├── useTheme.js              # Dark/light theme preference and toggling
└── index.js                 # Consolidated export of all hooks


⸻

🧩 Hook Overview

Hook	Purpose	Example Usage
useFetch	Simplifies async API requests (fetch/Axios) with loading & error handling.	const { data, loading } = useFetch('/api/events');
useDebounce	Delays execution of rapidly fired inputs (used in search bar & slider).	const query = useDebounce(inputValue, 300);
useResizeObserver	Watches an element’s size (for map/timeline responsiveness).	useResizeObserver(ref, onResize);
useTimelineRange	Stores and updates current timeline range; triggers data reloads.	const { range, setRange } = useTimelineRange();
useMapInteraction	Centralizes event listeners for MapLibre map interactions.	useMapInteraction(mapRef, onSelectLayer);
useKeyboardShortcuts	Adds keyboard navigation for accessibility (arrow keys, escape, tab).	useKeyboardShortcuts(shortcutMap);
useTheme	Manages user’s theme setting (persisted via localStorage).	const { theme, toggleTheme } = useTheme();


⸻

⚙️ Example Implementation

// useFetch.js
import { useState, useEffect } from "react";
import axios from "axios";

export function useFetch(url, options = {}) {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!url) return;
    let isMounted = true;
    setLoading(true);

    axios(url, options)
      .then(res => isMounted && setData(res.data))
      .catch(err => isMounted && setError(err))
      .finally(() => isMounted && setLoading(false));

    return () => { isMounted = false; };
  }, [url]);

  return { data, loading, error };
}

This standard hook pattern underpins all API requests used by the timeline, map, and entity panels.

⸻

🧠 Hook Data Flow

flowchart TD
  A["useTimelineRange\n(time window)"] --> B["MapView\n(fetch layers/events)"]
  A --> C["TimelineView\n(draw events)"]
  D["useFetch\n(API requests)"] --> C
  D --> E["AI Assistant\n(entity data)"]
  F["useTheme\n(user prefs)"] --> G["AppLayout\n(theme context)"]
%% END OF MERMAID

Hooks orchestrate synchronized updates across components:
	•	Timeline range changes trigger new data fetches.
	•	Map selections propagate to detail panels.
	•	User preferences persist between sessions.

⸻

🧩 Best Practices
	•	Encapsulation: Each hook handles one responsibility only.
	•	Naming: All hooks start with use and return predictable objects { data, loading, error }.
	•	Cleanup: Every hook must manage side effects (unsubscribe/abort signals on unmount).
	•	Testing: Simulate async and UI behaviors with Jest mocks and act() wrappers.
	•	Documentation: Include parameter, return type, and usage examples in JSDoc format.

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	REST/GraphQL API data, MapLibre map instance, user preferences
Outputs	Component-ready states (data, range, theme, focus)
Dependencies	React 18+, Axios, D3.js, MapLibre GL
Integrity	CI runs lint, type check, and hook coverage tests (≥ 85%)


⸻

🔗 Related Documentation
	•	Web Frontend Overview
	•	Web Frontend Utilities
	•	Web UI Architecture
	•	Accessibility Keyboard Focus Review

⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — built to MCP standards for reliability, modularity, and clarity.

“Custom hooks are the logic trail markers — guiding users through time, terrain, and story.”

