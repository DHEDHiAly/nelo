"""Inference backend interfaces."""

from typing import Protocol


class InferenceBackend(Protocol):
    """Contract for inference runtimes (local or remote)."""

    name: str

    def load_model(self, model_id: str) -> None:
        """Load or prepare a model for inference."""

    def infer(self, prompt: str) -> str:
        """Run an inference request and return output text."""
