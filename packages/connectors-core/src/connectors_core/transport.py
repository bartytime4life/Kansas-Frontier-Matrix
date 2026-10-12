"""Injected transport facade; bounded_curl supplies the optional live transport."""
from ._transport_execute import execute_retrieval
from ._transport_protocols import CancellationToken, Clock, JitterSource, Sleeper, Transport
from ._transport_request import (
    TransportCancelledError,
    TransportInputError,
    TransportMethod,
    TransportProfile,
    TransportRequest,
    TransportResponse,
)
from ._transport_result import AttemptRecord, CapturedPayload, RetrievalResult
from ._transport_retry import parse_retry_after

__all__ = [
    "AttemptRecord",
    "CancellationToken",
    "CapturedPayload",
    "Clock",
    "JitterSource",
    "RetrievalResult",
    "Sleeper",
    "Transport",
    "TransportCancelledError",
    "TransportInputError",
    "TransportMethod",
    "TransportProfile",
    "TransportRequest",
    "TransportResponse",
    "execute_retrieval",
    "parse_retry_after",
]
