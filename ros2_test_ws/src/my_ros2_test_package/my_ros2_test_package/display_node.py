import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, String, Int16

class DisplayNode(Node):
    def __init__(self):
        super().__init__('display_node')
        self.temperature_subscription = self.create_subscription(
            Float64, 
            'temperature', 
            self.temperature_callback, 
            10)
        self.light_subscription = self.create_subscription(
            Int16,
            'lightness',
            self.light_callback,
            10)
        self.switch_light_subscription = self.create_subscription(
            String,
            'switch_light',
            self.switch_callback,
            10)
        self.wind_speed_subscription = self.create_subscription(
            Int16,
            'wind_speed',
            self.wind_speed_callback,
            10)
        self.wind_direction_subscription = self.create_subscription(
            Int16,
            'wind_direction',
            self.wind_direction_callback,
            10)

    def temperature_callback(self, msg):
        self.get_logger().info('Temperatures: "%s" Celsius' % msg.data)
    
    def light_callback(self, msg):
        self.get_logger().info('Light level: "%s" Lux' % msg.data)
    
    def switch_callback(self,msg):
        self.get_logger().info(msg.data)  

    def wind_speed_callback(self, msg):
        self.get_logger().info(f'Wind speed: {msg.data} m/s')

    def wind_direction_callback(self, msg):
        self.get_logger().info(f'Wind direction: {msg.data} degrees')

def main(args = None):
    rclpy.init(args = args)
    display_node = DisplayNode()
    rclpy.spin(display_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
