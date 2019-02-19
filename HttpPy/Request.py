# Python
import requests
from threading import Lock

# Modules
from .Logger import log_request, log_request_response, log_error, log_warning

lock_print = Lock()

def make_request(req):
    res = None
    type = req.get("type")
    url = req.get("url")
    headers = req.get("headers")
    data = req.get("data")
    verbose = req.get("verbose")

    req_fn = getattr(requests, type, None)
    if req_fn is None:
        log_warning("[!] Method {} is not valid".format(type))
    else:

        try:
            if type in ["get", "delete"]:
                res = req_fn(url, headers=headers)
            else:
                res = req_fn(url, json=data, headers=headers)
            with lock_print:
                log_request(req, verbose)
                log_request_response(res, verbose)
        except requests.exceptions.ConnectionError as error:
            log_error("[X] Connection Error")
            log_error(error)
