import unittest

import numpy as np
from numpy import sqrt

from utils import angle_iter_to_unit_circil_coor_array


class UtilFcnsTestCase(unittest.TestCase):
    def test_basic_fcns(self):
        array2d = angle_iter_to_unit_circil_coor_array([
            0, 60, 180, 30, -30, 120
        ])

        self.assertTrue(np.allclose(array2d, [
            [1.0, 0.0],
            [0.5, .5 * sqrt(3.0)],
            [-1.0, 0.0],
            [.5 * sqrt(3.0), 0.5],
            [.5 * sqrt(3.0), -0.5],
            [-0.5, .5 * sqrt(3.0)],
        ]))


if __name__ == '__main__':
    unittest.main()
