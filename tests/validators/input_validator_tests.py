import unittest
from utils.validators.input_validator import is_valid_future_date, is_valid_input

class InputValidatorTest(unittest.TestCase):

    def test_is_input_valid_works_with_true(self):
        self.assertTrue(is_valid_input("ten_letter", 10))
        self.assertTrue(is_valid_input("h", 50))
        self.assertTrue(is_valid_input("testing", 100))
        self.assertTrue(is_valid_input("testing", 200))

    def test_is_input_valid_works_with_false(self):
        self.assertFalse(is_valid_input("testing", 1))
        self.assertFalse(is_valid_input("ten_letter", 5))
        self.assertFalse(is_valid_input(None, 100))
        self.assertFalse(is_valid_input("", 200))

    # test cases expires 2050 :)
    def test_is_valid_date_works_with_true(self):
        self.assertTrue(is_valid_future_date("2050-11-11 11:15"))
        self.assertTrue(is_valid_future_date("2050-01-01 17:00"))
        self.assertTrue(is_valid_future_date("2050-11-11 11:15"))
        self.assertTrue(is_valid_future_date("2052-02-29 15:00"))

    def test_is_valid_date_works_with_false(self):
        self.assertFalse(is_valid_future_date("2000-12-01 11:15"))
        self.assertFalse(is_valid_future_date("2022-01-01 17:00"))
        self.assertFalse(is_valid_future_date("1994-11-11 11:15"))
        self.assertFalse(is_valid_future_date(None))
        self.assertFalse(is_valid_future_date("not date"))