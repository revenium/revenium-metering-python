# Events

Types:

```python
from revenium_metering.types import MeteringResponseResource
```

Methods:

- <code title="post /v2/events">client.events.<a href="./src/revenium_metering/resources/events.py">create</a>(\*\*<a href="src/revenium_metering/types/event_create_params.py">params</a>) -> <a href="./src/revenium_metering/types/metering_response_resource.py">MeteringResponseResource</a></code>

# APIs

Methods:

- <code title="post /v2/apis/requests">client.apis.<a href="./src/revenium_metering/resources/apis.py">meter_request</a>(\*\*<a href="src/revenium_metering/types/api_meter_request_params.py">params</a>) -> <a href="./src/revenium_metering/types/metering_response_resource.py">MeteringResponseResource</a></code>
- <code title="post /v2/apis/responses">client.apis.<a href="./src/revenium_metering/resources/apis.py">meter_response</a>(\*\*<a href="src/revenium_metering/types/api_meter_response_params.py">params</a>) -> <a href="./src/revenium_metering/types/metering_response_resource.py">MeteringResponseResource</a></code>

# AI

Methods:

- <code title="post /v2/ai/completions">client.ai.<a href="./src/revenium_metering/resources/ai.py">create_completion</a>(\*\*<a href="src/revenium_metering/types/ai_create_completion_params.py">params</a>) -> <a href="./src/revenium_metering/types/metering_response_resource.py">MeteringResponseResource</a></code>
