"""Replay and effect invariants for ReplaySafeEffectLedgerCandidate."""
from __future__ import annotations

from collections import Counter
from collections.abc import Mapping

from tools.validators.runtime.replay_safe_effect_ledger_core import (
    CanonicalizationFailure,
    Finding,
    compute_spec_hash,
    effect_projection,
    event_projection,
    mapping,
    records,
    strings,
    timestamp,
)


def semantic_findings(candidate: Mapping[str, object]) -> set[Finding]:
    found: set[Finding] = set()

    def add(code: str, path: str) -> None:
        found.add(Finding(code, path))

    event, effect = mapping(candidate["event"]), mapping(candidate["effect_intent"])
    reservation, result = mapping(candidate["reservation"]), mapping(candidate["result"])
    deliveries, entries = records(candidate["deliveries"]), records(candidate["ledger_entries"])

    try:
        event_digest = compute_spec_hash(event_projection(event))
        if event.get("event_id") != "kfm:event:" + event_digest:
            add("EVENT_ID_MISMATCH", "/event/event_id")
        effect_digest = compute_spec_hash(effect_projection(event, effect))
        if effect.get("effect_key") != effect_digest:
            add("EFFECT_KEY_MISMATCH", "/effect_intent/effect_key")
        if effect.get("intent_id") != "kfm:effect-intent:" + effect_digest:
            add("INTENT_ID_MISMATCH", "/effect_intent/intent_id")
        identity = {
            key: value
            for key, value in candidate.items()
            if key not in {"ledger_id", "spec_hash"}
        }
        digest = compute_spec_hash(identity)
        ledger_id = (
            "kfm://runtime/replay-safe-effect-ledger/"
            + digest.removeprefix("sha256:")[:24]
        )
        if candidate.get("spec_hash") != digest:
            add("SPEC_HASH_MISMATCH", "/spec_hash")
        if candidate.get("ledger_id") != ledger_id:
            add("LEDGER_ID_MISMATCH", "/ledger_id")
    except (CanonicalizationFailure, KeyError, TypeError, ValueError):
        add("IDENTITY_EVALUATION_ERROR", "/")

    delivery_ids = [str(item.get("delivery_id", "")) for item in deliveries]
    by_delivery = dict(zip(delivery_ids, deliveries, strict=True))
    if len(set(delivery_ids)) != len(delivery_ids):
        add("DELIVERY_ID_DUPLICATE", "/deliveries")
    if [item.get("attempt") for item in deliveries] != list(
        range(1, len(deliveries) + 1)
    ):
        add("DELIVERY_ATTEMPT_ORDER_INVALID", "/deliveries")
    for index, delivery in enumerate(deliveries):
        predecessor = None if index == 0 else delivery_ids[index - 1]
        if delivery.get("predecessor_delivery_ref") != predecessor:
            add(
                "DELIVERY_PREDECESSOR_INVALID",
                f"/deliveries/{index}/predecessor_delivery_ref",
            )

    occurred = timestamp(event.get("occurred_at"))
    requested = timestamp(effect.get("requested_at"))
    delivery_times = [timestamp(item.get("received_at")) for item in deliveries]
    comparable_delivery_times = [item for item in delivery_times if item]
    if occurred and any(item < occurred for item in comparable_delivery_times):
        add("DELIVERY_TIME_INVALID", "/deliveries")
    if comparable_delivery_times != sorted(comparable_delivery_times):
        add("DELIVERY_TIME_ORDER_INVALID", "/deliveries")
    if occurred and requested and requested < occurred:
        add("INTENT_TIME_INVALID", "/effect_intent/requested_at")
    if comparable_delivery_times and requested and requested < comparable_delivery_times[0]:
        add("INTENT_TIME_INVALID", "/effect_intent/requested_at")

    entry_times = [timestamp(item.get("recorded_at")) for item in entries]
    comparable_entry_times = [item for item in entry_times if item]
    if comparable_entry_times != sorted(comparable_entry_times):
        add("LEDGER_TIME_ORDER_INVALID", "/ledger_entries")
    expected_ids = [f"ledger-entry:{number:04d}" for number in range(1, len(entries) + 1)]
    if [str(item.get("entry_id", "")) for item in entries] != expected_ids:
        add("LEDGER_ENTRY_ORDER_INVALID", "/ledger_entries")
    for index, entry in enumerate(entries):
        delivery = by_delivery.get(str(entry.get("delivery_ref", "")))
        if delivery is None:
            add("LEDGER_DELIVERY_REF_UNBOUND", f"/ledger_entries/{index}/delivery_ref")
        else:
            entry_time = timestamp(entry.get("recorded_at"))
            delivery_time = timestamp(delivery.get("received_at"))
            if entry_time and delivery_time and entry_time < delivery_time:
                add("LEDGER_ENTRY_BEFORE_DELIVERY", f"/ledger_entries/{index}/recorded_at")
        reasons = strings(entry.get("reason_codes"))
        if reasons != sorted(reasons):
            add("REASON_CODE_ORDER_INVALID", f"/ledger_entries/{index}/reason_codes")
    result_reasons = strings(result.get("reason_codes"))
    if result_reasons != sorted(result_reasons):
        add("REASON_CODE_ORDER_INVALID", "/result/reason_codes")

    states = [str(item.get("state", "")) for item in entries]
    completed_indexes = [i for i, state in enumerate(states) if state == "COMPLETED"]
    compensated_indexes = [i for i, state in enumerate(states) if state == "COMPENSATED"]
    released_indexes = [i for i, state in enumerate(states) if state == "RELEASED"]
    completed = len(completed_indexes)
    duplicates = Counter(
        str(item.get("delivery_id", ""))
        for item in deliveries
        if item.get("outcome") == "DUPLICATE"
    )
    suppressions = Counter(
        str(item.get("delivery_ref", ""))
        for item in entries
        if item.get("state") == "DUPLICATE_SUPPRESSED"
    )
    duplicate_count = sum(duplicates.values())
    if compensated_indexes:
        expected_outcome = "COMPENSATED"
    elif completed == 1 and duplicate_count:
        expected_outcome = "DUPLICATE_SUPPRESSED"
    elif completed == 1:
        expected_outcome = "EXECUTED_ONCE"
    elif "FAILED" in states:
        expected_outcome = "FAILED"
    else:
        expected_outcome = None
    if completed > 1:
        add("EFFECT_EXECUTED_MORE_THAN_ONCE", "/ledger_entries")
    if result.get("completed_effect_count") != min(completed, 1):
        add("COMPLETED_EFFECT_COUNT_MISMATCH", "/result/completed_effect_count")
    if result.get("duplicate_delivery_count") != duplicate_count:
        add("DUPLICATE_DELIVERY_COUNT_MISMATCH", "/result/duplicate_delivery_count")
    if duplicates != suppressions:
        add("DUPLICATE_SUPPRESSION_INCOMPLETE", "/ledger_entries")
    if expected_outcome is None or result.get("outcome") != expected_outcome:
        add("RESULT_OUTCOME_MISMATCH", "/result/outcome")

    if compensated_indexes:
        if completed != 1:
            add("COMPENSATION_WITHOUT_COMPLETION", "/ledger_entries")
        elif not (
            len(compensated_indexes) == 1
            and completed_indexes[0] < compensated_indexes[0]
            and any(index > compensated_indexes[0] for index in released_indexes)
        ):
            add("COMPENSATION_SEQUENCE_INVALID", "/ledger_entries")

    reservation_states = [
        state for state in states if state in {"RESERVED", "COMPLETED", "RELEASED"}
    ]
    ledger_state = reservation_states[-1] if reservation_states else "NONE"
    if reservation.get("state") != ledger_state:
        add("RESERVATION_STATE_MISMATCH", "/reservation/state")
    reserved_entries = [item for item in entries if item.get("state") == "RESERVED"]
    completed_entries = [item for item in entries if item.get("state") == "COMPLETED"]
    released_entries = [item for item in entries if item.get("state") == "RELEASED"]
    token_fields = [
        reservation.get(key)
        for key in ("reservation_token_digest", "reserved_by", "reserved_at")
    ]
    if reservation.get("state") == "NONE":
        if any(value is not None for value in token_fields):
            add("RESERVATION_FIELDS_INCOHERENT", "/reservation")
    elif any(value is None for value in token_fields):
        add("RESERVATION_FIELDS_INCOHERENT", "/reservation")
    ledger_bad = ledger_state == "NONE" and bool(
        reserved_entries or completed_entries or released_entries
    )
    if ledger_state != "NONE":
        ledger_bad |= len(reserved_entries) != 1 or completed > 1
        ledger_bad |= ledger_state == "RELEASED" and len(released_entries) != 1
        ledger_bad |= ledger_state != "RELEASED" and bool(released_entries)
    if ledger_bad:
        add("RESET•USÓ—ÓQÑT—ÒSÓÓTUH‹‹Ü™\Ù\˜][ÛˆŠBˆ™\Ù\™YØ]H[Y\İ[\
™\Ù\˜][Û‹™Ù]
œ™\Ù\™YØ]ŠJBˆÛÛ\]YØ]H[Y\İ[\
™\Ù\˜][Û‹™Ù]
™Y™™XİØÛÛ\]YØ]ŠJBˆ[YWØ˜YH˜[ÙBˆYˆ™\Ù\™YÙ[šY\È[™™\Ù\™YØ]‚ˆ[YWØ˜YH[Y\İ[\
™\Ù\™YÙ[šY\ÖÌK™Ù]
œ™XÛÜ™YØ]ŠJHOH™\Ù\™YØ]ˆ[YWØ˜YH›ÛÛ
™\]Y\İY[™™\Ù\™YØ]™\]Y\İY
BˆYˆÛÛ\]YOHN‚ˆYˆÛÛ\]YØ]\È›Û™N‚ˆY
ÓÓTUSÓ—ÕSQWÓRTÔÒS‘È‹‹Ü™\Ù\˜][Û‹ÙY™™XİØÛÛ\]YØ]ŠBˆ[ÙN‚ˆ[YWØ˜YH[Y\İ[\
ÛÛ\]YÙ[šY\ÖÌK™Ù]
œ™XÛÜ™YØ]ŠJHOHÛÛ\]YØ]ˆ[YWØ˜YH›ÛÛ
™\Ù\™YØ][™ÛÛ\]YØ]™\Ù\™YØ]
Bˆ[YˆÛÛ\]YØ]\È›İ›Û™N‚ˆY
ÓÓTUSÓ—ÕSQWÕS‘VPÕQ‹‹Ü™\Ù\˜][Û‹ÙY™™XİØÛÛ\]YØ]ŠBˆYˆ[YWØ˜Y‚ˆY
”‘TÑT•USÓ—ÕSQWÒS•SQ‹‹Ü™\Ù\˜][ÛˆŠBˆYˆ^XİYÛİ]ÛÛYHOHÓÓTS”ĞUQˆ[™YÙ\—Üİ]HOH”‘SPTÑQ‚ˆY
”‘TÑT•USÓ—ÔÕUWÓRTÓPUÒ‹‹Ü™\Ù\˜][Û‹Üİ]HŠBˆ™]\›ˆ›İ[™