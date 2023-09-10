import cv2 as cv

# img = cv.imread('Photos/cat.jpg')
# cv.imshow('Cat', img) # reading photo

# cv.waitKey(0)

capture = cv.VideoCapture(0)

while True:
	isTrue, frame = capture.read()
	cv.imshow("Video", frame)

	if cv.waitKey(20) & 0xFF==ord('d'): #if d is pressed break loop
		break

capture.release()

cv.destroyAllWindows
