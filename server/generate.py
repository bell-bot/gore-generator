#!/usr/bin/env python3

import os.path
import sys

from server.constants import IMAGE_PATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from plot_gore import plot_gore

from compute_gore import get_gore

def get_step_size_from_precision(precision: float):
    return 50.0/precision

def generate(radius: float, n_gores: int, precision: float):
    
    step_size = get_step_size_from_precision(precision)
        
    gore = get_gore(radius, n_gores, step_size)
    
    plot = plot_gore(gore)
    
    plot.savefig("server/" + IMAGE_PATH, format='pdf')
    