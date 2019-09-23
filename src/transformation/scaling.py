from typing import Union

from numpy import ndarray

from transformation.transformation_base import TransformationBase


class Scaling(TransformationBase):
    def __init__(self, factor: Union[float, int]):
        self.factor = float(factor)

    def _transform(self, x_array: ndarray) -> ndarray:
        return x_array * self.factor
