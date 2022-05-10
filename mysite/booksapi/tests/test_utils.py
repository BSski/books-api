from django.test import TestCase

from booksapi.utils import fetch_json_from_google_api


class UtilsTest(TestCase):
    def test_fetch_json_from_google_api(self):
        self.assertTrue(isinstance(fetch_json_from_google_api("hobbit"), dict))
