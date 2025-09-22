#!/usr/bin/env python3 
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from math import sqrt




class SpiralSubscriberNode(Node):
    def __init__(self):
        super().__init__("spiral_subscriber")
        self.pose_subscriber = self.create_subscription(
            Pose,"/turtle1/pose", self.pose_callback, 10)
        self.center_pos = 5.54444 
        
        
        


    def pose_callback(self, msg: Pose):
        a = abs(msg.x - self.center_pos)
        b = abs(msg.y - self.center_pos)
        dist_from_center = sqrt(a**2 + b**2)

        self.get_logger().info(
            #11.08 - 0
            "\nLatitude: " + str(msg.x) + "\nLongitude: " + str(msg.y) +
            "\nSpeed: " + str(msg.linear_velocity) + "\nRotation Speed: " + str(msg.angular_velocity) +
            "\nDistance from center " + str(dist_from_center) + "\n"
            )


def main(args=None):
    rclpy.init(args=args)

    node = SpiralSubscriberNode()
    rclpy.spin(node)


    rclpy.shutdown()