import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math


class Images():
    def __init__(self) -> None:
        self.__cap = cv2.VideoCapture(0)
        self.__detector = HandDetector(maxHands=1)
        self.__classifier = Classifier("Model/keras_model.h5", "Model/labels.txt")
        self.__offset = 20
        self.__img_size = 300
        self.__labels = ["A", "B", "C"]

    def __image_cropped(self, img, x, y, h, w, offset=0):
        img_crop = img[y-offset:y+h+offset, x-offset:x+w+offset]
        return img_crop

    def __image_white_bg(self, img_size):
        return np.ones((img_size, img_size, 3),np.uint8)*255

    def __prediction(self,img_white, img_crop, w, h, img_size):
        aspectRatio = h/w

        if aspectRatio > 1:
            k = img_size/h
            w_cal = math.ceil(k*w)
            img_resize = cv2.resize(img_crop, (w_cal, img_size))
            w_gap = math.ceil((img_size-w_cal)/2)

            img_white[:, w_gap:w_cal+w_gap] = img_resize
            prediction, index = self.__classifier.getPrediction(img_white, draw=False)
            print(prediction, index)
        else:
            k = img_size/w
            h_cal = math.ceil(k*h)
            img_resize = cv2.resize(img_crop, (img_size, h_cal))
            h_gap = math.ceil((img_size-h_cal)/2)
            img_white[h_gap:h_cal+h_gap, :] = img_resize
            prediction, index = self.__classifier.getPrediction(img_white, draw=False)
            print(prediction, index)
        return prediction, index

    def get_images(self):
        while True:
            success, img = self.__cap.read()
            img_output = img.copy()
            hands, img = self.__detector.findHands(img)

            if hands:
                hand = hands[0]
                x, y, w, h = hand['bbox']
                img_white = self.__image_white_bg(self.__img_size)
                img_crop = self.__image_cropped(img,x,y,w,h,offset=self.__offset)

                pred, index = self.__prediction(img_white=img_white, img_crop=img_crop, w=w, h=h, img_size=self.__img_size)

                cv2.putText(img_output, self.__labels[index], (x,y-20), cv2.FONT_HERSHEY_COMPLEX, 2, (0,255,0), 2)
                cv2.rectangle(img_output, (x-self.__offset,y-self.__offset), (x+w+self.__offset,y+h+self.__offset), (0,255,0),4)
        
            cv2.imshow("Image", img_output)