import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, String


class SwitchLightNode(Node):
    def __init__(self):
        super().__init__('switch_light')
        self.light_level = None
        self.light_level_subscription = self.create_subscription(
            Float64,
            'lightness',
            self.light_level_callback,
            10)
        self.light_level_subscription
        self.publisher_ = self.create_publisher(String, 'switch_light', 10)
        self.timer_period = 5.0 #seconds
        self.timer = self.create_timer(self.timer_period, self.publish_light_switch_status)

    def publish_light_switch_status(self):
        if self.light_level is not None:
            if self.light_level > 500.0:
                status = "Turn off the light, it's bright enought!"
            else:
                status = "Turn on the light, it's too dark outside!"
        msg = String()
        msg.data = status
        self.publisher_.publish(msg)
        self.get_logger().info(status)
    
    def light_level_callback(self,msg):
        self.light_level = msg.data

def main(args = None):
    rclpy.init(args = args)
    switch_light_node = SwitchLightNode()
    rclpy.spin(switch_light_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()