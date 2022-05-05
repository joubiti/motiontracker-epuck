import cv2 
import numpy as np 

def funct(x):
	pass


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)
cv2.createTrackbar("Hue Min","TrackBars",25,179,funct)
cv2.createTrackbar("Hue Max","TrackBars",173,179,funct)
cv2.createTrackbar("Sat Min","TrackBars",41,255,funct)
cv2.createTrackbar("Sat Max","TrackBars",255,255,funct)
cv2.createTrackbar("Val Min","TrackBars",0,255,funct)
cv2.createTrackbar("Val Max","TrackBars",255,255,funct)

while True:
	img=cv2.imread('test.png')
	imgHSV=cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
	h_min=cv2.getTrackbarPos("Hue Min","TrackBars")
	h_max=cv2.getTrackbarPos("Hue Max","TrackBars")
	s_min=cv2.getTrackbarPos("Sat Min","TrackBars")
	s_max=cv2.getTrackbarPos("Sat Max","TrackBars")
	v_min=cv2.getTrackbarPos("Val Min","TrackBars")
	v_max=cv2.getTrackbarPos("Val Max","TrackBars")

	print(h_min,h_max,s_min,s_max,v_min,v_max)
	ll=np.array([h_min,s_min,v_min])
	ul=np.array([h_max,s_max,v_max])
	mask=cv2.inRange(imgHSV,ll,ul)

	cv2.imshow("OC",img)
	cv2.imshow("HSV",imgHSV)
	cv2.imshow("mask",mask)

	cv2.waitKey(1)
