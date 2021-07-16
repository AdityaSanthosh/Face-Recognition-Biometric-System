from scipy.spatial import distance
import face_recognition
from datetime import datetime
import cv2
import numpy as np


def recognize_attendance():
    eyes_closed_time = 0
    eyes_opened_time = 0
    known_face_encodings = np.load('encode-data.npy', allow_pickle=True)
    known_face_names = np.load('known-faces.npy', allow_pickle=True)

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

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
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
            if True:
                current_face_locations = face_recognition.face_locations(rgb_small_frame)
                current_face_encodings = face_recognition.face_encodings(rgb_small_frame, current_face_locations)

                for (top, right, bottom, left), face_encoding in zip(current_face_locations,
                                                                     current_face_encodings):
                    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                    faceDis = face_recognition.face_distance(known_face_encodings, face_encoding)
                    matchIndex = np.argmin(faceDis)

                    if matches[matchIndex]:
                        name = known_face_names[matchIndex]
                        markAttendance(name)

                        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                        top *= 4
                        right *= 4
                        bottom *= 4
                        left *= 4
                    # Draw a Rectangle around the Face
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

                # display the frame
                cv2.imshow('Video', frame)
                # wait for 100 milliseconds
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    print('exited..\n')
                    cap.release()
                    cv2.destroyAllWindows()
                    break


def get_ear(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear