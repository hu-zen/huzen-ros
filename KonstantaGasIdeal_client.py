#!/usr/bin/env python
from __future__ import print_function
import sys
import rospy
from beginner_tutorials.srv import CalculateR

def calculate_R_client(P, V, n, T):
    rospy.wait_for_service('calculate_R')
    try:
        calculate_R = rospy.ServiceProxy('calculate_R', CalculateR)
        response = calculate_R(P, V, n, T)
        return response.R
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def usage():
    return "%s [P V n T]" % sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 5:
        P = float(sys.argv[1])
        V = float(sys.argv[2])
        n = float(sys.argv[3])
        T = float(sys.argv[4])
    else:
        print(usage())
        sys.exit(1)

    print("Requesting R for P=%s, V=%s, n=%s, T=%s" % (P, V, n, T))
    result = calculate_R_client(P, V, n, T)
    print("Calculated R = %.2f" % result)
