声明：本项目搬运自https://gitee.com/yu2324922276/master-degree.git ，为学习方便。

### open px4 user-guide

`yarn docs:dev`

### run px4

`make px4_sitl gz_x500_camera`

### add new model

`ROMFS/px4fmu_common/init.d-posix/airframes/CMakeLists.txt`，再在上级文件夹加加入文件

### run microdds

`MicroXRCEAgent udp4 -p 8888`

### 一些 tip

- 自定义 world 文件：`src/modules/simulation/gz_bridge/CMakeLists.txt`
- px4 的执行：`build/px4_sitl_default/bin/px4`
- 读一下 Makefile，了解一下编译的过程
- gz_gard 加文件：`GZ_SIM_RESOURCE_PATH`
- `ekf2 stop/start`
### 分支
- `dev`:开发分支
- `drone`:仿真分支

### 启动步骤
#### 仿真环境
ps:anaconda的环境是`py3.8`
- 先加载仿真环境变量：`cd ~/catkin_ws && source source_env.sh`
- 再打开GAZEBO 仿真环境 `roslaunch rtabmap_drone_example gazebo.launch`，可能需要运行`ekf2 stop` `ekf2 start`，不然无人机可能飞不起来
- 启动slam节点 `roslaunch rtabmap_drone_example slam.launch` 
- 起飞无人机 `rosrun rtabmap_drone_example offboard` 
- 启动rviz `roslaunch rtabmap_drone_example rviz.launch`
#### 导航环境
ps:环境保持`init`就可以，需要切换环境的时候会在脚本中切换
- 先运行模型推理 `cd ~/master-degree && source run_api.sh`
- 再运行c++服务 `source logic/cpp_op/catkin_ws/devel/setup.bash && source run_roslaunch.sh`
- 最后启动前后台系统 `source run_plus.sh`
- 之后就可以在前端页面上看到仿真的结果了 `http://127.0.0.1:8000/chat/`
