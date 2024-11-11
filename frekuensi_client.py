# File: frekuensi_client.py
#!/usr/bin/env python

from _future_ import print_function
import sys
import rospy
from beginner_tutorials.srv import FrekuensiCalc

def frekuensi_client(period):
    rospy.wait_for_service('hitung_frekuensi')
    try:
        hitung_frekuensi = rospy.ServiceProxy('hitung_frekuensi', FrekuensiCalc)
        resp = hitung_frekuensi(period)
        return resp.frequency
    except rospy.ServiceException as e:
        print(f"Service call failed: {e}")

def usage():
    return f"{sys.argv[0]} [periode_dalam_detik]"

if _name_ == "_main_":
    if len(sys.argv) == 2:
        period = float(sys.argv[1])
    else:
        print(usage())
        sys.exit(1)
    
    print(f"Menghitung frekuensi untuk periode {period} detik")
    frekuensi = frekuensi_client(period)
    print(f"Periode = {period} detik")
    print(f"Frekuensi = {frekuensi} Hz")

# File: CMakeLists.txt (tambahkan baris berikut)
add_service_files(
  FILES
  FrekuensiCalc.srv
)

catkin_install_python(PROGRAMS
  scripts/frekuensi_server.py
  scripts/frekuensi_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
