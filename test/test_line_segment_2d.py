from typing import List
from logging import Logger, getLogger, DEBUG
import unittest

from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes

from atoms.line_segment_2d import LineSegment2D
from utils import set_logger_config

logger: Logger = getLogger('geomagic')


class TestLineSegment2D(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        set_logger_config(logger, __file__, DEBUG)

    def test_basic_functions(self):

        line_segment_2d_list: List[LineSegment2D] = list()

        line_segment_2d_list.append(LineSegment2D((0, 0), (1, 1)))
        line_segment_2d_list.append(LineSegment2D((0, 1), (1, 0)))
        line_segment_2d_list.append(LineSegment2D((2, 1), (4, 3)))

        figure: Figure
        axis: Axes

        figure, axis = plt.subplots()
        for line_segment_2d in line_segment_2d_list:
            line_segment_2d.draw(axis)

        axis.axis('equal')

        figure.show()

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()

    if '__file__' in dir():
        plt.show()
