#!/usr/bin/env python

from __future__ import print_function
import sys
import rospy
from beginner_tutorials.srv import *

def multiply_three_ints_client(x, y, z):
    rospy.wait_for_service('multiply_three_ints')
    try:
        multiply_three_ints = rospy.ServiceProxy('multiply_three_ints', MultiplyThreeInts)
        resp1 = multiply_three_ints(x, y, z)
        return resp1.product
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def usage():
    return "%s [x y z]" % sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z = int(sys.argv[3])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s * %s * %s" % (x, y, z))
    print("%s * %s * %s = %s" % (x, y, z, multiply_three_ints_client(x, y, z)))
