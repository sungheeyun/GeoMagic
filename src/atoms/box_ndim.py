from typing import Iterable, Union

from matplotlib.axes import Axes
from numpy import array, ndarray, vstack

from atoms.geo_object_ndim import GeoObjectNDim
from transformation.transformation_base import TransformationBase


class BoxNDim(GeoObjectNDim):
    """
    Implements N-dimensional box for mostly range calculation.
    """

    def __init__(self, lower_left_iter: Iterable[Union[float, int]], upper_right_iter: Iterable[Union[float, int]]):
        self.lower_left_point: ndarray = array(lower_left_iter, float)
        self.upper_right_point: ndarray = array(upper_right_iter, float)

        self._check_attrs()

    def _check_attrs(self):
        assert self.lower_left_point.ndim == 1, self.lower_left_point
        assert self.upper_right_point.ndim == 1
        assert self.lower_left_point.shape == self.upper_right_point.shape, (
            self.lower_left_point.shape,
            self.upper_right_point.shape,
        )

    def get_name(self) -> str:
        return f"BoxNDim({self.lower_left_point}, {self.upper_right_point})"

    def get_num_dimensions(self) -> int:
        return self.lower_left_point.size

    def __add__(self, other: GeoObjectNDim) -> GeoObjectNDim:
        return BoxNDim(
            vstack((self.lower_left_point, other.lower_left_point)).min(axis=0),
            vstack((self.upper_right_point, other.upper_right_point)).max(axis=0),
        )

    def __radd__(self, other: int) -> GeoObjectNDim:
        if isinstance(other, int) and other == 0:
            return self

    def apply_transformation(self, transformer: TransformationBase) -> GeoObjectNDim:
        # XXX
        assert False

    def draw2d(self, axis: Axes, **kwargs):
        # XXX
        assert False

    def draw3d(self, axis: Axes, **kwargs):
        # XXX
        assert False

    def get_smallest_containing_box(self) -> GeoObjectNDim:
        return self