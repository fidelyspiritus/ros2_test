import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
from random import randint


class WindSensorNode(Node):
    def __init__(self):
        super().__init__('wind_sensor')
        self.speed_publisher = self.create_publisher(Int16, 'wind_speed', 10)
        self.direction_publisher = self.create_publisher(Int16, 'wind_direction', 10)
        self.timer_period = 1.0
        self.timer = self.create_timer(self.timer_period, self.publish_wind_data)  #ddirection or speed?

    def publish_wind_data(self):
        speed_msg, direction_msg = Int16(), Int16()
        speed_msg.data = randint(0, 25)
        self.speed_publisher.publish(speed_msg)

        direction_msg.data = randint(0, 360)
        self.direction_publisher.publish(direction_msg)
        self.get_logger().info(f'Wind speed is {speed_msg.data} m/s with {direction_msg.data} degree direction')

def main(args = None):
    rclpy.init(args=args)
    wind_sensor_node = WindSensorNode()
    rclpy.spin(wind_sensor_node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()