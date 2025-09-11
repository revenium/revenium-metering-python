# AI Development Guide

## Project Overview
Java/JVM SDK for direct access to Revenium's metering API. Provides comprehensive usage tracking for API calls, compute usage, database queries, and custom metrics with usage-based pricing integration.

## Development Environment Setup

### Prerequisites  
- Java 8+ (Java 11+ recommended)
- Maven 3.6+ or Gradle 6+
- IDE with Java support (IntelliJ IDEA, Eclipse, VS Code)

### Installation

#### Maven
```xml
<dependency>
    <groupId>io.revenium.metering</groupId>
    <artifactId>revenium-metering-sdk</artifactId>
    <version>1.0.0</version>
</dependency>
```

#### Gradle
```groovy
implementation 'io.revenium.metering:revenium-metering-sdk:1.0.0'
```

## Development Commands

```bash
# Maven
mvn clean compile    # Compile sources
mvn test            # Run tests
mvn package         # Build JAR
mvn clean install   # Install to local repository

# Gradle  
gradle clean build  # Clean and build
gradle test         # Run tests
gradle jar          # Build JAR
gradle publishToMavenLocal  # Publish to local repository
```

## Code Style Guidelines
- **Java Version**: Target Java 8 compatibility, use Java 11+ features when appropriate
- **Formatting**: Follow Google Java Style Guide or Oracle conventions
- **Documentation**: Use JavaDoc for all public methods and classes
- **Null Safety**: Prefer Optional<T> for nullable return values

## Testing & Validation
```bash
# Maven
mvn test                    # Run all tests
mvn test -Dtest=ClassName   # Run specific test class
mvn jacoco:report          # Generate code coverage

# Gradle
gradle test                 # Run all tests  
gradle test --tests ClassName  # Run specific test
gradle jacocoTestReport    # Generate coverage report
```

## Environment Setup
Required environment variables:
```bash
REVENIUM_API_KEY=your-revenium-api-key
REVENIUM_BASE_URL=https://api.revenium.io/meter/v1/api  # Optional: defaults to this URL
```

## Spring Boot Integration
```java
@Configuration
public class MeteringConfig {
    @Bean
    public DefaultApi meteringApi() {
        ApiClient client = new ApiClient();
        client.setBasePath("https://api.revenium.io/meter/v1/api");
        client.setApiKey(System.getenv("REVENIUM_API_KEY"));
        return new DefaultApi(client);
    }
}
```

## Pull Request Guidelines
- Include comprehensive JavaDoc for public APIs
- Add unit tests with good coverage (aim for >80%)
- Follow established coding patterns and conventions
- Ensure compatibility with Java 8+
- Include integration examples for new features

## Security Notes
- Never log API keys or credentials in code
- Use environment variables or secure configuration for sensitive data
- Ensure no PII is sent unless explicitly required for billing
- Always handle API exceptions gracefully

## Common Issues
1. **ClassNotFoundException**: Ensure dependency is properly added to build file
2. **Authentication errors**: Verify REVENIUM_API_KEY environment variable
3. **Build failures**: Check Java version compatibility (8+)

## Questions?
- Check README.md for complete installation and usage examples
- Review JavaDoc documentation for API details
- Email support@revenium.io for questions