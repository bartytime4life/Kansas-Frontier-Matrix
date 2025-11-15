---
title: "📑 Kansas Frontier Matrix — Markdown Structural & Formatting Rules (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/standards/markdown_rules.md"
version: "v10.4.1"
last_updated: "2025-11-15"
review_cycle: "Annual / Autonomous · FAIR+CARE Council Oversight"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.4.1/sbom.spdx.json"
manifest_ref: "../../releases/v10.4.1/manifest.zip"
telemetry_ref: "../../releases/v10.4.1/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/docs-markdown-rules-v3.json"
governance_ref: "governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v10.4"
status: "Active / Enforced"
doc_kind: "Standard"
intent: "policy"
fair_category: "F1-A1-I1-R1"
care_label: "Public / Low-Risk"
sensitivity_level: "None"
public_exposure_risk: "Low"
indigenous_rights_flag: false
data_steward: "KFM FAIR+CARE Council"
risk_category: "Low"
redaction_required: false
doc_uuid: "urn:kfm:doc:markdown-rules-v10.4.1"
semantic_document_id: "kfm-doc-markdown-rules"
immutability_status: "version-pinned"
---

<div align="center">

# 📑 **Kansas Frontier Matrix — Markdown Structural & Formatting Rules**  
`docs/standards/markdown_rules.md`

**Purpose:**  
Define the mandatory Markdown conventions for all KFM documentation (Diamond⁹ Ω / Crown∞Ω Ultimate Certified),
including **single-box ChatGPT outputs**, **directory layout trees**, and **safe code fences**.  
These rules ensure documentation is **visually consistent**, **GitHub-safe**, **copy-paste reliable**, and **machine
processable** in both the repository and the ChatGPT environment.

</div>

---

## 🧭 Guiding Principles (Unchanged)

- Documentation-first (MCP-DL v6.3).  
- FAIR+CARE aligned.  
- CI-enforced linting and schema validation.  
- GitHub-flavored Markdown only.  
- All docs must be render-safe and copy-paste-safe.

*(Existing sections on front-matter, titles, headings, links, tables, etc. remain valid. The following are **new**
additions and clarifications for KFM-MDP v10.4.1.)*

---

## 📦 Single-Box Output Rules for ChatGPT (KFM-SBO v1)

These rules apply **when ChatGPT generates Markdown files for KFM** (e.g., `web/ARCHITECTURE.md`):

1. **One outer code fence only**

   - ChatGPT MUST wrap the **entire file content** in exactly one outer fenced block:

     - Fence language: `markdown`  
     - Example pattern (no extra text before or after):

       - ` ```markdown`  
       - *(full file content here)*  
       - ` ````

   - There MUST be **no text outside** this outer fence in the response.

2. **No nested triple-backtick fences inside the file**

   - Inside the outer ` ```markdown` fence, you MUST NOT use another triple-backtick fence.  
   - For inner code blocks (e.g., directory trees, shell commands, JSON), you MUST use **alternative fencing**:
     - Either **tilde fences** (`~~~`)  
     - Or **4-space indentation**.

3. **Recommended pattern for inner code blocks**

   - Preferred style inside ChatGPT-generated files:

     - Use `~~~text` for directory trees and ASCII diagrams.  
     - Use `~~~bash`, `~~~json`, `~~~yaml`, etc. as needed for examples.  

   - Example (valid inside the outer ` ```markdown` fence):

     ~~~text
     web/
     ├── README.md
     └── src/
         └── main.tsx
     ~~~

4. **No badge images required**

   - To reduce header fragility, headers **do not require badges**.  
   - If badges are desired in the repo, they may be added manually after paste-in; ChatGPT is **not required**
     to emit shields.io images in architecture docs.

---

## 📁 Directory Layout & Tree Blocks (New Clarifications)

To guarantee consistent, readable directory layouts (and avoid the “ugly, misaligned tree” problem), all **directory
trees** MUST follow these rules:

1. **Always use a fenced `text` block for trees**

   - In repository files (once pasted in), directory trees MUST be wrapped in a fenced code block.  
   - When emitted by ChatGPT, the tree MUST be inside a tilde fence (`~~~text`) to avoid breaking the outer
     ` ```markdown` box:

     ~~~text
     web/                               # KFM web client root
     ├── README.md                      # High-level web overview
     ├── ARCHITECTURE.md                # Web architecture document
     ├── package.json                   # Dependencies and npm scripts
     └── src/                           # React/TypeScript SPA source
         ├── main.tsx                   # SPA bootstrap
         └── components/                # UI building blocks
     ~~~

2. **ASCII tree style**

   - Use only these Unicode characters for tree lines:
     - `├──`, `└──`, `│`, `─`  
   - No mixed drawing characters, no random arrows or emojis in the tree.

3. **Comment alignment rules**

   - Use **two or more spaces** between the path and the comment `#`.  
   - Try to vertically align comments for readability, but alignment does not need to be pixel-perfect across all
     rows.  
   - The **primary requirement** is that comments are clearly separated from paths with whitespace.

4. **Left alignment**

   - The directory root (`web/`, `src/`, etc.) begins at the **first column**.  
   - Child entries are indented with **4 spaces** per level (as in the example above).  
   - Do NOT mix tabs and spaces.

5. **No inline lists for trees**

   - Do not represent directory layouts as Markdown bullet lists.  
   - Use **only** the ASCII tree style inside a fenced block.

---

## 🧱 Internal Code & Example Blocks (Revised)

1. **Inner code block fencing**

   - Inside ChatGPT responses:
     - Use `~~~` fences, not triple-backtick fences, for any inner code block.  
     - This prevents the outer ` ```markdown` response from being prematurely closed.

   - In repository Markdown files (after paste), maintain whichever fence style is more idiomatic:
     - Triple-backticks or tildes are both acceptable, as long as they are consistent.

2. **Language annotations**

   - Files or snippets should be tagged appropriately:
     - `~~~text` for directory trees and plain ASCII diagrams.  
     - `~~~bash` or `~~~shell` for shell examples.  
     - `~~~json`, `~~~yaml`, `~~~mermaid` as relevant.  

3. **No unnecessary HTML wrappers for code**

   - Do not wrap code blocks in `<pre>`/`<code>` HTML manually.  
   - Let Markdown fences handle block semantics.

---

## 🤖 ChatGPT-Specific Implementation Notes (KFM-MDP v10.4.1)

To ensure **repeatable, good-looking output** that satisfies the “one GitHub-safe box” requirement:

1. **Response template for any KFM file**

   - ChatGPT MUST follow this outer pattern:

     - Literal line: ` ```markdown`  
     - YAML front-matter (if required)  
     - Body of the Markdown file  
     - Literal line: ` ````

2. **When including directory trees**

   - Use the `~~~text` fenced style inside the body, as shown above.  
   - Never use triple-backtick fences for those inner code blocks in a ChatGPT response.

3. **When updating architecture docs (`ARCHITECTURE.md`, etc.)**

   - Always:
     - Include front-matter that matches the current standard (FM-1 or FM-2 per user direction).  
     - Use a single centered header block (`<div align="center">` … `</div>`).  
     - Place the directory tree section **in one fenced `text` block**.  
     - Avoid badges unless explicitly requested.

4. **When user asks to “rebuild the whole file”**

   - Re-emit the entire file in a single ` ```markdown` fence.  
   - Never send partial content in multiple separate boxes.  
   - All examples must obey the nested-fence rule (inner `~~~`, outer ```markdown).

---

## 🕰 Version History (Markdown Rules)

| Version  | Date       | Summary                                                                                       |
|----------|------------|-----------------------------------------------------------------------------------------------|
| v10.4.1  | 2025-11-15 | Added single-box ChatGPT output rules, safe nested fences, and directory tree formatting spec |
| v10.4.0  | 2025-11-14 | Initial v10.4 release of Markdown Structural & Formatting Rules                               |

---