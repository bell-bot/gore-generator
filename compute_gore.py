import numpy as np
from math import pi, sin, radians

MIN_RADIUS = 0.0
MAX_RADIUS = 90.0

def compute_step_angles(step_size : float = 1.0):
    return np.arange(MIN_RADIUS, MAX_RADIUS+step_size, step_size)[::-1]

def compute_height(radius: float):
    return (2.0*pi*radius)/4.0

def compute_step(radius: float, height: float, angle: float, n_gores: int):
    r_angle = sin(radians(angle))*radius
    h_angle = height*((90.0-angle)/90.0)
    w_angle = (2*pi*r_angle)/n_gores
    
    return np.array([h_angle, w_angle])

def compute_gore_dimensions(radii: np.ndarray, height, n_gores):
    dimensions = []
    for radius in radii.tolist():
        dimensions.append(compute_step(radius, height, ))

if __name__=="__main__":
    r = compute_step_angles()
    print(r.shape)
    h = compute_gore_dimensions(r, 10, 6)