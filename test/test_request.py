# Python
import unittest
# Modules
from HttpPy.ParseRequest import ParseRequest
from HttpPy.Request import make_request


class TestRequest(unittest.TestCase):
    def __test_info_match(self,original_request, made_request):
        self.assertEqual(made_request.title, original_request.get('title'))
        self.assertEqual(made_request.url, original_request.get('url'))
        self.assertEqual(made_request.method.lower(), original_request.get('type').lower())

    def test_get_request(self):
        parser = ParseRequest()
        get_requests = parser.parse_file("test/get.request")
        original_request = get_requests[0]
        made_request = None

        res = make_request(original_request, should_log=False)
        made_request = res.request

        self.__test_info_match(original_request, made_request)


    def test_post_request(self):
        parser = ParseRequest()
        post_requests = parser.parse_file("test/post.request")
        original_request = post_requests[0]
        made_request = None

        res = make_request(original_request, should_log=False)
        made_request = res.request

        self.__test_info_match(original_request, made_request)
        self.assertEqual(made_request.body, None)
        self.assertNotEqual(res.text, None)
