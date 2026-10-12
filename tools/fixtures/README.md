# Isolated fixture regeneration

`regenerate.py` owns deterministic synthetic water fixture regeneration.
Its input/output digests are declared in the existing readiness control plane.
Run with the water-pilot Python environment; default output is a temporary
external directory. A supplied output directory must be empty and outside the
checkout. No network, approvals or reviewed-fixture overwrites occur. Other
fixture families remain outside this bounded profile and on their existing hold.
