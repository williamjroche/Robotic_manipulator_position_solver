import numpy as np
from sympy import Symbol, cos as c, sin as s, pi

theta1 = Symbol('1')
theta2 = Symbol('2')
theta3 = Symbol('3')
theta4 = Symbol('4')
L1 = Symbol('L1')
L2 = Symbol('L2')

phi = 180

#note (L1^2) >= (x^2) + (y^2)
x = int(input("Enter the X coordinate: "))
y = int(input("Enter the Y coordinate: "))
z = int(input("Enter the Z coordinate: "))
l1 = int(input("Enter L1: "))
l2 = int(input("Enter L2: "))


def transform_matrix(alpha, a, d, theta):
    T = np.array([[c(theta), -s(theta), 0, a],
                 [s(theta)*c(alpha), c(theta)*c(alpha), -s(alpha), -s(alpha)*d], 
                 [s(theta)*s(alpha), c(theta)*s(alpha), c(alpha), c(alpha)*d],
                 [0, 0, 0, 1]])
    return T

#Link parameters / DH table
dh = np.array([[0, 0, 0, theta1], [-pi/2, 0, 0, theta2], [0, L1, 0, theta3], [0, L2, 0, theta4]])

#needed transform matrices
T0_1 = transform_matrix(dh[0][0], dh[0][1], dh[0][2], dh[0][3])
T1_2 = transform_matrix(dh[1][0], dh[1][1], dh[1][2], dh[1][3])
T2_3 = transform_matrix(dh[2][0], dh[2][1], dh[2][2], dh[2][3])
T3_4 = transform_matrix(dh[3][0], dh[3][1], dh[3][2], dh[3][3])
T0_2 = np.matmul(T0_1, T1_2)
T0_3 = np.matmul(T0_2, T2_3)

#Transform matrix from base to end effector
T0_4 = np.matmul(T0_3, T3_4)

#Find theta 1,2,3 based on IK


