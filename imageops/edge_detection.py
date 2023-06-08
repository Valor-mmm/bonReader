import cv2
import numpy as np

from utils.image_utils import show_image
from utils.imgutils_copy import grab_contours


def edge_detection_prep(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5,), 0)
    return cv2.Canny(blurred, 75, 200)


def filter_and_sort_contours(contours, debug=False):
    """
        Sorts the contours to find the contour with the biggest length then it returns it
    """
    filtered_contours = []
    for c in contours:
        is_closed = cv2.isContourConvex(c)
        length = cv2.arcLength(c, is_closed)

        filtered_contours.append({
            'length': length,
            'contour': c,
            'is_closed': is_closed
        })

    sorted_contours = sorted(filtered_contours, key=lambda x: [x.get('length')], reverse=True)
    if debug:
        print(f'Sorted {len(contours)} contours')
        print(f'Longest contour: {sorted_contours[0].get("length")}')
    return sorted_contours[0]


def edge_detection(image, debug=False):
    prepped_image = edge_detection_prep(image)
    if debug:
        show_image("Prepared Image", prepped_image)

    contours = cv2.findContours(prepped_image.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)
    grabbed_contours = grab_contours(contours)

    longest_contour = filter_and_sort_contours(grabbed_contours, debug)
    rect = cv2.minAreaRect(longest_contour.get('contour'))
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    if debug:
        cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
        show_image("Longest Contour", image)

    return box
