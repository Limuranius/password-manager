import sqlite3
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
from Exceptions import RegistrationError, LoginError
from Structures import PwdData

ITERATIONS_FOR_KEY = 5000
ITERATIONS_FOR_PASSWORD = 100000


def hash_password(password: str, salt: bytes, iterations: int = ITERATIONS_FOR_PASSWORD) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
    )
    return kdf.derive(password.encode())

def password_to_key(password: str, salt: bytes) -> bytes:
    """Converts password + salt into 32 byte base64 encryption key used by Fernet"""
    hashed_pwd = hash_password(password, salt, ITERATIONS_FOR_KEY)
    key = base64.urlsafe_b64encode(hashed_pwd)
    return key


def scrub(text: str):
    """Removes sus sql injection stuff (and spaces) from string"""
    return ''.join(ch for ch in text if ch.isalnum())


class PasswordManager:
    def __init__(self, db_path: str):
        self.db = sqlite3.connect(db_path)
        self.cursor = self.db.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            login TEXT NOT NULL, 
            password BLOB NOT NULL, 
            salt BLOB NOT NULL
        )""")
        self.db.commit()

        self.login: str = None
        self.table_name: str = None
        self.key: str = None
        self.crypter: Fernet = None

    def register_user(self, login: str, password: str):
        """
        Register user and add his login and hashed password to table 'user'
        """
        if self.__is_login_exist(login):
            raise RegistrationError("Username already taken")
        else:
            salt = os.urandom(16)  # salt for salting password
            hashed_password = hash_password(password, salt)  # hash of pwd + salt
            self.cursor.execute("""
            INSERT INTO user(login, password, salt) 
            VALUES (?, ?, ?)
            """, (login, hashed_password, salt))  # storing user login and pwd

            table_name = scrub(login)
            if len(table_name) == 0:
                raise RegistrationError("Invalid username")
            self.cursor.execute("""
            CREATE TABLE {} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                desc BLOB NOT NULL, 
                login BLOB NOT NULL, 
                password BLOB NOT NULL
            )""".format(table_name))  # creating table named after user
            self.db.commit()

    def login_user(self, login: str, password: str) -> None:
        if not self.__is_login_exist(login):
            raise LoginError("Username not exist")
        if self.__is_pwd_correct(login, password):
            self.login = login
            self.table_name = scrub(login)
            salt = self.__get_salt(login)
            self.key = password_to_key(password, salt)
            self.crypter = Fernet(self.key)
        else:
            raise LoginError("Incorrect Password")

    def logout(self):
        self.login = None
        self.table_name = None
        self.key = None
        self.crypter = None

    def __get_salt(self, login: str) -> bytes:
        self.cursor.execute("""
        SELECT salt 
        FROM user 
        WHERE login = ? 
        LIMIT 1
        """, (login,))
        return self.cursor.fetchone()[0]

    def __is_login_exist(self, login: str) -> bool:
        self.cursor.execute("""
        SELECT * 
        FROM user 
        WHERE login = ?
        """, (login,))
        user = self.cursor.fetchone()  # would be None if login does not exist in DB
        return user is not None

    def __is_pwd_correct(self, login: str, password: str) -> bool:
        self.cursor.execute("""
        SELECT password 
        FROM user 
        WHERE login = ? 
        LIMIT 1
        """, (login,))
        hashed_password_db = self.cursor.fetchone()[0]
        salt = self.__get_salt(login)
        hashed_password_inp = hash_password(password, salt)
        return hashed_password_db == hashed_password_inp

    def get_all_user_records_decoded(self) -> list[PwdData]:
        self.cursor.execute("""
        SELECT * 
        FROM {}
        """.format(self.table_name))
        records = self.cursor.fetchall()
        res = []
        for record in records:
            record_id = record[0]
            description_decoded = self.crypter.decrypt(record[1]).decode()
            login_decoded = self.crypter.decrypt(record[2]).decode()
            password_decoded = self.crypter.decrypt(record[3]).decode()
            res.append(PwdData(description_decoded, login_decoded, password_decoded, record_id))
        return res

    def debug(self):
        print(*self.cursor.execute(f"SELECT * FROM {self.table_name}").fetchall(), sep="\n")
        print(self.login, self.key, self.get_all_user_records_decoded(), sep="\n")

    def add_record(self, record: PwdData):
        description_encoded = self.crypter.encrypt(record.description.encode())
        login_encoded = self.crypter.encrypt(record.login.encode())
        password_encoded = self.crypter.encrypt(record.password.encode())
        self.cursor.execute("""
        INSERT INTO {} (desc, login, password)
        VALUES (?, ?, ?)
        """.format(self.table_name), (description_encoded, login_encoded, password_encoded))
        self.db.commit()

    def remove_record(self, record_id: int):
        self.cursor.execute("""
        DELETE FROM {} 
        WHERE id = ?
        """.format(self.table_name), (record_id, ))
        self.db.commit()


if __name__ == "__main__":
    a = PasswordManager("passwords.db")
    a.register_user("a", "a")
    a.login_user("a", "a")
    print(a.get_all_user_records_decoded())

