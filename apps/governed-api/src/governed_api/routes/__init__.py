"""Route modules for governed API."""
from dataclasses import dataclass


@dataclass(frozen=True)
class RouteResponse:
    status: str
    payload: dict
