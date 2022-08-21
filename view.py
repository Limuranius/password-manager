from ui import Ui_MainWindow
from add_window import Ui_Dialog
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QModelIndex, pyqtSignal
from PyQt5.QtWidgets import QHeaderView, QMenu, QAction, QDialog
from Structures import LoginInfo, RegInfo, PwdData
from PasswordGenerator import generate_password


class AddDialog(QDialog):
    add_signal = pyqtSignal(PwdData)  # signal that is emitted when OK button is pressed

    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_rand_pwd.clicked.connect(self.set_rand_pwd)

    def get_data(self) -> PwdData:
        description = self.ui.lineEdit_description.text()
        login = self.ui.lineEdit_login.text()
        password = self.ui.lineEdit_password.text()
        return PwdData(description, login, password)

    def set_rand_pwd(self):
        rand_pwd = generate_password()
        self.ui.lineEdit_password.setText(rand_pwd)

    def accept(self):
        data = self.get_data()
        self.add_signal.emit(data)
        super().accept()

    def reject(self):
        super().reject()


class View(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.app = QtWidgets.QApplication([])
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)

    def show(self):
        self.MainWindow.show()
        self.app.exec()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.hide_all_error_labels()
        self.tableView_passwords.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableView_passwords.selectionChanged.connect(self.__on_tableView_selectionChanged)
        self.tableView_passwords.setContextMenuPolicy(Qt.CustomContextMenu)
        self.pushButton_debug.setVisible(False)

    def set_wrong_login_visible(self, status: bool):
        self.label_wrong_login_data.setVisible(status)

    def set_wrong_reg_visible(self, status: bool):
        self.label_wrong_reg_data.setVisible(status)

    def set_pwds_not_match_visible(self, status: bool):
        self.label_pwds_not_match.setVisible(status)

    def hide_all_error_labels(self):
        self.set_wrong_login_visible(False)
        self.set_wrong_reg_visible(False)
        self.set_pwds_not_match_visible(False)

    def set_page_number(self, page: int):
        self.stackedWidget.setCurrentIndex(page)

    def get_login_fields(self) -> LoginInfo:
        login = self.lineEdit_login_login.text()
        password = self.lineEdit_login_password.text()
        return LoginInfo(login, password)

    def get_register_fields(self) -> RegInfo:
        login = self.lineEdit_reg_login.text()
        password_1 = self.lineEdit_reg_password.text()
        password_2 = self.lineEdit_reg_password_2.text()
        return RegInfo(login, password_1, password_2)

    def get_tableView_selected_row(self) -> int:
        return self.tableView_passwords.currentIndex().row()


    # def __on_tableView_selectionChanged(self, selected, deselected):
    #     is_sth_selected = selected.count() > 0
    #     self.pushButton_rem_pwd.setEnabled(is_sth_selected)