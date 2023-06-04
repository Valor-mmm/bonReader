import cv2

from utils.image_utils import show_image
from utils.imgutils_copy import grab_contours


def edge_detection_prep(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5,), 0)
    return cv2.Canny(blurred, 75, 200)


def filter_contours(contours):
    """
        Filters the contours to find the fist contour with 4 edges
    """
    found_contour = None
    for c in contours:
        # approximate the contour
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)

        # if our approximated contour has four points, then we can
        # assume we have found the outline of the receipt
        if len(approx) == 4:
            found_contour = approx
            break

    if found_contour is None:
        raise Exception('Could not find the edge of the receipt')

    return found_contour


def edge_detection(image, debug=False):
    prepped_image = edge_detection_prep(image)
    if debug:
        show_image("Prepared Image", prepped_image)

    contours = cv2.findContours(prepped_image.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    grabbed_contours = grab_contours(contours)
    sorted_contours = sorted(grabbed_contours, key=cv2.contourArea, reverse=True)

    if debug:
        cv2.drawContours(image, [sorted_contours[0]], -1, (0, 255, 0), 2)
        show_image("Contour", image)
    return filter_contours(sorted_contours)
