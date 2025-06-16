# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventCreateParams"]


class EventCreateParams(TypedDict, total=False):
    payload: Required[Dict[str, object]]
    """The rating payload as a JSON object.

    For example, if you are sending key value pairs of 'requestTokens' and
    'responseTokens' with values of '1' and '2' respectively, the payload would be {
    "requestTokens": "1", "responseTokens": "2"}. If these keys do not already exist
    in Revenium, each key you send will be configured as a metering element on the
    relevant data source.
    """

    source_type: Required[
        Annotated[
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
    ]
    """the source type"""

    transaction_id: Required[Annotated[str, PropertyInfo(alias="transactionId")]]
    """The unique identifier of the metering event"""

    source_id: Annotated[str, PropertyInfo(alias="sourceId")]
    """the sourceId"""

    subscriber_credential: Annotated[str, PropertyInfo(alias="subscriberCredential")]
    """The unique identifier of the credential"""
