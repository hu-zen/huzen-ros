#!/usr/bin/env python
from __future__ import print_function
import rospy
from beginner_tutorials.srv import CalculateTrapezoidArea, CalculateTrapezoidAreaResponse

def handle_calculate_trapezoid_area(req):
    area = (req.a + req.b) * req.h / 2
    print("Calculating area with a=%s, b=%s, h=%s. Result: %s" % (req.a, req.b, req.h, area))
    return CalculateTrapezoidAreaResponse(area)

def trapezoid_area_server():
    rospy.init_node('trapezoid_area_server')
    s = rospy.Service('calculate_trapezoid_area', CalculateTrapezoidArea, handle_calculate_trapezoid_area)
    print("Ready to calculate trapezoid area.")
    rospy.spin()

if __name__ == "__main__":
    trapezoid_area_server()
