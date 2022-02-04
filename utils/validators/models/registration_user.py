from services import users
import re

class RegistrationUser:
    "Class validates user registration inputs from the form passed by parameter. "
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
        if not (len(value) >= 3 and len(value) <= 40):
            raise ValueError("Username too short.")

        if not users.is_username_unique(value):
            raise ValueError("Username not unique.")

        self._username = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if len(value) < 5:
            raise ValueError("Password too short!")
        self._password = value

    @property
    def is_doctor(self):
        return self._is_doctor

    @is_doctor.setter
    def is_doctor(self, value):
        if not value:
            raise ValueError("Role (doctor/patient) not existing.")
        self._is_doctor = value == "doctor"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 40:
            raise ValueError("Name cannot exceed 40 characters.")
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
        if value and value.startswith("+"):
            value = value[1:]

        if not len(value) <= 20 and not value.isdecimal():
            raise ValueError("Incorrect form of phone")
        self._phone = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if len(value) >= 50:
            raise ValueError("Address input too long!")
        self._address = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if len(value) >= 50:
            raise ValueError("City input too long!")
        self._city = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        if len(value) >= 50:
            raise ValueError("Country input too long!")
        self._country = value