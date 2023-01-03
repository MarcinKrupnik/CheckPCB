"""Import modules"""
import json
from roboflow import Roboflow
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore
from PIL import Image


def main():
    """Main function"""
    print("main")


def predict_pcb(self, choice):
    self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
    roboflow = Roboflow(api_key="x8OJScIiVtQRdqBexntp")
    project = roboflow.workspace().project("smdcomponents")
    model = project.version(6).model

    if choice == "base":
        image_path = "images/"+self.ui.base_combobox.currentText()+\
        '/'+self.ui.base_combobox.currentText() + \
            '_base/'+self.ui.base_combobox.currentText()+'_base.jpg'
        operating_image_path = "images/"+self.ui.base_combobox.currentText()+'/' + \
            self.ui.base_combobox.currentText()+'_operating/' + \
            self.ui.base_combobox.currentText()+'_base'
    else:
        image_path = "images/"+self.ui.base_combobox.currentText()+'/' + \
            self.ui.base_combobox.currentText()+'/'+self.ui.prod_combobox.currentText()
        operating_image_path = "images/"+self.ui.base_combobox.currentText()+'/' + \
            self.ui.base_combobox.currentText()+'_operating/' + \
            self.ui.prod_combobox.currentText()
    print(image_path)
    image = Image.open(image_path)
    image = image.resize((820, 616))
    image = image.save(operating_image_path+'_resized'+'.jpg')
    detected = model.predict(
        operating_image_path+'_resized'+'.jpg', confidence=30, overlap=15).json()
    model.predict(operating_image_path+'_resized'+'.jpg', confidence=30,
                  overlap=15).save(operating_image_path+"_prediction.jpg")
    width = self.ui.frame_4.frameGeometry().width()
    height = self.ui.frame_4.frameGeometry().height()
    self.ui.first_image.setMaximumSize(QtCore.QSize(width, height))
    self.image = QPixmap(operating_image_path+"_prediction.jpg")
    rez = QtCore.QSize(width, height)
    self.ui.first_image.setPixmap(self.image.scaled(rez))
    list_of_detected = []
    for item in detected['predictions']:
        if item['confidence'] > 0.3:
            list_of_detected.append(item)

    msg = QMessageBox()
    msg.setWindowTitle('Machine Learing informations')
    msg.setText('On image detected ' +
                str(len(list_of_detected)) + ' components')
    msg.exec_()

    with open(operating_image_path.rstrip('.jpg')+'data.json', 'w') as file:
        json_file = json.dumps(detected['predictions'])
        file.write(json_file)

    with open(operating_image_path.rstrip('.jpg')+'_detected.txt', 'w') as file:
        file.write(str(len(list_of_detected)))


if __name__ == "__main__":
    main()
