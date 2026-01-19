#!/usr/bin/env python3
"""
Test script for multimodal metering methods (BACK-257 validation)
Tests create_video, create_image, create_audio against dev API
"""

import os
import uuid
from datetime import datetime, timezone

# Get API key from environment
API_KEY = os.environ.get("REVENIUM_API_KEY")
API_BASE = os.environ.get("REVENIUM_API_BASE", "https://api.dev.hcapp.io")

if not API_KEY:
    print("ERROR: Set REVENIUM_API_KEY environment variable")
    print("  export REVENIUM_API_KEY='your-key-here'")
    exit(1)

from revenium_metering import ReveniumMetering

client = ReveniumMetering(
    api_key=API_KEY,
    base_url=API_BASE,
)

def test_create_video():
    """Test video metering endpoint"""
    print("\n" + "="*60)
    print("TEST: create_video() -> /v2/ai/video")
    print("="*60)

    now = datetime.now(timezone.utc).isoformat()
    transaction_id = f"test-video-{uuid.uuid4().hex[:8]}"

    try:
        result = client.ai.create_video(
            transaction_id=transaction_id,
            provider="RUNWAY",
            model="gen3a_turbo",
            request_time=now,
            response_time=now,
            request_duration=5000,
            stop_reason="END",
            # Billing fields at TOP LEVEL (per API spec)
            duration_seconds=5,
            middleware_source="test-script-back257",
        )
        print(f"✅ SUCCESS: {result}")
        return True
    except Exception as e:
        print(f"❌ FAILED: {type(e).__name__}: {e}")
        return False


def test_create_image():
    """Test image metering endpoint"""
    print("\n" + "="*60)
    print("TEST: create_image() -> /v2/ai/images")
    print("="*60)

    now = datetime.now(timezone.utc).isoformat()
    transaction_id = f"test-image-{uuid.uuid4().hex[:8]}"

    try:
        result = client.ai.create_image(
            transaction_id=transaction_id,
            provider="FAL",
            model="flux-pro",
            request_time=now,
            response_time=now,
            request_duration=3000,
            stop_reason="END",
            # Billing fields at TOP LEVEL (per API spec)
            actual_image_count=1,
            middleware_source="test-script-back257",
        )
        print(f"✅ SUCCESS: {result}")
        return True
    except Exception as e:
        print(f"❌ FAILED: {type(e).__name__}: {e}")
        return False


def test_create_audio():
    """Test audio metering endpoint"""
    print("\n" + "="*60)
    print("TEST: create_audio() -> /v2/ai/audio")
    print("="*60)

    now = datetime.now(timezone.utc).isoformat()
    transaction_id = f"test-audio-{uuid.uuid4().hex[:8]}"

    try:
        result = client.ai.create_audio(
            transaction_id=transaction_id,
            provider="OPENAI",
            model="whisper-1",
            request_time=now,
            response_time=now,
            request_duration=2000,
            stop_reason="END",
            # Billing fields at TOP LEVEL (per API spec)
            duration_seconds=60.5,
            middleware_source="test-script-back257",
        )
        print(f"✅ SUCCESS: {result}")
        return True
    except Exception as e:
        print(f"❌ FAILED: {type(e).__name__}: {e}")
        return False


def test_create_completion_still_works():
    """Verify existing create_completion method still works"""
    print("\n" + "="*60)
    print("TEST: create_completion() -> /v2/ai/completions (regression)")
    print("="*60)

    now = datetime.now(timezone.utc).isoformat()
    transaction_id = f"test-completion-{uuid.uuid4().hex[:8]}"

    try:
        result = client.ai.create_completion(
            transaction_id=transaction_id,
            provider="OPENAI",
            model="gpt-4o",
            completion_start_time=now,
            request_time=now,
            response_time=now,
            request_duration=1500,
            cost_type="AI",
            input_token_count=100,
            output_token_count=50,
            total_token_count=150,
            is_streamed=False,
            stop_reason="END",
            operation_type="CHAT",
            middleware_source="test-script-back257",
        )
        print(f"✅ SUCCESS: {result}")
        return True
    except Exception as e:
        print(f"❌ FAILED: {type(e).__name__}: {e}")
        return False


if __name__ == "__main__":
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║  BACK-257 Validation: Python SDK Multimodal Methods          ║
║  API Base: {API_BASE:<47} ║
╚══════════════════════════════════════════════════════════════╝
""")

    results = {
        "create_completion (regression)": test_create_completion_still_works(),
        "create_video": test_create_video(),
        "create_image": test_create_image(),
        "create_audio": test_create_audio(),
    }

    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)

    passed = sum(1 for v in results.values() if v)
    total = len(results)

    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status}: {test_name}")

    print(f"\nTotal: {passed}/{total} tests passed")

    if passed == total:
        print("\n🎉 All tests passed! Draft implementation is working.")
    else:
        print("\n⚠️  Some tests failed. Check error messages above.")

    exit(0 if passed == total else 1)
