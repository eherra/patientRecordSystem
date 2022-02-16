import unittest
from utils.validators.models.settings_user import SettingsUser

class SettingsUserTest(unittest.TestCase):
    def test_correct_form_given_not_raising_error(self):
        validated_user = SettingsUser(valid_test_form)
        self.assertIsNotNone(validated_user)

    def test_correct_form_empty_with_values(self):
        validated_user = SettingsUser(empty_valid_values)
        self.assertIsNotNone(validated_user)
    
    def test_correct_with_phone_prefix(self):
        validated_user = SettingsUser(phone_valid_prefix_test_form)
        self.assertIsNotNone(validated_user)
        self.assertEquals(validated_user.phone, '+4531231251323')

    def test_fails_with_incorrect_email(self):
        with self.assertRaises(ValueError):
            validated_user = SettingsUser(email_not_valid_test_form)
            self.assertIsNone(validated_user)

    def test_fails_with_incorrect_phone(self):
        with self.assertRaises(ValueError):
            validated_user = SettingsUser(phone_not_valid_test_form)
            self.assertIsNone(validated_user)

    def test_fails_with_too_long_address(self):
        with self.assertRaises(ValueError):
            validated_user = SettingsUser(address_not_valid_test_form)
            self.assertIsNone(validated_user)

    def test_fails_when_country_is_missing(self):
        with self.assertRaises(KeyError):
            validated_user = SettingsUser(country_missing_not_valid_test_form)
            self.assertIsNone(validated_user)

    def test_fails_when_phone_is_missing(self):
        with self.assertRaises(KeyError):
            validated_user = SettingsUser(phone_empty_not_valid_test_form)
            self.assertIsNone(validated_user)

# Test data
valid_test_form = {
    'name': 'testName',
    'email': 'test@hotmail.com',
    'phone': '0406412123123',
    'address': 'Testikuja 5B',
    'city': 'Bali',
    'country': 'Indonesia'
}

# Phone having no prefix + on phone -> valid
phone_valid_prefix_test_form = {
    'name': 'testName',
    'email': 'test@hotmail.com',
    'phone': '+4531231251323',
    'address': 'Testikuja 5B',
    'city': 'Bali',
    'country': 'Indonesia'
}

# Empty values => user not wanting to modify anything
empty_valid_values = {
    'name': '',
    'email': '',
    'phone': '',
    'address': '',
    'city': '',
    'country': ''
}

# Email missing "@"
email_not_valid_test_form = {
    'name': 'testName',
    'email': 'testhotmail.com',
    'phone': '+356412123123',
    'address': 'Testikuja 5B',
    'city': 'Bali',
    'country': 'Indonesia'
}

# Phone having illegal characters
phone_not_valid_test_form = {
    'name': 'testName',
    'email': 'test@hotmail.com',
    'phone': '3XXXX6412123123',
    'address': 'Testikuja 5B',
    'city': 'Bali',
    'country': 'Indonesia'
}

# Address value too long
address_not_valid_test_form = {
    'name': 'testName',
    'email': 'test@hotmail.com',
    'phone': '3XXXX6412123123',
    'address': 'Testikuja 5Testikuja 5BTestikuja 5BTestikuja 5BTestikuja 5BTestikuja 5BTestikuja 5BTestikuja 5BTestikuja 5BTestikuja 5BB',
    'city': 'Bali',
    'country': 'Indonesia'
}

# country key missing
country_missing_not_valid_test_form = {
    'name': 'testName',
    'email': 'test@hotmail.com',
    'phone': '31231236412123123',
    'address': 'Testikuja 5B',
    'city': 'Bali',
}

# Phone key missing
phone_empty_not_valid_test_form = {
    'name': 'testName',
    'email': 'test@hotmail.com',
    'address': 'Testikuja 5',
    'city': 'Bali',
    'country': 'Indonesia'
}