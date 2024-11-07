#!/usr/bin/env python

from __future__ import print_function
from beginner_tutorials.srv import MultiplyThreeInts, MultiplyThreeIntsResponse
import rospy

def handle_multiply_three_ints(req):
    print("Returning [%s * %s * %s = %s]" % (req.x, req.y, req.z, (req.x * req.y * req.z)))
    return MultiplyThreeIntsResponse(req.x * req.y * req.z)

def multiply_three_ints_server():
    rospy.init_node('multiply_three_ints_server')
    s = rospy.Service('multiply_three_ints', MultiplyThreeInts, handle_multiply_three_ints)
    print("Ready to calculate the product of three integers.")
    rospy.spin()

if __name__ == "__main__":
    multiply_three_ints_server()
