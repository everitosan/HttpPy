import requests
from Arguments import parse as parse_arguments
from ParseRequest import parse_file, parse_args as parse_req_args


def make_requests(requests_list):
    for req in requests_list:
        type = req["type"]
        url = req["url"]
        req_fn = getattr(requests, type)
        if type == "get" or type == "delete":
            res = req_fn(url=url)
        else:
            try:
                data = req["data"]
                res = req_fn(url=url, data=data)
            except KeyError:
                res = req_fn(url)
        print(res)


def main():
    args = parse_arguments()
    if args.i:
        requests = parse_file(args.i)
    else:
        requests = [parse_req_args(args)]

    make_requests(requests)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("bye bye!")
