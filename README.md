# Robotic Manipulator Position Algorithm
Program that solves for the angles needed to move a robotic manipulator to a certain position. Uses forward kinematics and inverse kinematics based on a 3 DOF robot.

Algorithm breakdown:
- test algorithm will be with 3 DOF robot
- input Link parameters and final position manipulator needs to be at
- get DH table
- solve for T0_3 or transform matrix from 0 to 3
- use T0_3 to solve fr IK algebraicly
- solve for IK by first finding X, Y, Z equations
- square and add method first to find Theta_2
- find K1 and K2, find r and Y(gamma), change of variable for K1 = rcos(Y) and K2 = rsin(Y)
- sub into X and Y for K1 and K2, use cos(a+b) and sin(a+b) to simplify
- solve for theta 1
- phi = theta1 + theta2 + theta3. Use this to solve for theta3

