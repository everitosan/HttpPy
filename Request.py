# Python
import requests

# Modules
from Logger import log_request, log_request_response

def make_request(req, verbose=False):
    res = None
    type = req.get("type")
    url = req.get("url")
    headers = req.get("headers")
    data = req.get("data")

    req_fn = getattr(requests, type)

    log_request(req, verbose)

    try:
        if type in ["get", "delete"]:
            res = req_fn(url)
        else:
            res = req_fn(url, data=data, headers=headers)
            # if data is not None:
            #     res = req_fn(url, data=data)
            # else:
                # res = req_fn(url)
        log_request_response(res, verbose)
    except requests.exceptions.ConnectionError as error:
        print("[X] Connection Error")
        print(error)
