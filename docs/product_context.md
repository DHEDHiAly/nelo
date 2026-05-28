# Product Context

Nelo is an embodied AI learning companion aimed at students and developers working in environments with inconsistent connectivity and low-cost hardware.

## Product objectives
- Deliver useful educational interactions offline.
- Support multimodal learning (speech, text, vision).
- Personalize behavior with local memory/context.
- Remain affordable and performant on edge devices.

## Constraints
- Limited CPU/RAM and often no dedicated GPU.
- Intermittent or unavailable internet.
- Need for safe defaults and predictable behavior.

## Engineering implications
- Prefer quantized/local models where possible.
- Make remote inference optional, not required.
- Keep component interfaces explicit for safe iteration.
