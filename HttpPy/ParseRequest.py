# Python
import json
import re

# Exceptions
from .Exceptions.RequestDefinition import RequestDefinitionException
from .Exceptions.KeyValDefinition import KeyValDefinitionException

class ParseRequest(object):

    def __init__(self: object) -> None:
        self.requests = []
        self.request = {}
        # Flags
        self.request_start = False
        self.header_finished = False
        self.body_finished = False
        # Patterns
        self.break_line_pattern = re.compile("\n")
        self.spaces_pattern= re.compile(" ")

    def __append_request(self: object) -> None:
        self.requests.append(self.request)
        self.request = {}
        self.header_finished = False
        self.body_finished = False
        self.request_start = False

    def __clean_line(self: object, line: str) -> str:
        return re.sub(self.break_line_pattern, "", line)

    def __is_request_defined(self: object, line: str) -> tuple:
        if "## " in line:
            return (True, line.split("## ")[1])
        else:
             return (False, None)

    def __normalize_request(self: object, line: str) -> tuple:
        type_url = line.split(" ")
        if len(type_url) != 2:
            raise RequestDefinitionException("[GET, POST, PUT, PATCH, DELETE] URL format is required after a request definition")
        return (
            type_url[0].lower(),
            type_url[1].lower()
        )

    def __parse_key_val_line(self: object, line: str, type: str) -> tuple:
        no_spaces_line = re.sub(self.spaces_pattern, "", line)
        no_quotes_line = re.sub(r"\"", "", no_spaces_line)
        header_key_val = no_quotes_line.split(":")
        if len(header_key_val) == 2:
            return (header_key_val[0], header_key_val[1])

    def __check_is_empty(self: object, line: str) -> bool:
        return line == "\n" or line == ""

    def __check_header_starts(self: object, line: str) -> bool:
        return "HEADER" in line.upper()

    def __check_body_starts(self: object, line:str) -> bool:
        return "{" in line

    def __check_body_ends(self: object, line: str) -> bool:
        return "}" in line

    def __add_remanent_request(self: object) -> None:
        if len(self.request.values()) > 0:
            self.__append_request()

    def parse_file(self: object, file_path: str, verbose: bool=False) -> list:
        file = open(file_path)

        for raw_line in file.readlines():
            line = self.__clean_line(raw_line)
            request_start, title = self.__is_request_defined(line)
            if request_start:
                self.__add_remanent_request()
                self.request = { "title": title, "verbose": verbose }
                self.request_start = request_start

            if self.request_start and not request_start:
                ## Request was detected previuosly
                current_request = self.request

                type = current_request.get("type")
                header = current_request.get("headers")
                body = current_request.get("body")

                if type is None:
                    http_verb, url = self.__normalize_request(line)
                    current_request["type"] = http_verb
                    current_request["url"] = url

                if header is None and self.__check_header_starts(line):
                    current_request["headers"] = {}
                elif header is not None and not self.header_finished:
                    if  not self.__check_is_empty(line) and not self.__check_body_starts(line) :
                        key, val = self.__parse_key_val_line(line, "header")
                        current_request["headers"][key] =  val
                    else:
                        self.header_finished = True

                if body is None and self.__check_body_starts(line):
                        current_request["body"] = line
                elif body is not None and not self.body_finished:
                    current_request["body"] += line
                    if self.__check_body_ends(line):
                        current_request["body"] = json.loads(current_request["body"])
                        self.body_finished = True
                        ## adds request to list
                        self.__append_request()


        self.__add_remanent_request()
        return self.requests


def parse_args(args):
    req = {
        "type": args.type,
        "url": args.url
    }
    if args.data:
        req["data"] = json.loads(args.data)
    if args.verbose:
        req["verbose"] = True
    return req
