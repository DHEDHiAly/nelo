# Architecture Overview

Nelo is structured around explicit module boundaries to support parallel development and low-risk refactoring.

## Core principles
- Offline-first behavior is the default.
- Edge hardware constraints are first-class.
- Contracts first: interfaces define boundaries before concrete implementations.

## Initial modules
- `nelo.inference`: model/runtime interfaces for local and optional remote inference.
- `nelo.routing`: policy layer choosing compute targets.
- `nelo.memory`: personalized context and recall interfaces.
- `nelo.multimodal`: text/audio/vision input contracts.
- `nelo.hardware`: hardware capability detection and profile access.
- `nelo.backend`: service-level orchestration boundaries.

## Near-term evolution
- Add concrete local inference adapters.
- Introduce routing heuristics based on latency, battery, and model availability.
- Add persistent memory backends for device-local personalization.
