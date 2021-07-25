# importing cv2 liberary
import cv2, numpy #datetime
import time

# 1. Create an object. zero for external camera
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# define a variable
count = 0

while True:
    # 3. Create a frame object
    ret, img = cam.read()

    # 4. Show the frame!


    # 7. For playing


    if ret:
        font = cv2.FONT_HERSHEY_TRIPLEX
        #dt = str(datetime.datetime.now())
        t = time.strftime("%d-%m-%Y %H:%M:%S")
        img = cv2.putText(img, t, (100, 450), font, 1, (0, 155, 155), 3, cv2.LINE_8)
        cv2.imshow("Test", img)
        k = cv2.waitKey(500)
        min = time.strftime("%M")
        sec = time.strftime("%S")
        m = int(min)
        s = int(sec)

    if k % 256 == 27:
        # For Esc key
        print("Close")
        break
    #elif k % 256 == 32:
    elif m % 10 == 0 and s % 53 <= 5:
        # For Space key

        print("Image " + t + "saved")
        file = 'C:/Users/Raja Saheb/Desktop/Base/' + t + '.jpg'
        cv2.imwrite(file, img)
        count += 1

cam.release
cv2.destroyAllWindows