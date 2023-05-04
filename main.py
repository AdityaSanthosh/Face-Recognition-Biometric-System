import os
import CameraCheck
import ImageCapture
import ImageTrainer
import Recognize
import remove_user


def title_bar():
    # os.system('clear')
    os.system('cls')
    # title of the program
    print("\t**********************************************")
    print("\t***** Face Recognition Attendance System *****")
    print("\t**********************************************")


def main_menu():
    title_bar()
    print(10 * "*", "WELCOME MENU", 10 * "*")
    print("[1] Check Camera")
    print("[2] New User")
    print("[3] Train Image")
    print("[4] Record Attendance")
    print("[5] Remove User")
    print("[6] Quit")

    while True:
        choice = int(input("Enter Choice: "))
        if choice == 1:
            check_camera()
            break
        elif choice == 2:
            CaptureImage()
            break
        elif choice == 3:
            train_image()
            break
        elif choice == 4:
            record_attendance()
            break
        elif choice == 5:
            remove_user()
            break
        elif choice == 6:
            print("Have a Nice Day!")
            break
        else:
            print("Invalid Choice. Enter 1-5")
            main_menu()
        # try:
    #     except ValueError:
    #         print("Invalid Choice. Enter 1-5\n Try Again")
    # exit


def check_camera():
    CameraCheck.camera_check()
    input("Enter any key to return main menu")
    main_menu()


def CaptureImage():
    ImageCapture.capture_image()
    input("Enter any key to return main menu")
    main_menu()


def record_attendance():
    Recognize.recognize_attendance()
    input("Enter any key to return main menu")
    main_menu()


def remove_user():
    print("Remove an existing User from the database\n This action cannot be undone")
    user_id = str(input("Enter the id of the user you want to remove"))
    remove_user.remove_user(user_id)
    input("Enter any key to return main menu")
    main_menu()


def train_image():
    ImageTrainer.train_image()
    input("Enter any key to return main menu")
    main_menu()


if __name__ == "__main__":
    main_menu()
