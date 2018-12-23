import requests
from ParseRequestFile import parse as parse_file
from Arguments import parse as parse_arguments
from ParseRequestFile import parse as parse_file


def make_requests(requests_list):
    for req in requests_list:
        type = req["type"]
        url = req["url"]
        req_fn = getattr(requests, type)
        if type == "get" or type == "delete":
            res = req_fn(url=url)
        else:
            data = req["data"]
            res = req_fn(url=url, data=data)
        print(res)

def main():
    args = parse_arguments()
    if args.i:
        requests = parse_file(args.i)
        make_requests(requests)
    else:
        print("args")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("bye bye!")
