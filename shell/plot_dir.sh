#!/bin/bash

if [ $# != 1 ]; then
	echo "Usage: ./plot_dir.sh PCD_DIR"
	exit 1
fi

pcd_dir=$@
pcd_dir_name=`basename $pcd_dir`

python3 ../pyscr/plot_pc_data.py \
    --pcd_path $pcd_dir/\* \
    --save_dir ../save/$pcd_dir_name \
    --flag_merge \
    --x_min -50 \
    --x_max 50 \
    --y_min -100 \
    --y_max 100