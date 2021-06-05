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
    known_faces = []

    for imagefilename in os.listdir(path):
        curImg = cv2.imread(path+'/'+imagefilename)
        print(imagefilename)
        known_faces.append(imagefilename.split('.')[0])
        encoding = findEncoding(curImg)
        encodeList.append(encoding)

    save('encode-data.npy', encodeList)
    save('known-faces.npy', known_faces)
    print(encodeList)
    print(known_faces)
    print("encoding Complete")
