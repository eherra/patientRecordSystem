import unittest
from utils.validators.models.registration_user import RegistrationUser

class RegistrationUserTest(unittest.TestCase):
    def test_correct_form_given_not_raising_error(self):
        validated_user = RegistrationUser(valid_test_form)
        self.assertIsNotNone(validated_user)

    def test_correct_and_is_doctor_value_true(self):
        validated_user = RegistrationUser(valid_test_form)
        self.assertIsNotNone(validated_user)
        self.assertTrue(validated_user._is_doctor)
    
    def test_correct_with_phone_prefix(self):
        validated_user = RegistrationUser(phone_valid_prefix_test_form)
        self.assertIsNotNone(validated_user)
        self.assertEquals(validated_user.phone, '+4531231251323')

    def test_correct_and_is_doctor_value_false(self):
        validated_user = RegistrationUser(phone_valid_prefix_test_form)
        self.assertIsNotNone(validated_user)
        self.assertFalse(validated_user._is_doctor)

    def test_fails_with_too_short_username(self):
        with self.assertRaises(ValueError):
            validated_user = RegistrationUser(too_short_username)
            self.assertIsNone(validated_user)

    def test_fails_with_too_short_password(self):
        with self.assertRaises(ValueError):
            validated_user = RegistrationUser(too_short_password)
            self.assertIsNone(validated_user)

    def test_fails_with_missing_value(self):
        with self.assertRaises(ValueError):
            validated_user = RegistrationUser(empty_name_value)
            self.assertIsNone(validated_user)

    def test_fails_with_incorrect_email(self):
        with self.assertRaises(ValueError):
            validated_user = RegistrationUser(email_not_valid_test_form)
            self.assertIsNone(validated_user)

    def test_fails_with_incorrect_phone(self):
        with self.assertRaises(ValueError):
            validated_user = RegistrationUser(phone_not_valid_test_form)
            self.assertIsNone(validated_user)

    def test_fails_with_too_long_address(self):
        with self.assertRaises(ValueError):
            validated_user = RegistrationUser(address_not_valid_test_form)
            self.assertIsNone(validated_user)

    def test_fails_when_country_is_missing(self):
        with self.assertRaises(KeyError):
            validated_user = RegistrationUser(country_missing_not_valid_test_form)
            self.assertIsNone(validated_user)

    def test_fails_when_phone_is_missing(self):
        with self.assertRaises(KeyError):
            validated_user = RegistrationUser(phone_empty_not_valid_test_form)
            self.assertIsNone(validated_user)

# Test data
valid_test_form = {
    'username': 'testUsername',
    'password': 'testPassword',
    'options': 'doctor',

    'name': 'testName',
    'email': 'test@hotmail.com',
    'phone': '0406412123123',
    'address': 'Testikuja 5B',
    'city': 'Bali',
    'country': 'Indonesia'
}

# Phone having no prefix + on phone -> valid
phone_valid_prefix_test_form = {
    'username': 'testUsername',
    'password': 'testPassword',
    'options': 'patient',

    'name': 'testName',
    'email': 'test@hotmail.com',
    'phone': '+4531231251323',
    'address': 'Testikuja 5B',
    'city': 'Bali',
    'country': 'Indonesia'
}

too_short_username = {
    'username': 'as',
    'password': 'testPassword',
    'options': 'doctor',

    'name': '',
    'email': 'test@hotmail.com',
    'phone': '+4531231251323',
    'address': 'Testikuja 5B',
    'city': 'Bali',
    'country': 'Indonesia'
}

too_short_password = {
    'username': 'testUsername',
    'password': 'jeep',
    'options': 'doctor',

    'name': '',
    'email': 'test@hotmail.com',
    'phone': '4531231251323',
    'address': 'Testikuja 5B',
    'city': 'Bali',
    'country': 'Indonesia'
}

# Empty name value
empty_name_value = {
    'username': 'testUsername',
    'password': 'testPassword',
    'options': 'doctor',

    'name': '',
    'email': 'test@hotmail.com',
    'phone': '4531231251323',
    'address': 'Testikuja 5B',
    'city': 'Bali',
    'country': 'Indonesia'
}

# Email missing "@"
email_not_valid_test_form = {
    'username': 'testUsername',
    'password': 'testPassword',
    'options': 'doctor',

    'name': 'testName',
    'email': 'testhotmail.com',
    'phone': '+356412123123',
    'address': 'Testikuja 5B',
    'city': 'Bali',
    'country': 'Indonesia'
}

# Phone having illegal characters
phone_not_valid_test_form = {
    'username': 'testUsername',
    'password': 'testPassword',
    'options': 'doctor',

    'name': 'testName',
    'email': 'test@hotmail.com',
    'phone': '3XXXX6412123123',
    'address': 'Testikuja 5B',
    'city': 'Bali',
    'country': 'Indonesia'
}

# Address value too long
address_not_valid_test_form = {
    'username': 'testUsername',
    'password': 'testPassword',
    'options': 'doctor',

    'name': 'testName',
    'email': 'test@hotmail.com',
    'phone': '3XXXX6412123123',
    'address': 'Testikuja 5Testikuja 5BTestikuja 5BTestikuja 5BTestikuja 5BTestikuja 5BTestikuja 5BTestikuja 5BTestikuja 5BTestikuja 5BB',
    'city': 'Bali',
    'country': 'Indonesia'
}

# country key missing
country_missing_not_valid_test_form = {
    'username': 'testUsername',
    'password': 'testPassword',
    'options': 'doctor',

    'name': 'testName',
    'email': 'test@hotmail.com',
    'phone': '31231236412123123',
    'address': 'Testikuja 5B',
    'city': 'Bali',
}

# Phone key missing
phone_empty_not_valid_test_form = {
    'username': 'testUsername',
    'password': 'testPassword',
    'options': 'doctor',

    'name': 'testName',
    'email': 'test@hotmail.com',
    'address': 'Testikuja 5',
    'city': 'Bali',
    'country': 'Indonesia'
}