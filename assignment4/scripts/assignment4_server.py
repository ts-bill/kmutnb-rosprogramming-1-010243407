#!/usr/bin/env python3

from __future__ import print_function

from assignment4.srv import data_point,data_pointResponse
import rospy
import csv
import os 

def handle_point(req):
    global point
    if req.n <= len(point) - 1 and req.n > 0 :
        response = point[req.n] #req ที่เข้ามาจะเป็น type เดียวกับที่เราตั้งไว้ใน .srv
        print("Returning {}, {}".format(response[0],response[1]))
        return data_pointResponse(int(response[0]),int(response[1])) # type ต้องตรงกับที่ตั้งไว้ใน .srv
    else :
        print("This index is out of data , You should request between 0-{}".format(len(point)-1))
        return data_pointResponse(None,None)

def read_point_server():
    rospy.init_node('read_point_server')
    s = rospy.Service('read_point', data_point, handle_point) #ชื่อต้องตรงกับสิ่งที่ client ส่งมา
    print("Ready get the sequence of points")
    rospy.spin()

if __name__ == "__main__":
    point = list()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    #print(dir_path)
    with open(dir_path + '/data.csv','r') as csv_file:
         csv_reader = csv.reader(csv_file, delimiter=',')
         next(csv_reader,None)
         for row in csv_reader:
             _,x,y = row
             point.append((x,y))
    read_point_server()