Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import cv2
>>> image_path='pt.jpg'
>>> casc_path='haarcascade_frontalface_default.xml'
>>> face_cascade=cv2.CascadeClassifier(casc_path)
>>> image=cv2.imread(image_path)
>>> gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
>>> face=face_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize = (30,30))
>>> for(x,y,z,h)in face:
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

	
Traceback (most recent call last):
  File "<pyshell#9>", line 2, in <module>
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
NameError: name 'w' is not defined
>>> for(x,y,w,h)in face:
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

	
array([[[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       ...,

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 254, 253],
        [255, 254, 253],
        [255, 254, 253]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]]], dtype=uint8)
>>> cv2.imshow("Face detected",image)
>>> import random
>>> for(x,y,w,h)in face:
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
	cv2.putText(image,str(random.randrange(15,20)),(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)

	
array([[[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       ...,

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 254, 253],
        [255, 254, 253],
        [255, 254, 253]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]]], dtype=uint8)
array([[[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       ...,

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 254, 253],
        [255, 254, 253],
        [255, 254, 253]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]],

       [[255, 255, 255],
        [255, 255, 255],
        [255, 255, 255],
        ...,
        [255, 255, 255],
        [255, 255, 255],
        [255, 255, 255]]], dtype=uint8)
>>> cv2.imshow("Face detected",image)
>>> cv2.imshow("Face detected",image)
>>> 
