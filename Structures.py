from typing import NamedTuple


class PwdData(NamedTuple):
    description: str
    login: str
    password: str
    record_id: int = None


class LoginInfo(NamedTuple):
    login: str
    password: str


class RegInfo(NamedTuple):
    login: str
    password_1: str
    password_2: str
