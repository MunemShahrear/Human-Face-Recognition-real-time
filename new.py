import cv2
import numpy as np
frontalface = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
nose = cv2.CascadeClassifier('haarcascade_mcs_nose.xml');
eye = cv2.CascadeClassifier('haarcascade_eye.xml');
eyeglass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml');
frontcat= cv2.CascadeClassifier('haarcascade_frontalcatface.xml');
frontcatex= cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml');
frontalalt= cv2.CascadeClassifier('haarcascade_frontalface_alt.xml');
frontalalttree= cv2.CascadeClassifier('haarcascade_frontalface_alt_tree.xml');
frontalalt2= cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml');
lefteyesplits= cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml');
righteyesplits= cv2.CascadeClassifier('haarcascade_righteye_2splits.xml');
profileface=cv2.CascadeClassifier('haarcascade_profileface.xml');
righteye = cv2.CascadeClassifier('haarcascade_mcs_righteye.xml');
rightear = cv2.CascadeClassifier('haarcascade_mcs_rightear.xml');
lefteye = cv2.CascadeClassifier('haarcascade_mcs_lefteye.xml');
leftear = cv2.CascadeClassifier('haarcascade_mcs_leftear.xml');
mouth = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml');
bigeye = cv2.CascadeClassifier('haarcascade_mcs_eyepair_big.xml');
smalleye = cv2.CascadeClassifier('haarcascade_mcs_eyepair_small.xml');
smile = cv2.CascadeClassifier('haarcascade_smile.xml');

cap=cv2.VideoCapture(1);

id=raw_input('enter user id')
num=0;

while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = frontalface.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in faces:
        num=num+1;
        cv2.imwrite("dataSet/User."+str(id)+"."+str(num)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100);
    cv2.imshow("facial recognition",img);
    cv2.waitKey(1);
    if(num >120):
       break
       

while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    nosy = nose.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in nosy:
        num=num+1;
        cv2.imwrite("dataSet/User."+str(id)+"."+str(num)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100);
    cv2.imshow("facial recognition",img);
    cv2.waitKey(1);
    if(num >140):
       break
       

while(True):
    
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    frntcat = frontcat.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in frntcat:
        num=num+1;
        cv2.imwrite("dataSet/User."+str(id)+"."+str(num)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100);
    cv2.imshow("facial recognition",img);
    cv2.waitKey(1);
    if(num >160):
       break
      
  

while(True):
   
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    frntcatx = frontcatex.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in frntcatx:
        num=num+1;
        cv2.imwrite("dataSet/User."+str(id)+"."+str(num)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100);
    cv2.imshow("facial recognition",img);
    cv2.waitKey(1);
    if(num >180):
       break
       

    
while(True):
    
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mth = mouth.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in mth:
        num=num+1;
        cv2.imwrite("dataSet/User."+str(id)+"."+str(num)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100);
    cv2.imshow("facial recognition",img);
    cv2.waitKey(1);
    if(num >200):
       break
   



    
cap.release()
cv2.destroyAllWindows()


