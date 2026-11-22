# Failed public reads keep their explanation (2026-11-22)

More than forty public data routes answer 502 or 504 when the provider they read from fails, each
with a sentence in the body that says what happened and what was not done, for example "The
exact historical radar frame is unavailable. No latest-image fallback was used."

On the public site that sentence never arrived. The hosting proxy replaces the body of any 502
or 504 with its own plain-text page, `error code: 502`. Pages that read the body as JSON then
failed on the proxy's text and showed a generic error. The live feeds route was moved to 503 for
this reason on 2026-11-15; the other routes were not.

## What changed

`server/browser-headers.mjs` (the delivery layer every response already passes through) now
sends a public read that ends in 502 or 504 as **503**, which the proxy passes through with its
body. The route's own status is kept in a response header:

```
HTTP/1.1 503 Service Unavailable
X-KFM-Upstream-Status: 502
```

- Only `GET` and `HEAD` under `/api/` are touched. Writes and the worker relays keep their exact
  statuses, because the machines on the other end may act on them.
- Body, content type, `Cache-Control` and every other header are unchanged.
- No route was edited. Their unit tests still see the 502 or 504 they return.

## What a page sees

Pages already treat 502, 503 and 504 alike: `app/browser-json-request.ts` retries all three as
transient, and the readers check `response.ok`. The difference is that the body is now the
route's JSON, so the message a route wrote is the one shown.

## Checks

`tests/upstream-failure-status.test.mjs` runs a small server behind the delivery layer and
checks each way Node can write a status (headers object, raw header array, reason phrase, and an
implicit header), that other statuses, writes and pages are untouched, and that a sample of the
routes still carry their explanation.

On the public site before this change:

```
$ curl -s https://kansasfrontiermatrix.com/api/event-atlas/radar-frame
error code: 502
```
