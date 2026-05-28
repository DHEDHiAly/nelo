"""Application configuration primitives."""

from dataclasses import dataclass
from os import getenv


def _get_bool(name: str, default: bool) -> bool:
    raw = getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


@dataclass(slots=True)
class NeloConfig:
    """Runtime configuration for Nelo services."""

    env: str = getenv("NELO_ENV", "development")
    offline_first: bool = _get_bool("NELO_OFFLINE_FIRST", True)
    remote_fallback: bool = _get_bool("NELO_REMOTE_FALLBACK", False)
    log_level: str = getenv("NELO_LOG_LEVEL", "INFO")
