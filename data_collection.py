import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
counter = 0
directory = "Data/dont swear"

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    offset = 20
    img_size = 300
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        img_white = np.ones((img_size, img_size, 3),np.uint8)*255
        img_crop = img[y-offset:y+h+offset, x-offset:x+w+offset]

        aspectRatio = h/w

        if aspectRatio > 1:
            k = img_size/h
            w_cal = math.ceil(k*w)
            img_resize = cv2.resize(img_crop, (w_cal, img_size))
            w_gap = math.ceil((img_size-w_cal)/2)
            img_white[:, w_gap:w_cal+w_gap] = img_resize
        else:
            k = img_size/w
            h_cal = math.ceil(k*h)
            img_resize = cv2.resize(img_crop, (img_size, h_cal))
            h_gap = math.ceil((img_size-h_cal)/2)
            img_white[h_gap:h_cal+h_gap, :] = img_resize

        cv2.imshow("ImageCrop", img_crop)
        cv2.imshow("ImageWhite", img_white)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    
    if key == ord("s"):
        counter += 1
        cv2.imwrite(f'{directory}/Image_{time.time()}.jpg', img_white)
        print(counter)