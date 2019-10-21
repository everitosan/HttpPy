# Python
from concurrent.futures import ThreadPoolExecutor
# Modules
from .Request import make_request_args
from .Arguments import parse as parse_arguments
from .ParseRequest import ParseRequest, parse_args as parse_req_args

# Packages
from .decorators.timming import timming


def make_requests(requests_list, parallel=False):
    if parallel:
        with ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(make_request_args, requests_list)
    else:
        for req in requests_list:
            make_request_args(req)


@timming
def main():
    args = parse_arguments()
    if args.input:
        parser = ParseRequest()
        requests = parser.parse_file(args.input, args.verbose)
    else:
        requests = [parse_req_args(args)]

    make_requests(requests, args.parallel)


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print("bye bye!")
