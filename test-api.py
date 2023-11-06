from unittest import TestCase
from Yandexapi_test import folder_creation, folder_creation_status

class TestApi(TestCase):
    def test_creation_folder(self):
        response = folder_creation()
        expected = 'papka sozdana'
        self.assertEqual(response, expected)

    def test_negative(self):
        response = folder_creation_status()
        expected = '409'
        self.assertEqual(response, expected)
