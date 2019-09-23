from atoms.line_segment_ndim import LineSegmentNDim
from numpy.core._multiarray_umath import ndarray
from transformation.transformation_base import TransformationBase


class SymmetryAroundLine(TransformationBase):
    """
    Implements symmetry transformation around a line.
    """

    def __init__(self, line_segment_ndim: LineSegmentNDim):
        self.line_segment_ndim: LineSegmentNDim = line_segment_ndim

    def _transform(self, x_array: ndarray) -> ndarray:
        v1: ndarray = self.line_segment_ndim.point_1
        v2: ndarray = self.line_segment_ndim.point_2
        v: ndarray = v1 - v2

        t = v.dot(x_array - v2) / v.dot(v1 - v2)
        y_array: ndarray = 2 * (t * v1 + (1.0 - t) * v2) - x_array

        return y_array

    def get_input_dimension(self) -> int:
        return self.line_segment_ndim.get_num_dimensions()

    def get_output_dimension(self) -> int:
        return self.line_segment_ndim.get_num_dimensions()
