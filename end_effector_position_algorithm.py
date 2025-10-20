import numpy as np
from sympy import Symbol, cos as c, sin as s, pi

theta1 = Symbol('theta1')
theta2 = Symbol('theta2')
theta3 = Symbol('theta3')
L1 = Symbol('L1')

phi = 180

#note (L1^2) >= (x^2) + (y^2)
x = int(input("Enter the X coordinate: "))
y = int(input("Enter the Y coordinate: "))
l1 = int(input("Enter L1: "))

def transform_matrix(alpha, a, d, theta):
    T = np.array([[c(theta), -s(theta), 0, a],
                 [s(theta)*c(alpha), c(theta)*c(alpha), -s(alpha), -s(alpha)*d], 
                 [s(theta)*s(alpha), c(theta)*s(alpha), c(alpha), c(alpha)*d],
                 [0, 0, 0, 1]])
    return T

#Link parameters / DH table
dh = np.array([[0, 0, 0, theta1], [-pi/2, 0, 0, theta2], [0, L1, 0, theta3]])

#needed transform matrices
T0_1 = transform_matrix(dh[0][0], dh[0][1], dh[0][2], dh[0][3])

T1_2 = transform_matrix(dh[1][0], dh[1][1], dh[1][2], dh[1][3])

T2_3 = transform_matrix(dh[2][0], dh[2][1], dh[2][2], dh[2][3])

T0_2 = np.matmul(T0_1, T1_2)

#Transform matrix from base to end effector
T0_3 = np.matmul(T0_2, T2_3)

#Find theta 1,2,3 based on solved IK equations
Theta2 = np.degrees(np.arctan(np.sqrt(((np.square(l1))/(np.square(x) + np.square(y)))-1)))

Theta1 = np.degrees(np.arctan(y/x))

Theta3 = phi-Theta1-Theta2

print("Theta 1 is ", Theta1, " degrees")
print("Theta 2 is ", Theta2, " degrees")
print("Theta 3 is ", Theta3, " degrees")
