#!/usr/bin/env python3

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np

def get_x_limit(gore: np.ndarray):
    return gore[1][0]

def get_y_limit(gore: np.ndarray):
    return gore[0][-1]

def get_bottom_boundary(gore: np.ndarray):
    bottom_boundary = np.array([[-1,1],[0,0]])
    
    return bottom_boundary*gore[1][0]

def get_mirror(gore: np.ndarray):
    gore_mirror = gore.copy()
    gore_mirror[1] = gore_mirror[1]*(-1)
    return gore_mirror

def setup_axes(ax, x_limit, y_limit):
    ax.axis('scaled')
    ax.set_xlim((-1)*x_limit,x_limit)
    ax.set_ylim(0,y_limit)
    ax.set_frame_on(False)
    ax.set_axis_off()

def plot_gore(gore):
    y_limit = get_y_limit(gore)
    x_limit = get_x_limit(gore)
    x_axis = get_bottom_boundary(gore)
    gore_mirror = get_mirror(gore)
    
    print(x_limit)
    print(y_limit)
    
    fig,ax = plt.subplots(figsize=(x_limit*2, y_limit))

    setup_axes(ax, x_limit, y_limit)
    ax.plot(gore[1], gore[0], color='black', linewidth=1)
    ax.plot(gore_mirror[1], gore_mirror[0], color='black', linewidth=1)
    ax.plot(x_axis[0], x_axis[1], color='black', linewidth=2)
    
    return fig, ax