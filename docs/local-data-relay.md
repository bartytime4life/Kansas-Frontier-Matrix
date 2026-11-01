# Local SQL data relay — phase 1, Storm Events

The owner decided on 2026-11-01 that pipeline data stays on the pipeline PC (dev)
and that the hosting SQL database is not used for it. This relay lets the public
site answer fixed, read-only questions from the PC's local SQL database without
copying the database to hosting and without any inbound route to the PC.

Phase 1 carries one dataset: Kansas Storm Events (NOAA NCEI, 1950–2026, 94,007
rows) from `observations.sqlite` on the PC's data disk.

## How it works

```
visitor ──GET /api/local-data/storm-events──▶ site (cache, 15 min fresh / 7 days stale)
                                               │ in-memory queue, signed with the gateway key
PC worker ──POST /api/local-data-worker/v1/lease (long poll, worker key)──▶ site
PC worker ──▶ 127.0.0.1:8788 gateway (verifies request, reads SQLite read-only, signs reply)
PC worker ──POST /api/local-data-worker/v1/result──▶ site (verifies the gateway signature)
```

- It is the same outbound-only relay as home inference (`server/home-relay.mjs`),
  run as a second, separate instance with its own routes, keys, limits and
  global (`Symbol.for('kfm.local-data')`). Neither relay can carry the other's
  routes, and neither worker key is accepted by the other relay.
- The worker holds no gateway key. It cannot create, change or replay a request
  or a reply; the site checks the gateway's signature over the exact request,
  status and bytes before parsing anything.
- The gateway listens on loopback only and opens the database with
  `readOnly: true` for each question. It answers only `GET /v1/health` and
  `POST /v1/data/storm-events`.
- If the worker has not polled for 30 s the PC is treated as away: a visitor gets
  the last cached answer marked `"cache":{"state":"stale"}`, or
  `503 {"state":"local-data-offline"}`. A job handed to a poll whose connection
  had already died still waits out its 15 s lease once.

## Public API

`GET /api/local-data/storm-events?county=&from=&to=&type=&limit=&offset=`

| Parameter | Accepted | Default |
|---|---|---|
| `county` | 1–3 digit county FIPS (counties only) or a county/zone name | all |
| `from`, `to` | `YYYY-MM-DD`, 1950–2100 | 1950-01-01, 2100-12-31 |
| `type` | NCEI event type, e.g. `Tornado`, `Hail` | all |
| `limit` | 1–200 | 50 |
| `offset` | 0–50,000 | 0 |

Anything else is `400 QUERY_INVALID`. Events are newest first. The answer carries
`total`, `count`, `events`, `source` (provider, URL, coverage, notes), `generatedAt`
and `cache` (`live`, `fresh` or `stale`, with its time).

**Publication allow-list (phase 1, needs owner approval before Live):** each event's
NCEI identifiers, type, county/zone, office, begin/end date and time with time
zone, direct/indirect injuries and deaths, property/crop damage strings as
published, magnitude, flood cause, category, tornado scale/length/width, begin/end
location and coordinates, source, the episode and event narratives, and the data
source. The fatalities table (age, sex, location of each death) is not exposed.

## Site settings

Off unless all are set. `KFM_LOCAL_DATA_ORIGIN` must be one of the controlled
hosting origins in `server/hosted-ai-origins.mjs`; Live is
`https://kansasfrontiermatrix.com` (`www` redirects there, so a worker polling
`www` would never connect).

| Variable | Value |
|---|---|
| `KFM_LOCAL_DATA` | `1` |
| `KFM_LOCAL_DATA_ORIGIN` | exact origin the worker polls |
| `KFM_LOCAL_DATA_GATEWAY_KEY_ID` / `KFM_LOCAL_DATA_GATEWAY_SECRET` | the PC gateway key |
| `KFM_LOCAL_DATA_WORKER_KEY_ID` / `KFM_LOCAL_DATA_WORKER_SECRET` | the PC worker key; must differ |

## PC services (dev)

`pc-pipeline-data/run/install-local-data.sh SOURCE_CHECKOUT [WORKER_SITE]` copies
the eight gateway/worker files into
`pc-pipeline-data/runtime/releases/local-data-<digest>/` with a `release.json`
(source commit, branch, whether the source was uncommitted, file digests), makes
the two owner-only keys once in `pc-pipeline-data/transfer-access/`, writes
`pc-pipeline-data/runtime/local-data.env` and installs two user units:

- `kfm-local-data-gateway.service` — enabled; mounts the data disk first.
- `kfm-local-data-worker.service` — installed but not started by the installer;
  pointing it at Live is a separate owner step.

`node pc-pipeline-data/run/check-local-data.mjs` makes a signed health check and
one sample query against the running gateway and prints only the result.

## Verification — 2026-11-01

- `tests/local-data.test.mjs` (11 tests) with the home-relay and home-inference
  suites: 73/73 pass. The tests cover query validation, the allow-list, gateway
  signing/replay/route refusal, the reply ceiling, configuration, route isolation
  between the two relays, a full relay trip over real loopback HTTP, cache, stale
  and offline answers, and a reply altered in transit.
- Full `npm test` (build and 2,478 tests): 2,454 pass, 24 skipped, 0 fail.
- The gateway service on dev against the real database: health 200 signed,
  94,007 rows; Sedgwick tornadoes 91.
- A local production build (`vinext build`) on 127.0.0.1, behind a stand-in proxy
  that presents requests as `https://kansasfrontiermatrix.com`, with the dev
  worker service polling it:
  - live answers in 0.2–0.3 s;
  - cached answers in 7 ms;
  - a 200-event page of 407 KB passed (the reply ceiling is 1,000,000 bytes);
  - bad queries were refused;
  - the worker route answered 503 on the wrong origin and 401 when unsigned;
  - chat stayed off.

  With the worker stopped, a cached query was still served. A new query got the
  offline answer: 15 s for the first query, then at once. The relay reconnected
  when the worker was started again.

Not yet proven: the long poll through the live hosting proxy and Cloudflare, and
that hosting runs one application process (the relay queue is in memory, as for
home inference).
