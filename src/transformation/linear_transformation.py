from typing import Optional

from numpy.core._multiarray_umath import ndarray
from transformation.transformation_base import TransformationBase


class LinearTransformation(TransformationBase):
    def __init__(self, array_2d: ndarray):
        self.array_2d: ndarray = array_2d.copy()
        self._check_attrs()
        self.array_2d_T: ndarray = self.array_2d.T

    def _check_attrs(self):
        if self.array_2d.ndim != 2:
            raise Exception(f"array_2d should be 2-D array; array_2d.ndim = {self.array_2d}")

    def get_input_dimension(self) -> Optional[int]:
        return self.array_2d.shape[1]

    def get_output_dimension(self) -> Optional[int]:
        return self.array_2d.shape[0]

    def _transform(self, x_array: ndarray) -> ndarray:
        return x_array.dot(self.array_2d_T)
