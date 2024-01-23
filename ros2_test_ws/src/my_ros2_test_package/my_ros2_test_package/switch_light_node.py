import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64


class SwitchLightNode(Node):
    def __init__(self):
        super().__init__('switch_light') 
        self.light_level_subscription = self.create_subscription(
            Float64,
            'lightness',
            self.light_level_callback,
            10)
        self.light_level_subscription
        self.light_threshold = 500.0 # Уровень освещенности для включения света

    def light_level_callback(self, msg):
        if msg.data is not None:
            if msg.data > self.light_threshold:
                self.get_logger().info("Turn off the light, it's bright enough!")
            else:
                self.get_logger().info("Turn on the light, it's too dark outside!") 

def main(args = None):
    rclpy.init(args = args)
    switch_light_node = SwitchLightNode()
    rclpy.spin(switch_light_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
