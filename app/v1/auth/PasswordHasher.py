import bcrypt


class PasswordHasher:
    def __init__(self, password):
        self.password = password
        self.__salt = self.__getSalt

    @property
    def __getSalt(self):
        return bcrypt.gensalt()

    def hashPassword(self):
        passwordBytes: bytes = bcrypt.hashpw(password=self.password.encode("utf-8"), salt=self.__salt)
        return passwordBytes