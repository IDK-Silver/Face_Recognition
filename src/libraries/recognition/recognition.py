import numpy
import face_recognition


def recognition(face_image: numpy.ndarray, face_datas: list, tolerance: float) -> str:
    result = 'unknown'
    cur_face_locs = face_recognition.face_locations(face_image)
    cur_face_encodes = face_recognition.face_encodings(face_image, cur_face_locs
                                                       )  # use small model of face landmarks
    known_face_encodes = [data.encode for data in face_datas]
    for cur_face_encode in cur_face_encodes:
        face_distance_list = face_recognition.face_distance(known_face_encodes, cur_face_encode)

        min_distance_index = numpy.argmin(face_distance_list)
        if face_distance_list[min_distance_index] < tolerance:
            result = face_datas[min_distance_index].face_name
        else:
            result = 'unknown'
    print(f'辨識結果: {result}')
    return result


if __name__ == "__main__":
    from ..face_data.face_data import *

    image = cv2.imread("./test_image/tim_cook.jpg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    recognition(image, load_face_data(os.path.abspath("../face_data/test_data")), 0.5)

    from ..face_detector.face_detector import *

    image = cv2.imread("./test_image/fake_tim.jpg")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    recognition(detector_face(image)[0], load_face_data(os.path.abspath("../face_data/test_data")), 0.5)

