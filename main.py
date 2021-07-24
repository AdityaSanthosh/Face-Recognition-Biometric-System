import os
import CameraCheck
import ImageCapture
import ImageTrainer
import Recognize


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
    # print("[3] Train Image")
    print("[3] Record Attendance")
    print("[4] Quit")

    while True:
        try:
            choice = int(input("Enter Choice: "))
            if choice == 1:
                check_camera()
                break
            elif choice == 2:
                CaptureImage()
                break
            # elif choice == 3:
            #     TrainImage()
            #     break
            elif choice == 3:
                record_attendance()
                break
            elif choice == 4:
                print("Have a Nice Day!")
                break
            else:
                print("Invalid Choice. Enter 1-3")
                main_menu()
        except ValueError:
            print("Invalid Choice. Enter 1-3\n Try Again")
    exit


def check_camera():
    CameraCheck.camera_check()
    key = input("Enter any key to return main menu")
    main_menu()


def CaptureImage():
    ImageCapture.capture_image()
    key = input("Enter any key to return main menu")
    main_menu()

#
# def TrainImage():
#     ImageTrainer.train_image()
#     key = input("Enter any key to return main menu")
#     main_menu()

def record_attendance():
    Recognize.recognize_attendance()
    key = input("Enter any key to return main menu")
    main_menu()


# main driver
main_menu()
