from typing import Iterable, Union

from atoms.geo_object_base import GeoObject
from numpy import array, vstack, ndarray
from matplotlib.axes import Axes

from atoms.geo_object_ndim import GeoObjectNDim
from transformation.transformer_base import TransformerBase


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

    def __repr__(self) -> str:
        return f"Seg({self.point_1}, {self.point_2})"

    def draw3d(self, axis: Axes, **kwargs):
        if self.get_num_dimensions() != 3:
            raise Exception(f"The dimension should be 3; it's {self.get_num_dimensions()}")

        axis.plot(self.point_array_2d[:, 0], self.point_array_2d[:, 1], self.point_array_2d[:, 2], **kwargs)

    def apply_transformation(self, transformer: TransformerBase) -> GeoObject:
        point1: ndarray = None
        point2: ndarray = None
        point1, point2 = transformer(self.point_array_2d)

        return LineSegmentNDim(point1, point2)
