from typing import Iterable, Union, List
from logging import getLogger, Logger

from atoms.line_segment_2d import LineSegment2D
from atoms.geo_object_base import GeoObject
from numpy import array, vstack, ndarray
from matplotlib.axes import Axes

from atoms.geo_object_ndim import GeoObjectNDim
from atoms.box_ndim import BoxNDim
from transformation.transformation_base import TransformationBase

logger: Logger = getLogger('geomagic')


class LineSegmentNDim(GeoObjectNDim):
    """
    Implements line segment in N-dimensional space.
    """

    def __init__(self, point_1: Iterable[Union[float, int]], point_2: Iterable[Union[float, int]]):
        self.point_1: ndarray = array(point_1, float)
        self.point_2: ndarray = array(point_2, float)

        self.point_array_2d: ndarray = vstack((self.point_1, self.point_2))

    def get_name(self) -> str:
        return f"{self.get_num_dimensions()}-D line segment"

    def get_num_dimensions(self) -> int:
        return self.point_1.size

    def get_projection_onto_2d_plane(self, first_coordinate_index: int, second_coordinate_index: int) -> LineSegment2D:
        coor_list: List[int] = [first_coordinate_index, second_coordinate_index]
        logger.debug(f"self.point_1 = {self.point_1}")
        logger.debug(f"self.point_2 = {self.point_2}")
        logger.debug(f"coor_list = {coor_list}")
        logger.debug(f"self.point_1[coor_list] = {self.point_1[coor_list]}")
        logger.debug(f"self.point_2[coor_list] = {self.point_2[coor_list]}")

        return LineSegment2D(self.point_1[coor_list], self.point_2[coor_list])

    def __repr__(self) -> str:
        return f"Seg({self.point_1}, {self.point_2})"

    def draw2d(self, axis: Axes, **kwargs):
        return axis.plot(self.point_array_2d[:, 0], self.point_array_2d[:, 1], **kwargs)

    def draw3d(self, axis: Axes, **kwargs):
        return axis.plot(self.point_array_2d[:, 0], self.point_array_2d[:, 1], self.point_array_2d[:, 2], **kwargs)

    def apply_transformation(self, transformer: TransformationBase) -> GeoObject:
        point1: ndarray
        point2: ndarray
        point1, point2 = transformer(self.point_array_2d)

        return LineSegmentNDim(point1, point2)

    def get_smallest_containing_box(self) -> BoxNDim:
        return BoxNDim(self.point_array_2d.min(axis=0), self.point_array_2d.max(axis=0))
