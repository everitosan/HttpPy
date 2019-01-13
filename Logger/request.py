def log_request(response, verbose=False):
    if not verbose:
        print(response.status_code)
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
