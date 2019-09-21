from typing import Union

from atoms.polygon_2d import Polygon
from complex_objs.polygon_ndim import PolygonNDim


class PolygonalPrism3D(PolygonNDim):
    """
    Implements a 3-D polygonal pyramid.
    """

    def __init__(self, polygon: Polygon, height: Union[float, int], z_ground: Union[float, int] = 0.0):
        super(PolygonalPrism3D, self).__init__(polygon, [float(z_ground)])
        self.height: float = float(height)

        # polygon in z=z_ground+height plane in 3-D space
        self.top_polygon: PolygonNDim = PolygonNDim(self.polygon, [self.rest_coordinate[0] + self.height])

        self._initialize()

    def _initialize(self):

        assert len(self.segment_ndim_list) == len(self.top_polygon.segment_ndim_list)

        bottom_top_point_pair_list = list()

        for idx, bottom_segment_ndim in enumerate(self.segment_ndim_list):
            top_segment_ndim = self.top_polygon.segment_ndim_list[idx]
            bottom_top_point_pair_list.append((bottom_segment_ndim.point1, top_segment_ndim.point1))

        for bottom_point, top_point in bottom_top_point_pair_list:
            self.add_segments((bottom_point, top_point))

        for top_segment_ndim in self.top_polygon.segment_ndim_list:
            self.segment_ndim_list.append(top_segment_ndim)
