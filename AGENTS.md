# AI Development Assistant Guide

## Overview
This is the Revenium Metering Python SDK - the core library for sending usage metering data to Revenium's API.

## Project Context
This SDK provides the foundation for all Python-based Revenium middleware implementations. It handles API communication, data validation, and error handling for metering events.

## Technology Stack
- Language: Python 3.8+
- Package Manager: pip
- Build System: setuptools/poetry
- Testing: pytest

## Development Setup

### Prerequisites
- Python 3.8 or higher
- Revenium API key (get from https://app.revenium.io)

### Installation
```bash
# For development
pip install -e .

# For testing
pip install -e ".[test]"
```

## Key Components
- `revenium_metering/`: Main SDK code
- `examples/`: Usage examples
- `tests/`: Test suite

## For External Contributors

### What You Can Contribute
- Bug fixes in API communication
- Improved error handling and retry logic
- Better connection pooling and performance
- Documentation improvements
- Additional examples

### What Requires Backend Changes
- New metadata fields (backend must support them first)
- Model pricing (automatically synced from backend)
- New API endpoints (must be added to backend first)

## Coding Standards
- Follow PEP 8
- Add type hints for all functions
- Maintain test coverage above 80%
- Document all public APIs

## Testing
```bash
# Run tests
pytest

# With coverage
pytest --cov=revenium_metering
```

## Security
- Never log API keys or authentication tokens
- Ensure no PII is sent to Revenium unless explicitly intended
- Use HTTPS for all API communications