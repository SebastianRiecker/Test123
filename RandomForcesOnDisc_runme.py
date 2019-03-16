# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 14:28:37 2019

@author: Sebastian
"""

import RandomForcesOnDisc_module as rfdm
import numpy as np

# INPUT
numbercount = np.array([10, 100, 1000])
bincount = 10

# RUNME
"""Step by step going through module to get histogram plot and effective Force"""
histogram_data, histogram_data_normalized, histogram_std, histogram_av = rfdm.calc_dataset(numbercount, bincount)
angles_deg, angles_rad = rfdm.generate_bin_positions(bincount)
Fx,Fy, F = rfdm.calculate_effective_force(rfdm.convert_polar_to_kartesian(histogram_data))
rfdm.make_bar_plot(angles_deg, 
                  histogram_data, 
                  histogram_data_normalized, 
                  bincount, 
                  numbercount, 
                  F)

# RUNME
run_module_rfdm(numbercount)


# TODO
# - run with lambda or map function on numbercount