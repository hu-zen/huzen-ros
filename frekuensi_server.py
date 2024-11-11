# File: frekuensi_server.py
#!/usr/bin/env python

from _future_ import print_function
from beginner_tutorials.srv import FrekuensiCalc, FrekuensiCalcResponse
import rospy

def handle_hitung_frekuensi(req):
    # Menghitung frekuensi (f = 1/T)
    if req.period == 0:
        rospy.logwarn("Periode tidak boleh nol!")
        return FrekuensiCalcResponse(0.0)
    
    frekuensi = 1.0 / req.period
    print(f"Menghitung frekuensi untuk periode {req.period} detik = {frekuensi} Hz")
    return FrekuensiCalcResponse(frekuensi)

def frekuensi_server():
    rospy.init_node('frekuensi_server')
    s = rospy.Service('hitung_frekuensi', FrekuensiCalc, handle_hitung_frekuensi)
    print("Server siap menghitung frekuensi.")
    rospy.spin()

if _name_ == "_main_":
    frekuensi_server()
