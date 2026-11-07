"""Mount the established Working Data and immutable Library desks in Studio."""
from pathlib import Path
import re
from urllib.parse import urlsplit

from tools.local_data import intake, intake_service

APP = Path(__file__).resolve().parent
DESK = APP.parent / "intake_desk"
VIEWS = {"working": ("/working-data", "Working Data", "working-nav"),
         "library": ("/library", "Data Library", "library-nav")}


class Workspace:
    def __init__(self, store, port, token):
        self.store = store
        self.desks = {}
        if store.kfm_root:
            root = intake.resolve_root(str(store.kfm_root))
            inbox = store.inbox.expanduser().resolve() if store.inbox else None
            if inbox is not None and (not inbox.is_dir() or inbox == root or root in inbox.parents or inbox in root.parents):
                raise ValueError("INBOX_MUST_BE_SEPARATE_FROM_STORE")
            self.desks["working"] = intake_service.Desk(root, inbox=inbox,
                raster_python=store.raster_python, max_files=intake.MAX_CONFIGURED_FILES)
        if store.library_root:
            root = intake.resolve_root(str(store.library_root))
            archive = intake.external_root(str(store.archive_root)) if store.archive_root else None
            if archive is not None and not archive.is_dir():
                raise ValueError("ARCHIVE_ROOT_MISSING")
            self.desks["library"] = intake_service.Desk(root, catalog_only=True, archive_root=archive)
        self.handlers = {}
        for name, desk in self.desks.items():
            desk.token = token
            self.handlers[name] = intake_service.handler(desk, port=port)

    def dispatch(self, request, method):
        parsed = urlsplit(request.path)
        match = re.fullmatch(r"/api/workspace/(working|library)(/.*)", parsed.path)
        if not match:
            return request.respond(404, {"error": "WORKSPACE_ROUTE_NOT_FOUND"})
        if not request.guard(header="X-KFM-Session"):
            return
        name, suffix = match.groups()
        if name not in self.handlers:
            return request.respond(503, {"error": "WORKSPACE_NOT_CONFIGURED"})
        if method == "POST" and suffix != "/cancel":
            try:
                self.store.check_volume()
            except RuntimeError as error:
                return request.respond(409, {"error": str(error)})
        # Dispatch directly to the existing HTTP handler, with the same request
        # streams and capability. No extra socket, public CORS route or iframe.
        handler = self.handlers[name]
        delegated = handler.__new__(handler)
        delegated.__dict__.update(request.__dict__)
        delegated.path = "/api" + suffix + ("?" + parsed.query if parsed.query else "")
        getattr(delegated, "do_" + method)()
        request.close_connection = delegated.close_connection


def page(name):
    _, title, active = VIEWS[name]
    studio = (APP / "local-web/index.html").read_text()
    sidebar = re.search(r'<aside class="sidebar">.*?</aside>', studio, re.S).group()
    sidebar = sidebar.replace('<span id="count">0</span>', '')
    sidebar = sidebar.replace('nav-item active', 'nav-item').replace(' aria-current="page"', '')
    sidebar = re.sub(r'<a\b[^>]*id="' + active + r'"[^>]*>',
                     lambda m: m[0].replace('class="nav-item"', 'class="nav-item active" aria-current="page"'), sidebar)
    sidebar = sidebar.replace('Connecting to local storage…', 'Private files and catalogs on this PC')
    desk = (DESK / "index.html").read_text().split('<body>', 1)[1].rsplit('</body>', 1)[0]
    desk = desk.replace('<main>', '<div class="desk-content">').replace('</main>', '</div>')
    desk = desk.replace('src="/desk.js"', 'src="/workspace/desk.js"').replace('src="/reviews.js"', 'src="/workspace/reviews.js"')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light"><title>KFM · {title}</title>
<link rel="stylesheet" href="/style.css"><link rel="stylesheet" href="/workspace/desk.css"></head>
<body data-kfm-workspace="{name}"><a class="skip" href="#data-main">Skip to workspace</a>{sidebar}
<main id="data-main" class="data-main"><header class="topbar"><span>WORKSPACE / {title.upper()}</span>
<span class="local-badge" id="workspace-connection">Connecting locally…</span></header>
<div class="data-workspace">{desk}</div></main></body></html>'''


def asset(path):
    files = {"/workspace/desk.js": ("desk.js", "application/javascript"),
             "/workspace/reviews.js": ("reviews.js", "application/javascript"),
             "/workspace/desk.css": ("desk.css", "text/css")}
    filename, mime = files[path]
    content = (DESK / filename).read_text()
    if filename == "desk.css":
        # Scope the mature desk styles so the shared Studio sidebar keeps its
        # layout. The desk's own main is a div inside the shared page main.
        content = re.sub(r"\bbody\b", ":scope", content.replace(":root", ":scope"))
        content = re.sub(r"\bmain\b", ".desk-content", content)
        content = "@scope (.data-workspace) {\n" + content + '''
:scope { --bg:#f5f4ec; --panel:#fffef9; --ink:#19392f; --muted:#5b6a60;
  --line:#d6dbcf; --accent:#173d32; --ok:#2f6f4e; --warn:#9a6512; --bad:#963c2d; }
.bar { padding:24px 0 18px; background:transparent; }
.brand { letter-spacing:normal; font-size:14px; align-items:flex-start; gap:6px; flex:1; min-width:280px; }
.brand strong { font-family:Georgia,serif; font-size:28px; font-weight:normal; }
.toggle { white-space:nowrap; }
h2, h3 { font-family:system-ui,-apple-system,"Segoe UI",sans-serif; }
.cards { grid-template-columns:repeat(5,minmax(0,1fr)); }
.cards.catalog-cards { grid-template-columns:repeat(4,minmax(0,1fr)); }
.cards .wide { grid-column:1/-1; }
.desk-content { padding:20px 0 40px; }
.workspace { grid-template-columns:minmax(280px,5fr) minmax(320px,7fr); }
.map-panel, .list-panel { min-width:0; }
@media(max-width:1250px) { .workspace { grid-template-columns:1fr; } }
@media(max-width:1000px) { .cards,.cards.catalog-cards { grid-template-columns:repeat(2,minmax(0,1fr)); } }
}
.data-main { max-width:none; }
.data-workspace { min-width:0; }
'''
    return content, mime
