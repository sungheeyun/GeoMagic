from typing import Union, List

from numpy import array

from atoms.polygon_2d import Polygon
from complex_objs.polygon_ndim import PolygonNDim


class PolygonalPyramid(PolygonNDim):
    """
    Implements a 3-D polygonal pyramid.
    """

    def __init__(self, polygon: Polygon, top_vertex: List[Union[float, int]], z_ground: Union[float, int] = 0.0):
        super(PolygonalPyramid, self).__init__(polygon, [float(z_ground)])
        self.top_vertex: array = array(top_vertex, float)

        self._initialize()

    def _initialize(self):

        bottom_top_point_pair_list = list()

        for bottom_segment_ndim in self.segment_ndim_list:
            bottom_top_point_pair_list.append((bottom_segment_ndim.point1, self.top_vertex))

        for bottom_point, top_point in bottom_top_point_pair_list:
            self.add_segments((bottom_point, top_point))
