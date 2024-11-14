#!/usr/bin/env python
from __future__ import print_function
import sys
import rospy
from beginner_tutorials.srv import CalculateGravitationalForce

def calculate_gravitational_force_client(mass1, mass2, distance):
    rospy.wait_for_service('calculate_gravitational_force')
    try:
        calculate_gravitational_force = rospy.ServiceProxy('calculate_gravitational_force', CalculateGravitationalForce)
        response = calculate_gravitational_force(mass1, mass2, distance)
        return response.force
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

def usage():
    return "%s [mass1 mass2 distance]" % sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        mass1 = float(sys.argv[1])
        mass2 = float(sys.argv[2])
        distance = float(sys.argv[3])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting gravitational force with mass1=%s, mass2=%s, distance=%s" % (mass1, mass2, distance))
    print("Gravitational force: %s N" % calculate_gravitational_force_client(mass1, mass2, distance))
