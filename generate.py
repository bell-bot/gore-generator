#!/usr/bin/env python3

import os.path
import sys

from constants import PDF_PATH, PNG_PATH
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from plot_gore import plot_gore

from compute_gore import get_gore

def get_step_size_from_precision(precision: float):
    return 50.0/precision

def generate(radius: float, n_gores: int, precision: float):
    
    step_size = get_step_size_from_precision(precision)
        
    gore = get_gore(radius, n_gores, step_size)
    
    fig, ax = plot_gore(gore)
    
    fig.savefig(PDF_PATH, format='pdf')
    aspect_ratio = ax.get_aspect()

    fig.set_size_inches(800/fig.dpi, (800*aspect_ratio)/fig.dpi)
    fig.savefig(PNG_PATH, format='png', bbox_inches="tight")
    