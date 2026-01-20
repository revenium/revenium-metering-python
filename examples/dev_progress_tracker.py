#!/usr/bin/env python3
"""
Dev Progress Tracker Demo

A mock AI tool that:
1. Makes real AI calls (using Anthropic Claude)
2. Meters the usage via Revenium Python SDK
3. Shows data flowing through: SDK -> Metering API -> Kafka -> Clickhouse -> Isotope

Usage:
    export ANTHROPIC_API_KEY="your-key"
    export REVENIUM_METERING_API_KEY="your-key"
    export REVENIUM_BASE_URL="http://localhost:8080/profitstream"  # for local dev

    python dev_progress_tracker.py
"""

import os
import time
import uuid
from datetime import datetime, timezone

import anthropic

from revenium_metering import ReveniumMetering


def get_metering_client() -> ReveniumMetering:
    """Initialize the Revenium metering client."""
    base_url = os.environ.get("REVENIUM_BASE_URL", "http://localhost:8080/profitstream")
    api_key = os.environ.get("REVENIUM_METERING_API_KEY", "demo-key")

    return ReveniumMetering(
        api_key=api_key,
        base_url=base_url,
    )


def analyze_code_with_claude(prompt: str) -> dict:
    """Make a real AI call to Claude and return usage stats."""
    client = anthropic.Anthropic()

    start_time = datetime.now(timezone.utc)

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    end_time = datetime.now(timezone.utc)
    duration_ms = int((end_time - start_time).total_seconds() * 1000)

    return {
        "model": response.model,
        "input_tokens": response.usage.input_tokens,
        "output_tokens": response.usage.output_tokens,
        "total_tokens": response.usage.input_tokens + response.usage.output_tokens,
        "duration_ms": duration_ms,
        "start_time": start_time.isoformat(),
        "end_time": end_time.isoformat(),
        "response_text": response.content[0].text,
        "stop_reason": response.stop_reason,
    }


def meter_ai_call(metering_client: ReveniumMetering, usage: dict):
    """Send the AI usage to Revenium metering."""
    transaction_id = str(uuid.uuid4())

    # Use the AI completion endpoint
    response = metering_client.ai.create_completion(
        transaction_id=transaction_id,
        model=usage["model"],
        provider="Anthropic",
        cost_type="AI",
        input_token_count=usage["input_tokens"],
        output_token_count=usage["output_tokens"],
        total_token_count=usage["total_tokens"],
        request_duration=usage["duration_ms"],
        request_time=usage["start_time"],
        response_time=usage["end_time"],
        completion_start_time=usage["start_time"],
        stop_reason=usage["stop_reason"].upper() if usage["stop_reason"] else "END",
        is_streamed=False,
    )

    print(f"  Metered: {response.id} | {usage['total_tokens']} tokens | {usage['duration_ms']}ms")
    return response


def meter_tool_event(metering_client: ReveniumMetering, tool_id: str, action: str, metadata: dict):
    """Send a generic tool event to Revenium metering."""
    transaction_id = str(uuid.uuid4())

    response = metering_client.events.create(
        transaction_id=transaction_id,
        source_type="SDK_PYTHON",
        source_id=tool_id,
        payload={
            "action": action,
            "tool_id": tool_id,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            **metadata,
        },
    )

    print(f"  Event: {response.id} | {action}")
    return response


def run_demo():
    """Run the demo showing AI calls being metered."""
    print("\n" + "=" * 60)
    print("  DEV PROGRESS TRACKER - Revenium Metering Demo")
    print("=" * 60)

    metering = get_metering_client()
    tool_id = "dev-progress-tracker"

    # Simulate tracking dev progress with AI assistance
    tasks = [
        "Summarize in one sentence: What is the main purpose of a Python decorator?",
        "In 2-3 sentences: What are the benefits of using type hints in Python?",
        "Brief answer: What is the difference between sync and async in Python?",
    ]

    print(f"\nTracking {len(tasks)} development tasks with AI assistance...\n")

    # Meter tool start event
    meter_tool_event(metering, tool_id, "session_start", {"task_count": len(tasks)})

    for i, task in enumerate(tasks, 1):
        print(f"\n[Task {i}/{len(tasks)}] {task[:50]}...")

        # Make real AI call
        usage = analyze_code_with_claude(task)
        print(f"  Claude: {usage['response_text'][:100]}...")

        # Meter the AI call
        meter_ai_call(metering, usage)

        # Small delay between calls
        time.sleep(0.5)

    # Meter tool end event
    meter_tool_event(metering, tool_id, "session_end", {"tasks_completed": len(tasks)})

    print("\n" + "=" * 60)
    print("  Demo complete! Check Isotope for the metered data.")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_demo()
