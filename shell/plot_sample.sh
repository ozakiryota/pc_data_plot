#!/bin/bash

pcd_dir="../pcd/sample"
pcd_dir_name=${pcd_dir##*/}

python3 ../pyscr/plot_pc_data.py \
    --pcd_path $pcd_dir/\* \
    --save_dir ../save/$pcd_dir_name \
    --flag_merge \
    --x_min -50 \
    --x_max 50 \
    --y_min -100 \
    --y_max 100