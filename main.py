import pickle
import time

import cv2
import numpy as np
import face_recognition
import os

tolerance = 0.6

known_face_list = [
    {
        'name': '朝勝',
        'filename': 'teacher.jpg',
        'encode': None,
    },
    {
        'name': '29',
        'filename': '29.jpg',
        'encode': None,
    },
{
        'name': '11',
        'filename': '11.jpg',
        'encode': None,
    },
]

test_fn_list = ["11_test.jpg"]

known_face_encodes = None

if False:
    # load image data by large model of face landmarks
    for data in known_face_list:
        img = cv2.imread(data['filename'])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        data['encode'] = face_recognition.face_encodings(img, model='large')[0]  # use large model of face landmarks

    known_face_encodes = [data['encode'] for data in known_face_list]

    with open('dataset_faces.dat', 'wb') as f:
        pickle.dump(known_face_encodes, f)


else:
    with open('dataset_faces.dat', 'rb') as f:
        known_face_encodes = pickle.load(f)



# face recognition
for fn in test_fn_list:
    img = cv2.imread(fn)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    cur_face_locs = face_recognition.face_locations(img)
    cur_face_encodes = face_recognition.face_encodings(img, cur_face_locs,
                                                       model='small')  # use small model of face landmarks

    for cur_face_encode in cur_face_encodes:
        face_distance_list = face_recognition.face_distance(known_face_encodes, cur_face_encode)

        min_distance_index = np.argmin(face_distance_list)
        if face_distance_list[min_distance_index] < tolerance:
            result = known_face_list[min_distance_index]['name']
        else:
            result = 'unknown'

        distance_with_name_list = [(face_data['name'], round(distance, 4)) for face_data, distance in
                                   zip(known_face_list, face_distance_list)]
        print(
            f'辨識檔案: {fn}, 辨識結果: {result}, 特徵距離: {distance_with_name_list}, 相差: {round(abs(distance_with_name_list[0][1] - distance_with_name_list[1][1]), 4)}')
#
# # face recognition 68
# for fn in test_fn_list:
#     img = cv2.imread(fn)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
#     cur_face_locs = face_recognition.face_locations(img)
#     cur_face_encodes = face_recognition.face_encodings(img, cur_face_locs,
#                                                        model='large')  # use large model of face landmarks
#
#     for cur_face_encode in cur_face_encodes:
#         face_distance_list = face_recognition.face_distance(known_face_encodes, cur_face_encode)
#
#         min_distance_index = np.argmin(face_distance_list)
#         if face_distance_list[min_distance_index] < tolerance:
#             result = known_face_list[min_distance_index]['name']
#         else:
#             result = 'unknown'
#
#         distance_with_name_list = [(face_data['name'], round(distance, 4)) for face_data, distance in
#                                    zip(known_face_list, face_distance_list)]
#         print(
#             f'辨識檔案: {fn}, 辨識結果: {result}, 特徵距離: {distance_with_name_list}, 相差: {round(abs(distance_with_name_list[0][1] - distance_with_name_list[1][1]), 4)}')
#
