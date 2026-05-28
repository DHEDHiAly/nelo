"""Multimodal adapter interfaces."""

from dataclasses import dataclass
from typing import Protocol


@dataclass(slots=True)
class TextInput:
    text: str


@dataclass(slots=True)
class AudioInput:
    bytes_data: bytes
    sample_rate_hz: int


@dataclass(slots=True)
class VisionInput:
    bytes_data: bytes
    content_type: str = "image/jpeg"


class MultimodalAdapter(Protocol):
    """Normalize multimodal input for downstream orchestration."""

    def from_text(self, text: TextInput) -> dict[str, str]:
        """Convert text input to normalized payload."""

    def from_audio(self, audio: AudioInput) -> dict[str, str]:
        """Convert audio input to normalized payload."""

    def from_vision(self, vision: VisionInput) -> dict[str, str]:
        """Convert vision input to normalized payload."""
