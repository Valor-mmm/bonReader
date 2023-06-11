import cv2
from utils.image_utils import resize_image, show_image
from imageops.edge_detection import edge_detection
from utils.imgutils_copy import four_point_transform
import pytesseract
import numpy as np


def extract_bon(image, debug=False):
    img = image.copy()
    resized_image = resize_image(img, 500)
    if debug:
        show_image("Resized Image", resized_image)

    bon_contour = edge_detection(resized_image, debug)
    ratio = img.shape[1] / float(resized_image.shape[1])
    reshaped_contour = bon_contour.reshape(np.shape(bon_contour)[0], 2) * ratio


    if debug:
        output = img.copy()
        cv2.drawContours(output, [reshaped_contour.astype(int)], -1, (0, 255, 0), 10)
        show_image("Reshaped contour", output)
        output2 = img.copy()
        for p in reshaped_contour:
            output2 = cv2.circle(output2, tuple(p.astype(int)), radius=30, color=(0, 255, 0), thickness=-1)
        show_image('Contour Points', output2)
    return four_point_transform(img, reshaped_contour)


def scan_bon(path, debug=False):
    orig = cv2.imread(path)
    image = orig.copy()

    bon = extract_bon(image, debug)

    if debug:
        show_image("Receipt", bon)

    colored_bon = cv2.cvtColor(bon, cv2.COLOR_BGR2GRAY)  # COLOR_BGR2RGB

    kernel = np.ones((5, 5), np.uint8)
    img_erosion = cv2.erode(reduced_noise, kernel, iterations=1)

    if debug:
        show_image("Erosion", img_erosion)

    options = "--psm 4"
    text = pytesseract.image_to_string(img_erosion, config=options, lang='eng+deu')

    # show the raw output of the OCR process
    print("[INFO] raw output:")
    print("==================")
    print(text)
    print("\n")



