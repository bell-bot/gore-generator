#!/usr/bin/env python3
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from constants import PDF_PATH, PNG_PATH

from plot_gore import plot_gore

from compute_gore import get_gore

import os

def get_step_size_from_precision(precision: float):
    return 50.0/precision

def generate(radius: float, n_gores: int, precision: float, uuid: str):
    
    step_size = get_step_size_from_precision(precision)
        
    gore = get_gore(radius, n_gores, step_size)
    
    fig, ax = plot_gore(gore)
    save_outputs(fig,ax)

    return True

def save_outputs(fig: Figure, ax: Axes, uuid: str):

    file_pdf_path = PDF_PATH(uuid)
    fig.savefig(file_pdf_path, format='pdf')
    print(f"Saved PDF to {os.path.abspath(file_pdf_path)}")

    aspect_ratio = ax.get_aspect()

    if type(aspect_ratio) != float:
        aspect_ratio = 1.0

    fig.set_size_inches(800/fig.dpi, (800*aspect_ratio)/fig.dpi)

    file_png_path = PNG_PATH(uuid)
    fig.savefig(file_png_path, format='png', bbox_inches="tight")
    print(f"Saved PNG to {os.path.abspath(file_png_path)}")
