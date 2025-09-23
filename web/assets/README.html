<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Web Assets — Kansas Frontier Matrix / Kansas Geo Timeline</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    :root{
      --bg:#0b0d10; --surface:#12151a; --text:#e8eef5; --muted:#9fb0c6;
      --accent:#69a7ff; --brand:#1c4e80; --border:#1f2630; --code:#0e1116;
    }
    html,body{margin:0;padding:0;background:var(--bg);color:var(--text);font:16px/1.6 system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,"Helvetica Neue",Arial,"Noto Sans",sans-serif}
    main{max-width:900px;margin:40px auto;padding:0 20px}
    h1,h2,h3{line-height:1.25;margin:1.2em 0 .4em}
    h1{font-size:2rem}
    h2{font-size:1.4rem;margin-top:2rem}
    h3{font-size:1.1rem;margin-top:1.4rem}
    p{margin:.7em 0}
    hr{border:0;border-top:1px solid var(--border);margin:2rem 0}
    .blockquote{border-left:4px solid var(--brand);padding:.6rem .9rem;background:rgba(28,78,128,.08);margin:1rem 0}
    code,kbd{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,"Roboto Mono",Consolas,"Liberation Mono","Courier New",monospace}
    pre{background:var(--code);border:1px solid var(--border);border-radius:8px;padding:12px;overflow:auto}
    pre code{color:#dbe7ff}
    ul,ol{padding-left:1.2rem}
    li{margin:.25rem 0}
    .dir{background:var(--surface)}
    .callout{font-weight:600;color:var(--muted)}
    a{color:var(--accent);text-decoration:none}
    a:hover{text-decoration:underline}
    table{width:100%;border-collapse:collapse;margin:1rem 0;background:var(--surface)}
    th,td{border:1px solid var(--border);padding:.6rem .5rem;vertical-align:top}
    th{background:#10141b;font-weight:700}
    .note{color:var(--muted);font-size:.95rem}
    .sep{margin:2rem 0;text-align:center;color:var(--muted)}
    .sep::before{content:"— — —";letter-spacing:.35em}
  </style>
</head>
<body>
<main>
  <h1>Web Assets — Kansas Frontier Matrix / Kansas Geo Timeline</h1>

  <p>This folder contains the <strong>UI/brand assets</strong> used by the lightweight MapLibre web viewer and GitHub Pages site.</p>

  <div class="blockquote">
    <p><strong>Required files (tests expect these to exist):</strong></p>
    <ul>
      <li><code>logo.png</code> — project logo (raster fallback)</li>
      <li><code>favicon.svg</code> — vector favicon for modern browsers <span class="note">(PNG fallbacks are optional; see “Favicons &amp; app icons”)</span></li>
    </ul>
  </div>

  <hr>

  <h2>Folder layout</h2>

  <pre class="dir"><code>web/
├─ app.js
├─ app.css
├─ app.config.json           # optional, rendered from STAC via make site-config
├─ layers.json               # minimal site manifest (written by make site)
└─ assets/
   ├─ logo.png
   ├─ favicon.svg
   ├─ icons/                 # platform icons (generated)
   ├─ palette.json           # design tokens (colors, spacing, radii)
   ├─ typography.json        # (optional) font tokens
   ├─ ui/                    # small UI svgs (buttons, chevrons, etc.)
   └─ screenshots/           # small, compressed demo screenshots
</code></pre>

  <hr>

  <h2>Naming &amp; conventions</h2>
  <ul>
    <li><strong>Lowercase, hyphen-separated</strong> filenames: <code>kansas-frontier-logo.svg</code>, <code>map-pin.svg</code></li>
    <li>Prefer <strong>SVG</strong> for flat graphics/icons, <strong>PNG</strong> for screenshots, <strong>JPEG</strong> for photos.</li>
    <li>Keep raster assets <strong>power-of-two</strong> or <strong>×2</strong> sizes where reasonable for crisp rendering on HiDPI.</li>
    <li><strong>No spaces</strong> in filenames (helps downstream tooling and URLs).</li>
  </ul>

  <hr>

  <h2>Brand tokens (design system)</h2>
  <p>Include a small set of tokens to keep the site consistent and easy to restyle.</p>

  <p><strong><code>palette.json</code> (example)</strong></p>
  <pre><code>{
  "brand": {
    "primary": "#1C4E80",
    "secondary": "#F3A712",
    "accent": "#6BB187"
  },
  "ui": {
    "bg": "#0B0D10",
    "surface": "#12151A",
    "muted": "#8FA3B9",
    "text": "#E8EEF5",
    "link": "#69A7FF",
    "danger": "#E24C4B",
    "warning": "#F2C94C",
    "success": "#2DBE7E"
  },
  "elevation": {
    "dem": "#B9D6F2",
    "hillshade": "#8C8C8C",
    "slope": "#E67E22",
    "aspect": "#1ABC9C"
  },
  "opacity": {
    "overlay": 0.85,
    "muted": 0.6
  },
  "radii": { "sm": 4, "md": 8, "lg": 12 }
}</code></pre>
  <p class="note"><strong>Usage:</strong> <code>app.js</code> can load <code>assets/palette.json</code> at startup to theme controls and legends.</p>

  <div class="sep"></div>

  <h2>Logo specs</h2>
  <p>Keep a master vector (prefer <code>logo.svg</code>) and export PNGs as needed.</p>

  <table>
    <thead>
      <tr><th>Purpose</th><th>File</th><th>Size(s)</th><th>Notes</th></tr>
    </thead>
    <tbody>
      <tr><td>Main logo</td><td><code>logo.png</code></td><td>512×512 (required)</td><td>Transparent background, ≤ 50 KB</td></tr>
      <tr><td>Vector logo</td><td><code>logo.svg</code></td><td>1× (scales)</td><td>Optional but recommended</td></tr>
      <tr><td>Social share</td><td><code>og.png</code></td><td>1200×630</td><td>Optional; Open Graph/Twitter Card</td></tr>
    </tbody>
  </table>

  <h3>Export tips</h3>
  <ul>
    <li>Trim extra transparent padding.</li>
    <li>For PNG: use indexed color when possible, and optimize (see below).</li>
  </ul>

  <div class="sep"></div>

  <h2>Favicons &amp; app icons</h2>
  <p>Place a single source (<code>favicon.svg</code>) and generate a small set of platform icons:</p>
  <ol>
    <li>Generate icons (local or CI) using your tool of choice (e.g., RealFaviconGenerator CLI, <code>sharp</code>, or a small script).</li>
    <li>Save to <code>web/assets/icons/</code>:</li>
  </ol>

  <table>
    <thead>
      <tr><th>File</th><th>Size</th><th>Purpose</th></tr>
    </thead>
    <tbody>
      <tr><td><code>favicon.svg</code></td><td>vector</td><td>Modern browsers (required)</td></tr>
      <tr><td><code>favicon-32.png</code> / <code>favicon-16.png</code></td><td>32/16 px</td><td>Legacy fallback</td></tr>
      <tr><td><code>apple-touch-icon.png</code></td><td>180×180</td><td>iOS home screen</td></tr>
      <tr><td><code>android-chrome-192x192.png</code></td><td>192×192</td><td>Android</td></tr>
      <tr><td><code>android-chrome-512x512.png</code></td><td>512×512</td><td>Android / PWA</td></tr>
      <tr><td><code>site.webmanifest</code></td><td>—</td><td>Optional PWA manifest</td></tr>
    </tbody>
  </table>

  <p class="note">If you don’t use a PWA, <code>site.webmanifest</code> is optional. Keep the SVG + a 32 px PNG fallback.</p>

  <div class="sep"></div>

  <h2>Optimization (keep the repo lean)</h2>
  <ul>
    <li><strong>SVG:</strong> run <code>svgo</code> (remove metadata, collapse groups).</li>
    <li><strong>PNG:</strong> run <code>oxipng -o 4 --strip all</code> or <code>pngquant --quality=70-85</code>.</li>
    <li><strong>JPEG:</strong> <code>mozjpeg -quality 78</code> or <code>cjpeg -quality 78 -optimize</code>.</li>
    <li>Aim for <strong>≤100 KB</strong> per asset; screenshots <strong>≤250 KB</strong>.</li>
  </ul>
  <p class="note">Large geospatial data (DEM/COGs) lives in <code>data/</code> and is already handled by Makefile + (optionally) Git LFS. Do <strong>not</strong> place heavy images here.</p>

  <div class="sep"></div>

  <h2>How the site uses these files</h2>
  <ul>
    <li><code>logo.png</code> + <code>favicon.svg</code> are referenced by <code>index.html</code>/<code>app.css</code> and used by tests.</li>
    <li><code>palette.json</code> (optional) can be fetched by <code>app.js</code> to style UI widgets.</li>
    <li>Icons in <code>assets/icons/</code> are linked in <code>&lt;head&gt;</code> tags when present.</li>
  </ul>

  <p>If you change file names, <strong>update references</strong> in:</p>
  <ul>
    <li><code>web/index.html</code> (or your template)</li>
    <li><code>web/app.css</code></li>
    <li><code>tests/test_sources.py</code> (if paths are asserted)</li>
  </ul>

  <div class="sep"></div>

  <h2>Quick checks (before commit)</h2>
  <ul>
    <li><code>logo.png</code> present, ≤50 KB, transparent, crisp on dark BG</li>
    <li><code>favicon.svg</code> loads in browser (no external fonts or <code>&lt;script&gt;</code>)</li>
    <li>Icons (PNGs) optimized (if added)</li>
    <li><code>palette.json</code> validates as JSON (no trailing commas)</li>
    <li>No unintended large binaries added here</li>
  </ul>

  <div class="sep"></div>

  <h2>Licensing &amp; attribution</h2>
  <ul>
    <li>Ensure any third-party icons/images are <strong>open-licensed</strong> (CC-BY/CC-0) and attributed in <code>CREDITS.md</code> (root or here).</li>
    <li>Your <strong>project logo</strong> should be clearly licensed under MIT repo terms or a separate notice.</li>
  </ul>

  <div class="sep"></div>

  <h2>Future niceties</h2>
  <ul>
    <li>Auto-generate favicons in CI (<code>npm run build:icons</code> or a small Python script).</li>
    <li>A tiny “legend” SVG based on <code>palette.json</code> that renders slope/aspect swatches.</li>
    <li>An <code>assets-manifest.json</code> (hash → path) if you add cache-busting later.</li>
  </ul>

  <div class="sep"></div>

  <h2>TL;DR</h2>
  <ul>
    <li>Keep <code>logo.png</code> and <code>favicon.svg</code> here.</li>
    <li>Optimize everything.</li>
    <li>Use <code>palette.json</code> to drive consistent UI colors.</li>
  </ul>

</main>
</body>
</html>
