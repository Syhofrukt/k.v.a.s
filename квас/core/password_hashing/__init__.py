import hashlib
import base64
import random


class PasswordHandler:
    def __init__(self, hash_algoritm, coding_algoritm, pepper=None) -> None:
        self.hash_algoritm = hash_algoritm
        self.coding_algoritm = coding_algoritm
        self.pepper = pepper

    def hash_password_with_salt(self, password: str) -> str:
        if self.pepper is None:
            salt = self.generate_salt()
            return self.hash_password(password + ":" + salt) + ":" + salt
        else:
            salt = self.generate_salt()
            pepper = self.pepper
            return self.hash_password(pepper + password + ":" + salt) + ":" + salt

    def verify_password(self, password: str, compared_hash: str) -> bool:
        if self.pepper is None:
            raw_hash, salt = compared_hash.split(":", 2)
            return self.hash_password(password + ":" + salt) == raw_hash
        else:
            pepper = self.pepper
            raw_hash, salt = compared_hash.split(":", 2)
            return self.hash_password(pepper + password + ":" + salt) == raw_hash

    def hash_password(self, password: str) -> str:
        try:
            data = getattr(hashlib, self.hash_algoritm)(password.encode("utf-8"))
        except AttributeError:
            raise ValueError(
                "Hash algoritm name is incorrect. Try putting: sha256, md5, sha1, etc."
            )

        try:
            return getattr(base64, self.coding_algoritm)(data.digest()).decode("utf-8")
        except AttributeError:
            raise ValueError(
                "Coding attribute is incorrect. Try putting: b16encode, b32encode, b64encode, b85encode"
            )

    def generate_salt(self) -> str:
        salt_number = random.randint(0, 2 ** 255)
        try:
            return getattr(base64, self.coding_algoritm)(
                salt_number.to_bytes(32, "little")
            ).decode("utf-8")
        except AttributeError:
            raise ValueError(
                "Coding attribute is incorrect. Try putting: b16encode, b32encode, b64encode, b85encode"
            )
