# [Blue Ball Tracking Robot Project Fall 2021]

Project Name: [provide catkin_ws name here].  
*For example, `followbot`, `wanderbot`, and `redball` are project names we've used in class.  When I install your code, I want to know where I'll find it in `~/catkin_ws/src/balltracker`*

Team:
- [Josh Hulburt, jthulbur@buffalo.edu]

---

## Project Description

The Following instructions describe how to implement code, that can:
- Help you reference your webcam
- Track a blue ball in your webcam video stream
- 

### Contributions

The interesting thing about this project is the challenge of making a robust object tracker and then applying it towards the goal of navigation.
There are exsisting Ball targeting object trackers that exsist out there but they are typically the intro example into object tracking code and work on a simply tracking an object of a single color across a screen. My task is a bit simpler because I know the size shape and color of my object of interest but completing this project well will let me practice basic concepts of more complex machine learing and object tracking

---

## Installation Instructions

*In this section you should provide instructions for someone else to install all of the code necessary to execute your project.
Your target audience should be a student from the Fall 2020 class.
You may assume that the student has ROS Indigo installed on Ubuntu 14.04.*

List of Prerequisite Software:
- ROS Noetic (rospy, cv bridge)
- Imutils
- python3-numpy
- python3-math
- Open CV CV2

---

## Installation instructions

Assuming ROS Noetic and Gazebo is already installed on your machine 

```
sudo apt-get install python3-dev
sudo pip install --upgrade numpy
sudo pip install --upgrade imutils 
sudo pip install opencv-contrib-python
```

install my ball tracker library instructions add `catkin_w/src/balltracker`

1. Create the Package:
```
cd ~/catkin_ws/src
catkin_create_pkg ballttracker rospy geometry_msgs sensor_msgs

```
2. Make the `scripts` directory
```
cd ~/catkin_ws/src/balltracker
mkdir scripts

```
3. Get the source code from the course github site:
```
cd ~/Downloads
rm -rf BallTracker
git clone https://github.com/jhulburt/Ball_Tracker.git

```

4. Copy the Python scripts to our teleopbot workspace
```
cd BallTracker/code/
cp scripts/* ~/catkin_ws/src/balltracker/scripts/

```

5. Make our Python scripts executable
```
cd ~/catkin_ws/src/teleopbot/scripts
chmod +x *.py

```

6. Compile/make our package
```
cd ~/catkin_ws
catkin_make
```

---

## Running the Code

1) Open 3 terminal windows

2) ```rosrun balltracker bueball.launch```
3) ```rosrun balltracker ball_follow.py```
4) ```rosrun balltracker ball_move.py```

A window with the roots view should open and the robot should follow the ball in the simulation.

---

## Measures of Success

*You have already defined these measures of success (MoS) in your proposal, and updated them after your progress report.  The purpose of this section is to highlight how well you did.  Also, these MoS will be useful in assigning partial credit.*

*The MoS summary should be in table form.  A sample is provided below:*
<TABLE>
<TR>
	<TH>Measure of Success (from your PROPOSAL)</TH>
	<TH>Status (completion percentage)</TH>
</TR>
<TR>
	<TD> Find a blue ball in an image </TD>
	<TD>100%</TD>
</TR>
<TR>
	<TD> Differentiate a blue ball from reasonably similar objects </TD>
	<TD>100%</TD>
</TR>
<TR>
	<TD> Simulate the Environment in Gazebo</TD>
	<TD>100%</TD>
</TR>
<TR>
	<TD> Follow the blue ball in the an environment </TD>
	<TD>100%</TD>
</TR>
<TR>
	<TD> Implement gazebo code to a actual robot? </TD>
	<TD>100%</TD>
</TR>
<TR>
	<TD> Implement the tracker on a real camera </TD>
	<TD>100%</TD>	
</TR>
</TABLE>

### Reach Goals

<TABLE>
<TR>
	<TH>Reach Goals</TH>
	<TH>Status (completion percentage)</TH>
</TR>
<TR>
	<TD> Implement the Code on a physical robot </TD>
	<TD>15% ? </TD>
</TR>
<TR>
	<TD> Use generic motion detector  </TD>
	<TD>0%</TD>
</TR>
</TABLE>

My set goals are 100% completed

---

## What did you learn from this project?

A good amount, on top of practicing skills that we had learned throughout the class, I learned alot. For example how world files are structured and how different types of objects ore treated in gazebo. How to interface with my computer hardware and find it from the command line. I got alot of troupble shooting practice on reading errors and correcting them as best I could. I learned about DHCP and how to manually configure a how a device connects to a network and more practices on how to discover problem areas.

---

## Future Work

Potentially build the blueball tracking script to adjust for different lighting conditions glare, darkness etc

Bring in a new Object Detection script to detect a "moving object" or some other pattern recognition software in a video frame captured from a camera on a moving robot. I could use a simple approach that only detects moving objects whle stationary or while moving very slowly. Since Tracking Moving objects in a moving video frame is quite difficult and very much a subject of research within computer vision my goal would be to differentiate the perspective motion of the background against the actual motion of an object in the image. That would mean interpolating the environment's structure and then and how it should move and subtracting it from how it is moving. This would be no small task and I would need more than one camera to accomplish that.

Lastly, I would like to be able to overcome internet issues and get the robot to work.

---

## References/Resources

*What resources did you use to help finish this project?*
- https://www.pyimagesearch.com/
- 



