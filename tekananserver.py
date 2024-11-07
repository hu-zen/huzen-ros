#!/usr/bin/env python

from __future__ import print_function

import sys
import rospy
from beginner_tutorials.srv import *

def hitung_tekanan_client(gaya, luas):
    rospy.wait_for_service('hitung_tekanan')
    try:
        hitung_tekanan = rospy.ServiceProxy('hitung_tekanan', HitungTekanan)
        resp1 = hitung_tekanan(gaya, luas)
        return resp1.tekanan
    except rospy.ServiceException as e:
        print("Gagal memanggil layanan: %s" % e)

def penggunaan():
    return "%s [gaya luas]" % sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        gaya = float(sys.argv[1])
        luas = float(sys.argv[2])
    else:
        print(penggunaan())
        sys.exit(1)
    print("Menghitung tekanan dengan gaya %s dan luas %s" % (gaya, luas))
    print("Tekanan = %s" % (hitung_tekanan_client(gaya, luas)))
