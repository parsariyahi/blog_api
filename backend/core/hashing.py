from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:

    @staticmethod
    def hash(input_):
        return password_context.hash(input_)

    @staticmethod
    def verify(palin, hashed):
        return password_context.verify(palin, hashed)