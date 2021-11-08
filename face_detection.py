import cv2
from cv2 import cv2

trained_dataset = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video = cv2.VideoCapture("Rajiv.mp4")
#img = cv2.imread("1.jpg")
#grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cordinates = trained_dataset.detectMultiScale(grayed)
# for (x, y, w, h) in cordinates:
#cv2.rectangle(img, (x, y), (x+w, y+h), (225, 0, 0), 2)
# print(cordinates)
# print("work")
#cv2.imshow("wow", img)
# cv2.waitKey()
running = True
while running:

    sucessful_frame_read, frame = video.read()
    grayscaledimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cordinates = trained_dataset.detectMultiScale(grayscaledimg)
    for (x, y, w, h) in face_cordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 225, 0), 2)
    cv2.imshow("face_detection", frame)
    key = cv2.waitKey(1)
    if key == 81 or key == 113:
        break
