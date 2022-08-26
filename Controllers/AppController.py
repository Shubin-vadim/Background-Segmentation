from PyQt5 import QtWidgets
from Views.MainView2 import MainView
from Models.BackgroundModel import BackgroundModule
import os
from cv2 import imdecode
from cv2 import IMREAD_UNCHANGED
from numpy import uint8
from numpy import fromfile


class AppController(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = MainView2()
        self.ui.setupUi(self)
        self.check = False
        self.ui.aplly_settings_btn.clicked.connect(self.apply_settings)
        self.ui.aply_choice_btn.clicked.connect(self.choose)
        self.ui.cancel_choice_btn.clicked.connect(self.cancel_choice)

    def choose(self):
        if self.check:
            self.check = True
            self.ui.aply_choice_btn.show()
            self.ui.cancel_choice_btn.hide()
        else:
            self.check = False
            self.ui.aply_choice_btn.hide()
            self.ui.cancel_choice_btn.show()
        if self.ui.pictures_RadioBtn.isChecked():
            self.choice_pictur()
            self.ui.color_RadionBtn.setEnabled(False)
        elif self.ui.color_RadionBtn.isChecked():
            self.choice_color()
            self.ui.pictures_RadioBtn.setEnabled(False)

    def cancel_choice(self):
        self.ui.cancel_choice_btn.hide()
        self.ui.aply_choice_btn.show()
        self.ui.pictures_RadioBtn.setEnabled(True)
        self.ui.color_RadionBtn.setEnabled(True)

    def choice_pictur(self):
        self.show_elements()
        self.ui.descript_lab.setText('Выбирите директорию картинок')
        self.ui.choice_edit.setStyleSheet('background-color: white;')
        self.ui.choice_edit.setText('')
        self.ui.choice_color_btn.hide()
        self.ui.choice_picture_btn.show()
        self.ui.choice_picture_btn.clicked.connect(self.review)

    def choice_color(self):
        self.show_elements()
        self.ui.descript_lab.setText('Выбирите цветовой оттенок')
        self.ui.choice_edit.setStyleSheet('background-color: black;')
        self.ui.choice_edit.setText('(0,0,0)')
        self.ui.choice_picture_btn.hide()
        self.ui.choice_color_btn.show()
        self.ui.choice_color_btn.clicked.connect(self.check_color)

    def show_elements(self):
        self.ui.descript_lab.show()
        self.ui.choice_edit.show()

    def add_imgs(self, path):
        listDir = os.listdir(path)
        imgs = []
        for imgPath in listDir:
            if imgPath.find('.jpg') != -1 or imgPath.find('.png') != -1 or imgPath.find('.gif') != -1:
                img = imdecode(fromfile(fr'{path}/{imgPath}', dtype=uint8), IMREAD_UNCHANGED)
                imgs.append(img)
        return imgs

    def review(self):
        self.file = QtWidgets.QFileDialog.getExistingDirectory(self)
        if self.file != '':
            self.ui.choice_edit.setText(self.file)
        else:
            pass

    def check_color(self):
        dil_color = QtWidgets.QColorDialog(self)
        color = dil_color.getColor()
        color_value = color.getRgb()
        r, g, b = color_value[0], color_value[1], color_value[2]
        self.ui.choice_edit.setStyleSheet(f"background-color:rgb({r}, {g}, {b})")
        self.ui.choice_edit.setText(str(r) + ',' + str(g) + ',' + str(b))

    def apply_settings(self):
        set = self.ui.choice_edit.text()
        if self.ui.pictures_RadioBtn.isChecked() and set != '':
            imgs = self.add_imgs(set)

        if not self.ui.allow_RadioBtn.isChecked():
            QtWidgets.QMessageBox.warning(self, 'Ошибка', 'Вы не дали доступ к вашей веб-камере')
        elif set == '':
            QtWidgets.QMessageBox.warning(self, 'Предупреждение',
                                          'Выбирите директорию картинок или цвет для заднего фона веб-камеры!')

        elif (self.ui.color_RadionBtn.isChecked()) and (self.ui.allow_RadioBtn.isChecked()):
            colors = set.split(',')
            rgb = (int(colors[2]), int(colors[1]), int(colors[0]))
            model = BackgroundModule(color=rgb)
            model.run()
        elif (self.ui.pictures_RadioBtn.isChecked()) and (self.ui.allow_RadioBtn.isChecked()) and len(imgs) > 0:
            model = BackgroundModule(imgs=imgs)
            model.run()
        else:
            QtWidgets.QMessageBox.warning(self, 'Предупреждение', 'В директории отсутствуют картинки')
