import cv2
import matplotlib.pyplot as plt
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def main():
    img = cv2.imread('your_image2.jpg')  # wczytanie obrazka
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # konwersja na czarno białe
    # wszystkie wartości powyżej 127 zamieniane na 255(biały)
    thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)[1]
    #plt.imshow(thresh, 'gray')
    # plt.show() # wyświetlanie obrazka

    output = pytesseract.image_to_string(thresh, lang='eng', config='--psm 11')
    print('Output: ', output)


if __name__ == "__main__":
    main()
