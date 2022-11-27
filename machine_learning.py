from roboflow import Roboflow
def main():
    rf = Roboflow(api_key="x8OJScIiVtQRdqBexntp")
    project = rf.workspace().project("smdcomponents")
    model = project.version(6).model

    # infer on a local image
    print(model.predict("your_image.jpg", confidence=65, overlap=15).json())

    # visualize your prediction
    model.predict("your_image.jpg", confidence=65, overlap=15).save("prediction.jpg")

    # infer on an image hosted elsewhere
    # print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())

if __name__ == "__main__":
    main()