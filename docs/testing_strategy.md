# Testing Strategy

## Goals
- Keep tests fast and deterministic.
- Verify module boundaries and import stability early.
- Expand test depth alongside concrete implementations.

## Current scope
- Smoke tests for package/module imports.
- Basic unit tests for shared config defaults.

## Expansion plan
- Add unit tests per concrete backend/policy/store implementation.
- Add contract tests for interface compliance.
- Add hardware-specific tests with mocked profiles.
