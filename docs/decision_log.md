# Decision Log

This file tracks significant technical decisions until the ADR catalog grows.

| Date | Decision | Rationale |
|---|---|---|
| 2026-05-28 | Use Python package with `src/` layout and pytest/ruff baseline | Fast onboarding, clear structure, low maintenance overhead |
| 2026-05-28 | Define interfaces first for core modules | Enables parallel implementation without coupling |
