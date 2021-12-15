# import the necessary packages
import imutils
import cv2
import math

camera = cv2.VideoCapture(0)


#				(90, 130, 40), (115, 255, 155) Bright environmemnts
#				(60, 30, 25), (135, 255, 195) dark environmemnts
colorRanges = [((60, 30, 25), (135, 255, 195), "ball")]


#find circularity of each contour Area vs Perimeter (sqrt(Area)/pi) = r = C/(2*pi))
#perhaps implement a perimetersimplification method to remove occlusions

def Area_vs_Perimeter(contours):
	P = cv2.arcLength(contours,True)
	A = cv2.contourArea(contours)
	R1 = P / (2*3.14159265) 
	R2 = math.sqrt(A/3.14159265)
	return abs(R1-R2)

# keep looping
while True:
	# grab the current frame
	(grabbed, frame) = camera.read()

	# resize the frame, blur it, and convert it to the HSV color space
	frame = imutils.resize(frame, width=440)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# loop over the color ranges
	for (lower, upper, colorName) in colorRanges:
		# construct a mask for all colors in the current HSV range, then
		# perform a series of dilations and erosions to remove any small
		# blobs left in the mask
		mask = cv2.inRange(hsv, lower, upper)
		cv2.imshow("mask", mask)
		mask = cv2.erode(mask, None, iterations=4)
		cv2.imshow("Erode", mask)
		mask = cv2.dilate(mask, None, iterations=2)
		cv2.imshow("Dilate", mask)

				# find contours in the mask
		cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		cnts = imutils.grab_contours(cnts)
		# only proceed if at least one contour was found
		if len(cnts) > 0:

			# find the largest contour in the mask, then use it to compute
			# the minimum enclosing circle and centroid
			c = min(cnts, key=Area_vs_Perimeter)
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			(cX, cY) = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
			P = cv2.arcLength(c,True)
			A = cv2.contourArea(c)
			R = ((P / (2*3.14159265)) + (math.sqrt(A/3.14159265)))/2

			
			# only draw the enclosing circle and text if the radious meets
			# a minimum size

			# Circular object filter
			# do the largest contours selected fit in a least radius circle plus or minus 10 pixels and a certain percentage of the circle

			# draw all contours on frame
			cv2.drawContours(frame, cnts ,0, (0,255,0), 3)
			if radius > 10 and Area_vs_Perimeter(c) < 20:
				#cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
				cv2.putText(frame, colorName, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 255), 2)
				cv2.putText(frame, "P " + str(round(P,1)), (cX, (cY+23)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
				cv2.putText(frame, "A " +str(round(A,1)), (cX, (cY+45)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
				cv2.putText(frame, "R " +str(round(R,1)), (cX, (cY+65)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
				cv2.drawContours(frame, cnts ,0, (25,25,255), 3)


	# show the frame to our screen
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()