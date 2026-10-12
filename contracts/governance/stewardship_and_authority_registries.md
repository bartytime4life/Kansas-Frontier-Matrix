# Stewardship and authority registries

The stewardship registry makes missing accountable roles explicit instead of
leaving `OWNER_TBD` text scattered across domain documents. An `UNASSIGNED` or
`HELD` record grants no authority and must not be treated as an implicit owner.

The authority index distinguishes implementation authority from coordination,
historical reference, and runtime observation. The only implementation
authority in the initial index is the reviewed GitHub repository. Drive and
Site records may be current coordination or runtime references, but their
currentness pointers resolve back to GitHub.

Validate both registries with:

```bash
python tools/validators/governance/validate_governance_registries.py all
```

The registries do not assign merge, source-admission, release, deployment,
publication, or host-control authority. Those remain separate governed
decisions.
