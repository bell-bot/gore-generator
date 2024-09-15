import os.path
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import unittest

from compute_gore import compute_height

class ComputeHeightTestCase(unittest.TestCase):

    def test_with_radius_1(self):
        actual_height = compute_height(1.0)
        expected_height = 1.570796327
        self.assertAlmostEqual(expected_height, actual_height)

    def test_with_radius_10(self):
        actual_height = compute_height(10.0)
        expected_height = 15.70796327
        self.assertAlmostEqual(expected_height, actual_height)