# Archaeology public-safe — invalid fixtures

`fixtures/domains/archaeology-public-safe/invalid/`

Status: draft / fixture lane, first payloads added per the parent README's
[Expected layout](../README.md#expected-layout).

Safe negative examples only. Each case is expected to fail a bounded check
(schema, no-leak helper, or release precheck) and is paired with an expected
error/reason. None of these files contain real or reverse-engineerable
archaeological content.

| File pair | Scenario | Expected outcome |
|---|---|---|
| `exact_location_request.input.json` / `.expected.json` | A request asks for exact-precision geometry on a candidate feature. | `DENY` — reason code only, no coordinates echoed. |
| `missing_review_record.json` / `.expected_error.txt` | A release-precheck payload is missing its required `review_ref`. | `ERROR` — release precheck fails closed on the missing field. |

Shared posture:

- Every "invalid" file is synthetic and safe to store; it must never contain the sensitive content the check is designed to reject.
- A passing negative test proves only that the declared failure/denial was detected for this fixture — not that any archaeology claim, cultural review, or release decision was made.

See also: [`../README.md`](../README.md) · [`../valid/README.md`](../valid/README.md)
