#!/usr/bin/env python

from _future_ import print_function
import rospy
from beginner_tutorials.srv import AddTwoInts, AddTwoIntsResponse
from math import sqrt

# Fungsi untuk menghitung jarak antara dua titik menggunakan rumus Pythagoras
def handle_calculate_distance(req):
    x1, y1 = req.a, req.b
    x2, y2 = req.c, req.d
    distance = sqrt((x2 - x1) * 2 + (y2 - y1) * 2)
    print("Returning distance between (%s, %s) and (%s, %s) = %s" % (x1, y1, x2, y2, distance))
    return AddTwoIntsResponse(distance)

# Server untuk menghitung jarak dua titik
def calculate_distance_server():
    rospy.init_node('calculate_distance_server')
    s = rospy.Service('calculate_distance', AddTwoInts, handle_calculate_distance)
    print("Ready to calculate distance between two points.")
    rospy.spin()

if _name_ == "_main_":
    calculate_distance_server()
