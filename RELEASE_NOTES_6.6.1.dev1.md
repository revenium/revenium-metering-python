# Release Notes: revenium_metering v6.6.1.dev1

**Release Date:** 2025-12-10
**Type:** Interim Development Release
**Ticket:** https://linear.app/revenium/issue/BACK-257

## Summary

This is an interim release with working multimodal metering methods (video, image, audio) validated against the dev API. It serves as a backup in case BACK-257 work is delayed.

## What's New

### Multimodal Metering Methods (REVAI-199)

Three new methods added to `client.ai.*`:

| Method | Endpoint | Primary Billing Fields |
|--------|----------|----------------------|
| `create_video()` | `POST /meter/ai/video` | `duration_seconds`, `credits_consumed` |
| `create_image()` | `POST /meter/ai/image` | `actual_image_count`, `requested_image_count` |
| `create_audio()` | `POST /meter/ai/audio` | `duration_seconds`, `character_count`, token counts |

### Critical API Contract Fix

**Billing fields MUST be at the TOP LEVEL of the request body, NOT nested in `attributes`.**

```python
# CORRECT - billing fields at top level
client.ai.create_video(
    transaction_id="...",
    provider="RUNWAY",
    model="gen3a_turbo",
    request_time="...",
    response_time="...",
    request_duration=5000,
    stop_reason="END",
    duration_seconds=5.0,  # TOP LEVEL - required for billing
)

# WRONG - this will return 422 error
client.ai.create_video(
    ...,
    attributes={"duration": 5}  # WRONG - attributes is only for optional metadata
)
```

## Test Results

All 4 endpoints validated against `https://api.dev.hcapp.io`:

| Test | Status |
|------|--------|
| `ai.create_completion()` | PASS |
| `ai.create_video()` | PASS |
| `ai.create_image()` | PASS |
| `ai.create_audio()` | PASS |

## Files Modified

### Core SDK
- `src/revenium_metering/resources/ai.py` - Added multimodal methods with billing parameters

### Type Definitions
- `src/revenium_metering/types/ai_create_video_params.py` - Video billing fields
- `src/revenium_metering/types/ai_create_image_params.py` - Image billing fields
- `src/revenium_metering/types/ai_create_audio_params.py` - Audio billing fields

## Installation

```bash
# From wheel
pip install revenium_metering-6.6.1.dev1-py3-none-any.whl

# From source
pip install revenium_metering-6.6.1.dev1.tar.gz
```

## Usage Example

```python
from revenium_metering import ReveniumMetering
from datetime import datetime

client = ReveniumMetering(
    api_key="your-api-key",
    base_url="https://api.dev.hcapp.io/meter/"
)

# Video metering
result = client.ai.create_video(
    transaction_id="video-" + datetime.now().isoformat(),
    provider="RUNWAY",
    model="gen3a_turbo",
    request_time=datetime.now().isoformat(),
    response_time=datetime.now().isoformat(),
    request_duration=5000,
    stop_reason="END",
    duration_seconds=5.0,
    middleware_source="my-app",
)
print(f"Transaction ID: {result.transaction_id}")
```

## Known Issues

### Existing Middleware Field Name Discrepancies

The Fal and Kling middlewares use deprecated field names that may no longer work:

| Middleware | Field Used | Correct Field |
|------------|-----------|---------------|
| Fal (image) | `imageCount` | `actualImageCount` |
| Kling (video) | `creditsUsed` | `creditsConsumed` |
| OpenAI Audio | `duration` | `durationSeconds` |

## Dependencies

- Python >= 3.8
- httpx >= 0.23.0, < 1
- pydantic >= 1.9.0, < 3

## Next Steps

1. BACK-257 completion will provide official SDK with OpenAPI spec alignment
2. Middleware repos need field name updates per ticket findings
