#!/bin/bash
source ~/master-degree/logic/cpp_op/catkin_ws/devel/setup.bash 
rm -rf ./data/img
rm logfile.log
conda activate py3.8
python3 app_plus.py
