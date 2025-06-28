Robot Mobil - Instrucțiuni de Instalare și Lansare

---

Prezentare Generală

Acest ghid oferă pașii structurați pentru a rula și controla sistemul robotului atât în simulare (robot virtual) cât și pe robotul fizic real, utilizând ROS 2 Humble.

---

Cerințe Prealabile

* ROS 2 Humble instalat
* Sistem Ubuntu actualizat
* Workspace-ul construit:

cd ~/dev_ws
rm -rf build install log
colcon build --symlink-install

---

LANSARE ÎN SIMULARE (ROBOT VIRTUAL)

Se utilizează use_sim_time:=true pentru rularea în simulare.

1. Rulează SLAM Toolbox

ros2 launch slam_toolbox online_async_launch.py
slam_params_file:=./src/robot_mobil/config/mapper_params_online_async.yaml
use_sim_time:=true

Pentru mapare (mapping), folosește online_sync_launch.py.

2. Lansează Simularea în Gazebo

ros2 launch robot_mobil launch_sim.launch.py
world:=./src/robot_mobil/worlds/MapaSimulare.world

3. Pornește RViz cu configurație personalizată

rviz2 -d ./src/robot_mobil/config/main_bot.rviz
sau
ros2 launch robot_mobil rviz_launch.py

4. Lansează Navigația

ros2 launch robot_mobil localization_launch.py
map:=./src/robot_mobil/maps/virtual_map_save.yaml
use_sim_time:=true

ros2 launch robot_mobil navigation_launch.py
use_sim_time:=true map_subscribe_transient_local:=true

A doua comandă este necesară pentru ca AMCL să funcționeze corect cu Nav2.

---

LANSARE PE ROBOTUL REAL

Se utilizează use_sim_time:=false

1. Pornește robotul și conectează-te

SSH disponibil la adresa:

ssh robot@192.168.0.101 (In cazul nostru)

2. Lansează Robotul

ros2 launch robot_mobil launch_robot.launch.py

3. Control cu Joystick

ros2 launch robot_mobil joystick.launch.py

Este preconfigurat pentru Xbox Controller.

4. Localizare AMCL

ros2 launch nav2_bringup localization_launch.py
map:=./src/robot_mobil/maps/apt_dalian.yaml
use_sim_time:=false

5. Navigație

ros2 launch nav2_bringup navigation_launch.py
use_sim_time:=false map_subscribe_transient_local:=false

6. Vizualizare în RViz

ros2 launch robot_mobil rviz_launch.py

EXTRA : Urmărire Obiect (Ball Tracker)

ros2 launch robot_mobil ball_tracker.launch.py

Detectare obiect (minge de tenis):
ros2 run ball_tracker detect_ball --ros-args -p tuning_mode:=true -r image_in:=camera/image_raw

Urmărirea obiectului:
ros2 run ball_tracker follow_ball --ros-args -r cmd_vel:=cmd_vel_tracker

---

Configurare Joystick

Instalare drivere joystick:

sudo apt install joystick jstest-gtk evtest

---

LIDAR și Cameră

Pentru a activa vizualizarea LIDAR:
Editează fișierul lidar.xacro și setează:

<param name="visualize" value="true"/>

Pentru o vizualizare mai clară în RViz, ascunde grila și modelul robotului dacă este necesar.

---

Configurare Rețea (Router Portabil)

1. Configurează routerul în modul WISP
2. Setează adrese IP statice în setările LAN ale routerului (din pool-ul de IP-uri alocate)
3. Obține gateway-ul cu comanda:

ip addr show

4. Adaugă adresa gateway în fișierele de configurare netplan de pe ambele dispozitive (robot și stație de lucru)

---

Recomandări Finale

* Reconstruiește întotdeauna cu colcon build --symlink-install după modificări
* Verifică setarea use_sim_time în funcție de context (real sau simulare)
* Menține ROS 2, Gazebo și dependințele actualizate
