### Robot Package

ros2 launch slam_toolbox online_async_launch.py slam_params_file:=./src/robot_mobil/config/mapper_params_online_async.yaml use_sim_time:=true //asta doar pentru localizare, pt. mapare foloseste cu sync

ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_controller/cmd_vel_unstamped

ros2 launch robot_mobil launch_sim.launch.py world:=./src/robot_mobil/worlds/MapaSimulare.world

rviz2 -d dev_ws/src/robot_mobil/config/main_bot.rviz

Package for the robot_mobil project.