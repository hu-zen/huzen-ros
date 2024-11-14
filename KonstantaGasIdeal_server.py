#!/usr/bin/env python

from __future__ import print_function
import rospy
from beginner_tutorials.srv import CalculateR, CalculateRResponse

def handle_calculate_R(req):
    # Calculate R using the equation: R = (P * V) / (n * T)
    R = (req.P * req.V) / (req.n * req.T)
    rospy.loginfo("Returning R = %.2f" % R)
    return CalculateRResponse(R)

def calculate_R_server():
    rospy.init_node('calculate_R_server')
    s = rospy.Service('calculate_R', CalculateR, handle_calculate_R)
    rospy.loginfo("Ready to calculate R.")
    rospy.spin()

if __name__ == "__main__":
    calculate_R_server()
