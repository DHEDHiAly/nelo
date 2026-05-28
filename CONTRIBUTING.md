# Contributing to Nelo

## Development workflow
1. Create a focused branch.
2. Keep changes scoped to one logical concern.
3. Run local checks before opening a PR:
   ```bash
   ruff check .
   pytest -q
   ```
4. Open a PR using the template and explain architectural impact.

## Engineering principles
- Offline-first by default.
- Keep modules decoupled (inference, routing, memory, multimodal, hardware).
- Prefer clear interfaces over implicit coupling.
- Optimize for low-power edge hardware assumptions.

## PR expectations
- Add or update tests for behavior changes.
- Update docs when module boundaries or setup changes.
- Keep PRs reviewable and incremental.
