# Robotic Manipulator Position Solver
Program that solves for the angles needed to move a robotic manipulator to a certain position. Uses forward kinematics and inverse kinematics based on a 3 DOF robot. Forward Kinematics is computed using Denavit Hartenberg method of finding link parameters. Inverse Kinematics (IK) is computed using the Levemberg-Marquadt Numerical method. This is a project I am doing to be used in a robotics projects as the main method for finding motor angle values for a given position.

Algebraic solver breakdown:

- input Link parameters and final position manipulator needs to be at
- get DH table
- solve for T0_3 or transform matrix from 0 to 3
- use T0_3 to solve for IK algebraically
- solve for IK by first finding X, Y, Z equations
- square and add method first to find Theta_2
- solve for theta 1 by dividing Y equation by X equation
- phi = theta1 + theta2 + theta3. Use this to solve for theta3
- write joint angles to motors

Numerical solver breakdown:

Note: This program is written in a jupyter notebook which ran in a miniconda environment for the roboticstoolbox library
- This is a much more simple approach because the roboticstoolbox library computes the math for us
- set up DH table for robot
- use roboticstoolbox to compute forward kinematics
- use Levemberg-Marquadt Numerical solving method to find IK
- joint angle speed control
- write joint angles to motors

*This is a work in progress*
