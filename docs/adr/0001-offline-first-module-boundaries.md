# ADR 0001: Offline-First Module Boundaries

## Status
Accepted

## Context
Nelo targets low-cost edge devices with intermittent connectivity. The codebase must support independent iteration across inference, routing, memory, multimodal, and hardware concerns.

## Decision
Adopt a `src/nelo` package with explicit submodules and interface-led scaffolding for major domains.

## Consequences
- Easier parallel development across a small team.
- Lower coupling and clearer ownership boundaries.
- Concrete implementations can evolve without reorganizing repository structure.
