import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
import geometry_msgs.msg import Twist

class TurtleController(Node):

    def __init__(self):
        super().__init__('turtle_controller')
        self.cmd_vel_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose_subscriber_ = self.create_subscription(
            Pose, '/turtle1/pose', self.pose_callback, 10)
        self.get_logger().info('Turtle Controller Node has been started')

    def pose_callback(self, msg: Pose):
        cmd = Twist()
        if msg.x > 9.0 or msg.x < 2.0 or msg.y > 9.0 or msg.y < 2.0:
            cmd.linear.x = 1.0
            cmd.angular.z = 0.9 # 0.7-0.9 Prevents the turtle from getting stuck in a loop
        else:
            cmd.linear.x = 5.0
            cmd.angular.z = 0.0
        self.cmd_vel_pub.publish(cmd)

def main(args=None):
    rclpy.init(args=args)
    turtle_ctrller = TurtleController()
    rclpy.spin(turtle_ctrller)
    rclpy.shutdown()
