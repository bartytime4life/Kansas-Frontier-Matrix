# Mobile map options repair — 2026-10-16

The owner reported unresponsive map options and supplied an iPhone screenshot
showing overlapping header actions. The GoDaddy dashboard was inspected after
owner sign-in: app `q9r9beo47t` uses `a0-crawler-guidance-20261015`; the candidate
starts at `ebe9709c67398ec73c12bfba2ce10efd954db43d`.

The account button follows the brand title, so the old `span:last-child`
selector no longer selects that title. Select the non-mark span explicitly;
keep account and Map/More actions in bounded phone grid columns. At the
narrowest widths the decorative mark yields space to the account action.

Map and More also closed on any blur whose related target was outside the
menu, including a null target. Safari can blur the summary without focusing
a tapped button. Closing at that point can hide the button before click.
Use one header-scoped document pointer/focus listener instead: definite outside
taps or keyboard focus departure close open menus; internal taps leave the
native action alive. Escape and existing action/focus-return handlers remain.
Cleanup removes the listeners on unmount. No timer or polling is introduced.

Regression coverage exercises no-focus pointer/blur/click ordering, outside
tap, keyboard departure, internal focus, listener cleanup and actual Escape
handlers. Existing mobile and workspace navigation tests cover retained drafts
and representation transitions. The change adds these checks to the existing
composition CI workflow. Production build and TypeScript are checked locally.

The cloud browser reports WebGL2 unavailable. Menu/panel interaction checks
there do not establish 3D-renderer or physical iPhone/Safari acceptance. A
synthetic event regression is not a physical-device test. Hosted publication
must be read back separately; no publication is implied by this source note.

Placement reuses existing app/tests/docs/workflow responsibilities. No API,
authentication, data, storage, provider, audience or DNS settings change. The
standalone GoDaddy composition is not the original native Sites application.
Rollback is reverting this focused change and republishing; no migration.
