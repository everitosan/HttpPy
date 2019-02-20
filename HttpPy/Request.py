# Python
import requests
from threading import Lock

# Modules
from .Logger import log_request, log_request_response, log_error, log_warning

lock_print = Lock()

def make_request(req: dict, should_log: bool=True):
    res = None
    type = req.get("type")
    url = req.get("url")
    headers = req.get("headers")
    body = req.get("body")
    verbose = req.get("verbose")

    req_fn = getattr(requests, type, None)
    if req_fn is None:
        log_warning("[!] Method {} is not valid".format(type))
    else:

        try:
            if type in ["get", "delete"]:
                res = req_fn(url, headers=headers)
            else:
                res = req_fn(url, json=body, headers=headers)

            res.request.title = req.get("title")

            if should_log:
                with lock_print:
                    log_request(res.request, verbose)
                    log_request_response(res, verbose)
            return res
        except requests.exceptions.ConnectionError as error:
            log_error("[X] Connection Error")
            log_error(error)
