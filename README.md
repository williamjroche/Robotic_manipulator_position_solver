# Robotic Manipulator Position Algorithm
Program that solves for the angles needed to move a robotic manipulator to a certain position. Uses forward kinematics and inverse kinematics based on a 3 DOF robot. Forward Kinematics is computed using Denavit Hartenberg method of finding link parameters. Inverse Kinematics is computed uing the algebraic method.

Algorithm breakdown:
- test algorithm will be with 3 DOF robot
- input Link parameters and final position manipulator needs to be at
- get DH table
- solve for T0_3 or transform matrix from 0 to 3
- use T0_3 to solve fr IK algebraicly
- solve for IK by first finding X, Y, Z equations
- square and add method first to find Theta_2
- solve for theta 1 by dividing Y equation by X equation
- phi = theta1 + theta2 + theta3. Use this to solve for theta3

*This is a work in progress*
