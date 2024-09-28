import unittest

from src.compute_gore import compute_step_angles

class ComputeStepAnglesTestCase(unittest.TestCase):
    
    def test_with_default_step_size(self):
        actual_radii = compute_step_angles()
        expected_length = 91
        expected_start_value = 90.0
        expected_stop_value = 0.0

        self.assertEqual(expected_length, actual_radii.size)
        self.assertEqual(expected_start_value, actual_radii[0])
        self.assertEqual(expected_stop_value, actual_radii[-1])

    def test_with_step_size_0_5(self):
        actual_radii = compute_step_angles(step_size=0.5)
        expected_length = 181
        expected_start_value = 90.0
        expected_stop_value = 0.0

        self.assertEqual(expected_length, actual_radii.size)
        self.assertEqual(expected_start_value, actual_radii[0])
        self.assertEqual(expected_stop_value, actual_radii[-1])

    def test_with_step_size_2_5(self):
        actual_radii = compute_step_angles(step_size=2.5)
        expected_length = 37
        expected_start_value = 90.0
        expected_stop_value = 0.0

        self.assertEqual(expected_length, actual_radii.size)
        self.assertEqual(expected_start_value, actual_radii[0])
        self.assertEqual(expected_stop_value, actual_radii[-1])

    
        