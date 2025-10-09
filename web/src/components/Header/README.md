<div align="center">

# 🧭 Kansas Frontier Matrix — Header Component  
`web/src/components/Header/`

**Global Navigation · Search Bar · Theme Toggle · Branding**

[![Build](https://img.shields.io/github/actions/workflow/status/bartytime4life/Kansas-Frontier-Matrix/ci.yml?label=Build)](../../../../../.github/workflows/ci.yml)
[![Docs · MCP](https://img.shields.io/badge/Docs-MCP-green)](../../../../../docs/)
[![Accessibility](https://img.shields.io/badge/WCAG%202.1-AA-yellow)](../../../../../docs/design/reviews/accessibility/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../../../../../LICENSE)

</div>

---

## 🧭 Overview

The **Header Component** provides the Kansas Frontier Matrix application’s **top navigation bar**.  
It acts as the user’s global control center, providing quick access to search, theme settings,  
language toggle, and application-level modals (Help, About, Settings).

This component embodies the **Master Coder Protocol (MCP)** design ethos:  
- Unified state management via `ThemeContext` and `AccessibilityContext`.  
- Accessibility-first implementation (ARIA roles, keyboard shortcuts).  
- Reproducible configuration through typed props and documented API contracts.  

The Header is present across all screens, ensuring a consistent user experience while maintaining  
performance and responsiveness across devices.

---

## 🧱 Directory Structure

```text
web/src/components/Header/
├── Header.tsx             # Main component logic and layout
├── SearchBar.tsx          # Autocomplete entity search input
├── ThemeToggle.tsx        # Dark/light mode switcher
├── LanguageSwitcher.tsx   # Multi-language dropdown
├── HelpMenu.tsx           # Modal with keyboard shortcuts + user guide
├── styles.scss            # Header-specific layout and color scheme
└── __tests__/             # Unit tests for UI interaction and API search


⸻

⚙️ Component Architecture

flowchart LR
  H["Header"] --> S["SearchBar\n(useDebounce + /search?q=)"]
  H --> T["ThemeToggle\n(light/dark via ThemeContext)"]
  H --> L["LanguageSwitcher\n(locale select)"]
  H --> M["HelpMenu\nkeyboard shortcuts, docs links"]
  H --> LOGO["Branding / Project Title"]
  S --> API["FastAPI\nGET /search?q="]
%% END OF MERMAID


⸻

🔍 Core Features

Feature	Description	Data / Context Source
Search Bar	Autocomplete-powered entity search (people, places, events).	/api/search
Theme Toggle	Switch between dark/light mode, persisted via localStorage.	ThemeContext
Language Switcher	Dynamically changes locale and date formatting.	i18n module
Help / Info Menu	Displays documentation links, keyboard shortcuts, and About modal.	Static config
Brand Identity	Displays project name, version, and logo (from package.json).	Local metadata
Accessibility	Full keyboard navigation, focus outlines, and ARIA landmarks.	AccessibilityContext


⸻

💬 Example Implementation

import React from "react";
import { useTheme } from "../../context/ThemeContext";
import { SearchBar } from "./SearchBar";
import { ThemeToggle } from "./ThemeToggle";
import { LanguageSwitcher } from "./LanguageSwitcher";
import "./styles.scss";

export const Header: React.FC = () => {
  const { theme } = useTheme();

  return (
    <header className={`kfm-header ${theme}`}>
      <div className="logo">
        <img src="/assets/logo.svg" alt="Kansas Frontier Matrix logo" />
        <h1>Kansas Frontier Matrix</h1>
      </div>
      <SearchBar placeholder="Search events, places, or people..." />
      <div className="controls">
        <LanguageSwitcher />
        <ThemeToggle />
      </div>
    </header>
  );
};


⸻

🧠 Data Flow

flowchart TD
  U["User Input"] --> SB["SearchBar\n(useDebounce)"]
  SB --> API["/api/search?q={term}"]
  API --> RES["Entity Results"]
  RES --> DP["DetailPanel\n(entity preview)"]
  T["ThemeToggle"] --> TC["ThemeContext\n(persisted)"]
%% END OF MERMAID


⸻

🎨 Styling & Layout
	•	Uses flexbox layout (display: flex; justify-content: space-between; align-items: center;).
	•	Theming controlled by CSS variables (--kfm-color-bg, --kfm-color-accent).
	•	Responsive breakpoints:
	•	<768px: collapses to a hamburger menu.
	•	<1024px: hides logo text, keeps icon.
	•	Transitions (Framer Motion): fade for theme toggle, slide-down for search results.
	•	Accessible focus styling from web/src/styles/variables.scss.

⸻

⚡ Search Functionality

The SearchBar integrates with the backend’s /api/search endpoint to find entities across
the knowledge graph. Results appear as autocomplete suggestions.

const { query, setQuery } = useState("");
const results = useFetch(`/api/search?q=${query}`);

Entities returned include:

interface SearchResult {
  id: string;
  label: string;
  type: "Person" | "Place" | "Event" | "Document";
  summary?: string;
}

Results are rendered with icons per type and clickable links to the DetailPanel.

⸻

♿ Accessibility
	•	role="banner" assigned to <header>.
	•	Search input uses aria-label and focus outlines visible via keyboard.
	•	Theme toggle and language switch buttons have aria-pressed and aria-label.
	•	Skip-to-content anchor available at top of header.
	•	Fully navigable via keyboard shortcuts (/ for focus search, T to toggle theme).

Accessibility tested with axe-core and Lighthouse, scoring ≥ 95.

⸻

🧪 Testing

Test	Purpose	Tool
Search API Mock	Verifies debounce + API request timing.	Jest + MSW
Theme Persistence	Confirms mode persists across reloads.	React Testing Library
Focus Management	Ensures keyboard users can cycle through header elements.	axe-core
Responsive Rendering	Validates layout at all breakpoints.	Cypress E2E

Coverage target: ≥ 90%.

⸻

🧾 Provenance & Integrity

Artifact	Description
Inputs	API search endpoint, context providers (Theme, Accessibility)
Outputs	Top navigation HTML/JSX rendered in AppShell
Dependencies	React, Framer Motion, TailwindCSS, Axios
Integrity	CI validates accessibility, snapshot consistency, and layout integrity


⸻

🔗 Related Documentation
	•	AppShell Component
	•	Web Frontend Components
	•	Context — Theme & Accessibility
	•	Web UI Architecture

⸻

📜 License

Released under the MIT License.
© 2025 Kansas Frontier Matrix — created under the Master Coder Protocol (MCP) for accessible,
documented, and reproducible design.

“The Header is Kansas Frontier Matrix’s compass — orienting users in time, data, and discovery.”

