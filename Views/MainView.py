from PyQt5 import QtCore, QtGui, QtWidgets


class MainView2(object):
    def setupUi(self, BackImg):
        BackImg.setObjectName("BackImg")
        BackImg.resize(742, 329)
        self.centralwidget = QtWidgets.QWidget(BackImg)
        self.centralwidget.setObjectName("centralwidget")

        self.title_lab = QtWidgets.QLabel(self.centralwidget)
        self.title_lab.setGeometry(QtCore.QRect(100, 10, 551, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.title_lab.setFont(font)
        self.title_lab.setObjectName("title_lab")

        self.choice_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.choice_edit.setGeometry(QtCore.QRect(260, 130, 411, 21))
        self.choice_edit.setObjectName("choice_edit")
        self.choice_edit.hide()

        self.choice_picture_btn = QtWidgets.QPushButton(self.centralwidget)
        self.choice_picture_btn.setGeometry(QtCore.QRect(400, 160, 111, 31))
        font.setPointSize(10)
        self.choice_picture_btn.setFont(font)
        self.choice_picture_btn.setObjectName("choice_picture_btn")
        self.choice_picture_btn.hide()

        self.choice_color_btn = QtWidgets.QPushButton(self.centralwidget)
        self.choice_color_btn.setGeometry(QtCore.QRect(400, 160, 111, 31))
        self.choice_color_btn.setFont(font)
        self.choice_color_btn.setObjectName("choice_color_btn")
        self.choice_color_btn.hide()

        self.aply_choice_btn = QtWidgets.QPushButton(self.centralwidget)
        self.aply_choice_btn.setGeometry(QtCore.QRect(140, 120, 100, 30))
        self.aply_choice_btn.setFont(font)
        self.aply_choice_btn.setObjectName("aply_choice_btn")

        self.cancel_choice_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_choice_btn.setGeometry(QtCore.QRect(140, 120, 100, 30))
        self.cancel_choice_btn.setFont(font)
        self.cancel_choice_btn.setObjectName("cancel_choice_btn")
        self.cancel_choice_btn.hide()

        self.allow_RadioBtn = QtWidgets.QCheckBox(self.centralwidget)
        self.allow_RadioBtn.setGeometry(QtCore.QRect(310, 190, 91, 21))
        self.allow_RadioBtn.setFont(font)
        self.allow_RadioBtn.setObjectName("allow_RadioBtn")

        self.aplly_settings_btn = QtWidgets.QPushButton(self.centralwidget)
        self.aplly_settings_btn.setGeometry(QtCore.QRect(290, 240, 161, 41))
        font = QtGui.QFont()
        self.aplly_settings_btn.setFont(font)
        self.aplly_settings_btn.setObjectName("aplly_settings_btn")

        self.choice_frame = QtWidgets.QFrame(self.centralwidget)
        self.choice_frame.setGeometry(QtCore.QRect(20, 90, 141, 71))
        self.choice_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.choice_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.choice_frame.setObjectName("choice_frame")

        self.webCam_lab = QtWidgets.QLabel(self.centralwidget)
        self.webCam_lab.setGeometry(QtCore.QRect(10, 190, 291, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.webCam_lab.setFont(font)
        self.webCam_lab.setObjectName("webCam_lab")

        self.pictures_RadioBtn = QtWidgets.QRadioButton(self.choice_frame)
        self.pictures_RadioBtn.setGeometry(QtCore.QRect(10, 10, 111, 21))
        self.pictures_RadioBtn.setFont(font)
        self.pictures_RadioBtn.setObjectName("pictures_RadioBtn")

        self.color_RadionBtn = QtWidgets.QRadioButton(self.choice_frame)
        self.color_RadionBtn.setGeometry(QtCore.QRect(10, 40, 91, 21))
        self.color_RadionBtn.setFont(font)
        self.color_RadionBtn.setObjectName("color_RadionBtn")

        self.choice_title_lab = QtWidgets.QLabel(self.centralwidget)
        self.choice_title_lab.setGeometry(QtCore.QRect(10, 60, 621, 31))
        self.choice_title_lab.setFont(font)
        self.choice_title_lab.setObjectName("choice_title_lab")

        self.descript_lab = QtWidgets.QLabel(self.centralwidget)
        self.descript_lab.setGeometry(QtCore.QRect(380, 105, 260, 20))
        self.descript_lab.setFont(font)
        self.descript_lab.setObjectName("descript_lab")
        self.descript_lab.hide()

        BackImg.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BackImg)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 21))
        self.menubar.setObjectName("menubar")
        BackImg.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BackImg)
        self.statusbar.setObjectName("statusbar")
        BackImg.setStatusBar(self.statusbar)

        self.retranslateUi(BackImg)
        QtCore.QMetaObject.connectSlotsByName(BackImg)

    def retranslateUi(self, BackImg):
        _translate = QtCore.QCoreApplication.translate
        BackImg.setWindowTitle(_translate("BackImg", "MainWindow"))
        self.title_lab.setText(_translate("BackImg", "Выбирите или создайте задний фон для ваших встреч!"))
        self.choice_picture_btn.setText(_translate("BackImg", "Обзор"))
        self.choice_color_btn.setText(_translate("BackImg", "Выбрать цвет"))
        self.webCam_lab.setText(_translate("BackImg", "Разрешите доступ к ващей веб-камере"))
        self.allow_RadioBtn.setText(_translate("BackImg", "Разрешаю"))
        self.aplly_settings_btn.setText(_translate("BackImg", "Применить настройки"))
        self.pictures_RadioBtn.setText(_translate("BackImg", "Картинки"))
        self.color_RadionBtn.setText(_translate("BackImg", "Цвет"))
        self.choice_title_lab.setText(_translate("BackImg", "Выбирите элемент, который хотите поставить на задний фон вашей веб-камеры"))
        self.descript_lab.setText(_translate("BackImg", "Текст"))
        self.aply_choice_btn.setText(_translate("BackImg", "Выбрать"))
        self.cancel_choice_btn.setText(_translate("BackImg", "Отменить"))
