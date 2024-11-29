import bcrypt


class PasswordValidator:
    def __init__(self, passwordBytes, password):
        self.passwordBytes = passwordBytes
        self.password = password

    async def passwordSamer(self):
        return bcrypt.checkpw(self.password.encode("utf-8"), self.passwordBytes)