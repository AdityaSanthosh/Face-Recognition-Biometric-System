def recognize_attendance():
    import face_recognition
    from datetime import datetime
    import cv2
    import numpy as np

    known_face_encodings = np.load('encode-data.npy', allow_pickle=True)
    known_face_names = np.load('known-faces.npy', allow_pickle=True)
    print(known_face_encodings)
    print(known_face_names)

    def markAttendance(name):
        with open('Attendance_Records/Attendance.csv', 'r+') as f:
            myDataList = f.readlines()
            face_names = []
            for line in myDataList:
                entry = line.split(',')
                face_names.append(entry[0])
            if name not in face_names:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                f.writelines(f'\n{name},{dtString}')

    cap = cv2.VideoCapture(0)
    process_this_frame = True
    while True:
        ret, frame = cap.read()
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            # Find all the faces and encodings in the current frame of video
            current_face_locations = face_recognition.face_locations(rgb_small_frame)
            current_face_encodings = face_recognition.face_encodings(rgb_small_frame, current_face_locations)
        process_this_frame = not process_this_frame

        for (top,right,bottom,left), face_encoding in zip(current_face_locations, current_face_encodings):
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
            break

    cap.release()
    cv2.destroyAllWindows()

