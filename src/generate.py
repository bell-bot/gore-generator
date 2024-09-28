#!/usr/bin/env python3

from matplotlib.axes import Axes
from matplotlib.figure import Figure
from src.constants import PDF_PATH, PNG_PATH

from src.plot_gore import plot_gore

from src.compute_gore import get_gore

def get_step_size_from_precision(precision: float):
    return 50.0/precision

def generate(radius: float, n_gores: int, precision: float):
    
    step_size = get_step_size_from_precision(precision)
        
    gore = get_gore(radius, n_gores, step_size)
    
    fig, ax = plot_gore(gore)
    
    save_outputs(fig,ax)

    return True

def save_outputs(fig: Figure, ax: Axes):
    fig.savefig(PDF_PATH, format='pdf')
    aspect_ratio = ax.get_aspect()

    if type(aspect_ratio) != float:
        aspect_ratio = 1.0

    fig.set_size_inches(800/fig.dpi, (800*aspect_ratio)/fig.dpi)
    fig.savefig(PNG_PATH, format='png', bbox_inches="tight")
