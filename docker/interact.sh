#!/bin/bash

xhost +

image="plot_pcd"
tag="latest"

docker run \
	-it \
	--rm \
	-e "DISPLAY" \
	-v "/tmp/.X11-unix:/tmp/.X11-unix:rw" \
	-v $(pwd)/../pcd:/root/$image/pcd \
	-v $(pwd)/..:/root/$image \
	$image:$tag