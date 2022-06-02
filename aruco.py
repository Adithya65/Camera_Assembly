import cv2
import cv2.aruco as aruco
import numpy as np
import os
def findArucoMarkers(img, markerSize = 6, totalMarkers=250, draw=True):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    bboxs, ids, rejected = aruco.detectMarkers(gray, arucoDict, parameters = arucoParam)
    if ids!=None:
        print(ids)
    if draw:
        aruco.drawDetectedMarkers(img, bboxs) 
        return ids
cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    ids=findArucoMarkers(img)
    img = cv2.putText(img, str(ids), (460, 60),cv2.FONT_HERSHEY_SIMPLEX, 
                  2, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
