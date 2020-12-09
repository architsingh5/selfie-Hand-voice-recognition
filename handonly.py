# Python Project, Topic = Selfie with Hand Recognition
# Contributors = Archit Singh, Abhishek Jajoo

# importing libraries
import cv2
import time
import os
from playsound import playsound

print("\nShow your palm to camera so that it can shoot picture after interval of approx. 3 seconds")
print("Press Esc key to close the camera and end the program\n")

# Detecting CascadeClassifier
palm_cascade = cv2.CascadeClassifier("haarcascade_palm.xml")

# Initializing Camera with camera 0, if code is not working for you, change the
# value in function to 1,2 ,3 or -1.
cap = cv2.VideoCapture(0)

# Defining flagging variables
flag = 1
# Count Variable for keeping track of no. of images and helping to rename new images.
count = 1
# TimeStamp Variable initialized to 0, changes when request for taking picture is made.
timestamp = 0

# while loop is checking that whether camera is opened and receiving images otherwise it doesn't run
# by function cap.isOpened()

while cap.isOpened():

    # cap.read() returns two values first is boolean type which confirms us that frame is received and
    # second variable gives us a frame
    ret, frame = cap.read()

    # flipping camera to accommodate lateral inversion
    frame = cv2.flip(frame, +1)

    # if frame is received, the further code runs, otherwise it just break the while loop
    if ret:

        # converting captured frame to gray to decrease computations
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detectMultiScale detects objects of different sizes in the input image. The detected objects
        # are returned as a list of rectangles.
        palms = palm_cascade.detectMultiScale(gray, 1.3, 5)

        if len(palms) and flag:

            # Collecting timestamp when request for taking picture is made.
            timestamp = time.time()
            flag = 0
            print("Palm Detected")

        # loop to show rectangle around the detected palm
        for x, y, w, h in palms:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

        # Code to show countdown and then finally taking picture
        if flag == 0:

            if timestamp < time.time() < (timestamp+1):
                cv2.putText(frame, "Taking picture in 3", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

            elif timestamp < time.time() < (timestamp+2):
                cv2.putText(frame, "Taking picture in 2", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

            elif timestamp < time.time() < (timestamp+3):
                cv2.putText(frame, "Taking picture in 1", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

            if (timestamp+4) < time.time():
                print("Picture Taken\n")

                # Code to maintain serial wise images name in images folder.
                for i in range(1, 10000):
                    if not os.path.isfile("./images/img" + str(i) + ".png"):
                        count = i
                        break

                # writing image to storage
                cv2.imwrite("images/img" + str(count) + ".png", frame)
                # playing camera shutter sound to create effect
                playsound("Camera-Beep.mp3")

                flag = 1
                time1 = 0

        # continuously displaying frames
        cv2.imshow('Camera', frame)

        # Code waiting for Esc key to end the loop
        if cv2.waitKey(1) == 27:
            break
    else:
        break

# ending and deallocating memory commands
cap.release()
cv2.destroyAllWindows()
print("Thank You")
