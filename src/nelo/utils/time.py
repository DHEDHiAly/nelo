"""Time helpers."""

from time import monotonic


def monotonic_ms() -> int:
    """Return monotonic time in milliseconds."""
    return int(monotonic() * 1000)
