from roboflow import Roboflow
from PyQt5.QtGui import QColor, QPixmap
import check_pcb
from ui import *
def main():
    print("main")

def predict_pcb(self):
    rf = Roboflow(api_key="x8OJScIiVtQRdqBexntp")
    project = rf.workspace().project("smdcomponents")
    model = project.version(6).model

    # infer on a local image
    print(model.predict("your_image.jpg", confidence=65, overlap=15).json())

    # visualize your prediction
    model.predict("your_image.jpg", confidence=65, overlap=15).save("prediction.jpg")
    # infer on an image hosted elsewhere
    # print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
    width = self.ui.frame_4.frameGeometry().width()
    height = self.ui.frame_4.frameGeometry().height()
    self.ui.first_image.setMaximumSize(QtCore.QSize(width, height))
    self.image=QPixmap("prediction.jpg")
    rez = QtCore.QSize(width, height)
    self.ui.first_image.setPixmap(self.image.scaled(rez))

if __name__ == "__main__":
    main()