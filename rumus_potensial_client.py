#!/usr/bin/env python

from __future__ import print_function
import sys
import rospy
from beginner_tutorials.srv import *

def rumus_potensial_client(x, y, z):
    # Menunggu hingga layanan 'rumus_potensial' tersedia
    rospy.wait_for_service('rumus_potensial')
    try:
        # Membuat proxy untuk layanan 'rumus_potensial'
        rumus_potensial = rospy.ServiceProxy('rumus_potensial', MultiplyThreeInts)
        # Memanggil layanan dengan tiga argumen (x, y, z)
        resp1 = rumus_potensial(x, y, z)
        return resp1.product
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def usage():
    return "%s [x y z]" % sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        # Mengambil tiga argumen dari command line
        x = int(sys.argv[1])
        y = int(sys.argv[2])
        z = int(sys.argv[3])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s * %s * %s" % (x, y, z))
    print("%s * %s * %s = %s" % (x, y, z, rumus_potensial_client(x, y, z)))
