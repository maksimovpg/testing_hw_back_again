import unittest
from unittest.mock import patch
from what_is_year_now import what_is_year_now


class TestWhatIsYearNow(unittest.TestCase):

    def test_format_ymd(self):
        with patch('what_is_year_now.json.load') as mock_1:
            mock_1.return_value = {'currentDateTime': '2019-03-01'}
            self.assertEqual(what_is_year_now(), 2019)

    def test_format_dmy(self):
        with patch('what_is_year_now.json.load') as mock_2:
            mock_2.return_value = {'currentDateTime': '01.03.2019'}
            self.assertEqual(what_is_year_now(), 2019)

    def test_format_random(self):
        with patch('what_is_year_now.json.load') as mock_3:
            mock_3.return_value = {'currentDateTime': '2019/03/01'}
            with self.assertRaises(ValueError):
                what_is_year_now()
