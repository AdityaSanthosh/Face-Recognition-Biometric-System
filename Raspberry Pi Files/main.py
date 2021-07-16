from scipy.spatial import distance
import face_recognition
from datetime import datetime
import numpy as np
import picamera
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
# Select GPIO mode
GPIO.setmode(GPIO.BCM)
# Set buzzer - pin 23 as output
buzzer = 23
GPIO.setup(buzzer, GPIO.OUT)


def markAttendance(name):
    with open('Attendance_Records/Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        face_names = []
    for line in myDataList:
        entry = line.split(',')
        face_names.append(entry[0])
    if name not in face_names:
        now = datetime.now()
        dtString = now.strftime('%H:%M')
        f.writelines(f'\n{name},{dtString},{datetime.today().strftime("%d-%m-%Y")}')
        # BUZZER SOUND with Name on Display
        GPIO.output(buzzer, GPIO.HIGH)
        # Send Attendance Data to an external computer via Internet or Streaming


def recognize_attendance():
    eyes_closed_time = 0
    eyes_opened_time = 0
    known_face_encodings = np.load('encode-data.npy', allow_pickle=True)
    known_face_names = np.load('known-faces.npy', allow_pickle=True)

    while True:
        camera = picamera.PiCamera()
        camera.resolution = (320, 240)
        camera.color_effects = (128, 128)
        rgb_small_frame = np.empty((240, 320, 3), dtype=np.uint8)
        camera.capture(rgb_small_frame, format="rgb")
        face_landmarks_list = face_recognition.face_landmarks(rgb_small_frame)
        for face_landmark in face_landmarks_list:
            left_eye = face_landmark['left_eye']
            right_eye = face_landmark['right_eye']
            ear_left = get_ear(left_eye)
            ear_right = get_ear(right_eye)
            closed = ear_left < 0.2 and ear_right < 0.2
            if closed:
                eyes_closed_time += 1
            else:
                eyes_opened_time += 1
            if eyes_closed_time > 1 and eyes_closed_time > 1:
                current_face_locations = face_recognition.face_locations(rgb_small_frame)
                current_face_encodings = face_recognition.face_encodings(rgb_small_frame, current_face_locations)

                for face_encoding in current_face_encodings:
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    faceDis = face_recognition.face_distance(known_face_encodings, face_encoding)
                    matchIndex = np.argmin(faceDis)

                    if matches[matchIndex]:
                        name = known_face_names[matchIndex]
                        markAttendance(name)


def get_ear(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear


recognize_attendance()
