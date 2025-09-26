#!/bin/bash
# source /opt/ros/noetic/setup.bash
rm -rf ./data/img
rm logfile.log
uvicorn app:app --port 8082 2>&1 | tee logfile.log
