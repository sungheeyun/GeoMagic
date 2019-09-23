from typing import Iterable, Optional, List

from numpy.core._multiarray_umath import ndarray
from transformation.transformation_base import TransformationBase


class CompositeTransformation(TransformationBase):
    """
    XXX
    """

    def __init__(self, transformer_iter: Iterable[TransformationBase]):
        self.transformer_list: List[TransformationBase] = list(transformer_iter)

    def _transform(self, x_array: ndarray) -> ndarray:
        y_array: ndarray = x_array.copy()
        for transformer in self.transformer_list:
            y_array = transformer(y_array)

        return y_array

    def get_input_dimension(self) -> Optional[int]:
        return self.transformer_list[0].get_input_dimension()

    def get_output_dimension(self) -> Optional[int]:
        return self.transformer_list[-1].get_output_dimension()
