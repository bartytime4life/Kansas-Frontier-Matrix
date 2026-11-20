"""Held retrieval seam for the AHGP connector.

No AHGP source is admitted: ``descriptor.yaml`` leaves ``role`` and ``rights``
unresolved, and no retrieval profile, endpoint, credential or rights review
exists. Until a reviewed change admits a source, this module is inert.
Importing it performs no I/O, and ``retrieve`` raises ``ConnectorFetchHold``
with reason code ``CONNECTOR_FETCH_NOT_ADMITTED`` instead of contacting any
host, reading credentials or writing a file.
"""
from __future__ import annotations

CONNECTOR = "ahgp"
HOLD_REASON_CODE = "CONNECTOR_FETCH_NOT_ADMITTED"


class ConnectorFetchHold(RuntimeError):
    """Raised in place of any retrieval while the connector is held."""

    def __init__(self) -> None:
        super().__init__(
            f"{HOLD_REASON_CODE}: the {CONNECTOR} connector has no admitted source; "
            "nothing was fetched."
        )
        self.reason_code = HOLD_REASON_CODE
        self.connector = CONNECTOR


def retrieve(*args: object, **kwargs: object) -> None:
    """Refuse every retrieval request while the connector is held."""
    raise ConnectorFetchHold()
