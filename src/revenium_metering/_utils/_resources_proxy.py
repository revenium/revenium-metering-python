from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `revenium_metering.resources` module.

    This is used so that we can lazily import `revenium_metering.resources` only when
    needed *and* so that users can just import `revenium_metering` and reference `revenium_metering.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("revenium_metering.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
