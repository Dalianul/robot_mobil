### Robot Package

#### Setup and Launch Instructions

1. **Run SLAM Toolbox**:
    ```bash
    ros2 launch slam_toolbox online_async_launch.py slam_params_file:=./src/robot_mobil/config/mapper_params_online_async.yaml use_sim_time:=true
    ```

    > Note: For mapping, use synchronous launch instead.

2. **Launch Simulation in Gazebo**:
    ```bash
    ros2 launch robot_mobil launch_sim.launch.py world:=./src/robot_mobil/worlds/MapaSimulare.world
    ```

    > Note: Specified a custom world in the launch command.

3. **Start RViz2**:
    ```bash
    rviz2 -d dev_ws/src/robot_mobil/config/main_bot.rviz
    ```

    > Note: Specified a custom config in the launch command.

ros2 launch rosbridge_server rosbridge_websocket_launch.xml //to start the rosbridge server

!!! Dont't forget about the visualize parameter in lidar.xacro-> true/false

#### Joystick Setup

1. **Install Joystick Drivers**:
    ```bash
    sudo apt install joystick jstest-gtk evtest
    ```

2. **Launch Joystick Control**:
    ```bash
    ros2 launch robot_mobil joystick.launch.py
    ```

    > Configured for Xbox Series X controller. For configuring another controller, use the `joy_tester` repo.

#### Additional Notes

- If you want to configure another joystick, install and use the `joy_tester` repo in your workspace:
    ```bash
    cd your_workspace
    git clone https://github.com/joshnewans/joy_tester.git
    colcon build --symlink-install
    ```
    > Ignore the deprecation warnings.

- **LIDAR Visualization**:
    - Toggle the `visualize` parameter in `lidar.xacro` between `true/false`.

- **RViz Visibility**:
    - For better camera visibility, uncheck the robot model, grid model, etc.

- **Important**:
    - Update Ubuntu OS and all ROS2 tools to the latest version.
    - Perform a fresh rebuild of the project:
        ```bash
        cd your_workspace
        rm -rf build install log
        colcon build --symlink-install
        ```
