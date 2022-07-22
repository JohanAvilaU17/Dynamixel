#!/usr/bin/python3

import sys

import rospy
from ingeniero.msg import MiMsg


class LeerMiMsg:

    def __init__(self):
        self.sub = rospy.Subscriber(
            "/ingeniero/miMgs",
            MiMsg,
            self.pringMgs,
            queue_size=100)

    def pringMgs(self, ros_MiMgs):
        print("pringMgs")
        print(ros_MiMgs.header.stamp)
        print(ros_MiMgs.data)
        print("")


if __name__ == '__main__':
    rospy.init_node('leer_Mi_Msg')
    leer_Mi_Msg = LeerMiMsg()

    rospy.loginfo("\033[1;32m-> leer_Mi_Msg.\033[0m")
    rospy.loginfo("control + C para salir")
    rospy.spin()
