from typing import Iterable, Union

from numpy import array, vstack
from matplotlib.axes import Axes

from atoms.geo_object_ndim import GeoObjectNDim


class SegmentNDim(GeoObjectNDim):

    def __init__(
            self,
            point1: Iterable[Union[float, int]],
            point2: Iterable[Union[float, int]]
    ):
        self.point1 = array(point1, float)
        self.point2 = array(point2, float)

        self.point_array_2d = vstack((self.point1, self.point2))

    def get_name(self) -> str:
        return f'{self.get_num_dimensions()}-D line segment'

    def get_num_dimensions(self) -> int:
        return self.point1.size

    def __repr__(self) -> str:
        return f'Seg({self.point1}, {self.point2})'

    def draw3d(self, axis: Axes, **kwargs):
        if self.get_num_dimensions() != 3:
            raise Exception(f"The dimension should be 3; it's {self.get_num_dimensions()}")

        axis.plot(
            self.point_array_2d[:, 0],
            self.point_array_2d[:, 1],
            self.point_array_2d[:, 2],
            **kwargs
        )
