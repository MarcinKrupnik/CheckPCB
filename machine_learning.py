from roboflow import Roboflow
from PyQt5.QtGui import QColor, QPixmap
from PyQt5.QtWidgets import QMessageBox
import check_pcb
from ui import *
from PIL import Image, ImageChops
import json
def main():
    print("main")

def predict_pcb(self,choice):
    self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
    rf = Roboflow(api_key="x8OJScIiVtQRdqBexntp")
    project = rf.workspace().project("smdcomponents")
    model = project.version(6).model
    C=""
    if choice=="base":
        image_path="images/"+self.ui.base_combobox.currentText()+'/'+self.ui.base_combobox.currentText()+'_base/'+self.ui.base_combobox.currentText()+'_base.jpg'
    else:
        image_path="images/"+self.ui.base_combobox.currentText()+'/'+self.ui.base_combobox.currentText()+'/'+self.ui.prod_combobox.currentText()
    print(image_path)
    # infer on a local image
    image = Image.open(image_path)
    image=image.resize((820,616))
    image=image.save(image_path.rstrip('.jpg')+'_resized'+'.jpg')
    detected = model.predict(image_path.rstrip('.jpg')+'_resized'+'.jpg', confidence=15, overlap=15).json()
    # visualize your prediction
    model.predict(image_path.rstrip('.jpg')+'_resized'+'.jpg', confidence=15, overlap=15).save(image_path.rstrip('.jpg')+"_prediction.jpg")
    # infer on an image hosted elsewhere
    # print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
    width = self.ui.frame_4.frameGeometry().width()
    height = self.ui.frame_4.frameGeometry().height()
    self.ui.first_image.setMaximumSize(QtCore.QSize(width, height))
    self.image=QPixmap(image_path.rstrip('.jpg')+"_prediction.jpg")
    rez = QtCore.QSize(width, height)
    self.ui.first_image.setPixmap(self.image.scaled(rez))
    #self.ui.frame_4.show()
    list_of_detected=[]
    for item in detected['predictions']:
        if item['confidence']>0.3:
            list_of_detected.append(item)

    msg= QMessageBox()
    msg.setWindowTitle('Machine Learing informations')
    msg.setText('On image detected '+str(len(list_of_detected))+ ' components')
    msg.exec_()
    
    with open('data.json', 'w') as file:
        json_file=json.dumps(detected['predictions'])
        file.write(json_file)
    

    
if __name__ == "__main__":
    main()