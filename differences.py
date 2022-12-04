from PyQt5.QtGui import QColor, QPixmap
from ui import *
from PIL import Image, ImageChops
def main():
    print("main")

def differences(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        image1 = Image.open('images/'+self.ui.choose_base_combobox.currentText()+'/'+self.ui.choose_base_combobox.currentText()+'/'+self.ui.difference_combobox.currentText())
        image2 = Image.open('images/'+self.ui.choose_base_combobox.currentText()+'/'+self.ui.choose_base_combobox.currentText()+'_base/'+self.ui.choose_base_combobox.currentText()+'_base.jpg')
        diff = ImageChops.difference(image1,image2)
        diff = diff.save('/images/'+self.ui.choose_base_combobox.currentText()+'/'+self.ui.choose_base_combobox.currentText()+'/difference.jpg')
        self.image=QPixmap('/images/'+self.ui.choose_base_combobox.currentText()+'/'+self.ui.choose_base_combobox.currentText()+'/difference.jpg')
        self.ui.first_image.setMaximumSize(QtCore.QSize(self.width, self.height))
        self.ui.first_image.setPixmap(self.image.scaled(self.rez))
        #self.ui.frame_4.show()
if __name__ == "__main__":
    main()