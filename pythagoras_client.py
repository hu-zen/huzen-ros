#!/usr/bin/env python

from _future_ import print_function
import sys
import rospy
from beginner_tutorials.srv import AddTwoInts

# Fungsi untuk memanggil service yang menghitung jarak antara dua titik
def calculate_distance_client(x1, y1, x2, y2):
    rospy.wait_for_service('calculate_distance')
    try:
        calculate_distance = rospy.ServiceProxy('calculate_distance', AddTwoInts)
        response = calculate_distance(x1, y1, x2, y2)
        return response.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

# Fungsi untuk menunjukkan cara penggunaan
def usage():
    return "%s [x1 y1 x2 y2]" % sys.argv[0]

if _name_ == "_main_":
    if len(sys.argv) == 5:
        x1 = int(sys.argv[1])
        y1 = int(sys.argv[2])
        x2 = int(sys.argv[3])
        y2 = int(sys.argv[4])
    else:
        print(usage())
        sys.exit(1)

    print("Requesting distance between (%s, %s) and (%s, %s)" % (x1, y1, x2, y2))
    print("Distance between (%s, %s) and (%s, %s) = %s" % (x1, y1, x2, y2, calculate_distance_client(x1, y1, x2, y2)))
