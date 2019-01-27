from colorama import init
from .request import log_request, log_request_response
from .generics import log_error, log_warning, log_accent, log_main, log_success

init()

__all__ = [
    log_main,
    log_success,
    log_accent,
    log_warning,
    log_error,
    log_request,
    log_request_response,
]
