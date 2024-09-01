import numpy as np

MIN_RADIUS = 0.0
MAX_RADIUS = 90.0

def compute_radii(step_size : float = 1.0):

    return np.arange(MIN_RADIUS, MAX_RADIUS+step_size, step_size)[::-1]