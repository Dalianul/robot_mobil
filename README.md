### Robot Package

ros2 launch slam_toolbox online_async_launch.py slam_params_file:=./src/robot_mobil/config/mapper_params_online_async.yaml use_sim_time:=true //asta doar pentru localizare, pt. mapare foloseste cu sync

ros2 launch robot_mobil launch_sim.launch.py world:=./src/robot_mobil/worlds/MapaSimulare.world //Gazebo with custom world

rviz2 -d dev_ws/src/robot_mobil/config/main_bot.rviz //RViz2

ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r /cmd_vel:=/diff_controller/cmd_vel_unstamped //For controlling the robot with the keyboard

//Joystick drivers install
sudo apt install joystick jstest-gtk evtest

!!! Install joy_tester repo also: https://github.com/joshnewans/joy_tester //For configuring joystick and also for Gazebo
//Ignore the deprecation warnings

ros2 launch robot_mobil joystick.launch.py //Controlling robot with joystick (configured Xbox Series X controller)

!!! Dont't forget about the visualize parameter in lidar.xacro-> true/false

!!! In Rviz for good visibility of the camera uncheck robot model, grid model etc.

!!! Important: Update Ubuntu OS and all the ROS2 tools to the latest version