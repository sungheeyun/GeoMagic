from typing import Iterable

from numpy.core._multiarray_umath import ndarray
from transformation.transformer_base import TransformerBase


class CompositeTransformer(TransformerBase):
    """
    XXX
    """

    def __init__(self, transformer_list: Iterable[TransformerBase]):
        self.transformer_list: Iterable[TransformerBase] = transformer_list

    def _transform(self, x_array: ndarray) -> ndarray:
        y_array: ndarray = x_array.copy()
        for transformer in self.transformer_list:
            y_array = transformer(y_array)

        return y_array
