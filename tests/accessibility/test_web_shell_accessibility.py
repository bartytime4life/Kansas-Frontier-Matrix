from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def _read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def test_shell_frame_exposes_landmarks_and_skip_link() -> None:
    shell_frame = _read("apps/web/src/shell/shell-frame.js")

    assert 'href="#workspace-start"' in shell_frame
    assert 'aria-label="Primary"' in shell_frame
    assert 'aria-label="Map and trust workspace"' in shell_frame


def test_evidence_and_focus_panels_expose_announced_runtime_state() -> None:
    evidence_drawer = _read("apps/web/src/evidence/evidence-drawer.js")
    focus_panel = _read("apps/web/src/focus/focus-panel.js")

    assert 'setAttribute("aria-labelledby", "evidence-drawer-heading")' in evidence_drawer
    assert 'id="evidence-drawer-status" role="status" aria-live="polite"' in evidence_drawer

    assert 'setAttribute("aria-labelledby", "focus-panel-heading")' in focus_panel
    assert 'role="status" aria-live="polite"' in focus_panel


def test_map_surface_has_non_visual_descriptor_and_reduced_motion_hook() -> None:
    map_pane = _read("apps/web/src/map/map-pane.js")
    styles = _read("apps/web/src/styles/app.css")

    assert 'role="img"' in map_pane
    assert 'aria-label="Map preview placeholder for released layers"' in map_pane
    assert "@media (prefers-reduced-motion: reduce)" in styles
