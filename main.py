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
            TrainImage()
            break
        elif choice == 4:
            record_attendance()
            break
        elif choice == 5:
            removeUser()
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
    key = input("Enter any key to return main menu")
    main_menu()


def CaptureImage():
    ImageCapture.capture_image()
    key = input("Enter any key to return main menu")
    main_menu()



def record_attendance():
    Recognize.recognize_attendance()
    key = input("Enter any key to return main menu")
    main_menu()


def removeUser():
    remove_user.remove_user()
    key = input("Enter any key to return main menu")
    main_menu()

def TrainImage():
    ImageTrainer.train_image()
    key = input("Enter any key to return main menu")
    main_menu()

# main driver
main_menu()
