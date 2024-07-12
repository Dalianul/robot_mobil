from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
  return LaunchDescription([
    Node(
      package='l3xz_sweep_scanner',
      executable='l3xz_sweep_scanner_node',
      name='sweep_node',
      namespace='l3xz',
      output='screen',
      parameters=[
          {'topic' : 'laser'},
          #Modify the serial_port path based on what machine you have connected the lidar
          {'serial_port' : '/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.1:1.0-port0'},
          {'rotation_speed': 5},
          {'sample_rate': 1000},
          {'frame_id' : 'lidar_frame'}])
  ])
