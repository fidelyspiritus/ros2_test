import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16, String


class SwitchLightNode(Node):
    def __init__(self):
        super().__init__('switch_light')
        self.light_level_subscription = self.create_subscription(
            Int16,
            'lightness',
            self.light_level_callback,
            10)
        self.publisher_ = self.create_publisher(String, 'switch_light', 10)
        self.light_threshold = 500.0  # Уровень освещенности для включения света

    def publish_light_switch_status(self):
        if self.light_level is not None:
            if self.light_level > self.light_threshold:
                status = "Turn off the light, it's bright enough!"
            else:
                status = "Turn on the light, it's too dark outside!"
            msg = String()
            msg.data = status
            self.publisher_.publish(msg)
            self.get_logger().info(status)

    
    def light_level_callback(self, msg):
        self.light_level = msg.data
        self.publish_light_switch_status()

def main(args = None):
    rclpy.init(args = args)
    switch_light_node = SwitchLightNode()
    rclpy.spin(switch_light_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
