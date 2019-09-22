from typing import Union, Iterable

from numpy import ndarray, array
from transformation.transformer_base import TransformerBase


class Shifting(TransformerBase):
    def __init__(self, delta_iter: Iterable[Union[float, int]]):
        self.delta_iter = array(delta_iter, float)

    def _transform(self, x_array: ndarray) -> ndarray:
        return x_array + self.delta_iter
