# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_login)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame = QtWidgets.QFrame(self.page_login)
        self.frame.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_wrong_login_data = QtWidgets.QLabel(self.frame)
        self.label_wrong_login_data.setStyleSheet("color: red;")
        self.label_wrong_login_data.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wrong_login_data.setObjectName("label_wrong_login_data")
        self.verticalLayout_2.addWidget(self.label_wrong_login_data)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout.setContentsMargins(0, -1, 0, -1)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_login_login = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_login_login.setObjectName("lineEdit_login_login")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_login_login)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_login_password = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_login_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_login_password.setObjectName("lineEdit_login_password")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_login_password)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.pushButton_login_enter = QtWidgets.QPushButton(self.frame)
        self.pushButton_login_enter.setObjectName("pushButton_login_enter")
        self.verticalLayout_2.addWidget(self.pushButton_login_enter)
        self.pushButton_login_register = QtWidgets.QPushButton(self.frame)
        self.pushButton_login_register.setObjectName("pushButton_login_register")
        self.verticalLayout_2.addWidget(self.pushButton_login_register)
        self.verticalLayout_3.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.page_login)
        self.page_register = QtWidgets.QWidget()
        self.page_register.setObjectName("page_register")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_register)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_9 = QtWidgets.QFrame(self.page_register)
        self.frame_9.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_9.setAutoFillBackground(False)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_13 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setIndent(0)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_10.addWidget(self.label_13)
        self.label_wrong_reg_data = QtWidgets.QLabel(self.frame_9)
        self.label_wrong_reg_data.setStyleSheet("color: red;")
        self.label_wrong_reg_data.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wrong_reg_data.setObjectName("label_wrong_reg_data")
        self.verticalLayout_10.addWidget(self.label_wrong_reg_data)
        self.frame_10 = QtWidgets.QFrame(self.frame_9)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.formLayout_5 = QtWidgets.QFormLayout(self.frame_10)
        self.formLayout_5.setContentsMargins(0, -1, 0, -1)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_14 = QtWidgets.QLabel(self.frame_10)
        self.label_14.setObjectName("label_14")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_reg_login = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_reg_login.setObjectName("lineEdit_reg_login")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_reg_login)
        self.label_15 = QtWidgets.QLabel(self.frame_10)
        self.label_15.setObjectName("label_15")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.lineEdit_reg_password = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_reg_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_reg_password.setObjectName("lineEdit_reg_password")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_reg_password)
        self.lineEdit_reg_password_2 = QtWidgets.QLineEdit(self.frame_10)
        self.lineEdit_reg_password_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_reg_password_2.setObjectName("lineEdit_reg_password_2")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_reg_password_2)
        self.label_16 = QtWidgets.QLabel(self.frame_10)
        self.label_16.setObjectName("label_16")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.label_pwds_not_match = QtWidgets.QLabel(self.frame_10)
        self.label_pwds_not_match.setStyleSheet("color: red;")
        self.label_pwds_not_match.setAlignment(QtCore.Qt.AlignCenter)
        self.label_pwds_not_match.setObjectName("label_pwds_not_match")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_pwds_not_match)
        self.verticalLayout_10.addWidget(self.frame_10)
        self.pushButton_reg_register = QtWidgets.QPushButton(self.frame_9)
        self.pushButton_reg_register.setObjectName("pushButton_reg_register")
        self.verticalLayout_10.addWidget(self.pushButton_reg_register)
        self.horizontalLayout_2.addWidget(self.frame_9)
        self.stackedWidget.addWidget(self.page_register)
        self.page_passwords = QtWidgets.QWidget()
        self.page_passwords.setObjectName("page_passwords")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_passwords)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView_passwords = QtWidgets.QTableView(self.page_passwords)
        self.tableView_passwords.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableView_passwords.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableView_passwords.setObjectName("tableView_passwords")
        self.verticalLayout.addWidget(self.tableView_passwords)
        self.frame_3 = QtWidgets.QFrame(self.page_passwords)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_add_pwd = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_add_pwd.setObjectName("pushButton_add_pwd")
        self.horizontalLayout_3.addWidget(self.pushButton_add_pwd)
        self.pushButton_rem_pwd = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_rem_pwd.setEnabled(False)
        self.pushButton_rem_pwd.setObjectName("pushButton_rem_pwd")
        self.horizontalLayout_3.addWidget(self.pushButton_rem_pwd)
        self.pushButton_debug = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_debug.setObjectName("pushButton_debug")
        self.horizontalLayout_3.addWidget(self.pushButton_debug)
        self.verticalLayout.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter)
        self.stackedWidget.addWidget(self.page_passwords)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "???????????????? ??????????????"))
        self.label.setText(_translate("MainWindow", "??????????"))
        self.label_wrong_login_data.setText(_translate("MainWindow", "?????????????? ?????????????????? ????????????!"))
        self.label_2.setText(_translate("MainWindow", "??????????"))
        self.label_3.setText(_translate("MainWindow", "????????????"))
        self.pushButton_login_enter.setText(_translate("MainWindow", "??????????"))
        self.pushButton_login_register.setText(_translate("MainWindow", "??????????????????????"))
        self.label_13.setText(_translate("MainWindow", "??????????????????????"))
        self.label_wrong_reg_data.setText(_translate("MainWindow", "?????????? ???????????????????????? ?????? ????????????????????!"))
        self.label_14.setText(_translate("MainWindow", "??????????"))
        self.label_15.setText(_translate("MainWindow", "????????????"))
        self.label_16.setText(_translate("MainWindow", "???????????? ????????????????"))
        self.label_pwds_not_match.setText(_translate("MainWindow", "???????????? ???? ??????????????????!"))
        self.pushButton_reg_register.setText(_translate("MainWindow", "????????????????????????????????"))
        self.pushButton_add_pwd.setText(_translate("MainWindow", "????????????????..."))
        self.pushButton_rem_pwd.setText(_translate("MainWindow", "??????????????"))
        self.pushButton_debug.setText(_translate("MainWindow", "??????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
