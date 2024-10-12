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

    ```bash
    ros2 launch robot_mobil rviz_launch.py
    ```

    > Note: Specified a custom config in the launch command, use the ros2 launch command for Nav2.

4. **Nav2**:
    ```bash
    ros2 launch robot_mobil localization_launch.py map:=./src/robot_mobil/maps/virtual_map_save.yaml use_sim_time:=true
    ```
    > Note: For AMCL Localization.

    ```bash
    ros2 launch robot_mobil navigation_launch.py use_sim_time:=true map_subscribe_transient_local:=true
    ```

    ```bash
    ros2 launch robot_mobil navigation_launch.py use_sim_time:=true 
    ```
    > Note: For Nav2 Navigation, use the one with map_subscribe_transient_local:=true for running together with AMCL.

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
- **Portable Router Config**:
    - Configure it on WISP mode.
    - For the static ip addresses: open the router's main menu, go to network lan settings and pick some ip addresses from the alocated ip address pool.
    - Gateway: connect to the router, open the terminal and write the command:
        ```bash
        ip addr show
        ```
    And you get from the name of our router the second address from inet, that is the gateway which needs to be put in both netplan files for the dev machine and for your robot machine.
    Current robot machine ip address to use when connecting with ssh: 192.168.0.101

- **l3xz_sweep_scanner modification**:
    - You have to add the two lines from below the SweepScannerNode.cpp:
        -laser_scan_msg.header.stamp = this->now(); after laser_scan_msg.header.frame_id = _frame_id;
        -laser_scan_msg.ranges.resize(200, std::numeric_limits<float>::infinity()); after laser_scan_msg.ranges.assign(scan.samples.size(), std::numeric_limits<float>::infinity());