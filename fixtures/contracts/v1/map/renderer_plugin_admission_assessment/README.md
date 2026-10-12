# Renderer plugin admission assessment fixtures

These fixtures exercise a synthetic plugin declaration only. They do not name a real admitted package, query a registry, download bytes, install or import code, mutate a lockfile, evaluate policy, approve review, or boot a renderer.

Run:

```bash
python tools/validators/map/validate_renderer_plugin_admission_assessment.py --fixtures
```

The manifest binds every case to an exact expected `PASS`, `ABSTAIN`, `DENY`, or `ERROR` polarity and value-free finding set.
