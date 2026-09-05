# Explorer temporal conformance adapter

This feature mirrors the proposed common TemporalViewState profile for the
Explorer UI. The JSON Schema and Python validator remain the shape and semantic
baseline; this TypeScript module provides browser-safe canonical identity,
bounded temporal normalization, frame-context hygiene, and a generation-guarded
runtime reducer.

The adapter consumes existing public workspace context and governed layer
identities. It does not fetch data, resolve evidence, make policy or release
decisions, expose a model provider, or publish a Site. Requested state is kept
separate from committed frame context so map, chart, legend, table, Evidence
Drawer, report preview, and AI handoff can bind to one future resolver result.

Unknown timezones and geologic-age boundaries return explicit unsupported
outcomes. Raw values remain available for labels and provenance; only
timezone-aware instants are compared as instants. A withheld layer carries no
actual timestamp or evidence reference.
