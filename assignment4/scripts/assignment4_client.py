#!/usr/bin/env python3

from __future__ import print_function

import sys
import rospy
from assignment4.srv import *


def point_client(n):
    rospy.wait_for_service('read_point') #x1
    try:
        point = rospy.ServiceProxy('read_point', data_point) #x1 กับตรงนี้ต้องชื่อเดียวกันซึ่งเป็นชื่อเดียวกับตอนตั้ง server
        resp1 = point(n)
        return [resp1.x, resp1.y]
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)


def usage():
    return "%s [n]" % sys.argv[0]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting {}".format(n))
    x, y = point_client(n)
    print("return point is = {}, {}" .format(x,y))
