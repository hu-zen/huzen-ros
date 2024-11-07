#!/usr/bin/env python

from __future__ import print_function
import rospy
from beginner_tutorials.srv import AddTwoInts, AddTwoIntsResponse

# Fungsi untuk menghitung luas segitiga
def handle_calculate_area(req):
    alas = req.a
    tinggi = req.b
    luas = 0.5 * alas * tinggi
    print("Returning area of triangle with base %s and height %s = %s" % (alas, tinggi, luas))
    return AddTwoIntsResponse(luas)

# Server untuk menghitung luas segitiga
def calculate_area_server():
    rospy.init_node('calculate_area_server')
    s = rospy.Service('calculate_area', AddTwoInts, handle_calculate_area)
    print("Ready to calculate area of a triangle.")
    rospy.spin()

if __name__ == "__main__":
    calculate_area_server()
