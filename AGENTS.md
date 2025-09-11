# AI Development Guide

## Project Overview
Python SDK for Revenium Metering API, generated from OpenAPI specification. Provides direct access to Revenium's REST API for dispatching metering metadata.

## Development Environment Setup

### Prerequisites
- Python 3.8+
- pip
- Virtual environment (recommended)

### Installation
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Install development dependencies
pip install -e .[dev]
```

## Development Commands

```bash
# Install package in development mode
pip install -e .

# Install with development dependencies
pip install -e .[dev]

# Run tests
pytest

# Run tests with coverage
pytest --cov

# Code formatting
black .

# Linting
flake8

# Type checking  
mypy .

# Build package
python -m build
```

## Code Style Guidelines
- **Formatting**: Black with default settings (88 characters)
- **Linting**: flake8 for style enforcement
- **Type Hints**: mypy for static type checking, prefer explicit types
- **Imports**: Follow PEP 8, group imports (standard, third-party, local)

## Testing & Validation
```bash
# Run full test suite
pytest

# Run with coverage report
pytest --cov --cov-report=html

# Test specific module
pytest tests/test_middleware.py

# Run tests with verbose output
pytest -v
```

## Environment Setup
Required environment variables:
```bash
REVENIUM_METERING_API_KEY=your-revenium-key
# Optional: For running tests
REVENIUM_METERING_BASE_URL=https://api.revenium.io/meter
```

## Pull Request Guidelines
- Include type hints for all new functions and methods
- Add tests with good coverage for new functionality
- Follow PEP 8 style guidelines
- Update documentation for API changes
- Ensure compatibility with Python 3.8+

## Security Notes
- Never log API keys or credentials in code
- Ensure no PII is sent unless explicitly configured for billing
- Always fail gracefully - never break the underlying API calls
- Use environment variables for all sensitive configuration

## Common Issues
1. **Import errors**: Ensure package installed with `pip install -e .`
2. **Missing dependencies**: Install dev dependencies with `pip install -e .[dev]`
3. **Test failures**: Check environment variables are set correctly

## Questions?
- Check README.md for complete installation and usage examples
- Visit https://docs.revenium.io for documentation
- Email support@revenium.io for questions