"""Backend orchestration interfaces."""

from typing import Protocol


class BackendService(Protocol):
    """Service interface for request orchestration."""

    def handle_request(self, payload: dict[str, str]) -> dict[str, str]:
        """Handle a normalized request payload."""
