"""Held admission seam for the Kansas State Archives connector.

No Kansas State Archives source is admitted: ``descriptor.yaml`` leaves ``role`` and ``rights``
unresolved, and no parser, quarantine route or candidate envelope exists.
Until a reviewed change admits a source, this module is inert. Importing it
performs no I/O, and ``admit`` raises ``ConnectorAdmissionHold`` with reason
code ``CONNECTOR_ADMISSION_NOT_ADMITTED`` instead of routing, admitting or
persisting anything.
"""
from __future__ import annotations

CONNECTOR = "kansas_state_archives"
HOLD_REASON_CODE = "CONNECTOR_ADMISSION_NOT_ADMITTED"


class ConnectorAdmissionHold(RuntimeError):
    """Raised in place of any admission decision while the connector is held."""

    def __init__(self) -> None:
        super().__init__(
            f"{HOLD_REASON_CODE}: the {CONNECTOR} connector has no admitted source; "
            "nothing was routed or admitted."
        )
        self.reason_code = HOLD_REASON_CODE
        self.connector = CONNECTOR


def admit(*args: object, **kwargs: object) -> None:
    """Refuse every admission request while the connector is held."""
    raise ConnectorAdmissionHold()
