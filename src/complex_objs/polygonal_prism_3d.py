from typing import Union
from copy import deepcopy

from atoms.polygon import Polygon
from complex_objs.polygon_2d_ndim import Polygon2DInNDim
from complex_objs.line_segment_ndim_collection import LineSegmentNDimCollection


class PolygonalPrism3D(LineSegmentNDimCollection):
    """
    Implements a 3-D polygonal pyramid.
    """

    def __init__(self, polygon: Polygon, height: Union[float, int], z_ground: Union[float, int] = 0.0):
        super(PolygonalPrism3D, self).__init__(3)

        self.height: float = float(height)
        self.z_ground: float = float(z_ground)

        self.bottom_polygon: Polygon2DInNDim = Polygon2DInNDim(polygon, [self.z_ground])
        self.top_polygon: Polygon2DInNDim = Polygon2DInNDim(polygon, [self.z_ground + self.height])

        self._initialize()

    def _initialize(self):

        for segment_ndim in self.bottom_polygon.segment_ndim_list:
            self.segment_ndim_list.append(deepcopy(segment_ndim))

        for segment_ndim in self.top_polygon.segment_ndim_list:
            self.segment_ndim_list.append(deepcopy(segment_ndim))

        for idx, bottom_point in enumerate(self.bottom_polygon.point_array_2d):
            top_point = self.top_polygon.point_array_2d[idx]
            self.add_segments((bottom_point, top_point))
