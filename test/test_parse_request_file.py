# Python
import unittest
# Modules
from ParseRequestFile import parse as parse_file


requests = parse_file("test/test.request")


class TestParseRequestFile(unittest.TestCase):
    def test_request_structure(self):
        self.assertIsInstance(requests, list)
        self.assertEqual(len(requests), 4)
