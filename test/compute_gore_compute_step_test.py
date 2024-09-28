import unittest
from numpy.testing import assert_array_almost_equal
from compute_gore import compute_step

class ComputeStepTestCase(unittest.TestCase):

    def test_gore_midpoint_step(self):
        actual_result = compute_step(10, 15.70796327, 45.0, 6)
        expected_result = [7.853981635, 7.404804897]

        assert_array_almost_equal(actual_result, expected_result)

    def test_gore_two_third_step(self):
        actual_result = compute_step(10, 15.70796327, 30.0, 6)
        expected_result = [(2.0*15.70796327)/3.0, 5.235987756]

        assert_array_almost_equal(actual_result, expected_result)

    def test_gore_one_third_step(self):
        actual_result = compute_step(10, 15.70796327, 60.0, 6)
        expected_result = [15.70796327/3.0, 9.068996821]

        assert_array_almost_equal(actual_result, expected_result)