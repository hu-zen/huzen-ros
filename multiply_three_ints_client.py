#!/usr/bin/env python

from __future__ import print_function
import sys
import rospy
from beginner_tutorials.srv import MultiplyThreeInts

def multiply_three_ints_client(a, b, c):
    rospy.wait_for_service('multiply_three_ints')
    try:
        multiply_three_ints = rospy.ServiceProxy('multiply_three_ints', MultiplyThreeInts)
        resp1 = multiply_three_ints(a, b, c)
        return resp1.product
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def usage():
    return "%s [a b c]" % sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        c = int(sys.argv[3])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s * %s * %s" % (a, b, c))
    print("%s * %s * %s = %s" % (a, b, c, multiply_three_ints_client(a, b, c)))
