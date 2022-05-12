import os

import cv2
import numpy

from ..app_config.file_path_manage.file_path_manage import bin_file_path


def detector_face(detector_image: numpy.ndarray):
    mark_image = list()
    bgr_detector_image = cv2.cvtColor(detector_image, cv2.COLOR_RGB2BGR)
    crop_image = numpy.ndarray
    lib_path = os.path.dirname(__file__)
    face_cascade = cv2.CascadeClassifier(os.path.join(bin_file_path, "haarcascade_frontalface_alt.xml"))
    gray = cv2.cvtColor(bgr_detector_image, cv2.COLOR_BGR2GRAY)  # 轉換成灰階
    faces = face_cascade.detectMultiScale(bgr_detector_image, scaleFactor=1.1, minNeighbors=5, minSize=(80, 80))
    for (x, y, w, h) in faces:
        # mark face
        mark_image = cv2.rectangle(detector_image, (x, y), (x + w, y + h), (50, 159, 242), 3)
        crop_image = bgr_detector_image[y:y + h, x:x + w]
    return cv2.cvtColor(crop_image, cv2.COLOR_BGR2RGB), cv2.cvtColor(mark_image, cv2.COLOR_BGR2RGB)


if __name__ == "__main__":
    image = cv2.imread("./test_image/tim_cook.jpg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imwrite("face_detector.jpg", cv2.cvtColor(detector_face(image), cv2.COLOR_RGB2BGR))
