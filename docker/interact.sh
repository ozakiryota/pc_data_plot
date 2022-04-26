#!/bin/bash

xhost +

image="plot_pc_data"
tag="latest"

docker run \
	-it \
	--rm \
	-e "DISPLAY" \
	-v "/tmp/.X11-unix:/tmp/.X11-unix:rw" \
	-v $(pwd)/../pcd:/root/$image/pcd \
	-v $(pwd)/../save:/root/$image/save \
	-v $(pwd)/../shell:/root/$image/shell \
	$image:$tag