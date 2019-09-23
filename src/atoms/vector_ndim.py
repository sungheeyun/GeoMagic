from typing import List, Union

from numpy import ndarray, array

from atoms.geo_object_ndim import GeoObjectNDim
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
