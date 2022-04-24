#!/bin/bash

pcd_dir="../pcd/sample"
pcd_dir_name=${pcd_dir##*/}

python3 ../pyscr/plot_pcd.py \
    --pcd_path $pcd_dir/\* \
    --save_dir ../save/$pcd_dir_name \
    --flag_merge