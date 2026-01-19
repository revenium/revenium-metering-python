#!/usr/bin/env python3
"""
Test script for multimodal metering - using raw httpx to bypass SDK
This helps identify the exact API payload requirements
"""

import os
import uuid
import json
import httpx
from datetime import datetime, timezone

API_KEY = os.environ.get("REVENIUM_API_KEY")
API_BASE = os.environ.get("REVENIUM_API_BASE", "https://api.dev.hcapp.io")

if not API_KEY:
    print("ERROR: Set REVENIUM_API_KEY environment variable")
    exit(1)

HEADERS = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json",
}

def test_video_with_different_fields():
    """Test video endpoint with various field combinations"""
    print("\n" + "="*60)
    print("TEST: /v2/ai/video - trying different billing field combinations")
    print("="*60)

    now = datetime.now(timezone.utc).isoformat()
    base_payload = {
        "transactionId": f"test-video-{uuid.uuid4().hex[:8]}",
        "provider": "RUNWAY",
        "model": "gen3a_turbo",
        "requestTime": now,
        "responseTime": now,
        "requestDuration": 5000,
        "stopReason": "END",
        "middlewareSource": "test-script-back257",
    }

    # Try different attribute combinations
    test_cases = [
        {"durationSeconds": 5},
        {"requestedDurationSeconds": 5},
        {"creditsConsumed": 10},
        {"duration": 5, "creditsUsed": 10},  # What Kling uses
    ]

    for i, attrs in enumerate(test_cases, 1):
        payload = {**base_payload}
        payload["transactionId"] = f"test-video-{uuid.uuid4().hex[:8]}"
        payload["attributes"] = attrs

        print(f"\n  Test {i}: attributes = {attrs}")
        try:
            response = httpx.post(
                f"{API_BASE}/meter/v2/ai/video",
                json=payload,
                headers=HEADERS,
                timeout=30.0,
            )
            if response.status_code in (200, 201, 202):
                print(f"    ✅ SUCCESS: {response.status_code}")
                return attrs  # Return the working attributes
            else:
                print(f"    ❌ FAILED: {response.status_code} - {response.text[:200]}")
        except Exception as e:
            print(f"    ❌ ERROR: {e}")

    return None


def test_image_with_different_fields():
    """Test image endpoint with various field combinations"""
    print("\n" + "="*60)
    print("TEST: /v2/ai/images - trying different billing field combinations")
    print("="*60)

    now = datetime.now(timezone.utc).isoformat()
    base_payload = {
        "transactionId": f"test-image-{uuid.uuid4().hex[:8]}",
        "provider": "FAL",
        "model": "flux-pro",
        "requestTime": now,
        "responseTime": now,
        "requestDuration": 3000,
        "stopReason": "END",
        "middlewareSource": "test-script-back257",
    }

    test_cases = [
        {"actualImageCount": 1},
        {"requestedImageCount": 1},
        {"imageCount": 1},  # What Fal uses
        {"actualImageCount": 1, "requestedImageCount": 1},
    ]

    for i, attrs in enumerate(test_cases, 1):
        payload = {**base_payload}
        payload["transactionId"] = f"test-image-{uuid.uuid4().hex[:8]}"
        payload["attributes"] = attrs

        print(f"\n  Test {i}: attributes = {attrs}")
        try:
            response = httpx.post(
                f"{API_BASE}/meter/v2/ai/images",
                json=payload,
                headers=HEADERS,
                timeout=30.0,
            )
            if response.status_code in (200, 201, 202):
                print(f"    ✅ SUCCESS: {response.status_code}")
                return attrs
            else:
                print(f"    ❌ FAILED: {response.status_code} - {response.text[:200]}")
        except Exception as e:
            print(f"    ❌ ERROR: {e}")

    return None


def test_audio_with_different_fields():
    """Test audio endpoint with various field combinations"""
    print("\n" + "="*60)
    print("TEST: /v2/ai/audio - trying different billing field combinations")
    print("="*60)

    now = datetime.now(timezone.utc).isoformat()
    base_payload = {
        "transactionId": f"test-audio-{uuid.uuid4().hex[:8]}",
        "provider": "OPENAI",
        "model": "whisper-1",
        "requestTime": now,
        "responseTime": now,
        "requestDuration": 2000,
        "stopReason": "END",
        "middlewareSource": "test-script-back257",
    }

    test_cases = [
        {"durationSeconds": 60.5},
        {"characterCount": 750},
        {"inputAudioTokenCount": 1000},
        {"outputAudioTokenCount": 500},
    ]

    for i, attrs in enumerate(test_cases, 1):
        payload = {**base_payload}
        payload["transactionId"] = f"test-audio-{uuid.uuid4().hex[:8]}"
        payload["attributes"] = attrs

        print(f"\n  Test {i}: attributes = {attrs}")
        try:
            response = httpx.post(
                f"{API_BASE}/meter/v2/ai/audio",
                json=payload,
                headers=HEADERS,
                timeout=30.0,
            )
            if response.status_code in (200, 201, 202):
                print(f"    ✅ SUCCESS: {response.status_code}")
                return attrs
            else:
                print(f"    ❌ FAILED: {response.status_code} - {response.text[:200]}")
        except Exception as e:
            print(f"    ❌ ERROR: {e}")

    return None


if __name__ == "__main__":
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║  API Field Discovery Test - Finding Working Field Names      ║
║  API Base: {API_BASE:<47} ║
╚══════════════════════════════════════════════════════════════╝
""")

    video_attrs = test_video_with_different_fields()
    image_attrs = test_image_with_different_fields()
    audio_attrs = test_audio_with_different_fields()

    print("\n" + "="*60)
    print("DISCOVERY RESULTS")
    print("="*60)
    print(f"\nWorking Video attributes: {video_attrs}")
    print(f"Working Image attributes: {image_attrs}")
    print(f"Working Audio attributes: {audio_attrs}")

    if all([video_attrs, image_attrs, audio_attrs]):
        print("\n🎉 Found working field names for all endpoints!")
    else:
        print("\n⚠️  Some endpoints need further investigation")
