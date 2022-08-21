class RegistrationError(Exception):
    def __init__(self, value):
        self.value = value


class LoginError(Exception):
    def __init__(self, value):
        self.value = value
