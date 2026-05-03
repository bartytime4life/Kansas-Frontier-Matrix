from pathlib import Path
req=["docs","control_plane","contracts","schemas","policy","tests","fixtures","tools","scripts","apps","packages","connectors","pipelines","pipeline_specs","data","release","runtime","infra","configs","migrations","examples"]
missing=[p for p in req if not Path(p).exists()]
print("FAIL" if missing else "PASS", missing)
raise SystemExit(1 if missing else 0)
