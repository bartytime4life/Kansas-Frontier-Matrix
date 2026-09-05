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
outcomes. The public-context adapter also rejects unparsed or ambiguous time
strings instead of reclassifying them as uncertain history. Explicit numeric
offsets are normalized to UTC for comparison while their raw value and source
offset remain available for labels and provenance. A withheld layer carries no
actual timestamp or evidence reference.
