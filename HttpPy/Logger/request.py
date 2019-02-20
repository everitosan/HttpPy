# Python
import json
# Modules
from .generics import log_success, log_main

def __parse_body(response):
    content_type = response.headers.get('Content-Type')
    if response.text and content_type:
        if "application/json" in content_type:
            return json.dumps(json.loads(response.text), indent=2)
        else:
            return response.text
    return ""

def log_request(req, verbose: bool=False) -> None:
    log_data = []
    url = req.url
    method = req.method
    log_data.append("=====> ")
    log_data.append("Making {} request to: {} \n".format(method, url))

    if verbose:
        headers = req.headers
        body = req.body
        title = req.title

        if title is not None:
            log_data.insert(0,"\n{} \n".format("-"*8) )
            log_data.insert(1, "{}{} \n".format("-"*8, title.upper()))
            log_data.insert(2,"{} \n".format("-"*8) )

        if headers is not None:
            log_data.append("HEADERS: {}\n".format(str(headers)))
        if body is not None:
            json_body = body.decode("utf-8")
            log_data.append("BODY: {}\n".format(json_body))

    log_main("".join(log_data))

def log_request_response(response, verbose=False):
    log_data = []

    if not verbose:
        log_data.append("<===== ")
        log_data.append("{}\n".format(response.status_code))
        log_success("".join(log_data))
    else:
        __print_request_part("[{}] {}".format(response.status_code, response.url), "response")
        __print_request_part(response.headers, "headers")
        __print_request_part(__parse_body(response), "body")


def __print_request_part(data, part):
    __print_request_part_header(part)
    print(data)

def __print_request_part_header(part="extra"):
    log_success("-"*30, end="")
    log_success(" {} ".format(part.upper()), end="")
    log_success("-"*30, flush=True)
