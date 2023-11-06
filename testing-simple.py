from unittest import TestCase
from tests_module import get_key, stats, maximum, converter, ids, country, geo_logs


class Testkey(TestCase):
    def test_key(self):
        response = get_key(stats, maximum)
        expected = 'yandex'
        self.assertEqual(response, expected)

class TestConvertor(TestCase):
    def test_convert(self):
        response = converter(ids)
        expected = {213,15}
        self.assertEqual(response, expected)

class TestCountryFunc(TestCase):
    def test_country_func(self):
        response = country(geo_logs)
        expected = ['Архангельск', 'Россия']
        self.assertEqual(response, expected)
        
