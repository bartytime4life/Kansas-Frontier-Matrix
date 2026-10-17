"""Held seam for a future local Ollama model adapter.

ADR-0008 and ADR-0019 are proposed, and
docs/architecture/governed-ai/OLLAMA_INTEGRATION.md defers a live Ollama
binding until the contract, evidence, citation, receipt and security gates
pass. Until a reviewed change admits that binding, this module is inert:
importing it performs no I/O, and constructing the adapter raises
``OllamaAdapterHold`` with a named reason code instead of returning a response.
It never reads ``OLLAMA_HOST``, opens a socket, starts a process, or calls a
model. Tests that need finite runtime outcomes use ``MockAdapter``.
"""
from __future__ import annotations


HOLD_REASON_CODE = "OLLAMA_ADAPTER_NOT_ADMITTED"


class OllamaAdapterHold(RuntimeError):
    """Raised in place of any adapter behavior while the live binding is held."""

    def __init__(self) -> None:
        super().__init__(
            f"{HOLD_REASON_CODE}: the local Ollama adapter is held; "
            "no model was called and no response was produced."
        )
        self.reason_code = HOLD_REASON_CODE


class OllamaAdapter:
    """Fail-closed adapter seam: construction always raises the named hold."""

    def __init__(self, *args: object, **kwargs: object) -> None:
        raise OllamaAdapterHold()
