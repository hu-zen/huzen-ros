#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from beginner_tutorials.srv import *

# Fungsi untuk memanggil service yang menghitung luas segitiga
def calculate_area_client(x, y):
    rospy.wait_for_service('calculate_area')
    try:
        calculate_area = rospy.ServiceProxy('calculate_area', AddTwoInts)
        resp1 = calculate_area(x, y)
        return resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

# Fungsi untuk menunjukkan cara penggunaan
def usage():
    return "%s [alas tinggi]" % sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        alas = int(sys.argv[1])
        tinggi = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    
    print("Requesting area with base %s and height %s" % (alas, tinggi))
    print("Area of triangle with base %s and height %s = %s" % (alas, tinggi, calculate_area_client(alas, tinggi)))
