# DependencyOriginPolicy fixtures

Synthetic no-network cases for the proposed static dependency-origin guard.

The suite covers:

- an accepted pnpm/Python declaration;
- a package-manager pin mismatch;
- a surfaced alternative lockfile;
- an internal `@kfm/` package escaping workspace/link resolution;
- a direct npm URL dependency;
- a lock entry without integrity;
- an unexpected remote registry host;
- a Python direct URL reference.

Fixtures do not contact registries, install packages, reserve names, verify publishers, or create release authority.
