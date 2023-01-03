from PyQt5.QtGui import QColor, QPixmap
from ui import *
from PIL import Image, ImageChops, ImageFilter
from PyQt5.QtWidgets import QMessageBox


def main():
    print("main")


def differences(self):
    self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
    image1 = Image.open('images/'+self.ui.choose_base_combobox.currentText()+'/' +
                        self.ui.choose_base_combobox.currentText()+'/'+self.ui.difference_combobox.currentText())
    image2 = Image.open('images/'+self.ui.choose_base_combobox.currentText()+'/' +
                        self.ui.choose_base_combobox.currentText()+'_base/'+self.ui.choose_base_combobox.currentText()+'_base.jpg')
    diff = ImageChops.difference(image1, image2)
    diff = diff.filter(ImageFilter.MinFilter(5))
    pix_incorrectness = list(diff.getdata())
    size_of_diff = image1.size
    number_of_pixels = size_of_diff[0]*size_of_diff[1]
    lighter = 0
    for pixel in pix_incorrectness:
        check = 0
        for color in pixel:
            if color >= 60:
                check += 1
        if check >= 1:
            lighter += 1
    percents_of_incorrectness = round((lighter/number_of_pixels)*100,2)
    diff = diff.save('images/'+self.ui.choose_base_combobox.currentText()+'/'+self.ui.choose_base_combobox.currentText() +
                     '_operating/'+self.ui.choose_base_combobox.currentText()+'_difference.jpg')
    self.image = QPixmap('images/'+self.ui.choose_base_combobox.currentText()+'/'+self.ui.choose_base_combobox.currentText() +
                         '_operating/'+self.ui.choose_base_combobox.currentText()+'_difference.jpg')
    self.ui.first_image.setMaximumSize(QtCore.QSize(self.width, self.height))
    self.ui.first_image.setPixmap(self.image.scaled(self.rez))
    msg = QMessageBox()
    msg.setWindowTitle('Differences')
    msg.setText('Percents of incorrectness ' +
                str(percents_of_incorrectness) + '%')
    msg.exec_()
    with open(('images/'+self.ui.choose_base_combobox.currentText()+'/'+self.ui.choose_base_combobox.currentText()+'_operating/'+self.ui.choose_base_combobox.currentText()).rstrip('.jpg')+'_incorrectness.txt', 'w') as file:
        file.write(str(percents_of_incorrectness))


if __name__ == "__main__":
    main()
