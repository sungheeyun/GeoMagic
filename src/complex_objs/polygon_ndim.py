from typing import Iterable, Union
from numpy import ndarray, array, vstack

from complex_objs.line_segment_ndim_collection import LineSegmentNDimCollection


class PolygonNDim(LineSegmentNDimCollection):
    """
    Implements connected N-dimensional segments.
    """

    def __init__(self, iter_iter: Iterable[Iterable[Union[float, int]]]):
        self.point_array_2d: ndarray = array(iter_iter, float)
        super(PolygonNDim, self).__init__(
            self.point_array_2d.shape[1], vstack((self.point_array_2d, self.point_array_2d[0]))
        )

    def get_num_vertices(self) -> int:
        return self.point_array_2d.shape[0]

    def get_center_of_gravity_point(self) -> ndarray:
        return self.point_array_2d.sum(axis=0)
