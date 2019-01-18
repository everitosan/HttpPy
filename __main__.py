from Request import make_request
from Arguments import parse as parse_arguments
from ParseRequest import ParseRequest, parse_args as parse_req_args
from Logger import log_accent

from time import time


args = parse_arguments()

def make_requests(requests_list):
    for req in requests_list:
        make_request(req, args.verbose)

def main():
    if args.input:
        parser = ParseRequest()
        requests = parser.parse_file(args.input)
    else:
        requests = [parse_req_args(args)]

    make_requests(requests)


if __name__ == "__main__":
    try:
        start_time = time()
        main()
        elapsed_time = time()-start_time
        log_accent("\nRequests made in: {} s".format(elapsed_time))

    except KeyboardInterrupt:
        print("bye bye!")
