#!/usr/bin/env python
from __future__ import print_function
import rospy
from gravitasi.srv import CalculateGravitationalForce, CalculateGravitationalForceResponse

# Konstanta gravitasi (m^3 kg^-1 s^-2)
G = 6.67430e-11

def handle_calculate_gravitational_force(req):
    force = G * (req.mass1 * req.mass2) / (req.distance ** 2)
    print("Calculating gravitational force with mass1=%s, mass2=%s, distance=%s. Result: %s" % (req.mass1, req.mass2, req.distance, force))
    return CalculateGravitationalForceResponse(force)

def gravitational_force_server():
    rospy.init_node('gravitational_force_server')
    s = rospy.Service('calculate_gravitational_force', CalculateGravitationalForce, handle_calculate_gravitational_force)
    print("Ready to calculate gravitational force.")
    rospy.spin()

if __name__ == "__main__":
    gravitational_force_server()
