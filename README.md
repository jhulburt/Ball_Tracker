This document (`README_template.md`) provides a template for your **final** documentation (**NOT YOUR PROPOSAL**).

- Your final document should be named simply `README.md`.  
- I've left several comments below.  These should obviously be removed from your document.
- You may add additional sections as you see fit, but you should not **remove** any of the sections defined below.
- Any supplementary images should go in a directory called `Images`.  See [README.md](README.md) for more information about the required directory structure.
- Please keep in mind that the audience for this document should be students in the Fall 2022 section of this class.  (In other words, write this such that 3-month-younger you would've been able to utilize this document.)

---

# [Blue Ball Tracking Robot Project Fall 2021]

Project Name: [provide catkin_ws name here].  
*For example, `followbot`, `wanderbot`, and `redball` are project names we've used in class.  When I install your code, I want to know where I'll find it in `~/catkin_ws/src/balltracker`*

Team:
- [Josh Hulburt, jthulbur@buffalo.edu]

---

## Project Description

*In this section, describe what your project does. This should be descriptive.  Someone from next year's class should be able to fully understand the aims and scope of your project. I highly recommend using pictures to help explain things.  Maybe even post a YouTube video showing your code in action.*

*NOTE:  This is not a proposal.  This is a final report describing your actual completed project.*



### Contributions

The interesting thing about this roject is the challenge of making a robust object tracker and then applying it towards the goal of navigation.
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


*The expectation is that the user should only have to follow these steps one time.  For example, if your project requires generating Gazebo mazes, the task of INSTALLING the maze generation code should go in this section.*

---

## Installation instructions

Assuming ROS Noetic and Gazebo is already installed on your machine 

```
sudo apt-get install python3-dev
pip install --upgrade numpy
pip install --upgrade imutils 
sudo pip install opencv-contrib-python

```

install my ball tracker library instructions add `catkin_w/src/balltracker`

---

## Running the Code

*Provide detailed step-by-step instructions to run your code.*

*NOTE 1:  At this point, the user should have already installed the necessary code.  This section should simply describe the steps for RUNNING your project.*  

*NOTE 2:  If you're generating mazes, for example, the task of GENERATING a new maze would go here.*

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
</TABLE>

*NOTE 1:  I have your proposals...don't move the goal posts!*

*NOTE 2:  For activities less than 100% complete, you should differentiate between what you completed and what you were unable to complete. I suggest you add details in a bullet list below.* 


---

## What did you learn from this project?

What I learned form this project is 

---

## Future Work

Potentially build the blueball tracking script to adjust for different lighting conditions glare, darkness etc

Bring in a new Object Detection script to detect a "moving object" or some other pattern recognition software in a video frame captured from a camera on a moving robot.

---

## References/Resources

*What resources did you use to help finish this project?*
- https://www.pyimagesearch.com/
- 



