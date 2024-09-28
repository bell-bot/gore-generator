import unittest
import numpy as np
import numpy.testing as nptest

from src.compute_gore import compute_gore_dimensions

class ComputeGoreDimensionsTestCase(unittest.TestCase):
    
    def test_returns_correct_dimensions(self):
        input_array = np.array([[0.0,30.0,90.0],[0, 0.5, 1]], dtype=np.float64)
        height = 1.0
        n_gores = 6
        height_const = 0.5
        width_const = 0.1
        
        actual_result = compute_gore_dimensions(input_array, height_const, width_const)
        
        expected_result = np.array([[45.0, 30.0, 0.0],[0.0,0.05,0.1]], dtype=np.float64)
        
        nptest.assert_allclose(actual_result, expected_result)
        
        