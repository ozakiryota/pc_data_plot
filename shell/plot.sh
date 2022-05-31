#!/bin/bash

if [ $# != 1 ]; then
	echo "Usage: ./plot.sh PCD_PATH"
	exit 1
fi

pcd_path=$@
pcd_dir=`dirname $pcd_path`
pcd_dir_name=`basename $pcd_dir`

python3 ../pyscr/plot_pc_data.py \
    --pcd_path $pcd_path \
    --save_dir ../save/$pcd_dir_name \
    --flag_merge \
    --x_min -50 \
    --x_max 50 \
    --y_min -100 \
    --y_max 100