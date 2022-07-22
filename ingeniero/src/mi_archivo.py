#!/usr/bin/python3

import sys

import rospy
from ingeniero.msg import MiMsg


class MiArchivo:

    def __init__(self):
        self.pub = rospy.Publisher(
            "/ingeniero/miMgs",
            MiMsg)

    def printArgumento(self):
        print("argumentos")
        print(sys.argv)
        print("")

    def publicarMgs(self):
        print("publicarMgs")
        mi_mgs = MiMsg()
        mi_mgs.header.stamp = rospy.Time.now()
        mi_mgs.data = str(sys.argv) 
        print(mi_mgs.header.stamp)
        print(mi_mgs.data)
        print("")
        self.pub.publish(mi_mgs)


if __name__ == '__main__':
    rospy.init_node('mi_Archivo')
    mi_archivo = MiArchivo()
    mi_archivo.printArgumento()

    rospy.loginfo("\033[1;32m-> MiArchivo.\033[0m")
    rospy.loginfo("control + C para salir")
    while not rospy.is_shutdown():
        mi_archivo.publicarMgs()
