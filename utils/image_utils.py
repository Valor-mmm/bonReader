import cv2


def show_image(name, image):
    cv2.namedWindow(name, cv2.WINDOW_KEEPRATIO)
    cv2.imshow(name, image)
    cv2.resizeWindow(name, 1000, 800)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def resize_image(image, width):
    h, w = image.shape[0:2]
    new_h = int(width * (h / w))
    return cv2.resize(image, (width, new_h))
