#!/bin/bash
python make_hdf5.py --dataset DOORS --batch_size 128 --data_root data
python calculate_inception_moments.py --dataset DOORS --data_root data