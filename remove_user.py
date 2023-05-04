def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


def remove_user(user_id):
    import numpy as np
    import ImageTrainer
    import os

    known_faces_data = np.load("known-faces-data.npy", allow_pickle=True)
    known_faces, face_id = zip(*known_faces_data)
    print(face_id)

    if is_number(user_id) and user_id in face_id:
        print("Id found")
        confirmation = str(input(f'Removing user with id {user_id}. Do you really want to Continue\t Y or N?'))
        if confirmation.lower() == "y":
            index = face_id.index(user_id)
            face_id = list(face_id)
            known_faces = list(known_faces)
            face_id.remove(user_id)
            face_removed = known_faces.pop(index)
            known_faces = tuple(known_faces)
            face_id = tuple(face_id)
            face_name = face_removed + "." + user_id + ".jpg"
            os.remove("StudentDetails/StudentPictures/%s" % face_name)
            ImageTrainer.train_image()
            print("id removed.\n You have to register again in case this is an accident")
        else:
            print("Exiting the wizard..")
    else:
        print("Id not found.")
