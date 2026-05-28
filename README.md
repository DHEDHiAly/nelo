# Nelo

Nelo is an offline-first embodied AI educational companion designed for low-cost edge hardware (for example Raspberry Pi-class devices), combining local inference, multimodal interaction, routing, and memory into a practical learning companion that can operate with limited connectivity.

## Vision
Build a reliable, affordable physical AI companion that helps learners through conversational, visual, and contextual interaction while keeping core experiences available offline.

## Problem Nelo Solves
Most AI learning tools assume persistent internet, cloud-scale hardware, and single-modality interactions. Nelo prioritizes low-power local operation, adaptive compute routing, and embodied multimodal workflows suitable for real classrooms and constrained environments.

## Architecture Direction (High Level)
- `inference`: local/quantized model runtime boundaries and backend abstraction.
- `routing`: policies to choose local vs remote inference when available.
- `memory`: lightweight contextual and personalization interfaces.
- `multimodal`: text/audio/vision input normalization and adapters.
- `hardware`: device capability detection and hardware-aware constraints.
- `backend`: service-facing orchestration boundaries.
- `core`/`utils`: shared config, logging, and common helpers.

## Current Repository Purpose
This repository is in its **foundational setup phase**. It establishes clean module boundaries, docs, tests, and CI so multiple engineers can build features in parallel without reworking structure later.

## Local Development Setup
1. Install Python 3.11+.
2. Create and activate a virtual environment.
3. Install project and dev dependencies:
   ```bash
   pip install -e .[dev]
   ```
4. Run checks:
   ```bash
   ruff check .
   pytest -q
   ```

See `docs/dev_setup.md` for details.

## Module Overview
- `src/nelo/core`: shared config and logging.
- `src/nelo/inference`: inference backend contracts.
- `src/nelo/routing`: routing policy contracts.
- `src/nelo/memory`: memory store contracts.
- `src/nelo/multimodal`: input adapter contracts.
- `src/nelo/backend`: backend-facing service contracts.
- `src/nelo/hardware`: hardware profile detection.
- `tests/`: smoke and module-level tests.
- `docs/`: architecture and development documentation.

## Hardware and Offline-First Notes
- Local execution is the default path; remote compute is optional augmentation.
- Interfaces are designed to keep model/runtime decisions isolated from application logic.
- Hardware capability detection is explicit so code can make edge-aware decisions.

## Contributing
Start with `CONTRIBUTING.md`, review architecture docs, and open focused PRs that keep module boundaries clear.

## Status / Current Phase
✅ Foundation initialized: repository structure, base module interfaces, docs, tests, and CI scaffolding are in place.

## License
Distributed under the MIT License. See `LICENSE`.
