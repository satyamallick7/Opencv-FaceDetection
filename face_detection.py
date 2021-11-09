import cv2
import os
os.system("cls")

face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# img = cv2.imread("faces.jpg")

webcam = cv2.VideoCapture(0)

color = (0,0,255)
thickness = 2


while True:
    frame_read, frame = webcam.read()

    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = face_data.detectMultiScale(grayscale_img)

    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, thickness)

    cv2.imshow("faces", frame)

    key = cv2.waitKey(1)

    if key==27:
        cv2.destroyAllWindows()
        break














# print(face_coordinates)



