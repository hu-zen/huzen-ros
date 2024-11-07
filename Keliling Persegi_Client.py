#!/usr/bin/env python

from __future__ import print_function 

import sys
import rospy
from beginner_tutorials.srv import MultiplyTwoInts *

def KelilingPersegi_client(a, b): 
    rospy.wait_for_service('KelilingPersegi') 
    try:
        multiply_two_ints = rospy.ServiceProxy('KelilingPersegi',   MultiplyTwoInts)
        resp1 = multiply_two_ints(a, b) 
        return resp1.product
    except rospy.ServiceException as e: 
        print("Service call failed: %s" % e)

def usage():
    return "%s [a b]" % sys.argv[0]

if __name__ == "__main__": 
    if len(sys.argv) == 3:
        a = int(sys.argv[1])
        b = int(sys.argv[2]) 
    else:
        print(usage()) 
        sys.exit(1)
print("Requesting 4 * %s" % (a, b))
print("4 * %s = %s" % (a, b, KelilingPersegi_client(a, b))) 
