# Stubs for falcon.testing.srmock (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class StartResponseMock:
    status: Any = ...
    headers: Any = ...
    exc_info: Any = ...
    def __init__(self) -> None: ...
    headers_dict: Any = ...
    def __call__(self, status: Any, headers: Any, exc_info: Optional[Any] = ...) -> None: ...
    @property
    def call_count(self): ...
