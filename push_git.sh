source_path=/home/fuyx/catkin_ws/src/rtabmap_drone_example
dst_path=/home/fuyx/drone_master_degree/master-degree
cd /home/fuyx/drone_master_degree/master-degree && git checkout drone
cp -r $source_path/src $source_path/launch $source_path/include $source_path/msg $source_path/srv $source_path/docker .
cp  $source_path/*.sh $source_path/*.txt .
pwd
git add .
git commit -m "commit"
git push --set-upstream origin drone