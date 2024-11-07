#!/usr/bin/env python

from __future__ import print_function
from beginner_tutorials.srv import MultiplyThreeInts, MultiplyThreeIntsResponse
import rospy

def handle_rumus_potensial(req):
    # Mengalikan tiga angka yang diterima dari client
    print("Returning [%s * %s * %s = %s]" % (req.x, req.y, req.z, (req.x * req.y * req.z)))
    return MultiplyThreeIntsResponse(req.x * req.y * req.z)

def rumus_potensial_server():
    # Inisialisasi node ROS dan buat layanan 'rumus_potensial'
    rospy.init_node('rumus_potensial_server')
    s = rospy.Service('rumus_potensial', MultiplyThreeInts, handle_rumus_potensial)
    print("Ready to calculate the potential formula (multiplication of three ints).")
    rospy.spin()

if __name__ == "__main__":
    rumus_potensial_server()
