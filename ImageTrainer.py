import face_recognition
import os
import cv2
from numpy import save


def findEncoding(img):
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    faces = face_recognition.face_locations(image)
    encode = face_recognition.face_encodings(image, faces)[0]
    return encode


def train_image():
    path = "StudentDetails/StudentPictures"
    encodeList = []
    known_face_names = []
    known_face_ids = []

    for imagefilename in os.listdir(path):
        curImg = cv2.imread(path+'/'+imagefilename)
        known_face_names.append(imagefilename.split('.')[0])
        known_face_ids.append(imagefilename.split('.')[1])
        encoding = findEncoding(curImg)
        encodeList.append(encoding)

    known_faces_data = list(zip(known_face_names, known_face_ids))
    save('encode-data.npy', encodeList)
    save('known-faces-data.npy', known_faces_data)
    print(encodeList)
    print(known_faces_data)
    print("encoding Complete")