import numpy as np
from math import pi, sin, radians

MIN_RADIUS = 0.0
MAX_RADIUS = 90.0

def compute_step_angles(step_size : float = 1.0):
    return np.arange(MIN_RADIUS, MAX_RADIUS+step_size, step_size)[::-1]

def compute_height(radius: float):
    return (2.0*pi*radius)/4.0

def compute_sin(angles: np.ndarray):
    result_array = np.tile(angles, (2,1))
    result_array[1] = np.sin(np.deg2rad(result_array[1]))
    return result_array

def compute_step(radius: float, height: float, angle: float, n_gores: int):
    r_angle = sin(radians(angle))*radius
    h_angle = height*((90.0-angle)/90.0)
    w_angle = (2*pi*r_angle)/n_gores
    
    return [h_angle, w_angle]

def compute_gore_dimensions(input_array: np.ndarray, height: float, n_gores: int, height_const: float, width_const: float):
    
    const_array = np.array([height_const, width_const]).reshape((2,1))
    input_array[0] = 90 - input_array[0]
        
    return np.multiply(const_array,input_array)

def get_height_constant(height: float):
    return height/90.0

def get_width_constant(n_gores: int):
    return (2*pi)/n_gores