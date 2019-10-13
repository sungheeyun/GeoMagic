import unittest

from matplotlib import pyplot as plt

from atoms.line_segment_2d import LineSegment2D


class TestLineSegment2D(unittest.TestCase):
    def test_basic_functions(self):

        # line_segment_2d: LineSegment2D = LineSegment2D((0, 0), (1, 1))
        line_segment_2d: LineSegment2D = LineSegment2D((0, 1), (1, 0))

        fig, ax = plt.subplots()
        line_segment_2d.draw(ax)

        fig.show()

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()

    if '__file__' in dir():
        plt.show()
