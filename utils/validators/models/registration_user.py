import re
from services import users_service

class RegistrationUser:
    """Class validates user registration inputs from the form passed as a parameter."""
    def __init__(self, form):
        self.username = form["username"]
        self.password = form["password"]
        self.is_doctor = form["options"]

        self.name = form["name"]
        self.email = form["email"]
        self.phone = form["phone"]
        self.address = form["address"]
        self.city = form["city"]
        self.country = form["country"]

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if len(value) < 3 or len(value) > 40 or value.isspace():
            raise ValueError("Username should be 3-40 characters!")

        if users_service.is_username_taken(value):
            raise ValueError("Username not unique. Try other one!")

        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if len(value) < 5 or value.isspace():
            raise ValueError("Password too short!")
        self._password = value

    @property
    def is_doctor(self):
        return self._is_doctor

    @is_doctor.setter
    def is_doctor(self, value):
        if not value:
            raise ValueError("Role (doctor/patient) not existing!")
        self._is_doctor = value == "doctor"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 3 or len(value) > 40 or value.isspace():
            raise ValueError("Full name should be 3-40 characters.")
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        regex = "^.+@.{3,40}"
        if not re.match(regex, value):
            raise ValueError("It's not an email address.")
        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        validate_value = value
        if validate_value.startswith("+"):
            validate_value = validate_value[1:]

        if len(validate_value) < 3 or len(validate_value) > 20 or not validate_value.isdecimal():
            raise ValueError("Incorrect form of phone.")
        self._phone = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if len(value) < 2 or len(value) > 50 or value.isspace():
            raise ValueError("Address should be 2-50 characters long.")
        self._address = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if len(value) < 2 or len(value) > 50 or value.isspace():
            raise ValueError("City should be 2-50 characters long.")
        self._city = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        if len(value) < 2 or len(value) > 50 or value.isspace():
            raise ValueError("Country should be 2-50 characters long.")
        self._country = value
        