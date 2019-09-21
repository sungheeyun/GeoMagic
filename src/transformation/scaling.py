from typing import Union

from numpy import ndarray

from transformation.transformer_base import TransformerBase


class Scaling(TransformerBase):
    def __init__(self, factor: Union[float, int]):
        self.factor = float(factor)

    def _transform(self, x_array: ndarray) -> ndarray:
        return x_array * self.factor
