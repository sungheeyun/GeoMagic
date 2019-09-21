from typing import Union

from numpy.core._multiarray_umath import ndarray
from transformation.transformer_base import TransformerBase


class Shift(TransformerBase):
    def __init__(self, delta: Union[float, int]):
        self.delta = float(delta)

    def _transform(self, x_array: ndarray) -> ndarray:
        return x_array + self.delta
