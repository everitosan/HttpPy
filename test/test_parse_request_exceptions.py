# Python
import unittest
# Modules
from HttpPy.ParseRequest import ParseRequest


class TestExceptionsParseRequestFile(unittest.TestCase):
    def test_after_request_definition(self):
        """
        The next line after a request title '## ', should be the request definition:
        REQUEST_VERB URL
        REQUEST_VERB = [GET, POST, PATCH, PUT, DELETE]
        URL = http or https url
        """
        pass
        # file_path = "test/test.bad.request"
        # parser = ParseRequest()
        # self.assertRaises(Exception, parser.parse_file(file_path))
