from typing import List, Union

from matplotlib.axes import Axes
from numpy import ndarray, array

from atoms.geo_object_2d import GeoObject2D
from atoms.geo_object_base import GeoObject
from atoms.geo_object_ndim import GeoObjectNDim
from atoms.vector2d import Vector2D
from transformation.transformation_base import TransformationBase


class VectorNDim(GeoObjectNDim):
    """
    Implements n-dimensional vector.
    """

    def __init__(self, iter_1d: List[Union[float, int]]):
        self.array_1d: ndarray = array(iter_1d, float)

        self._check_attrs()

    def _check_attrs(self):
        for x in self.array_1d:
            if not isinstance(x, float):
                raise Exception(f"iter_1d should be 1-dimensional iterable! It's shape is {self.array_1d.shape}")

    def get_name(self) -> str:
        return f"{self.get_num_dimensions()}-D Vector"

    def get_num_dimensions(self) -> int:
        return self.array_1d.size

    def apply_transformation(self, transformer: TransformationBase) -> GeoObjectNDim:
        return VectorNDim(transformer(self.array_1d))

    def draw2d(self, axis: Axes, **kwargs):
        # TODO (1) implement VectorNDim.draw2d
        assert False

    def draw3d(self, axis: Axes, **kwargs):
        # TODO (1) implement VectorNDim.draw3d
        assert False

    def get_smallest_containing_box(self) -> GeoObject:
        # TODO (1) implement VectorNDim.get_smallest_containing_box(self) -> GeoObject:
        pass

    def get_projection_onto_2d_plane(self, first_coordinate_index: int, second_coordinate_index: int) -> Vector2D:
        return Vector2D(self.array_1d[[first_coordinate_index, second_coordinate_index]])
