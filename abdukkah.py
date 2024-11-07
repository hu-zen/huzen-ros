#!/usr/bin/env python

from__future	 import print_function

from beginner_tutorials.srv import MultiplyTwoInts, MultiplyTwoIntsResponse 
import rospy

def handle_KelilingPersegi(req):
print("Returning [4 * %s = %s]" % (req.b, (req.a * req.b)))
return MultiplyTwoIntsResponse(req.a * req.b)


def KelilingPersegi_server(): rospy.init_node('KelilingPersegi_server')
s = rospy.Service('KelilingPersegi', MultiplyTwoInts,    handle_KelilingPersegi)
print("Ready to calculate Keliling Persegi.") 
rospy.spin()

if 		name	 == "	main	": KelilingPersegi_server()
