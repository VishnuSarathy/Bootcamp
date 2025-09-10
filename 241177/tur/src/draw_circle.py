#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.srv import TeleportAbsolute
from geometry_msgs.msg import Twist
from tur.srv import DrawCircle
import math


class DrawCircleService(Node):
    def __init__(self):
        super().__init__('draw_circle_service')
        self.srv = self.create_service(DrawCircle, 'draw_circle', self.draw_circle_callback)
        self.cmd_vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = None
        self.end_time = None
        self.twist = Twist()

    def draw_circle_callback(self, request, response):
        try:
            client = self.create_client(TeleportAbsolute, '/turtle1/teleport_absolute')
            while not client.wait_for_service(timeout_sec=1.0):
                self.get_logger().info('Waiting for teleport')

            teleport_req = TeleportAbsolute.Request()
            teleport_req.x = request.x
            teleport_req.y = request.y
            teleport_req.theta = 0.0

            future = client.call_async(teleport_req)
            future.add_done_callback(lambda f: self.start_circle(request.radius))

            response.success = True
        except Exception as e:
            self.get_logger().error(f"Service failed ")
            response.success = False

        return response

    def start_circle(self, radius):
        self.twist = Twist()
        self.twist.linear.x = 2.0                 
        self.twist.angular.z = self.twist.linear.x / radius  

        duration = 2 * math.pi / self.twist.angular.z
        self.end_time = self.get_clock().now().nanoseconds / 1e9 + duration
        self.timer = self.create_timer(0.05, self.publish_twist)

    def publish_twist(self):
        now = self.get_clock().now().nanoseconds / 1e9
        if now < self.end_time:
            self.cmd_vel_pub.publish(self.twist)
        else:
            self.cmd_vel_pub.publish(Twist())
            if self.timer:
                self.timer.cancel()
                self.timer = None


def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleService()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
