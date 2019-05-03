import cv2
import numpy as np
Detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cap=cv2.VideoCapture(0);

id=raw_input('enter user id')
num=0;
while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = Detector.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        num=num+1;
        cv2.imwrite("dataSet/User."+str(id)+"."+str(num)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100);
    cv2.imshow("frame",img);
    cv2.waitKey(1);
    if(num >20):
       break
cap.release()
cv2.destroyAllWindows()


