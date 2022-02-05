import re

class SettingsUser:
    """Class validates user settings page inputs from the form passed by parameter.
       Note: if form["xyz"] is empty - validation is not done due to the user indicating
       that not desiring to change the value."""
    def __init__(self, form):
        self.name = form["name"]
        self.email = form["email"]
        self.phone = form["phone"]
        self.address = form["address"]
        self.city = form["city"]
        self.country = form["country"]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value:
            if len(value) < 3 or len(value) > 40:
                raise ValueError("Name cannot exceed 40 characters.")
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if value:
            regex = "^.+@.{3,40}"
            if not re.match(regex, value):
                raise ValueError("Email format incorrect!")
        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if value:
            validate_value = value
            if validate_value.startswith("+"):
                validate_value = validate_value[1:]

            if len(validate_value) < 2 or len(validate_value) > 20 or not validate_value.isdecimal():
                raise ValueError("Incorrect form of the phone number.")
        self._phone = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if value:
            if len(value) < 3 or len(value) > 50:
                raise ValueError("Address input too long!")
        self._address = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if value:
            if len(value) < 3 or len(value) > 50:
                raise ValueError("City input too long!")
        self._city = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        if value:
            if len(value) < 3 or len(value) > 50:
                    raise ValueError("Country input too long!")
        self._country = value