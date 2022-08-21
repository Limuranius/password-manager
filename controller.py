from model import Model
from view import View, AddDialog

from PyQt5.QtWidgets import QMenu


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        self.setup_connections()
        self.view.show()

    def setup_connections(self):
        self.view.tableView_passwords.setModel(self.model.pwd_table_model)

        self.view.pushButton_login_enter.clicked.connect(self.__on_login_enter_button_clicked)
        self.view.pushButton_login_register.clicked.connect(self.__on_login_reg_button_clicked)
        self.view.pushButton_reg_register.clicked.connect(self.__on_reg_reg_button_clicked)

        self.view.pushButton_add_pwd.clicked.connect(self.__on_add_pwd_button_clicked)
        self.view.pushButton_rem_pwd.clicked.connect(self.__on_rem_pwd_button_clicked)
        self.view.tableView_passwords.selectionModel().selectionChanged.connect(self.__on_tableView_selectionChanged)
        self.view.tableView_passwords.customContextMenuRequested.connect(self.__on_context_menu_requested)

        self.view.pushButton_debug.clicked.connect(self.model.pm.debug)

    def logout(self):
        self.model.logout()
        self.view.set_page_number(0)

    def __on_login_enter_button_clicked(self):
        data = self.view.get_login_fields()
        success = self.model.login_user(data.login, data.password)
        if success:
            self.view.hide_all_error_labels()
            self.view.set_page_number(2)
        else:
            self.view.set_wrong_login_visible(True)

    def __on_login_reg_button_clicked(self):
        self.view.hide_all_error_labels()
        self.view.set_page_number(1)

    def __on_reg_reg_button_clicked(self):
        data = self.view.get_register_fields()
        if data.password_1 != data.password_2:
            self.view.set_pwds_not_match_visible(True)
            return
        success = self.model.register_user(data.login, data.password_1)
        if success:
            self.view.set_page_number(0)
            self.view.hide_all_error_labels()
        else:
            self.view.set_wrong_reg_visible(True)

    def __on_add_pwd_button_clicked(self):
        dialog = AddDialog()
        dialog.add_signal.connect(self.model.add_record)
        dialog.exec()

    def __on_rem_pwd_button_clicked(self):
        row = self.view.get_tableView_selected_row()
        self.model.remove_row(row)

    def __on_tableView_selectionChanged(self, selected, deselected):
        is_sth_selected = selected.count() > 0
        self.view.pushButton_rem_pwd.setEnabled(is_sth_selected)

    def __on_context_menu_requested(self, pos):
        index = self.view.tableView_passwords.indexAt(pos)
        self.view.tableView_passwords.setCurrentIndex(index)
        menu = QMenu()
        menu.addAction("Копировать", lambda: self.model.clipboard_index(index))
        menu.exec(self.view.tableView_passwords.mapToGlobal(pos))
