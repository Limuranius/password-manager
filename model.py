from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QModelIndex, Qt
from PasswordManager import PasswordManager
from Exceptions import LoginError, RegistrationError
from Structures import PwdData
import pyperclip


class PasswordsTableModel(QStandardItemModel):
    def __init__(self):
        super().__init__()
        self.headers = ["Описание", "Логин", "Пароль"]
        self.setColumnCount(len(self.headers))
        self.setHorizontalHeaderLabels(self.headers)
        self.ids: list[int] = []

    def add_record(self, record: PwdData):
        row = self.rowCount()
        self.insertRow(row)

        desc = QStandardItem(record.description)
        login = QStandardItem(record.login)

        password = QStandardItem()
        password.setText("*" * len(record.password))
        password.setData(record.password, Qt.UserRole)

        self.setItem(row, 0, desc)
        self.setItem(row, 1, login)
        self.setItem(row, 2, password)

        self.ids.append(record.record_id)

    def add_records(self, records: list[PwdData]):
        for record in records:
            self.add_record(record)

    def set_records(self, records: list[PwdData]):
        self.clear_all_data()
        self.add_records(records)

    def clear_all_data(self):
        self.removeRows(0, self.rowCount())
        self.ids = []

    def get_row_id(self, row: int) -> int:
        return self.ids[row]

    def get_index_data(self, index: QModelIndex) -> str:
        if index.column() == 2:  # password column
            return self.data(index, Qt.UserRole)
        else:
            return self.data(index)


class Model:
    def __init__(self):
        self.pm = PasswordManager("passwords.db")
        self.pwd_table_model = PasswordsTableModel()

    def login_user(self, login: str, password: str) -> bool:
        try:
            self.pm.login_user(login, password)
            values = self.pm.get_all_user_records_decoded()
            for value in values:
                self.pwd_table_model.add_record(value)
            return True
        except LoginError:
            return False

    def logout(self):
        self.pm.logout()
        self.pwd_table_model.clear_all_data()

    def register_user(self, login: str, password: str) -> bool:
        try:
            self.pm.register_user(login, password)
            return True
        except RegistrationError:
            return False

    def add_record(self, record: PwdData):
        self.pm.add_record(record)
        self.__update_table_model()

    def remove_row(self, row: int):
        record_id = self.pwd_table_model.get_row_id(row)
        print(f"Removing: {row=} {record_id=}")
        self.pm.remove_record(record_id)
        self.__update_table_model()

    def __update_table_model(self):
        records = self.pm.get_all_user_records_decoded()
        self.pwd_table_model.set_records(records)

    def clipboard_index(self, index: QModelIndex):
        data = self.pwd_table_model.get_index_data(index)
        pyperclip.copy(data)