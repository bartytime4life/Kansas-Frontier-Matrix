import json
from pathlib import Path
from tools.soilgrids import soilgrids_notification_delivery as m


def test_rejects_missing_notification_delivery_spec():
    errs = m.validate_notification_delivery_spec({"schema":"NotificationDeliverySpec.v1"})
    assert "notification_delivery_id" in errs and "dataset_id" in errs


def test_rejects_malformed_notification_delivery_spec():
    errs = m.validate_notification_delivery_spec({"schema":"NotificationDeliverySpec.v1","notification_delivery_id":"x","dataset_id":"d","delivery":{"ack_deadline_hours":"bad"}})
    assert "ack_deadline_hours" in errs


def test_rejects_unsupported_schema():
    assert "schema" in m.validate_notification_delivery_spec({"schema":"Other","notification_delivery_id":"x","dataset_id":"d"})


def test_notification_spec_hash_stable():
    s={"schema":"NotificationDeliverySpec.v1","notification_delivery_id":"n","dataset_id":"d"}
    assert m.compute_notification_spec_hash(s)==m.compute_notification_spec_hash(dict(s))


def test_notification_policy_hash_stable():
    p=m.load_notification_delivery_policy(None)
    assert m.compute_notification_policy_hash(p)==m.compute_notification_policy_hash(dict(p))


def test_rejects_external_delivery_enabled_by_default():
    errs=m.validate_notification_delivery_spec({"schema":"NotificationDeliverySpec.v1","notification_delivery_id":"x","dataset_id":"d","delivery":{"external_delivery_enabled":True}})
    assert "external_delivery_enabled_forbidden" in errs


def test_rejects_unknown_channel():
    errs=m.validate_notification_delivery_spec({"schema":"NotificationDeliverySpec.v1","notification_delivery_id":"x","dataset_id":"d","delivery":{"allowed_channels":["fax"]}})
    assert any(e.startswith("unknown_channel") for e in errs)


def test_builds_notification_outbox(tmp_path):
    spec={"schema":"NotificationDeliverySpec.v1","notification_delivery_id":"n","dataset_id":"d","delivery":{"ack_deadline_hours":72},"exports":{"write_cloudevents":True}}
    plan={"planned_notifications":[{"notification_id":"a","recipient_type":"consumer","recipient_hash":None,"channel":"local_outbox","severity":"high","ack_required":True,"source_packet_schema":"ConsumerNotificationPacket.v1"}]}
    outbox=m.build_notification_outbox(spec,plan,tmp_path)
    assert outbox["schema"]=="NotificationOutbox.v1"


def test_builds_notification_envelope():
    spec={"notification_delivery_id":"n"}
    env=m.build_notification_envelope(spec,{"notification_id":"a","recipient_type":"consumer","recipient_hash":None,"channel":"local_outbox","severity":"high","ack_required":True,"source_packet_schema":"ConsumerNotificationPacket.v1"})
    assert env["schema"]=="NotificationEnvelope.v1"


def test_cloudevents_envelope_has_required_fields():
    spec={"exports":{"write_cloudevents":True},"recipients":{"redact_subjects":True}}
    ce=m.build_cloudevents_envelope_if_requested(spec,{"notification_id":"a","notification_hash":"h","severity":"high","ack_required":True,"subject":"x"})
    for k in ["specversion","type","source","id","time","datacontenttype","data"]:
        assert k in ce


def test_deliver_local_writes_attempt_and_receipt(tmp_path):
    st=tmp_path
    (st/"outbox/envelopes").mkdir(parents=True)
    env={"schema":"NotificationEnvelope.v1","notification_id":"a","ack_deadline_utc":None}
    (st/"outbox/envelopes/a.json").write_text(json.dumps(env),encoding="utf-8")
    out={"notifications":[{"notification_id":"a","envelope_path":"outbox/envelopes/a.json","ack_required":False}]}
    rs=m.deliver_local_outbox(st,out)
    assert rs and rs[0]["schema"]=="DeliveryReceipt.v1"
