from typing import Union

from numpy import ndarray, matrix, mat, eye, pi, cos, sin, array
from transformation.transformer_base import TransformerBase


class Rotation(TransformerBase):
    """
    Implements general rotation transformation in N-dimensional space.
    """

    def __init__(self, angle: Union[float, int]):
        self.angle: float = float(angle)
        self.rotation_2d_array: ndarray = None

        self._initialize()

    def _initialize(self):
        angle_rad: float = self.angle * pi / 180.0
        cos_value: float = cos(angle_rad)
        sin_value: float = sin(angle_rad)
        self.rotation_2d_array = array([
            [cos_value, -sin_value],
            [sin_value, cos_value]
        ])

    def _transform(self, x_array: ndarray) -> ndarray:
        num_dimensions = x_array.size

        if num_dimensions < 2:
            raise Exception(f"The number of dimension of x_array should be greater than 1; it's {num_dimensions}")

        mapping_mat: matrix = mat(eye(num_dimensions))
        mapping_mat[:2, :2] = self.rotation_2d_array

        return (x_array * mapping_mat.T).A1
