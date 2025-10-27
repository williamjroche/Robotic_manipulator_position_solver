# Robotic Manipulator Position Solver
Program that solves for the angles needed to move a robotic manipulator to a certain position. Uses forward kinematics and inverse kinematics based on a 3 DOF robot. Forward Kinematics is computed using Denavit Hartenberg method of finding link parameters. Inverse Kinematics (IK) is computed uing the analytical method. This is a project I am doing to hopefully use in future robotics projects as the main method for finding motor angle values for a given position.

Algebraic solver breakdown:
- test algorithm will be with 3 DOF robot
- input Link parameters and final position manipulator needs to be at
- get DH table
- solve for T0_3 or transform matrix from 0 to 3
- use T0_3 to solve for IK algebraically
- solve for IK by first finding X, Y, Z equations
- square and add method first to find Theta_2
- solve for theta 1 by dividing Y equation by X equation
- phi = theta1 + theta2 + theta3. Use this to solve for theta3

Numerical solver breakdown:
- coming soon

*This is a work in progress*
Note: This current program uses analytical IK which need to be re-calculated for each robot and cannot be used for all robots. A new program is being developed using numerical IK which can be used for any robot.
