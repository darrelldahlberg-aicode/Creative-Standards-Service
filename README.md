# Creative Standards Service

The shared creative-specification and asset-validation layer for Creative OS, AI Agency OS, and every industry agent.

## Purpose

Creative Standards Service is the source of truth for:

- Canvas dimensions and aspect ratios
- Safe areas and crop guidance
- Accepted file types and file-size limits
- Platform and channel format identifiers
- Deterministic asset validation
- Versioned creative specifications

It is industry agnostic. Furniture, law, automotive, political, retail, and future verticals consume the same format contracts while keeping their brand rules and campaign strategy outside this service.

## Ready formats

The v1 catalog includes:

- `display.2160x720`
- `meta.feed.square`
- `meta.story.vertical`
- `google.display.300x250`
- `google.display.728x90`
- `tiktok.video.vertical`
- `email.hero.1200x600`

## Python API

```python
from creative_standards import get_format, list_formats, validate_asset

spec = get_format("display.2160x720")

result = validate_asset(
    "display.2160x720",
    width=2160,
    height=720,
    file_type="png",
    file_bytes=500_000,
)

assert result.valid
```

## Contract rules

- Format identifiers are stable within a major version.
- Breaking changes require a new major version.
- Validation is deterministic and does not make network calls.
- Platform claims must be sourced and dated before they are treated as current.
- Creative OS may add campaign-specific constraints, but may not weaken format validation.

## Architecture

```text
Creative OS / Agent
        |
        v
Creative Standards Service
  - format catalog
  - safe-area rules
  - file constraints
  - validator
        |
        v
Validated creative brief or asset result
```

The inherited paid-media tooling remains available as a legacy compatibility layer while reusable standards are progressively extracted into `creative_standards/`.

## Development

```bash
python -m pip install -e .
python -m pytest -q
```

## Licensing and attribution

This repository contains original Creative Standards Service code and inherited MIT-licensed components from Claude Ads. Existing `LICENSE`, `THIRD_PARTY_NOTICES.md`, and source-ledger records must be preserved. Third-party platforms, trademarks, documentation, and APIs remain subject to their respective terms.
