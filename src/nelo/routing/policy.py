"""Inference routing policy contracts."""

from dataclasses import dataclass
from typing import Protocol


@dataclass(slots=True)
class RoutingDecision:
    backend: str
    reason: str


class RoutingPolicy(Protocol):
    """Choose which backend should execute a request."""

    def choose_backend(self, *, prompt: str, requires_vision: bool = False) -> RoutingDecision:
        """Return the selected backend and reasoning."""
