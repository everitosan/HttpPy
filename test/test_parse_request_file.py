# Python
import unittest
# Modules
from HttpPy.ParseRequest import ParseRequest


parser = ParseRequest()
requests = parser.parse_file("test/test.request")

class TestParseRequestFile(unittest.TestCase):
    def test_check_header_is_present_in_line(self):
        line = "header"
        is_present = parser._ParseRequest__check_header_starts(line)
        self.assertTrue(is_present)

    def test_request_structure(self):
        self.assertIsInstance(requests, list)
        self.assertEqual(len(requests), 4)

    def __test_request(self, req_to_test, data={}):
        self.assertIsInstance(req_to_test, dict)
        # print(data.items())
        for key, value in data.items():
            self.assertEqual(req_to_test[key], value)

    def test_first_get_request(self):
        self.__test_request(requests[0], {
            "type": "get",
            "url": "http://127.0.0.1:8000"
        })

    def test_second_post_request(self):
        self.__test_request(requests[1], {
            "type": "post",
            "url": "http://127.0.0.1:8000"
        })

    def test_third_post_request(self):
        self.__test_request(requests[2], {
            "type": "post",
            "url": "http://127.0.0.1:8000",
            "body": {"id": 2, "user": "ever", "password": "12345"}
        })

    def test_fourth_get_request(self):
        self.__test_request(requests[3], {
            "type": "get",
            "url": "http://127.0.0.1:3000"
        })
