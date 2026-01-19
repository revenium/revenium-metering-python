#!/usr/bin/env python3
"""
Test script for multimodal metering - testing top-level fields vs nested attributes
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

def test_video_top_level():
    """Test video endpoint with fields at TOP LEVEL (not nested in attributes)"""
    print("\n" + "="*60)
    print("TEST: /v2/ai/video - fields at TOP LEVEL")
    print("="*60)

    now = datetime.now(timezone.utc).isoformat()

    test_cases = [
        # Try durationSeconds at top level
        {
            "transactionId": f"test-video-{uuid.uuid4().hex[:8]}",
            "provider": "RUNWAY",
            "model": "gen3a_turbo",
            "requestTime": now,
            "responseTime": now,
            "requestDuration": 5000,
            "stopReason": "END",
            "middlewareSource": "test-script-back257",
            "durationSeconds": 5,  # TOP LEVEL
        },
        # Try creditsConsumed at top level
        {
            "transactionId": f"test-video-{uuid.uuid4().hex[:8]}",
            "provider": "RUNWAY",
            "model": "gen3a_turbo",
            "requestTime": now,
            "responseTime": now,
            "requestDuration": 5000,
            "stopReason": "END",
            "middlewareSource": "test-script-back257",
            "creditsConsumed": 10,  # TOP LEVEL
        },
    ]

    for i, payload in enumerate(test_cases, 1):
        billing_field = [k for k in payload.keys() if k in ['durationSeconds', 'creditsConsumed', 'requestedDurationSeconds']]
        print(f"\n  Test {i}: {billing_field[0]} at top level")
        print(f"    Payload: {json.dumps(payload, indent=2)[:300]}...")
        try:
            response = httpx.post(
                f"{API_BASE}/meter/v2/ai/video",
                json=payload,
                headers=HEADERS,
                timeout=30.0,
            )
            if response.status_code in (200, 201, 202):
                print(f"    ✅ SUCCESS: {response.status_code}")
                return payload
            else:
                print(f"    ❌ FAILED: {response.status_code} - {response.text[:300]}")
        except Exception as e:
            print(f"    ❌ ERROR: {e}")

    return None


def test_image_top_level():
    """Test image endpoint with fields at TOP LEVEL"""
    print("\n" + "="*60)
    print("TEST: /v2/ai/images - fields at TOP LEVEL")
    print("="*60)

    now = datetime.now(timezone.utc).isoformat()

    test_cases = [
        # Try actualImageCount at top level
        {
            "transactionId": f"test-image-{uuid.uuid4().hex[:8]}",
            "provider": "FAL",
            "model": "flux-pro",
            "requestTime": now,
            "responseTime": now,
            "requestDuration": 3000,
            "stopReason": "END",
            "middlewareSource": "test-script-back257",
            "actualImageCount": 1,  # TOP LEVEL
        },
        # Try requestedImageCount at top level
        {
            "transactionId": f"test-image-{uuid.uuid4().hex[:8]}",
            "provider": "FAL",
            "model": "flux-pro",
            "requestTime": now,
            "responseTime": now,
            "requestDuration": 3000,
            "stopReason": "END",
            "middlewareSource": "test-script-back257",
            "requestedImageCount": 1,  # TOP LEVEL
        },
    ]

    for i, payload in enumerate(test_cases, 1):
        billing_field = [k for k in payload.keys() if k in ['actualImageCount', 'requestedImageCount']]
        print(f"\n  Test {i}: {billing_field[0]} at top level")
        try:
            response = httpx.post(
                f"{API_BASE}/meter/v2/ai/images",
                json=payload,
                headers=HEADERS,
                timeout=30.0,
            )
            if response.status_code in (200, 201, 202):
                print(f"    ✅ SUCCESS: {response.status_code}")
                return payload
            else:
                print(f"    ❌ FAILED: {response.status_code} - {response.text[:300]}")
        except Exception as e:
            print(f"    ❌ ERROR: {e}")

    return None


def test_audio_top_level():
    """Test audio endpoint with fields at TOP LEVEL"""
    print("\n" + "="*60)
    print("TEST: /v2/ai/audio - fields at TOP LEVEL")
    print("="*60)

    now = datetime.now(timezone.utc).isoformat()

    test_cases = [
        # Try durationSeconds at top level
        {
            "transactionId": f"test-audio-{uuid.uuid4().hex[:8]}",
            "provider": "OPENAI",
            "model": "whisper-1",
            "requestTime": now,
            "responseTime": now,
            "requestDuration": 2000,
            "stopReason": "END",
            "middlewareSource": "test-script-back257",
            "durationSeconds": 60.5,  # TOP LEVEL
        },
        # Try characterCount at top level
        {
            "transactionId": f"test-audio-{uuid.uuid4().hex[:8]}",
            "provider": "OPENAI",
            "model": "tts-1-hd",
            "requestTime": now,
            "responseTime": now,
            "requestDuration": 2000,
            "stopReason": "END",
            "middlewareSource": "test-script-back257",
            "characterCount": 750,  # TOP LEVEL
        },
    ]

    for i, payload in enumerate(test_cases, 1):
        billing_field = [k for k in payload.keys() if k in ['durationSeconds', 'characterCount', 'inputAudioTokenCount', 'outputAudioTokenCount']]
        print(f"\n  Test {i}: {billing_field[0]} at top level")
        try:
            response = httpx.post(
                f"{API_BASE}/meter/v2/ai/audio",
                json=payload,
                headers=HEADERS,
                timeout=30.0,
            )
            if response.status_code in (200, 201, 202):
                print(f"    ✅ SUCCESS: {response.status_code}")
                return payload
            else:
                print(f"    ❌ FAILED: {response.status_code} - {response.text[:300]}")
        except Exception as e:
            print(f"    ❌ ERROR: {e}")

    return None


if __name__ == "__main__":
    print(f"""
╔══════════════════════════════════════════════════════════════╗
║  API Test - Top Level Fields vs Nested Attributes            ║
║  API Base: {API_BASE:<47} ║
╚══════════════════════════════════════════════════════════════╝
""")

    video_result = test_video_top_level()
    image_result = test_image_top_level()
    audio_result = test_audio_top_level()

    print("\n" + "="*60)
    print("RESULTS")
    print("="*60)
    print(f"\nVideo: {'✅ WORKING' if video_result else '❌ FAILED'}")
    print(f"Image: {'✅ WORKING' if image_result else '❌ FAILED'}")
    print(f"Audio: {'✅ WORKING' if audio_result else '❌ FAILED'}")
