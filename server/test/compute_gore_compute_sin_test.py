import unittest
import numpy as np
import numpy.testing as nptest

from scripts.compute_gore import compute_sin

class ComputeSinTestCase(unittest.TestCase):
    
    def test_computes_correct_output(self):
        angles = np.array([0,30,90], dtype=np.float64)
        actual_result = compute_sin(angles)
        expected_result = np.array([[0,30,90],[0, 0.5, 1]], dtype=np.float64)
        
        nptest.assert_allclose(actual_result, expected_result)