# Stubs for falcon.routing.converters (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class BaseConverter:
    def convert(self, value: Any) -> None: ...

class IntConverter(BaseConverter):
    def __init__(self, num_digits: Optional[Any] = ..., min: Optional[Any] = ..., max: Optional[Any] = ...) -> None: ...
    def convert(self, value: Any): ...

class DateTimeConverter(BaseConverter):
    def __init__(self, format_string: str = ...) -> None: ...
    def convert(self, value: Any): ...

class UUIDConverter(BaseConverter):
    def convert(self, value: Any): ...
