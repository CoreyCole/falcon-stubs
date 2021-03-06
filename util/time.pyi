# Stubs for falcon.util.time (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import datetime
from typing import Any

class TimezoneGMT(datetime.tzinfo):
    GMT_ZERO: Any = ...
    def utcoffset(self, dt: Any): ...
    def tzname(self, dt: Any): ...
    def dst(self, dt: Any): ...
