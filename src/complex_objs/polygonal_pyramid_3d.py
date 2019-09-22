from typing import Union, List
from copy import deepcopy

from numpy import array, ndarray

from atoms.polygon_2d import Polygon
from complex_objs.polygon_2d_ndim import Polygon2DInNDim
from complex_objs.seg_collection_ndim import SegCollectionNDim
from complex_objs.polygon_ndim import PolygonNDim


class PolygonalPyramid3D(SegCollectionNDim):
    """
    Implements a 3-D polygonal pyramid.
    """

    def __init__(self, polygon: Polygon, top_vertex: List[Union[float, int]], z_ground: Union[float, int] = 0.0):
        super(PolygonalPyramid3D, self).__init__(3)

        self.bottom_polygon: Polygon2DInNDim = Polygon2DInNDim(polygon, [float(z_ground)])
        self.top_vertex: ndarray = array(top_vertex, float)

        self._initialize()

    def _initialize(self):
        for segment_ndim in self.bottom_polygon.segment_ndim_list:
            self.segment_ndim_list.append(deepcopy(segment_ndim))

        for bottom_point in self.bottom_polygon.point_array_2d:
            self.add_segments((bottom_point, self.top_vertex))

    def get_side_face_list(self) -> List[PolygonNDim]:
        side_face_list: List[PolygonNDim] = list()

        bottom_point_array_2d: ndarray = self.bottom_polygon.point_array_2d
        num_points = bottom_point_array_2d.shape[0]
        for idx, bottom_point1 in enumerate(bottom_point_array_2d):
            bottom_point2: ndarray = bottom_point_array_2d[(idx + 1) % num_points]
            side_face_list.append(PolygonNDim((bottom_point1, bottom_point2, self.top_vertex)))

        return side_face_list
