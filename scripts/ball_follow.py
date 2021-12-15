#!/usr/bin/env python3

# write a readme 
# submit two lane navigtion script
# submit a intersection

import rospy, cv2, cv_bridge, numpy, time, math, imutils
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

#global state
#global err

#				(90, 130, 40), (115, 255, 155) Bright environmemnts
#				(60, 30, 25), (135, 255, 195) dark environmemnts
colorRanges = [((60, 30, 25), (135, 255, 195), "ball")]


def Area_vs_Perimeter(contours):
	P = cv2.arcLength(contours,True)
	A = cv2.contourArea(contours)
	R1 = P / (2*3.14159265) 
	R2 = math.sqrt(A/3.14159265)
	return abs(R1-R2)


class Follower:
	def __init__(self):
		self.bridge = cv_bridge.CvBridge()
		#cv2.namedWindow("window", 1)
		self.image_sub = rospy.Subscriber('/camera/rgb/image_raw', 
										  Image, self.image_callback)
		self.cmd_vel_pub = rospy.Publisher('/cmd_vel',
										   Twist, queue_size=1)
		self.twist = Twist()


	def image_callback(self, msg):
		image = self.bridge.imgmsg_to_cv2(msg,desired_encoding='bgr8')
		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		
		h, w, d = image.shape

		# grab the current image

	
		# resize the image, blur it, and convert it to the HSV color space
		image = imutils.resize(image, width=840)
		blurred = cv2.GaussianBlur(image, (11, 11), 0)
		hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	
		# loop over the color ranges
		for (lower, upper, colorName) in colorRanges:
			# construct a mask for all colors in the current HSV range, then
			# perform a series of dilations and erosions to remove any small
			# blobs left in the mask
			mask = cv2.inRange(hsv, lower, upper)
			#cv2.imshow("mask", mask)
			mask = cv2.erode(mask, None, iterations=4)
			#cv2.imshow("Erode", mask)
			mask = cv2.dilate(mask, None, iterations=2)
			#cv2.imshow("Dilate", mask)
	
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
				R = ((P / (2*3.14159265)) + (math.sqrt(A/3.14159265)))/2 #Radius in pixel count caluculated by average
				err = cX - w/2

				# calculate estimated distance

				# Ball Radius = 1.5" = 0.0381m 
				# Percieved Focal distance from 7 measurements
					# avg 543.998
					# stdev 45
				P_Focal = 543.998 # percieved focal distance
				Ball_Radius  = 0.0381

				Dist = (Ball_Radius * P_Focal)/R  #calculated distance
				linear = Dist/2 - 0.3 #set the linear velocity
				

				# only draw the enclosing circle and text if the radious meets
				# a minimum size
	
				# Circular object filter
				# do the largest contours selected fit in a least radius circle plus or minus 10 pixels and a certain percentage of the circle
	
				# draw all contours on image
				cv2.drawContours(image, cnts ,0, (0,255,0), 3)
				if radius > 5 and Area_vs_Perimeter(c) < 15: #when ball
					#cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 255), 2)
					cv2.putText(image, "ball", (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 255), 2)
					cv2.putText(image, "Perimeter: " + str(round(P,1)), (5, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
					cv2.putText(image, "Area: " +str(round(A,1)),  (5, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
					cv2.putText(image, "Distance: " +str(round(Dist,2)),  (5,55), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
					cv2.drawContours(image, cnts ,0, (25,25,255), 3) 

			else:
				linear =  0
				angular = 0.25

		angular = -float(err) / w
		self.twist.linear.x = linear
		cv2.putText(image, "Linear V: " +str(round(linear,2)),  (5,75), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
		self.twist.angular.z = angular
		cv2.putText(image, "Angular V: " +str(round(angular,2)),  (5,92), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
		self.cmd_vel_pub.publish(self.twist)
		cv2.imshow("View", image)
		cv2.waitKey(3)


rospy.init_node('follower')
follower = Follower()
rospy.spin()


