def log_request(req: dict, verbose: bool=False) -> None:
    log_data = []

    url = req.get("url")
    log_data.append("=====> ")
    log_data.append("Making request to: {} \n".format(url))

    if verbose:
        headers = req.get("headers")
        body = req.get("body")
        title = req.get("title")

        log_data.insert(0,"\n{} \n".format("-"*8) )
        log_data.insert(1, "{}{} \n".format("-"*8, title.upper()))
        log_data.insert(2,"{} \n".format("-"*8) )

        if headers is not None:
            log_data.append("HEADERS: {}\n".format(str(headers)))
        if body is not None:
            log_data.append("BODY: {}\n".format(str(body)))

    print("".join(log_data), end="", flush=True)

def log_request_response(response, verbose=False):
    log_data = []
    if not verbose:
        log_data.append("<===== ")
        log_data.append("{}\n".format(response.status_code))
        print("".join(log_data), end="", flush=True)
    else:
        __print_request_part("[{}] {}".format(response.status_code, response.url), "response")
        __print_request_part(response.headers, "headers")
        __print_request_part(response.text, "body")


def __print_request_part(data, part):
    __print_request_part_header(part)
    print(data)

def __print_request_part_header(part="extra"):
    print("-"*30, end="")
    print(" {} ".format(part.upper()), end="")
    print("-"*30, flush=True)
