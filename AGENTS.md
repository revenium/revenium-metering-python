# AI Development Guide

## Project Overview
This is a middleware library that automatically meters and monitors API usage, sending usage data to Revenium for billing and analytics.

## Development Commands

```bash
# Install dependencies
npm install

# Run tests  
npm test

# Build the project
npm run build

# Lint code
npm run lint

# Type check (TypeScript projects)
npm run typecheck
```

## Key Patterns

### Basic Usage
See README.md for complete installation and usage examples.

### Testing
- Mock external API calls in tests
- Test both success and error scenarios
- Validate that middleware doesn't break underlying API calls

## Security Notes
- Never log API keys or credentials
- Ensure no PII is sent unless explicitly configured for billing
- Always fail gracefully - never break the underlying API calls

## Common Issues
1. **No metering data**: Check environment variables and API keys
2. **Build/test errors**: Ensure dependencies are installed
3. **TypeScript errors**: Check imports and type definitions

## Questions?
- Check the README.md for detailed usage examples
- Open an issue for bugs or feature requests  
- Email support@revenium.io for questions