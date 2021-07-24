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


def remove_user():
    import numpy as np
    import ImageTrainer
    import os

    print("Remove an existing User from the database\n This action cannot be undone")
    id = str(input("Enter the id of the user you want to remove"))
    known_faces_data = np.load("known-faces-data.npy", allow_pickle=True)
    known_faces, face_id = zip(*known_faces_data)
    print(face_id)

    if is_number(id) and id in face_id:
        print("Id found")
        confirmation = str(input(f'Removing user with id {id}. Do you really want to Continue\t Y or N?'))
        if confirmation.lower() == "y":
            index = face_id.index(id)
            face_id = list(face_id)
            known_faces = list(known_faces)
            face_id.remove(id)
            face_removed = known_faces.pop(index)
            known_faces = tuple(known_faces)
            face_id = tuple(face_id)
            face_name = face_removed + "." + id + ".jpg"
            os.remove("StudentDetails/StudentPictures/%s" % face_name)
            ImageTrainer.train_image()
            print("id removed.\n You have to register again in case this is an accident")
        else:
            print("Exiting the wizard..")
    else:
        print("Id not found.")
