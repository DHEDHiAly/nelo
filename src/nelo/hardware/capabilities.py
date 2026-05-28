"""Hardware capability detection for edge-aware decisions."""

import os
import platform
from dataclasses import dataclass


@dataclass(slots=True)
class HardwareProfile:
    cpu_count: int
    architecture: str
    platform_name: str


def detect_hardware() -> HardwareProfile:
    """Return a lightweight profile for runtime decisions."""
    return HardwareProfile(
        cpu_count=os.cpu_count() or 1,
        architecture=platform.machine() or "unknown",
        platform_name=platform.system() or "unknown",
    )
