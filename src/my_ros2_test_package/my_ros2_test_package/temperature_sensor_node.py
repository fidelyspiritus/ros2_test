import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from random import uniform
import time

class TemperatureSensorNode(Node):
    def __init__(self):
        super().__init__('temperature_sensor')
        self.publisher_ = self.create_publisher(Float64, 'temperature', 10)
        self.timer_period = 1.0 #seconds
        self.timer = self.create_timer(self.timer_period, self.publish_temperature)

    def publish_temperature(self):
        temperature = uniform(15.0, 25.0)
        msg = Float64()
        msg.data = temperature
        self.publisher_.publish(msg)
        self.get_logger().info('Temperature: "%s"' % msg.data)

def main(args = None):
    rclpy.init(args = args)
    temperature_sensor_node = TemperatureSensorNode()
    rclpy.spin(temperature_sensor_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()