import cv2
import numpy as np
import datetime
frontalface = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cap=cv2.VideoCapture(1);
rec=cv2.createLBPHFaceRecognizer();
rec.load("recognizer\\trainingData.yml")
id=0
text_file = open("entry.txt", "a")
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,5,1)
while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = frontalface.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if(conf<40):
             id="Unkown"
             cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,0,255));
        else:
           cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
           if(id==1 ):
             id="152-15-5715"
             text_file.write("\nMunem Shahrear                    "+id)
             
             
             cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,255,0));
           elif(id==2):
             id="151-15-5236"
             text_file.write("\nMehedi Hasan                    "+id)
             cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,255,0));
           elif(id==3):
             id="152-15-5677"
             text_file.write("\nNoor-E-Shams                    "+id)
             cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,255,0));     
           elif(id==4):
             id="151-15-4960"
             text_file.write("\nMd Zahid Hasan                   "+id)
             cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,255,0));
           elif(id==5):
             id="152-15-5672"
             text_file.write("\nRabeya sultana Ripa                    "+id)
             cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,255,0));
           elif(id==6):
             id="152-15-5977"
             text_file.write("\nDip Dutt                    "+id)
             cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,255,0));
           elif(id==7):
             id="152-15-5979"
             text_file.write("\nShaidul Hasan                   "+id)
             cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,255,0));     
           elif(id==8):
             id="152-15-5728"
             text_file.write("\nRezwan sheikh                    "+id)
             cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,255,0));
           elif(id==9):
             id="152-15-5967"
             text_file.write("\nRakibul Hasan                    "+id)
             cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,255,0));
           elif(id==10):
             id="152-15-5941"
             text_file.write("\nArif Hasan                    "+id)
             cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,255,0));
           elif(id==11):
             id="152-15-5974"
             text_file.write("\nShihab Uddin                    "+id)
             cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,255,0));     
           elif(id==12):
             id="152-15-5954"
             text_file.write("\nKangkan Bar                    "+id)
             cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,255,0));
           elif(id==13):
             id="152-15-5956"
             text_file.write("\nIshrat Jahan                    "+id)
             cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,255,0));
           elif(id==14):
             id="152-15-5528"
             text_file.write("\nReshmi Akter                    "+id)
             cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,(0,255,0));
           
    cv2.imshow('frame',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()

