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
        self.temperature_subscription   #to prevent unused variable warning
        self.light_subscription
        self.switch_light_subscription

    def temperature_callback(self, msg):
        self.get_logger().info('Temperatures: "%s" Celsius' % msg.data)
    
    def light_callback(self, msg):
        self.get_logger().info('Light level: "%s" Lux' % msg.data)
    
    def switch_callback(self,msg):
        self.get_logger().info(msg.data)  
def main(args = None):
    rclpy.init(args = args)
    display_node = DisplayNode()
    rclpy.spin(display_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
