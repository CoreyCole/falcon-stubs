# Stubs for falcon.request (Python 3.7)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

NativeStream: Any
SimpleCookie: Any
DEFAULT_ERROR_LOG_FORMAT: str
TRUE_STRINGS: Any
FALSE_STRINGS: Any
WSGI_CONTENT_HEADERS: Any
strptime: Any
now: Any


class Request:
    context_type: Any = ...
    env: Any = ...
    options: Any = ...
    method: Any = ...
    uri_template: Any = ...
    path: Any = ...
    query_string: Any = ...
    content_type: Any = ...
    stream: Any = ...
    context: Any = ...

    def __init__(self, env: Any, options: Optional[Any] = ...) -> None: ...
    user_agent: Any = ...
    auth: Any = ...
    expect: Any = ...
    referer: Any = ...

    @property
    def forwarded(self): ...

    @property
    def client_accepts_json(self): ...

    @property
    def client_accepts_msgpack(self): ...

    @property
    def client_accepts_xml(self): ...

    @property
    def accept(self): ...

    @property
    def content_length(self): ...

    @property
    def bounded_stream(self): ...

    @property
    def date(self): ...

    @property
    def if_modified_since(self): ...

    @property
    def if_unmodified_since(self): ...

    @property
    def range(self): ...

    @property
    def range_unit(self): ...

    @property
    def app(self): ...

    @property
    def scheme(self): ...

    @property
    def forwarded_scheme(self): ...
    protocol: Any = ...

    @property
    def uri(self): ...
    url: Any = ...

    @property
    def forwarded_uri(self): ...

    @property
    def relative_uri(self): ...

    @property
    def prefix(self): ...

    @property
    def forwarded_prefix(self): ...

    @property
    def host(self): ...

    @property
    def forwarded_host(self): ...

    @property
    def subdomain(self): ...

    @property
    def headers(self): ...

    @property
    def params(self): ...

    @property
    def cookies(self): ...

    @property
    def access_route(self): ...

    @property
    def remote_addr(self): ...

    @property
    def port(self): ...

    @property
    def netloc(self): ...

    @property
    def media(self): ...

    def client_accepts(self, media_type: Any): ...

    def client_prefers(self, media_types: Any): ...

    def get_header(self, name: Any, required: bool = ..., default: Optional[Any] = ...): ...

    def get_header_as_datetime(self, header: Any, required: bool = ..., obs_date: bool = ...): ...

    def get_param(self, name: Any, required: bool = ..., store: Optional[Any] = ..., default: Optional[Any] = ...): ...

    def get_param_as_int(self, name: Any, required: bool = ...,
                         min: Optional[Any] = ..., max: Optional[Any] = ..., store: Optional[Any] = ...): ...

    def get_param_as_uuid(self, name: Any, required: bool = ..., store: Optional[Any] = ...): ...

    def get_param_as_bool(self, name: Any, required: bool = ..., store: Optional[Any] = ..., blank_as_true: bool = ...): ...

    def get_param_as_list(self, name: Any, transform: Optional[Any] = ..., required: bool = ..., store: Optional[Any] = ...): ...

    def get_param_as_datetime(self, name: Any, format_string: str = ..., required: bool = ..., store: Optional[Any] = ...): ...

    def get_param_as_date(self, name: Any, format_string: str = ..., required: bool = ..., store: Optional[Any] = ...): ...

    def get_param_as_json(self, name: Any, required: bool = ..., store: Optional[Any] = ...): ...
    get_param_as_dict: Any = ...

    def log_error(self, message: Any) -> None: ...


class RequestOptions:
    keep_blank_qs_values: bool = ...
    auto_parse_form_urlencoded: bool = ...
    auto_parse_qs_csv: bool = ...
    strip_url_path_trailing_slash: bool = ...
    default_media_type: Any = ...
    media_handlers: Any = ...

    def __init__(self) -> None: ...
