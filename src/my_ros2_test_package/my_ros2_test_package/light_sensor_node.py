import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from random import uniform


class LightSensorNode(Node):
    def __init__(self):
        super().__init__('light_sensor')
        self.publisher_ = self.create_publisher(Float64, 'light', 10)
        self.timer_period = 1.0 #seconds
        self.timer = self.create_timer(self.timer_period,self.publish_light_level)
    
    def publish_light_level(self):
        light_level = uniform(100.0, 1000.0)
        msg = Float64()
        msg.data = light_level
        self.publisher_.publish(msg)
        self.get_logger().info('Light level is %s' % msg.data)

def main(args = None):
    rclpy.init(args = args)
    light_sensor_node = LightSensorNode()
    rclpy.spin(light_sensor_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
