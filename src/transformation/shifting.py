from typing import Union, Iterable, Optional

from numpy import ndarray, array
from transformation.transformation_base import TransformationBase
from transformation.inverible_transformation import InvertibleTransformation


class Shifting(InvertibleTransformation):
    def __init__(self, delta_iter: Iterable[Union[float, int]]):
        self.delta_array: ndarray = array(delta_iter, float)
        self._check_attrs()

    def _check_attrs(self) -> None:
        if self.delta_array.ndim != 1:
            raise Exception(f"delta_array should be 1-dimensional array; delta_array.ndim = {self.delta_array.ndim}")

    def _transform(self, x_array: ndarray) -> ndarray:
        return x_array + self.delta_array

    def get_input_dimension(self) -> Optional[int]:
        return self.delta_array.size

    def get_output_dimension(self) -> Optional[int]:
        return self.delta_array.size

    def get_inverse_transformation(self) -> TransformationBase:
        return Shifting(-self.delta_array)
