from setuptools import find_packages, setup

package_name = 'my_ros2_test_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='anastasiia',
    maintainer_email='anastasiia@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'temperature_sensor = my_ros2_test_package.temperature_sensor_node:main',
            'light_sensor = my_ros2_test_package.light_sensor_node:main',
            'display = my_ros2_test_package.display_node:main',
            'switch_light = my_ros2_test_package.switch_light_node:main',
            'wind_sensor = my_ros2_test_package.wind_sensor_node:main',
        ],
    },
)
