"""Memory store interfaces."""

from typing import Protocol


class MemoryStore(Protocol):
    """Simple key-value memory contract for personalization/context."""

    def put(self, key: str, value: str) -> None:
        """Persist a memory item."""

    def get(self, key: str) -> str | None:
        """Read a memory item by key."""
