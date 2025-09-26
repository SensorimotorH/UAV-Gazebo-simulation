PX4_PREFIX=/home/fuyx/rtabmap_drone_example/PX4-Autopilot
source $PX4_PREFIX/Tools/setup_gazebo.bash $PX4_PREFIX $PX4_PREFIX/build/px4_sitl_default
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$PX4_PREFIX
export ROS_PACKAGE_PATH=$ROS_PACKAGE_PATH:$PX4_PREFIX/Tools/sitl_gazebo
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/home/fuyx/catkin_ws/src/rtabmap_drone_example/models
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/home/fuyx/rtabmap_drone_example/catkin_ws/src/realsense_gazebo_plugin/models
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/home/fuyx/rtabmap_drone_example/aws-robomaker-small-house-world/models
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/home/fuyx/rtabmap_drone_example/aws-robomaker-small-warehouse-world/models
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/home/fuyx/rtabmap_drone_example/aws-robomaker-hospital-world/models
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/home/fuyx/rtabmap_drone_example/aws-robomaker-hospital-world/fuel_models
export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/home/fuyx/.gazebo/models
