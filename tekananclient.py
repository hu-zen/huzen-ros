#!/usr/bin/env python

from __future__ import print_function

from beginner_tutorials.srv import HitungTekanan, HitungTekananResponse
import rospy

def handle_hitung_tekanan(req):
    tekanan = req.gaya / req.luas
    print("Menghitung [Tekanan = %s / %s = %s]" % (req.gaya, req.luas, tekanan))
    return HitungTekananResponse(tekanan)

def server_hitung_tekanan():
    rospy.init_node('server_hitung_tekanan')
    s = rospy.Service('hitung_tekanan', HitungTekanan, handle_hitung_tekanan)
    print("Siap menghitung tekanan.")
    rospy.spin()

if __name__ == "__main__":
    server_hitung_tekanan()
