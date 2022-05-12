import os
import pickle
import cv2
import face_recognition


class FaceInfo:
    def __init__(self, face_name: str, face_image_path: str):
        self.face_name = face_name
        self.face_image_path = face_image_path


class FaceData:
    def __init__(self):
        self.face_name = str()
        self.encode = list()


def add_face_data(data_path: str, add_face_info: FaceInfo):
    # read image
    image = cv2.imread(add_face_info.face_image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # create face data about encode and face name
    face_data = FaceData()
    face_data.face_name = add_face_info.face_name
    face_data.encode = face_recognition.face_encodings(image, model='large')[0]

    # add face data
    face_datas = load_face_data(data_path)
    face_datas.append(face_data)

    # save face datas
    with open(data_path, 'wb') as f:
        pickle.dump(face_datas, f)


def load_face_data(data_path: str):
    datas = list()
    # read file
    if os.path.isfile(data_path):
        with open(data_path, 'rb') as f:
            datas = pickle.load(f)
    # if datas file is not create, return blank
    else:
        return list()
    return datas


if __name__ == "__main__":
    face_info = FaceInfo("Tim Cook", "./test_image/tim_cook.jpg")
    add_face_data("./test_data", face_info)

