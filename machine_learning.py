from roboflow import Roboflow
from PyQt5.QtGui import QColor, QPixmap
import check_pcb
from ui import *
def main():
    print("main")

def predict_pcb(self,choice):
    self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
    rf = Roboflow(api_key="x8OJScIiVtQRdqBexntp")
    project = rf.workspace().project("smdcomponents")
    model = project.version(6).model
    image_path=""
    if choice=="base":
        image_path="images/"+self.ui.base_combobox.currentText()+'/'+self.ui.base_combobox.currentText()+'base/'+self.ui.base_combobox.currentText()+'base.jpg'
    else:
        image_path="images/"+self.ui.base_combobox.currentText()+'/'+self.ui.base_combobox.currentText()+'/'+self.ui.prod_combobox.currentText()
    # infer on a local image
    print(model.predict(image_path.resize((1640,1232)), confidence=65, overlap=15).json())

    # visualize your prediction
    model.predict(image_path, confidence=65, overlap=15).save("prediction.jpg")
    # infer on an image hosted elsewhere
    # print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
    width = self.ui.frame_4.frameGeometry().width()
    height = self.ui.frame_4.frameGeometry().height()
    self.ui.first_image.setMaximumSize(QtCore.QSize(width, height))
    self.image=QPixmap("prediction.jpg")
    rez = QtCore.QSize(width, height)
    self.ui.first_image.setPixmap(self.image.scaled(rez))
    #self.ui.frame_4.show()

if __name__ == "__main__":
    main()