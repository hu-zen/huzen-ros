#!/usr/bin/env python
from __future__ import print_function
import sys
import rospy
from beginner_tutorials.srv import CalculateTrapezoidArea

def calculate_trapezoid_area_client(a, b, h):
    rospy.wait_for_service('calculate_trapezoid_area')
    try:
        calculate_trapezoid_area = rospy.ServiceProxy('calculate_trapezoid_area', CalculateTrapezoidArea)
        response = calculate_trapezoid_area(a, b, h)
        return response.area
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def usage():
    return "%s [a b h]" % sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        a = float(sys.argv[1])
        b = float(sys.argv[2])
        h = float(sys.argv[3])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting area with a=%s, b=%s, h=%s" % (a, b, h))
    print("Area of trapezoid: %s" % calculate_trapezoid_area_client(a, b, h))
