# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventCreateParams"]


class EventCreateParams(TypedDict, total=False):
    payload: Required[Dict[str, object]]
    """
    The rating payload as a JSON object containing key-value pairs representing
    usage metrics to track. For example, a SaaS application might send: {
    "storageGB": 15.5, "apiCalls": 1250, "computeMinutes": 480 }. If these keys do
    not already exist in Revenium, each key you send will be automatically
    configured as a metering element on the relevant data source.
    """

    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]
    """The unique identifier of the metering event"""

    source_id: Annotated[str, PropertyInfo(alias="sourceId")]
    """
    Optional identifier for the source that represents the feature under which usage
    charges should be tracked. In the events endpoint, sources typically represent
    categories for billable units such as features, services, or resources (e.g.,
    'storageCharges' or 'CpuCharges'). If you wish for the key value pairs you send
    to be automatically applied to a source that is used in a product to calculate
    usage-based revenue, you should specify the relevant sourceId here. Sources must
    be pre-configured in the Revenium platform. The ID can be found on the sources
    page or retrieved via the list sources endpoint.
    """

    source_type: Annotated[
        Literal[
            "UNKNOWN",
            "AI",
            "SDK_PYTHON",
            "SDK_JS",
            "SDK_JVM",
            "SDK_SPRING",
            "SDK_DOTNET",
            "SDK_GOLANG",
            "SDK_RUST",
            "EBPF",
            "AWS",
            "AZURE",
            "SNOWFLAKE",
            "KONG",
            "GRAVITEE",
            "MULESOFT",
            "BOOMI",
            "REVENIUM",
            "INTERNAL",
        ],
        PropertyInfo(alias="sourceType"),
    ]
    """Specifies the originating SDK or gateway of the metered event traffic.

    This is used for Revenium analytics only, and does not affect how Revenium
    processes and categorizes incoming metrics. Optional - defaults to 'UNKNOWN' if
    not specified.
    """

    subscriber_credential: Annotated[str, PropertyInfo(alias="subscriberCredential")]
    """
    Optional unique identifier for the subscriber/customer associated with this
    usage event. This credential maps the metered usage to a specific subscription
    and its associated product pricing rules. Can be any unique identifier from your
    system (customer ID, subscription ID, API key, etc.) that you've configured as a
    subscriber credential in the Revenium platform. Visible on the subscriber
    credentials page in Revenium.
    """
