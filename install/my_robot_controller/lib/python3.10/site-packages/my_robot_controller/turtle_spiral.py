#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleSpiralNode(Node):
    def __init__(self):
        super().__init__("turtle_spiral")
        self.cmd_vel_pub = self.create_publisher(Twist,"/turtle1/cmd_vel", 10)
        self.timer = self.create_timer(0.5,self.send_velocity_command)
        self.get_logger().info("Turtle Spiral started")

        self.theta = 0.5

    def send_velocity_command(self):
        msg = Twist()

        self.theta -= 0.1 # Rate of Radius change

        msg.linear.x = self.theta
        msg.angular.z = 2.0

        self.cmd_vel_pub.publish(msg)


def main(args= None):
    rclpy.init(args=args)
    node = TurtleSpiralNode()
    rclpy.spin(node)
    rclpy.shutdown
