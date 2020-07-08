import cv2 as cv
video = cv.VideoCapture(0, cv.CAP_DSHOW)
video.set(cv.CAP_PROP_FRAME_WIDTH, 1500)
video.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
while(True):
	ret, frame = video.read()
	#frame = cv.GaussianBlur(frame,(1,1),0)
	cartoon_image = cv.stylization(frame, sigma_s=60, sigma_r=0.25)  
	dst = cv.detailEnhance(cartoon_image, sigma_s=30, sigma_r=0.1)
	cv.imshow('cartoon', dst)  
	if cv.waitKey(20) & 0xFF == ord('q'): 
		break