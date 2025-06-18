# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["MeteringResponseResource", "_Links"]


class _Links(BaseModel):
    deprecation: Optional[str] = None

    href: Optional[str] = None

    hreflang: Optional[str] = None

    name: Optional[str] = None

    profile: Optional[str] = None

    templated: Optional[bool] = None

    title: Optional[str] = None

    type: Optional[str] = None


class MeteringResponseResource(BaseModel):
    id: str
    """Unique identifier for the metering response"""

    label: str
    """A descriptive label for the metering response"""

    resource_type: str = FieldInfo(alias="resourceType")
    """Type of the object, typically 'metering'"""

    signature: str
    """Signature used for validating the response data"""

    api_links: Optional[Dict[str, _Links]] = FieldInfo(alias="_links", default=None)

    created: Optional[str] = None
    """ISO8601 formatted timestamp when the response was created"""

    updated: Optional[str] = None
    """ISO8601 formatted timestamp when the response was last updated"""
