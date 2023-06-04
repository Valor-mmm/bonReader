import cv2
from utils.image_utils import resize_image, show_image
from imageops.edge_detection import edge_detection
from utils.imgutils_copy import four_point_transform
import pytesseract


def extract_bon(image, debug=False):
    img = image.copy()
    resized_image = resize_image(img, 500)
    if debug:
        show_image("Resized Image", resized_image)

    bon_contour = edge_detection(resized_image, debug)
    if debug:
        output = img.copy()
        cv2.drawContours(output, [bon_contour], -1, (0, 255, 0), 2)
        show_image("Contour", output)

    ratio = img.shape[1] / float(resized_image.shape[1])
    return four_point_transform(img, bon_contour.reshape(4, 2) * ratio)


def scan_bon(path):
    orig = cv2.imread(path)
    image = orig.copy()

    bon = extract_bon(image, True)
    show_image("Receipt", bon)

    resize_image = cv2.resize(bon, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    colored_bon = cv2.cvtColor(resize_image, cv2.COLOR_BGR2RGB)  # COLOR_BGR2GRAY
    show_image("Colored", colored_bon)

    options = "--psm 4"
    text = pytesseract.image_to_string(colored_bon, config=options)

    # show the raw output of the OCR process
    print("[INFO] raw output:")
    print("==================")
    # print(text)
    print("\n")



